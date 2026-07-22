"""Exact extension profiles for fixed labelled instances and orderings."""

from __future__ import annotations

import itertools
import json
from collections.abc import Sequence as SequenceABC
from dataclasses import dataclass

from .errors import ValidationError
from .model import Hypergraph3
from .serialization import instance_id


def _require_instance(instance: object) -> Hypergraph3:
    if not isinstance(instance, Hypergraph3):
        raise ValidationError("instance must be a Hypergraph3")
    return instance


def _validate_bits(bits: object, *, maximum: int) -> tuple[int, ...]:
    if isinstance(bits, (str, bytes, bytearray)) or not isinstance(
        bits, SequenceABC
    ):
        raise ValidationError("prefix bits must be a finite non-string sequence")
    values = tuple(bits)
    if len(values) > maximum:
        raise ValidationError("prefix is longer than the ordering")
    if any(type(value) is not int or value not in (0, 1) for value in values):
        raise ValidationError("prefix bits must be strict integer bits")
    return values


def _bits_index(bits: tuple[int, ...]) -> int:
    value = 0
    for bit in bits:
        value = (value << 1) | bit
    return value


def validate_ordering(instance: Hypergraph3, ordering: object) -> tuple[int, ...]:
    instance = _require_instance(instance)
    if isinstance(ordering, (str, bytes, bytearray)) or not isinstance(
        ordering, SequenceABC
    ):
        raise ValidationError("ordering must be a finite non-string sequence")
    values = tuple(ordering)
    if len(values) != instance.n:
        raise ValidationError("ordering length must equal the vertex count")
    if any(type(vertex) is not int for vertex in values):
        raise ValidationError("ordering entries must be integers excluding Booleans")
    if set(values) != set(range(instance.n)):
        raise ValidationError("ordering must be a permutation of 0, ..., n-1")
    return values


def _satisfies_ordered(
    instance: Hypergraph3,
    ordering: tuple[int, ...],
    assignment: tuple[int, ...],
) -> bool:
    colours = [0] * instance.n
    for position, vertex in enumerate(ordering):
        colours[vertex] = assignment[position]
    return all(
        not (colours[u] == colours[v] == colours[w])
        for u, v, w in instance.edges
    )


def _boundary(
    instance: Hypergraph3,
    ordering: tuple[int, ...],
    index: int,
) -> tuple[int, ...]:
    remainder = set(ordering[index:])
    return tuple(
        vertex
        for vertex in ordering[:index]
        if any(
            vertex in edge and any(other in remainder for other in edge)
            for edge in instance.edges
        )
    )


def _processed_valid_boundary_states(
    instance: Hypergraph3,
    ordering: tuple[int, ...],
    index: int,
    boundary: tuple[int, ...],
) -> int:
    positions = {
        vertex: position for position, vertex in enumerate(ordering[:index])
    }
    completed = tuple(
        edge
        for edge in instance.edges
        if all(vertex in positions for vertex in edge)
    )
    states: set[tuple[int, ...]] = set()
    for prefix in itertools.product((0, 1), repeat=index):
        if all(
            not (
                prefix[positions[u]]
                == prefix[positions[v]]
                == prefix[positions[w]]
            )
            for u, v, w in completed
        ):
            states.add(
                tuple(prefix[positions[vertex]] for vertex in boundary)
            )
    return len(states)


def _validate_vertex_tuple(name: str, value: object) -> tuple[int, ...]:
    if type(value) is not tuple:
        raise ValidationError(f"{name} must be a tuple")
    if any(type(vertex) is not int or vertex < 0 for vertex in value):
        raise ValidationError(f"{name} must contain nonnegative integer vertices")
    if len(set(value)) != len(value):
        raise ValidationError(f"{name} must not contain duplicate vertices")
    return value


@dataclass(frozen=True, slots=True)
class ProfileLevel:
    index: int
    prefix_vertices: tuple[int, ...]
    remainder_vertices: tuple[int, ...]
    boundary_vertices: tuple[int, ...]
    assignment_class_ids: tuple[int, ...]
    class_masks: tuple[int, ...]
    transitions: tuple[tuple[int, int], ...] | None
    processed_valid_boundary_states: int

    def __post_init__(self) -> None:
        if type(self.index) is not int or self.index < 0:
            raise ValidationError("level index must be a nonnegative integer")
        prefix = _validate_vertex_tuple("prefix_vertices", self.prefix_vertices)
        remainder = _validate_vertex_tuple(
            "remainder_vertices", self.remainder_vertices
        )
        boundary = _validate_vertex_tuple(
            "boundary_vertices", self.boundary_vertices
        )
        if len(prefix) != self.index:
            raise ValidationError("prefix length must equal the level index")
        if set(prefix) & set(remainder):
            raise ValidationError("prefix and remainder vertices must be disjoint")
        if not set(boundary) <= set(prefix):
            raise ValidationError("boundary vertices must belong to the prefix")
        if type(self.assignment_class_ids) is not tuple:
            raise ValidationError("assignment class map must be a tuple")
        if len(self.assignment_class_ids) != 1 << self.index:
            raise ValidationError("assignment class map has the wrong length")
        if type(self.class_masks) is not tuple or not self.class_masks:
            raise ValidationError("each level must contain a nonempty mask tuple")
        if any(type(mask) is not int or mask < 0 for mask in self.class_masks):
            raise ValidationError("class masks must be nonnegative integers")
        if len(set(self.class_masks)) != len(self.class_masks):
            raise ValidationError("class masks must be pairwise distinct")
        if any(
            type(class_id) is not int
            or class_id < 0
            or class_id >= len(self.class_masks)
            for class_id in self.assignment_class_ids
        ):
            raise ValidationError("assignment class identifier is out of range")

        seen: set[int] = set()
        next_identifier = 0
        for class_id in self.assignment_class_ids:
            if class_id not in seen:
                if class_id != next_identifier:
                    raise ValidationError(
                        "class identifiers must follow first-occurrence order"
                    )
                seen.add(class_id)
                next_identifier += 1
        if len(seen) != len(self.class_masks):
            raise ValidationError("every class must occur in the assignment map")

        if self.transitions is not None:
            if type(self.transitions) is not tuple:
                raise ValidationError("transitions must be a tuple or None")
            if len(self.transitions) != len(self.class_masks):
                raise ValidationError("transition count must equal the class count")
            for transition in self.transitions:
                if (
                    type(transition) is not tuple
                    or len(transition) != 2
                    or any(
                        type(class_id) is not int or class_id < 0
                        for class_id in transition
                    )
                ):
                    raise ValidationError(
                        "each transition must be a pair of nonnegative class identifiers"
                    )
        if (
            type(self.processed_valid_boundary_states) is not int
            or self.processed_valid_boundary_states < 0
        ):
            raise ValidationError("boundary-state count must be nonnegative")
        if self.processed_valid_boundary_states > 1 << len(boundary):
            raise ValidationError("boundary-state count exceeds its state space")

    @property
    def raw_assignment_count(self) -> int:
        return len(self.assignment_class_ids)

    @property
    def class_count(self) -> int:
        return len(self.class_masks)

    @property
    def live_class_count(self) -> int:
        return sum(mask != 0 for mask in self.class_masks)

    @property
    def dead_class_id(self) -> int | None:
        try:
            return self.class_masks.index(0)
        except ValueError:
            return None


@dataclass(frozen=True, slots=True)
class ExactProfile:
    instance: Hypergraph3
    ordering: tuple[int, ...]
    levels: tuple[ProfileLevel, ...]

    def __post_init__(self) -> None:
        instance = _require_instance(self.instance)
        ordering = validate_ordering(instance, self.ordering)
        if type(self.levels) is not tuple:
            raise ValidationError("profile levels must be a tuple")
        if len(self.levels) != instance.n + 1:
            raise ValidationError("profile must contain one level per prefix length")

        for index, level in enumerate(self.levels):
            if not isinstance(level, ProfileLevel):
                raise ValidationError("every profile level must be a ProfileLevel")
            if level.index != index:
                raise ValidationError(
                    "profile levels must be in increasing index order"
                )
            if level.prefix_vertices != ordering[:index]:
                raise ValidationError(
                    "level prefix vertices disagree with the ordering"
                )
            if level.remainder_vertices != ordering[index:]:
                raise ValidationError(
                    "level remainder vertices disagree with the ordering"
                )
            expected_boundary = _boundary(instance, ordering, index)
            if level.boundary_vertices != expected_boundary:
                raise ValidationError("level boundary is not the exact processed boundary")
            expected_boundary_count = _processed_valid_boundary_states(
                instance,
                ordering,
                index,
                expected_boundary,
            )
            if level.processed_valid_boundary_states != expected_boundary_count:
                raise ValidationError("level boundary-state count is incorrect")

            completion_width = 1 << (instance.n - index)
            if any(mask.bit_length() > completion_width for mask in level.class_masks):
                raise ValidationError("class mask exceeds its semantic completion width")

            if index == instance.n:
                if level.transitions is not None:
                    raise ValidationError("the final level cannot have transitions")
                if any(mask not in (0, 1) for mask in level.class_masks):
                    raise ValidationError("final-level class masks must be zero or one")
            elif level.transitions is None:
                raise ValidationError("nonfinal levels require transitions")

        final = self.levels[instance.n]
        for assignment_index, assignment in enumerate(
            itertools.product((0, 1), repeat=instance.n)
        ):
            class_id = final.assignment_class_ids[assignment_index]
            actual = final.class_masks[class_id]
            expected = 1 if _satisfies_ordered(instance, ordering, assignment) else 0
            if actual != expected:
                raise ValidationError(
                    "final assignment classes disagree with instance satisfaction"
                )

        for index in range(instance.n):
            level = self.levels[index]
            next_level = self.levels[index + 1]
            assert level.transitions is not None
            child_width = 1 << (instance.n - index - 1)
            lower_mask = (1 << child_width) - 1

            for class_id, transition in enumerate(level.transitions):
                zero_class, one_class = transition
                if (
                    zero_class >= next_level.class_count
                    or one_class >= next_level.class_count
                ):
                    raise ValidationError("transition target is out of range")
                mask = level.class_masks[class_id]
                if next_level.class_masks[zero_class] != mask & lower_mask:
                    raise ValidationError("zero transition disagrees with mask slicing")
                if next_level.class_masks[one_class] != mask >> child_width:
                    raise ValidationError("one transition disagrees with mask slicing")

            for prefix, class_id in enumerate(level.assignment_class_ids):
                expected_transition = (
                    next_level.assignment_class_ids[2 * prefix],
                    next_level.assignment_class_ids[2 * prefix + 1],
                )
                if level.transitions[class_id] != expected_transition:
                    raise ValidationError(
                        "class transition disagrees with member assignment successors"
                    )

    @property
    def satisfiable(self) -> bool:
        root = self.levels[0]
        return root.class_masks[root.assignment_class_ids[0]] != 0


def build_exact_profile(
    instance: Hypergraph3,
    ordering: object,
) -> ExactProfile:
    """Construct every exact completion mask and quotient transition."""
    instance = _require_instance(instance)
    ordering = validate_ordering(instance, ordering)
    n = instance.n

    assignment_masks: list[tuple[int, ...]] = [()] * (n + 1)
    assignment_masks[n] = tuple(
        1 if _satisfies_ordered(instance, ordering, assignment) else 0
        for assignment in itertools.product((0, 1), repeat=n)
    )

    for index in range(n - 1, -1, -1):
        child_width = 1 << (n - index - 1)
        children = assignment_masks[index + 1]
        assignment_masks[index] = tuple(
            children[2 * prefix]
            | (children[2 * prefix + 1] << child_width)
            for prefix in range(1 << index)
        )

    assignment_ids: list[tuple[int, ...]] = []
    class_masks: list[tuple[int, ...]] = []
    for masks in assignment_masks:
        mask_to_class: dict[int, int] = {}
        ids: list[int] = []
        classes: list[int] = []
        for mask in masks:
            class_id = mask_to_class.get(mask)
            if class_id is None:
                class_id = len(classes)
                mask_to_class[mask] = class_id
                classes.append(mask)
            ids.append(class_id)
        assignment_ids.append(tuple(ids))
        class_masks.append(tuple(classes))

    levels: list[ProfileLevel] = []
    for index in range(n + 1):
        transitions = None
        if index < n:
            child_width = 1 << (n - index - 1)
            lower_mask = (1 << child_width) - 1
            next_lookup = {
                mask: class_id
                for class_id, mask in enumerate(class_masks[index + 1])
            }
            transition_rows: list[tuple[int, int]] = []
            for mask in class_masks[index]:
                lower = mask & lower_mask
                upper = mask >> child_width
                if lower not in next_lookup or upper not in next_lookup:
                    raise AssertionError("exact mask slice has no successor class")
                transition_rows.append((next_lookup[lower], next_lookup[upper]))
            transitions = tuple(transition_rows)

        boundary = _boundary(instance, ordering, index)
        levels.append(
            ProfileLevel(
                index=index,
                prefix_vertices=ordering[:index],
                remainder_vertices=ordering[index:],
                boundary_vertices=boundary,
                assignment_class_ids=assignment_ids[index],
                class_masks=class_masks[index],
                transitions=transitions,
                processed_valid_boundary_states=_processed_valid_boundary_states(
                    instance,
                    ordering,
                    index,
                    boundary,
                ),
            )
        )

    return ExactProfile(instance, ordering, tuple(levels))


def extension_mask(
    instance: Hypergraph3,
    ordering: object,
    prefix_bits: object,
) -> int:
    """Return the exact completion mask for one prefix assignment."""
    instance = _require_instance(instance)
    ordering = validate_ordering(instance, ordering)
    bits = _validate_bits(prefix_bits, maximum=instance.n)
    profile = build_exact_profile(instance, ordering)
    level = profile.levels[len(bits)]
    class_id = level.assignment_class_ids[_bits_index(bits)]
    return level.class_masks[class_id]


def _fixed_hex(mask: int, bit_width: int) -> str:
    digits = max(1, (bit_width + 3) // 4)
    return format(mask, f"0{digits}x")


def profile_record(profile: ExactProfile) -> dict[str, object]:
    """Return the canonical semantic record for a fixed profile."""
    if not isinstance(profile, ExactProfile):
        raise ValidationError("profile must be an ExactProfile")

    level_records: list[dict[str, object]] = []
    for level in profile.levels:
        completion_width = 1 << len(level.remainder_vertices)
        class_id_bits = (
            0
            if level.class_count <= 1
            else (level.class_count - 1).bit_length()
        )
        next_class_count = (
            profile.levels[level.index + 1].class_count
            if level.index < profile.instance.n
            else 0
        )
        next_id_bits = (
            0
            if next_class_count <= 1
            else (next_class_count - 1).bit_length()
        )
        level_records.append(
            {
                "index": level.index,
                "prefix_vertices": list(level.prefix_vertices),
                "remainder_vertices": list(level.remainder_vertices),
                "boundary_vertices": list(level.boundary_vertices),
                "raw_assignments": level.raw_assignment_count,
                "class_count": level.class_count,
                "live_class_count": level.live_class_count,
                "processed_valid_boundary_states": (
                    level.processed_valid_boundary_states
                ),
                "dense_unique_completion_bits": (
                    level.class_count * completion_width
                ),
                "assignment_map_bits": (
                    level.raw_assignment_count * class_id_bits
                ),
                "transition_bits": (
                    0
                    if level.transitions is None
                    else 2 * level.class_count * next_id_bits
                ),
                "class_masks": [
                    _fixed_hex(mask, completion_width)
                    for mask in level.class_masks
                ],
                "assignment_class_ids": list(level.assignment_class_ids),
                "transitions": (
                    None
                    if level.transitions is None
                    else [list(transition) for transition in level.transitions]
                ),
            }
        )

    return {
        "format": "nae3-vs03-profile-v1",
        "id": instance_id(profile.instance),
        "ordering": list(profile.ordering),
        "satisfiable": profile.satisfiable,
        "levels": level_records,
    }


def profile_bytes(profile: ExactProfile) -> bytes:
    return json.dumps(
        profile_record(profile),
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("utf-8")
