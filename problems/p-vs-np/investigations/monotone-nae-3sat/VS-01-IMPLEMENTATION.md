# VS-01 Implementation Specification — Canonical Instance Model

**Slice:** `VS-01`  
**Status:** `COMPLETE / CHECKED`  
**Updated:** 2026-07-22

## Purpose

Provide the single executable representation used by later Monotone NAE-3SAT experiments, finite proof checks, oracles, profile engines, and corpora. This slice does not decide satisfiability.

## Runtime and layout

Use Python 3.11 or later and the standard library only.

```text
tools/monotone-nae-3sat/
├── README.md
├── nae3sat/
│   ├── __init__.py
│   ├── cli.py
│   ├── errors.py
│   ├── model.py
│   └── serialization.py
└── tests/
    ├── fixtures/
    └── test_vs01.py
```

Generated experimental results belong under the investigation's `experiments/` directory, not under `tools/`.

## Canonical mathematical object

An instance is

\[
H=(V,E),\qquad V=\{0,1,\ldots,n-1\},\qquad E\subseteq\binom{V}{3}.
\]

Isolated vertices are preserved in canonical identity. Removing them is a separate satisfiability-preserving operation.

The explicit vertex list prevents a succinct-encoding ambiguity: an `O(n+m)` algorithm must be polynomial in actual encoded length, so all `n` vertices are serialized explicitly.

## Core values

```python
@dataclass(frozen=True, slots=True)
class Hypergraph3:
    n: int
    edges: tuple[tuple[int, int, int], ...]

@dataclass(frozen=True, slots=True)
class RelabeledHypergraph3:
    graph: Hypergraph3
    new_to_old: tuple[int, ...]
```

### `Hypergraph3` invariants

- `n` is a nonnegative strict integer;
- every edge is a tuple of exactly three strict integer labels;
- edge labels satisfy `0 <= u < v < w < n`;
- the edge tuple is strictly lexicographically increasing;
- duplicates are absent.

Direct construction rejects noncanonical values. `normalize_instance` is the normalizing construction path.

### Relabelling invariants

- `len(new_to_old) == graph.n`;
- `new_to_old` is strictly increasing;
- new vertex `i` represents original vertex `new_to_old[i]`.

## Public API

```python
def normalize_instance(n, edges) -> Hypergraph3: ...
def parse_instance_json(data) -> Hypergraph3: ...
def to_canonical_json(instance) -> str: ...
def canonical_bytes(instance) -> bytes: ...
def instance_id(instance) -> str: ...
def encoded_size_bytes(instance) -> int: ...
def incidence_components(instance) -> tuple[tuple[int, ...], ...]: ...
def induced_subinstance(instance, vertices) -> RelabeledHypergraph3: ...
def active_core(instance) -> RelabeledHypergraph3: ...
def verify_coloring(instance, coloring) -> bool: ...
def first_violated_edge(instance, coloring) -> tuple[int, int, int] | None: ...
```

All public operations requiring an instance reject non-`Hypergraph3` values explicitly.

## Versioned JSON schema

Canonical output is:

```json
{"format":"nae3-v1","vertices":[0,1,2,3],"edges":[[0,1,2],[1,2,3]]}
```

The parser requires exactly the keys `format`, `vertices`, and `edges`; the format must be `nae3-v1`; the vertex array must be a permutation of `0,...,n-1`; and every edge must be a three-element integer array.

It rejects:

- duplicate or unknown keys;
- missing fields;
- unsupported versions;
- invalid UTF-8;
- `NaN` and `Infinity`;
- Boolean and floating-point labels;
- malformed edges and repeated edge vertices.

Input ordering and duplicate edges may be noncanonical; parsing normalizes them. Canonical output is compact UTF-8 with key order `format`, `vertices`, `edges`.

## Stable identifier

```text
instance_id(H) = "nae3-v1-sha256-" + hex(SHA256(canonical_bytes(H)))
```

This is canonical for a fixed labelling, not up to hypergraph isomorphism.

## Component and relabelling semantics

`incidence_components` includes isolated singleton vertices and returns components in increasing least-vertex order.

`induced_subinstance`:

- accepts an iterable of unique valid labels;
- rejects Booleans, duplicates, and out-of-range labels;
- orders selected labels increasingly;
- retains exactly edges fully contained in the selected set;
- returns the new-to-old map.

`active_core` selects exactly vertices occurring in an edge.

An increasing relabelling preserves the canonical order of the retained edge subsequence, so no second sorting or normalization pass is used.

## Colouring contract

A colouring must be a non-string finite `Sequence` of length `n` whose entries are strict integers `0` or `1`.

Sets, mappings, generators, strings, byte strings, Booleans, floating-point values, nonbinary integers, and wrong-length sequences are rejected with `ColoringError`.

An edge `(u,v,w)` is satisfied exactly when:

```python
not (coloring[u] == coloring[v] == coloring[w])
```

`first_violated_edge` returns the first monochromatic edge in canonical edge order. `verify_coloring` is true exactly when no violated edge exists.

## Complexity obligations

Let `n` be explicit vertex count, `m` supplied edge count, and `L` canonical byte length.

- normalization: expected `O(m)` hashing plus `O(m log m)` edge sorting;
- strict parsing and vertex validation: `O(L)`;
- serialization, hashing, and byte measurement: `O(L)`;
- witness validation and checking: `O(n+m)`;
- components: `O(n+m)`;
- selected-vertex validation: `O(n+k)` for `k` supplied labels;
- induced subinstance and active core: `O(n+m)`;
- retained memory: `O(n+m)`.

All claims are polynomial in the explicit encoded input length.

## Reproducible verification

```bash
cd tools/monotone-nae-3sat
python3 -m unittest discover -s tests -v
python3 -m nae3sat.cli validate tests/fixtures/fano-plane.json
```

The committed suite covers canonical construction, strict parsing, serialization, pinned identifiers, components, relabelling, colouring validation, CLI behavior, wrong public types, and a deterministic 1,350-instance independent reference cross-check with seed `20260722`.

## Exit gate determination

The package, APIs, fixtures, tests, CLI, pinned identifiers, complexity audit, and authoritative progress records are present. `VS-01` is complete.

## Non-goals

This slice contains no satisfiability solver, exhaustive instance corpus, extension-profile engine, graph-isomorphism canon, or implication for `P=NP` or `P!=NP`.
