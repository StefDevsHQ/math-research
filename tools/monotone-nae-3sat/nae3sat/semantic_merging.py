"""Exact VS-07 measurements of live semantic merging and symmetry."""

from __future__ import annotations

from dataclasses import dataclass

from .controls import processed_boundary
from .errors import ValidationError
from .model import Hypergraph3, incidence_components, normalize_instance
from .profile import ExactProfile, build_exact_profile, profile_bytes, validate_ordering


def _require_instance(instance: object) -> Hypergraph3:
    if not isinstance(instance, Hypergraph3):
        raise ValidationError("instance must be a Hypergraph3")
    return instance


def _strict_level(value: object, n: int) -> int:
    if type(value) is not int or value < 0 or value > n:
        raise ValidationError("level must be an integer between zero and n")
    return value


def _prefix_bit(prefix_index: int, level: int, position: int) -> int:
    return (prefix_index >> (level - 1 - position)) & 1


def _project_prefix(
    prefix_index: int,
    level: int,
    positions: tuple[int, ...],
) -> int:
    result = 0
    for position in positions:
        result = (result << 1) | _prefix_bit(prefix_index, level, position)
    return result


def _processed_consistent(
    instance: Hypergraph3,
    positions: dict[int, int],
    level: int,
    prefix_index: int,
) -> bool:
    for edge in instance.edges:
        edge_positions = tuple(positions[vertex] for vertex in edge)
        if max(edge_positions) >= level:
            continue
        values = tuple(
            _prefix_bit(prefix_index, level, position)
            for position in edge_positions
        )
        if values[0] == values[1] == values[2]:
            return False
    return True


def _component_flip_group(
    instance: Hypergraph3,
    ordering: tuple[int, ...],
    level: int,
) -> tuple[tuple[int, int], ...]:
    positions = {vertex: index for index, vertex in enumerate(ordering)}
    generators: list[tuple[int, int]] = []
    for component in incidence_components(instance):
        prefix_xor = 0
        suffix_xor = 0
        for vertex in component:
            position = positions[vertex]
            if position < level:
                prefix_xor ^= 1 << (level - 1 - position)
            else:
                suffix_xor ^= 1 << (instance.n - 1 - position)
        generators.append((prefix_xor, suffix_xor))

    group: set[tuple[int, int]] = {(0, 0)}
    for prefix_generator, suffix_generator in generators:
        translated = {
            (
                prefix ^ prefix_generator,
                suffix ^ suffix_generator,
            )
            for prefix, suffix in group
        }
        group |= translated
    return tuple(sorted(group))


def _permute_completion_mask(mask: int, suffix_xor: int) -> int:
    result = 0
    remaining = mask
    while remaining:
        lowest = remaining & -remaining
        index = lowest.bit_length() - 1
        result |= 1 << (index ^ suffix_xor)
        remaining -= lowest
    return result


def _fixed_width_payload_bytes(count: int, bit_width: int) -> int:
    """Raw fixed-width payload bytes, excluding framing and metadata."""
    return count * ((bit_width + 7) // 8)


def _packed_identifier_payload_bytes(item_count: int, class_count: int) -> int:
    """Raw packed identifier bytes, excluding framing and metadata."""
    bits_per_identifier = (
        0 if class_count <= 1 else (class_count - 1).bit_length()
    )
    return (item_count * bits_per_identifier + 7) // 8


@dataclass(frozen=True, slots=True)
class SemanticMergingLevel:
    level: int
    prefix_count: int
    live_prefix_count: int
    dead_prefix_count: int
    semantic_class_count: int
    live_semantic_class_count: int
    dead_class_count: int
    live_prefix_component_orbit_count: int
    live_semantic_component_orbit_count: int
    exact_cross_orbit_merge_class_count: int
    exact_cross_orbit_merge_excess: int
    orbit_normalized_merge_excess: int
    boundary_width: int
    processed_valid_boundary_state_count: int
    live_boundary_state_count: int
    dead_boundary_state_count: int
    completion_bits_per_mask: int
    dense_semantic_mask_bytes: int
    dense_live_semantic_mask_bytes: int
    packed_assignment_class_bytes: int
    explicit_live_boundary_bytes: int

    def __post_init__(self) -> None:
        integer_fields = tuple(
            getattr(self, field)
            for field in self.__dataclass_fields__
        )
        if any(type(value) is not int or value < 0 for value in integer_fields):
            raise ValidationError(
                "semantic-merging metrics must be nonnegative integers"
            )
        if self.prefix_count != self.live_prefix_count + self.dead_prefix_count:
            raise ValidationError("live and dead prefixes must partition all prefixes")
        if self.semantic_class_count != (
            self.live_semantic_class_count + self.dead_class_count
        ):
            raise ValidationError(
                "live and dead classes must partition semantic classes"
            )
        if self.dead_class_count not in (0, 1):
            raise ValidationError("there is at most one empty completion class")
        if self.live_semantic_class_count > self.live_boundary_state_count:
            raise ValidationError(
                "exact boundary states must determine live semantics"
            )
        if self.processed_valid_boundary_state_count != (
            self.live_boundary_state_count + self.dead_boundary_state_count
        ):
            raise ValidationError(
                "live and dead boundary states must partition valid states"
            )
        if self.live_semantic_component_orbit_count > (
            self.live_prefix_component_orbit_count
        ):
            raise ValidationError(
                "semantic symmetry quotient cannot exceed prefix orbit count"
            )
        if self.orbit_normalized_merge_excess != (
            self.live_prefix_component_orbit_count
            - self.live_semantic_component_orbit_count
        ):
            raise ValidationError(
                "orbit-normalized merge excess is inconsistent"
            )


@dataclass(frozen=True, slots=True)
class SemanticMergingProfile:
    instance: Hypergraph3
    ordering: tuple[int, ...]
    levels: tuple[SemanticMergingLevel, ...]
    exact_profile_json_bytes: int

    def __post_init__(self) -> None:
        instance = _require_instance(self.instance)
        ordering = validate_ordering(instance, self.ordering)
        if type(self.levels) is not tuple:
            raise ValidationError("levels must be a tuple")
        if len(self.levels) != instance.n + 1:
            raise ValidationError(
                "one semantic-merging level is required per prefix length"
            )
        for index, level in enumerate(self.levels):
            if not isinstance(level, SemanticMergingLevel):
                raise ValidationError(
                    "every level must be a SemanticMergingLevel"
                )
            if level.level != index:
                raise ValidationError("semantic-merging levels must be ordered")
        if (
            type(self.exact_profile_json_bytes) is not int
            or self.exact_profile_json_bytes < 0
        ):
            raise ValidationError("profile byte size must be nonnegative")
        if ordering != self.ordering:
            raise ValidationError("ordering is not canonical")

    @property
    def peak_live_semantic_classes(self) -> int:
        return max(level.live_semantic_class_count for level in self.levels)

    @property
    def peak_live_semantic_component_orbits(self) -> int:
        return max(
            level.live_semantic_component_orbit_count
            for level in self.levels
        )

    @property
    def peak_live_boundary_states(self) -> int:
        return max(level.live_boundary_state_count for level in self.levels)


def _measure_level_from_exact(
    instance: Hypergraph3,
    ordering: tuple[int, ...],
    exact: ExactProfile,
    level: int,
) -> SemanticMergingLevel:
    exact_level = exact.levels[level]
    prefix_masks = tuple(
        exact_level.class_masks[class_id]
        for class_id in exact_level.assignment_class_ids
    )
    live_prefixes = tuple(
        prefix
        for prefix, mask in enumerate(prefix_masks)
        if mask != 0
    )
    group = _component_flip_group(instance, ordering, level)

    prefix_orbit_representatives = {
        prefix: min(prefix ^ prefix_xor for prefix_xor, _ in group)
        for prefix in live_prefixes
    }
    live_masks = {prefix_masks[prefix] for prefix in live_prefixes}
    semantic_orbit_representatives = {
        mask: min(
            _permute_completion_mask(mask, suffix_xor)
            for _, suffix_xor in group
        )
        for mask in live_masks
    }

    prefix_orbits_by_mask: dict[int, set[int]] = {}
    for prefix in live_prefixes:
        prefix_orbits_by_mask.setdefault(prefix_masks[prefix], set()).add(
            prefix_orbit_representatives[prefix]
        )
    cross_orbit_sizes = tuple(
        len(orbits)
        for orbits in prefix_orbits_by_mask.values()
        if len(orbits) > 1
    )

    ordering_positions = {
        vertex: position for position, vertex in enumerate(ordering)
    }
    boundary_vertices = processed_boundary(instance, ordering, level)
    boundary_positions = tuple(
        ordering_positions[vertex] for vertex in boundary_vertices
    )
    live_boundary_states = {
        _project_prefix(prefix, level, boundary_positions)
        for prefix in live_prefixes
    }
    valid_boundary_states = {
        _project_prefix(prefix, level, boundary_positions)
        for prefix in range(1 << level)
        if _processed_consistent(
            instance,
            ordering_positions,
            level,
            prefix,
        )
    }
    if len(valid_boundary_states) != exact_level.processed_valid_boundary_states:
        raise AssertionError(
            "independent boundary-state count disagrees with VS-03"
        )
    if not live_boundary_states <= valid_boundary_states:
        raise AssertionError("live boundary state was not processed-valid")

    live_prefix_component_orbits = len(
        set(prefix_orbit_representatives.values())
    )
    live_semantic_component_orbits = len(
        set(semantic_orbit_representatives.values())
    )
    semantic_class_count = len(exact_level.class_masks)
    live_semantic_class_count = sum(
        mask != 0 for mask in exact_level.class_masks
    )
    completion_bits = 1 << (instance.n - level)
    boundary_width = len(boundary_vertices)

    return SemanticMergingLevel(
        level=level,
        prefix_count=1 << level,
        live_prefix_count=len(live_prefixes),
        dead_prefix_count=(1 << level) - len(live_prefixes),
        semantic_class_count=semantic_class_count,
        live_semantic_class_count=live_semantic_class_count,
        dead_class_count=int(0 in exact_level.class_masks),
        live_prefix_component_orbit_count=live_prefix_component_orbits,
        live_semantic_component_orbit_count=live_semantic_component_orbits,
        exact_cross_orbit_merge_class_count=len(cross_orbit_sizes),
        exact_cross_orbit_merge_excess=sum(
            size - 1 for size in cross_orbit_sizes
        ),
        orbit_normalized_merge_excess=(
            live_prefix_component_orbits
            - live_semantic_component_orbits
        ),
        boundary_width=boundary_width,
        processed_valid_boundary_state_count=len(valid_boundary_states),
        live_boundary_state_count=len(live_boundary_states),
        dead_boundary_state_count=len(
            valid_boundary_states - live_boundary_states
        ),
        completion_bits_per_mask=completion_bits,
        dense_semantic_mask_bytes=_fixed_width_payload_bytes(
            semantic_class_count,
            completion_bits,
        ),
        dense_live_semantic_mask_bytes=_fixed_width_payload_bytes(
            live_semantic_class_count,
            completion_bits,
        ),
        packed_assignment_class_bytes=_packed_identifier_payload_bytes(
            1 << level,
            semantic_class_count,
        ),
        explicit_live_boundary_bytes=_fixed_width_payload_bytes(
            len(live_boundary_states),
            boundary_width,
        ),
    )


def measure_semantic_merging_level(
    instance: Hypergraph3,
    ordering: object,
    level: object,
) -> SemanticMergingLevel:
    instance = _require_instance(instance)
    ordering = validate_ordering(instance, ordering)
    level = _strict_level(level, instance.n)
    exact = build_exact_profile(instance, ordering)
    return _measure_level_from_exact(instance, ordering, exact, level)


def measure_semantic_merging_profile(
    instance: Hypergraph3,
    ordering: object,
) -> SemanticMergingProfile:
    instance = _require_instance(instance)
    ordering = validate_ordering(instance, ordering)
    exact = build_exact_profile(instance, ordering)
    levels = tuple(
        _measure_level_from_exact(instance, ordering, exact, level)
        for level in range(instance.n + 1)
    )
    return SemanticMergingProfile(
        instance=instance,
        ordering=ordering,
        levels=levels,
        exact_profile_json_bytes=len(profile_bytes(exact)),
    )


def fan_instance(edge_count: object) -> Hypergraph3:
    if type(edge_count) is not int or edge_count < 1:
        raise ValidationError("fan edge count must be a positive integer")
    return normalize_instance(
        2 * edge_count + 1,
        (
            (0, 1 + index, 1 + edge_count + index)
            for index in range(edge_count)
        ),
    )


def fan_bad_ordering(edge_count: object) -> tuple[int, ...]:
    if type(edge_count) is not int or edge_count < 1:
        raise ValidationError("fan edge count must be a positive integer")
    return tuple(
        [0]
        + list(range(1, edge_count + 1))
        + list(range(edge_count + 1, 2 * edge_count + 1))
    )


def fan_good_ordering(edge_count: object) -> tuple[int, ...]:
    if type(edge_count) is not int or edge_count < 1:
        raise ValidationError("fan edge count must be a positive integer")
    ordering = [0]
    for index in range(edge_count):
        ordering.extend((1 + index, 1 + edge_count + index))
    return tuple(ordering)
