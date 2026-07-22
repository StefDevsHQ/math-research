"""Propagation-closed signed residual normal forms for VS-08."""

from __future__ import annotations

import itertools
import json
from collections.abc import Mapping, Sequence as SequenceABC
from dataclasses import dataclass

from .errors import ValidationError
from .model import Hypergraph3
from .profile import build_exact_profile, validate_ordering

FORMAT = "nae3-vs08-pcrnf-v1"

Unary = tuple[int, int]
SignedBinary = tuple[int, int, int]
Ternary = tuple[int, int, int]


def _strict_bit(value: object, name: str = "bit") -> int:
    if type(value) is not int or value not in (0, 1):
        raise ValidationError(f"{name} must be the integer zero or one")
    return value


def _strict_vertices(value: object, name: str) -> tuple[int, ...]:
    if type(value) is not tuple:
        raise ValidationError(f"{name} must be a tuple")
    previous: int | None = None
    for vertex in value:
        if type(vertex) is not int or vertex < 0:
            raise ValidationError(f"{name} must contain nonnegative integers")
        if previous is not None and vertex <= previous:
            raise ValidationError(f"{name} must be strictly increasing")
        previous = vertex
    return value


def _strict_unaries(
    value: object,
    vertices: frozenset[int],
) -> tuple[Unary, ...]:
    if type(value) is not tuple:
        raise ValidationError("unaries must be a tuple")
    previous: Unary | None = None
    seen: set[int] = set()
    for unary in value:
        if type(unary) is not tuple or len(unary) != 2:
            raise ValidationError("each unary must be a vertex-colour pair")
        vertex, colour = unary
        if type(vertex) is not int or vertex not in vertices:
            raise ValidationError("unary vertex must belong to the component")
        _strict_bit(colour, "unary colour")
        if vertex in seen:
            raise ValidationError("a canonical component has at most one unary per vertex")
        if previous is not None and unary <= previous:
            raise ValidationError("unaries must be strictly sorted")
        seen.add(vertex)
        previous = unary
    return value


def _strict_binaries(
    value: object,
    vertices: frozenset[int],
) -> tuple[SignedBinary, ...]:
    if type(value) is not tuple:
        raise ValidationError("binaries must be a tuple")
    previous: SignedBinary | None = None
    for binary in value:
        if type(binary) is not tuple or len(binary) != 3:
            raise ValidationError("each signed binary must be a triple")
        left, right, colour = binary
        if (
            type(left) is not int
            or type(right) is not int
            or left not in vertices
            or right not in vertices
            or left >= right
        ):
            raise ValidationError("binary endpoints must be increasing component vertices")
        _strict_bit(colour, "binary sign")
        if previous is not None and binary <= previous:
            raise ValidationError("binaries must be strictly sorted without duplicates")
        previous = binary
    return value


def _strict_ternaries(
    value: object,
    vertices: frozenset[int],
) -> tuple[Ternary, ...]:
    if type(value) is not tuple:
        raise ValidationError("ternaries must be a tuple")
    previous: Ternary | None = None
    for ternary in value:
        if type(ternary) is not tuple or len(ternary) != 3:
            raise ValidationError("each ternary must be a triple")
        left, middle, right = ternary
        if (
            type(left) is not int
            or type(middle) is not int
            or type(right) is not int
            or not left < middle < right
            or left not in vertices
            or middle not in vertices
            or right not in vertices
        ):
            raise ValidationError("ternary vertices must be increasing component vertices")
        if previous is not None and ternary <= previous:
            raise ValidationError("ternaries must be strictly sorted without duplicates")
        previous = ternary
    return value


@dataclass(frozen=True, slots=True, order=True)
class ResidualComponent:
    """One labelled residual component in a recorded colour orientation."""

    vertices: tuple[int, ...]
    flip: int
    unaries: tuple[Unary, ...]
    binaries: tuple[SignedBinary, ...]
    ternaries: tuple[Ternary, ...]

    def __post_init__(self) -> None:
        vertices = _strict_vertices(self.vertices, "component vertices")
        if not vertices:
            raise ValidationError("a residual component must contain a vertex")
        _strict_bit(self.flip, "component orientation")
        vertex_set = frozenset(vertices)
        _strict_unaries(self.unaries, vertex_set)
        _strict_binaries(self.binaries, vertex_set)
        _strict_ternaries(self.ternaries, vertex_set)


@dataclass(frozen=True, slots=True)
class SignedResidual:
    """Canonical exact residual with explicit component orientation bits."""

    remaining_vertices: tuple[int, ...]
    contradiction: bool
    components: tuple[ResidualComponent, ...]

    def __post_init__(self) -> None:
        remaining = _strict_vertices(
            self.remaining_vertices,
            "remaining vertices",
        )
        if type(self.contradiction) is not bool:
            raise ValidationError("contradiction must be a Boolean")
        if type(self.components) is not tuple:
            raise ValidationError("components must be a tuple")
        if self.contradiction:
            if self.components:
                raise ValidationError("a contradictory residual has no component payload")
            return
        previous: ResidualComponent | None = None
        flattened: list[int] = []
        for component in self.components:
            if not isinstance(component, ResidualComponent):
                raise ValidationError("every component must be a ResidualComponent")
            if previous is not None and component <= previous:
                raise ValidationError("components must be strictly sorted")
            flattened.extend(component.vertices)
            previous = component
        if tuple(sorted(flattened)) != remaining:
            raise ValidationError("components must partition the remaining vertices")
        if len(flattened) != len(set(flattened)):
            raise ValidationError("residual components must be vertex-disjoint")

    @property
    def is_final_accepting(self) -> bool:
        return not self.contradiction and not self.remaining_vertices


def _require_instance(instance: object) -> Hypergraph3:
    if not isinstance(instance, Hypergraph3):
        raise ValidationError("instance must be a Hypergraph3")
    return instance


def _validate_prefix(prefix: object, maximum: int) -> tuple[int, ...]:
    if isinstance(prefix, (str, bytes, bytearray)) or not isinstance(
        prefix,
        SequenceABC,
    ):
        raise ValidationError("prefix must be a finite non-string sequence")
    values = tuple(prefix)
    if len(values) > maximum:
        raise ValidationError("prefix is longer than the ordering")
    if any(type(bit) is not int or bit not in (0, 1) for bit in values):
        raise ValidationError("prefix entries must be strict integer bits")
    return values


def _add_force(forces: dict[int, int], vertex: int, colour: int) -> bool:
    previous = forces.get(vertex)
    if previous is None:
        forces[vertex] = colour
        return True
    if previous != colour:
        raise _Contradiction
    return False


class _Contradiction(Exception):
    pass


def _actual_constraint_tuple(
    unaries: tuple[Unary, ...],
    binaries: tuple[SignedBinary, ...],
    ternaries: tuple[Ternary, ...],
) -> tuple[object, ...]:
    return (unaries, binaries, ternaries)


def _componentize(
    variables: tuple[int, ...],
    forces: Mapping[int, int],
    binaries: set[SignedBinary],
    ternaries: set[Ternary],
) -> tuple[ResidualComponent, ...]:
    adjacency = {vertex: set() for vertex in variables}
    for left, right, _ in binaries:
        adjacency[left].add(right)
        adjacency[right].add(left)
    for left, middle, right in ternaries:
        adjacency[left].update((middle, right))
        adjacency[middle].update((left, right))
        adjacency[right].update((left, middle))

    components: list[ResidualComponent] = []
    seen: set[int] = set()
    for start in variables:
        if start in seen:
            continue
        seen.add(start)
        stack = [start]
        members: list[int] = []
        while stack:
            vertex = stack.pop()
            members.append(vertex)
            for neighbour in adjacency[vertex]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    stack.append(neighbour)
        vertices = tuple(sorted(members))
        vertex_set = frozenset(vertices)
        unaries = tuple(
            sorted(
                (vertex, colour)
                for vertex, colour in forces.items()
                if vertex in vertex_set
            )
        )
        component_binaries = tuple(
            sorted(
                binary
                for binary in binaries
                if binary[0] in vertex_set
            )
        )
        component_ternaries = tuple(
            sorted(
                ternary
                for ternary in ternaries
                if ternary[0] in vertex_set
            )
        )
        actual = _actual_constraint_tuple(
            unaries,
            component_binaries,
            component_ternaries,
        )
        complemented = _actual_constraint_tuple(
            tuple((vertex, 1 - colour) for vertex, colour in unaries),
            tuple(
                (left, right, 1 - colour)
                for left, right, colour in component_binaries
            ),
            component_ternaries,
        )
        if complemented < actual:
            components.append(
                ResidualComponent(
                    vertices,
                    1,
                    complemented[0],
                    complemented[1],
                    complemented[2],
                )
            )
        else:
            components.append(
                ResidualComponent(
                    vertices,
                    0,
                    unaries,
                    component_binaries,
                    component_ternaries,
                )
            )
    return tuple(sorted(components))


def _close_actual(
    variables: tuple[int, ...],
    *,
    unaries: tuple[Unary, ...] = (),
    binaries: tuple[SignedBinary, ...] = (),
    ternaries: tuple[Ternary, ...] = (),
    contradiction: bool = False,
) -> SignedResidual:
    variables = tuple(sorted(variables))
    variable_set = frozenset(variables)
    if contradiction:
        return SignedResidual(variables, True, ())

    forces: dict[int, int] = {}
    binary_set: set[SignedBinary] = set()
    ternary_set: set[Ternary] = set()
    try:
        for vertex, colour in unaries:
            if vertex not in variable_set:
                raise ValidationError("unary vertex is not a remaining vertex")
            _strict_bit(colour, "unary colour")
            _add_force(forces, vertex, colour)
        for left, right, colour in binaries:
            if left > right:
                left, right = right, left
            if (
                left == right
                or left not in variable_set
                or right not in variable_set
            ):
                raise ValidationError("binary endpoints must be distinct remaining vertices")
            _strict_bit(colour, "binary sign")
            binary_set.add((left, right, colour))
        for raw in ternaries:
            ternary = tuple(sorted(raw))
            if len(set(ternary)) != 3 or any(
                vertex not in variable_set for vertex in ternary
            ):
                raise ValidationError("ternary must use three remaining vertices")
            ternary_set.add(ternary)

        changed = True
        while changed:
            changed = False
            next_binaries: set[SignedBinary] = set()
            for left, right, colour in sorted(binary_set):
                left_value = forces.get(left)
                right_value = forces.get(right)
                if left_value is not None and right_value is not None:
                    if left_value == colour and right_value == colour:
                        raise _Contradiction
                    changed = True
                    continue
                if left_value is not None:
                    if left_value == colour:
                        changed |= _add_force(forces, right, 1 - colour)
                    changed = True
                    continue
                if right_value is not None:
                    if right_value == colour:
                        changed |= _add_force(forces, left, 1 - colour)
                    changed = True
                    continue
                next_binaries.add((left, right, colour))
            binary_set = next_binaries

            next_ternaries: set[Ternary] = set()
            generated_binaries: list[SignedBinary] = []
            for ternary in sorted(ternary_set):
                fixed = tuple(
                    (vertex, forces[vertex])
                    for vertex in ternary
                    if vertex in forces
                )
                if not fixed:
                    next_ternaries.add(ternary)
                    continue
                changed = True
                free = tuple(
                    vertex for vertex in ternary if vertex not in forces
                )
                colours = tuple(colour for _, colour in fixed)
                if len(fixed) == 1:
                    left, right = sorted(free)
                    generated_binaries.append(
                        (left, right, colours[0])
                    )
                elif len(fixed) == 2:
                    if colours[0] == colours[1]:
                        _add_force(forces, free[0], 1 - colours[0])
                elif colours[0] == colours[1] == colours[2]:
                    raise _Contradiction
            ternary_set = next_ternaries
            binary_set.update(generated_binaries)
    except _Contradiction:
        return SignedResidual(variables, True, ())

    if any(
        left in forces or right in forces
        for left, right, _ in binary_set
    ):
        raise AssertionError("closure retained a binary incident to a forced vertex")
    if any(
        any(vertex in forces for vertex in ternary)
        for ternary in ternary_set
    ):
        raise AssertionError("closure retained a ternary incident to a forced vertex")

    return SignedResidual(
        variables,
        False,
        _componentize(
            variables,
            forces,
            binary_set,
            ternary_set,
        ),
    )


def _decode_actual(
    residual: SignedResidual,
) -> tuple[tuple[Unary, ...], tuple[SignedBinary, ...], tuple[Ternary, ...]]:
    if residual.contradiction:
        return (), (), ()
    unaries: list[Unary] = []
    binaries: list[SignedBinary] = []
    ternaries: list[Ternary] = []
    for component in residual.components:
        if component.flip:
            unaries.extend(
                (vertex, 1 - colour)
                for vertex, colour in component.unaries
            )
            binaries.extend(
                (left, right, 1 - colour)
                for left, right, colour in component.binaries
            )
        else:
            unaries.extend(component.unaries)
            binaries.extend(component.binaries)
        ternaries.extend(component.ternaries)
    return (
        tuple(sorted(unaries)),
        tuple(sorted(binaries)),
        tuple(sorted(ternaries)),
    )


def build_pcrnf(
    instance: Hypergraph3,
    ordering: object,
    prefix: object,
) -> SignedResidual:
    """Build the exact oriented PCRNF after one processed prefix."""
    instance = _require_instance(instance)
    ordering = validate_ordering(instance, ordering)
    prefix = _validate_prefix(prefix, instance.n)
    assigned = dict(zip(ordering[: len(prefix)], prefix))
    remaining = tuple(sorted(ordering[len(prefix) :]))
    unaries: list[Unary] = []
    binaries: list[SignedBinary] = []
    ternaries: list[Ternary] = []

    for edge in instance.edges:
        fixed = tuple(
            (vertex, assigned[vertex])
            for vertex in edge
            if vertex in assigned
        )
        free = tuple(vertex for vertex in edge if vertex not in assigned)
        if not fixed:
            ternaries.append(edge)
        elif len(fixed) == 1:
            left, right = sorted(free)
            binaries.append((left, right, fixed[0][1]))
        elif len(fixed) == 2:
            if fixed[0][1] == fixed[1][1]:
                unaries.append((free[0], 1 - fixed[0][1]))
        else:
            colours = tuple(colour for _, colour in fixed)
            if colours[0] == colours[1] == colours[2]:
                return _close_actual(remaining, contradiction=True)

    return _close_actual(
        remaining,
        unaries=tuple(unaries),
        binaries=tuple(binaries),
        ternaries=tuple(ternaries),
    )


def transition_pcrnf(
    residual: SignedResidual,
    vertex: object,
    colour: object,
) -> SignedResidual:
    """Restrict one remaining labelled vertex and re-close exactly."""
    if not isinstance(residual, SignedResidual):
        raise ValidationError("residual must be a SignedResidual")
    if type(vertex) is not int or vertex not in residual.remaining_vertices:
        raise ValidationError("transition vertex must be a remaining vertex")
    colour = _strict_bit(colour, "transition colour")
    remaining = tuple(
        candidate
        for candidate in residual.remaining_vertices
        if candidate != vertex
    )
    if residual.contradiction:
        return _close_actual(remaining, contradiction=True)

    unaries, binaries, ternaries = _decode_actual(residual)
    restricted = _close_actual(
        residual.remaining_vertices,
        unaries=unaries + ((vertex, colour),),
        binaries=binaries,
        ternaries=ternaries,
    )
    if restricted.contradiction:
        return _close_actual(remaining, contradiction=True)

    closed_unaries, closed_binaries, closed_ternaries = _decode_actual(
        restricted
    )
    projected_unaries = tuple(
        unary for unary in closed_unaries if unary[0] != vertex
    )
    if any(vertex in binary[:2] for binary in closed_binaries):
        raise AssertionError("restricted vertex survived in a binary")
    if any(vertex in ternary for ternary in closed_ternaries):
        raise AssertionError("restricted vertex survived in a ternary")
    return _close_actual(
        remaining,
        unaries=projected_unaries,
        binaries=closed_binaries,
        ternaries=closed_ternaries,
    )


def satisfies_pcrnf(
    residual: SignedResidual,
    assignment: Mapping[int, int],
) -> bool:
    """Verify one complete labelled assignment of the residual variables."""
    if not isinstance(residual, SignedResidual):
        raise ValidationError("residual must be a SignedResidual")
    if not isinstance(assignment, Mapping):
        raise ValidationError("assignment must be a mapping")
    if set(assignment) != set(residual.remaining_vertices):
        raise ValidationError("assignment domain must equal the remaining vertices")
    values: dict[int, int] = {}
    for vertex, colour in assignment.items():
        if type(vertex) is not int:
            raise ValidationError("assignment keys must be integer vertices")
        values[vertex] = _strict_bit(colour, "assignment colour")
    if residual.contradiction:
        return False
    unaries, binaries, ternaries = _decode_actual(residual)
    return (
        all(values[vertex] == colour for vertex, colour in unaries)
        and all(
            not (
                values[left] == values[right] == colour
            )
            for left, right, colour in binaries
        )
        and all(
            not (
                values[left]
                == values[middle]
                == values[right]
            )
            for left, middle, right in ternaries
        )
    )


def pcrnf_completion_mask(
    residual: SignedResidual,
    variable_order: object,
) -> int:
    """Return the exact completion mask in one explicit suffix order."""
    if isinstance(variable_order, (str, bytes, bytearray)) or not isinstance(
        variable_order,
        SequenceABC,
    ):
        raise ValidationError("variable order must be a finite sequence")
    order = tuple(variable_order)
    if set(order) != set(residual.remaining_vertices) or len(order) != len(
        residual.remaining_vertices
    ):
        raise ValidationError("variable order must permute the remaining vertices")
    mask = 0
    for index, bits in enumerate(
        itertools.product((0, 1), repeat=len(order))
    ):
        assignment = dict(zip(order, bits))
        if satisfies_pcrnf(residual, assignment):
            mask |= 1 << index
    return mask


def pcrnf_record(residual: SignedResidual) -> dict[str, object]:
    if not isinstance(residual, SignedResidual):
        raise ValidationError("residual must be a SignedResidual")
    return {
        "format": FORMAT,
        "remaining_vertices": list(residual.remaining_vertices),
        "contradiction": residual.contradiction,
        "components": [
            {
                "vertices": list(component.vertices),
                "flip": component.flip,
                "unaries": [list(unary) for unary in component.unaries],
                "binaries": [list(binary) for binary in component.binaries],
                "ternaries": [list(ternary) for ternary in component.ternaries],
            }
            for component in residual.components
        ],
    }


def pcrnf_bytes(residual: SignedResidual) -> bytes:
    return json.dumps(
        pcrnf_record(residual),
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("utf-8")


def unoriented_pcrnf_key(residual: SignedResidual) -> tuple[object, ...]:
    """Return the intentionally unsafe key obtained by dropping flip bits."""
    if not isinstance(residual, SignedResidual):
        raise ValidationError("residual must be a SignedResidual")
    return (
        residual.remaining_vertices,
        residual.contradiction,
        tuple(
            (
                component.vertices,
                component.unaries,
                component.binaries,
                component.ternaries,
            )
            for component in residual.components
        ),
    )


@dataclass(frozen=True, slots=True)
class PCRNFLevelComparison:
    level: int
    prefix_count: int
    pcrnf_state_count: int
    exact_class_count: int
    live_pcrnf_state_count: int
    dead_pcrnf_state_count: int
    incompleteness_excess: int
    total_unique_encoded_bytes: int

    def __post_init__(self) -> None:
        values = tuple(
            getattr(self, field)
            for field in self.__dataclass_fields__
        )
        if any(type(value) is not int or value < 0 for value in values):
            raise ValidationError("PCRNF comparison metrics must be nonnegative integers")
        if self.pcrnf_state_count != (
            self.live_pcrnf_state_count + self.dead_pcrnf_state_count
        ):
            raise ValidationError("live and dead PCRNF states must partition all states")
        if self.pcrnf_state_count < self.exact_class_count:
            raise ValidationError("a sound PCRNF quotient cannot be smaller than the exact quotient")
        if self.incompleteness_excess != (
            self.pcrnf_state_count - self.exact_class_count
        ):
            raise ValidationError("PCRNF incompleteness excess is inconsistent")


@dataclass(frozen=True, slots=True)
class PCRNFProfileComparison:
    ordering: tuple[int, ...]
    levels: tuple[PCRNFLevelComparison, ...]

    @property
    def peak_states(self) -> int:
        return max(level.pcrnf_state_count for level in self.levels)

    @property
    def total_states(self) -> int:
        return sum(level.pcrnf_state_count for level in self.levels)

    @property
    def total_encoded_bytes(self) -> int:
        return sum(level.total_unique_encoded_bytes for level in self.levels)


def compare_pcrnf_profile(
    instance: Hypergraph3,
    ordering: object,
) -> PCRNFProfileComparison:
    """Compare PCRNF byte equality with exact completion-mask equality."""
    instance = _require_instance(instance)
    ordering = validate_ordering(instance, ordering)
    exact = build_exact_profile(instance, ordering)
    comparisons: list[PCRNFLevelComparison] = []
    for level in range(instance.n + 1):
        residual_to_masks: dict[SignedResidual, set[int]] = {}
        exact_masks: set[int] = set()
        live_states: set[SignedResidual] = set()
        dead_states: set[SignedResidual] = set()
        for prefix in itertools.product((0, 1), repeat=level):
            residual = build_pcrnf(instance, ordering, prefix)
            exact_level = exact.levels[level]
            prefix_index = 0
            for bit in prefix:
                prefix_index = (prefix_index << 1) | bit
            class_id = exact_level.assignment_class_ids[prefix_index]
            exact_mask = exact_level.class_masks[class_id]
            actual_mask = pcrnf_completion_mask(
                residual,
                ordering[level:],
            )
            if actual_mask != exact_mask:
                raise AssertionError("PCRNF semantics disagree with the exact profile")
            residual_to_masks.setdefault(residual, set()).add(exact_mask)
            exact_masks.add(exact_mask)
            if exact_mask:
                live_states.add(residual)
            else:
                dead_states.add(residual)
        if any(len(masks) != 1 for masks in residual_to_masks.values()):
            raise AssertionError("one PCRNF has multiple exact completion masks")
        states = tuple(residual_to_masks)
        comparisons.append(
            PCRNFLevelComparison(
                level=level,
                prefix_count=1 << level,
                pcrnf_state_count=len(states),
                exact_class_count=len(exact_masks),
                live_pcrnf_state_count=len(live_states),
                dead_pcrnf_state_count=len(dead_states),
                incompleteness_excess=len(states) - len(exact_masks),
                total_unique_encoded_bytes=sum(
                    len(pcrnf_bytes(state)) for state in states
                ),
            )
        )
    return PCRNFProfileComparison(ordering, tuple(comparisons))


def traverse_pcrnf(
    instance: Hypergraph3,
    ordering: object,
) -> tuple[tuple[SignedResidual, ...], ...]:
    """Construct the memoized PCRNF state graph level by level."""
    instance = _require_instance(instance)
    ordering = validate_ordering(instance, ordering)
    levels: list[tuple[SignedResidual, ...]] = [
        (build_pcrnf(instance, ordering, ()),)
    ]
    for vertex in ordering:
        next_states = {
            transition_pcrnf(state, vertex, colour)
            for state in levels[-1]
            for colour in (0, 1)
        }
        levels.append(tuple(sorted(next_states, key=pcrnf_bytes)))
    return tuple(levels)
