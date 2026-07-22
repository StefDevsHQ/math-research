# VS-01 Implementation Specification — Canonical Instance Model

**Slice:** `VS-01`  
**Status:** `PARTIAL` — reviewed and implementation-ready; executable model and tests remain  
**Updated:** 2026-07-22

## Purpose

Create the single executable representation used by later Monotone NAE-3SAT experiments, finite proof checks, oracles, profile engines, and corpora.

This slice does not decide satisfiability. It establishes:

- what an encoded instance is;
- how input is validated and normalized;
- how canonical bytes and stable identifiers are produced;
- how incidence components and relabelled subinstances are computed;
- how a proposed colouring is checked.

The mathematical object remains the one defined in `OBJECT.md`. This file specifies its executable realization.

## Implementation decision

Use **Python 3.11 or later** and the standard library only.

Reasons:

- exhaustive small-instance work benefits from direct integer and bit operations;
- a standard-library-only runtime keeps the laboratory portable;
- Python is sufficient for the initial exhaustive domains;
- later optimized implementations can preserve the same canonical format and semantics.

Tests use `unittest`. No package installation, third-party build backend, or manual `PYTHONPATH` modification is required.

## Repository layout

Use a flat package so all commands work from a clean checkout with the Python standard library alone:

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
    ├── test_model.py
    ├── test_serialization.py
    ├── test_components.py
    └── test_verifier.py
```

Generated experimental results belong under the investigation's future `experiments/` directory, not under `tools/`.

## Canonical mathematical object

An instance is

\[
H=(V,E),
\qquad
V=\{0,1,\ldots,n-1\},
\qquad
E\subseteq\binom{V}{3}.
\]

The executable model preserves isolated vertices. Removing them is a separate satisfiability-preserving derived operation, not part of canonical identity.

### Encoding discipline

The canonical serialized form explicitly lists every vertex. This is deliberate.

Storing only `n` in binary while allowing arbitrarily many isolated vertices would create a succinct encoding in which iterating over all vertices or writing a total colouring could take time exponential in the encoded length. Explicit vertex enumeration ensures that:

\[
L=\Theta((n+m)\log(n+1))
\]

up to fixed JSON punctuation under the selected decimal encoding, and that all `O(n+m)` operations below are polynomial in the actual input length.

## Core data types

```python
from dataclasses import dataclass
from typing import Iterable, Sequence, TypeAlias

Vertex: TypeAlias = int
Edge: TypeAlias = tuple[Vertex, Vertex, Vertex]
Coloring: TypeAlias = tuple[int, ...]

@dataclass(frozen=True, slots=True)
class Hypergraph3:
    n: int
    edges: tuple[Edge, ...]

    def __post_init__(self) -> None:
        """Reject any value that is not already in canonical internal form."""

@dataclass(frozen=True, slots=True)
class RelabeledHypergraph3:
    graph: Hypergraph3
    new_to_old: tuple[Vertex, ...]
```

`normalize_instance` is the normalizing construction path. Direct `Hypergraph3(...)` construction remains public for tests and internal use, but `__post_init__` must reject noncanonical values rather than silently normalize them.

### `Hypergraph3` invariants

Every constructed value must satisfy:

1. `n` is an integer, not a Boolean;
2. `n >= 0`;
3. vertices are exactly `0, ..., n-1`;
4. `edges` is a tuple of edge tuples;
5. every edge has length three;
6. edge entries are integers, not Booleans;
7. all three vertices in an edge are distinct;
8. every vertex lies in `[0, n)`;
9. each edge is strictly increasing;
10. the edge tuple is lexicographically increasing;
11. duplicate edges are absent.

### `RelabeledHypergraph3` invariants

1. `len(new_to_old) == graph.n`;
2. `new_to_old` is strictly increasing;
3. entry `i` identifies the original vertex represented by new vertex `i`.

The original ambient vertex count is not inferred from this derived object and must be retained by the caller when needed.

## Public API

```python
def normalize_instance(n: int, edges: Iterable[Sequence[int]]) -> Hypergraph3:
    """Validate, sort, deduplicate, and construct a canonical instance."""


def parse_instance_json(data: str | bytes) -> Hypergraph3:
    """Parse the versioned JSON input schema and return a normalized instance."""


def to_canonical_json(instance: Hypergraph3) -> str:
    """Return the unique compact versioned JSON serialization."""


def canonical_bytes(instance: Hypergraph3) -> bytes:
    """Return UTF-8 bytes of the canonical JSON serialization."""


def instance_id(instance: Hypergraph3) -> str:
    """Return 'nae3-v1-sha256-' followed by SHA-256 of canonical bytes."""


def encoded_size_bytes(instance: Hypergraph3) -> int:
    """Return the exact length of canonical bytes."""


def incidence_components(instance: Hypergraph3) -> tuple[tuple[int, ...], ...]:
    """Return all components, including isolated singleton vertices, in canonical order."""


def induced_subinstance(
    instance: Hypergraph3,
    vertices: Iterable[int],
) -> RelabeledHypergraph3:
    """Return the induced subhypergraph relabelled increasingly to 0..k-1."""


def active_core(instance: Hypergraph3) -> RelabeledHypergraph3:
    """Remove isolated vertices and relabel; preserve the new-to-old map."""


def verify_coloring(instance: Hypergraph3, coloring: Sequence[int]) -> bool:
    """Return whether a valid total binary colouring satisfies every edge."""


def first_violated_edge(instance: Hypergraph3, coloring: Sequence[int]) -> Edge | None:
    """Return the first canonical monochromatic edge, or None when the colouring satisfies."""
```

### Derived-subinstance input rules

`induced_subinstance` must reject:

- Boolean vertex labels;
- duplicate requested vertices;
- negative or out-of-range vertices.

The empty vertex set is valid and produces the empty graph with an empty map. Relabelling follows increasing original vertex order, making the map deterministic.

## Versioned JSON schema

Canonical output has exactly this shape:

```json
{"format":"nae3-v1","vertices":[0,1,2,3],"edges":[[0,1,2],[1,2,3]]}
```

Rules:

- the top-level object has exactly `format`, `vertices`, and `edges`;
- `format` is exactly `"nae3-v1"`;
- `vertices` is an explicit array of distinct nonnegative integers;
- after normalization, the vertex set must be exactly `0, ..., n-1`;
- `edges` is an array of arrays of exactly three integer labels;
- integers exclude Booleans and floating-point numbers;
- input vertices and edges may be out of order;
- repeated input edges are accepted and deduplicated;
- repeated vertices inside one edge are rejected;
- unknown or missing keys are rejected;
- duplicate JSON object keys are rejected;
- nonstandard constants such as `NaN` and `Infinity` are rejected;
- invalid UTF-8 bytes are rejected;
- malformed JSON and malformed mathematical instances raise explicit errors.

Canonical output:

- sorts vertices increasingly;
- sorts each edge increasingly;
- sorts and deduplicates edges;
- uses key order `format`, `vertices`, `edges`;
- omits insignificant whitespace;
- uses UTF-8 and a terminal-free byte string.

Use `json.dumps(..., separators=(",", ":"), ensure_ascii=True)` over an insertion-ordered object. Strict parsing requires an `object_pairs_hook` that detects duplicate keys and a `parse_constant` callback that rejects nonstandard numeric constants.

The parser accepts valid noncanonical ordering and produces the canonical instance. Only `to_canonical_json` claims unique canonical output.

## Stable identifier

Define

```text
instance_id(H) = "nae3-v1-sha256-" + hex(SHA256(canonical_bytes(H)))
```

Because the version tag is part of the canonical bytes and prefix, future incompatible formats must use a new version and identifier namespace.

The identifier is canonical for a fixed vertex labelling. It is not canonical up to hypergraph isomorphism.

## Error model

```python
class NAE3Error(Exception): ...
class ParseError(NAE3Error): ...
class ValidationError(NAE3Error): ...
class ColoringError(NAE3Error): ...
```

Required distinction:

- malformed JSON structure or encoding raises `ParseError`;
- a mathematically invalid graph or direct noncanonical construction raises `ValidationError`;
- a malformed colouring raises `ColoringError`;
- a valid total binary colouring that violates an edge returns `False` from `verify_coloring`.

`first_violated_edge` validates the colouring under the same rules before checking edges. `verify_coloring` may be implemented as `first_violated_edge(...) is None` so the two APIs cannot disagree.

## Component semantics

The incidence graph has one node for every vertex and one node for every hyperedge, with an incidence edge connecting each hyperedge to its three vertices.

For a simple 3-uniform hypergraph, two vertices lie in the same nontrivial component exactly when they are connected by a sequence of overlapping hyperedges.

`incidence_components` must:

- include each isolated vertex as a singleton component;
- sort vertices within each component;
- sort components by their least vertex;
- return the empty tuple for `n = 0`.

A deterministic `O(n+m)` implementation may build vertex adjacency from the canonical edge list, mark components by breadth-first or depth-first search, and perform a final increasing scan of vertices to produce sorted groups without sorting each component separately.

The later satisfiability factorization theorem is:

> An instance is satisfiable exactly when each nontrivial incidence component is satisfiable; isolated vertices are unconstrained.

Using this theorem in a solver belongs to `VS-02`, not `VS-01`.

## Colouring semantics

A colouring is a non-string sequence of length `n` whose entries are exactly integers `0` or `1`, excluding Booleans.

For edge `(u, v, w)`, satisfaction is:

```python
not (coloring[u] == coloring[v] == coloring[w])
```

Boundary cases:

- the empty colouring satisfies the empty graph;
- isolated vertices may take either colour;
- duplicate input edges disappear under normalization;
- complementing every bit preserves validity and satisfaction;
- if several edges are violated, `first_violated_edge` returns the first edge in canonical edge order.

## Determinism requirements

For identical labelled mathematical input, every supported construction path must produce:

- equal `Hypergraph3` values;
- byte-identical canonical serialization;
- the same identifier;
- identically ordered components;
- identical relabelling maps;
- the same first violated edge.

No result may depend on hash-table iteration order, process identity, machine architecture, locale, or input edge order.

## Complexity obligations

Let `n` be the explicitly listed vertex count and `m` the number of supplied edges before deduplication.

Under a word-RAM view with `O(log n)`-bit vertex labels:

- JSON structure validation: linear in parsed input size;
- graph normalization: `O(n + m log m)` tuple comparisons;
- serialization and hashing: `O(L)` where `L` is canonical byte length;
- colouring validation and verification: `O(n + m)`;
- incidence components: `O(n + m)`;
- induced subinstance and active core: `O(n + m)` expected time with membership tables, or deterministic `O((n+m) log n)` using ordered lookup;
- retained memory: `O(n + m)` excluding input and output text.

In the bit model, tuple comparisons include the cost of comparing `O(log n)`-bit labels. Every operation above remains polynomial in the explicit canonical byte length. The implementation audit must state which concrete data structures realize the claimed bound.

## Required tests

### Direct construction and normalization

1. `n = 0`, no edges;
2. positive `n`, no edges;
3. unsorted edge becomes sorted through `normalize_instance`;
4. repeated edges are deduplicated;
5. edge collection becomes lexicographically sorted;
6. repeated vertex inside one edge is rejected;
7. negative vertex is rejected;
8. out-of-range vertex is rejected;
9. negative `n` is rejected;
10. Boolean values are rejected where integers are required;
11. floating-point values are rejected;
12. edge with length other than three is rejected;
13. direct `Hypergraph3` construction rejects noncanonical edge order;
14. direct construction rejects duplicate edges;
15. generator and one-shot iterable inputs normalize correctly.

### Parsing and serialization

1. round trip preserves equality;
2. differently ordered valid inputs serialize identically;
3. explicit isolated vertices survive round trip;
4. changing only isolated-vertex count changes canonical bytes and identifier;
5. canonical serialization has no insignificant whitespace;
6. unknown and missing top-level fields are rejected;
7. wrong format version is rejected;
8. duplicate JSON keys are rejected;
9. `NaN` and `Infinity` are rejected;
10. malformed JSON is rejected;
11. invalid UTF-8 is rejected;
12. duplicate or noncontiguous vertex lists are rejected;
13. IDs are stable across round trips;
14. `encoded_size_bytes` equals `len(canonical_bytes(...))`.

### Components and relabelling

1. empty instance has no components;
2. isolated vertices are singleton components;
3. one edge forms one component;
4. overlapping edges form one component;
5. disjoint edges form separate components;
6. mixed isolated and nontrivial components are ordered canonically;
7. induced subinstance relabels increasingly and returns the correct map;
8. empty induced subinstance is valid;
9. duplicate and invalid requested vertices are rejected;
10. `active_core` removes only isolated vertices;
11. `active_core` of an edgeless graph is the empty graph with an empty map.

### Witness verification

1. empty colouring verifies the empty instance;
2. one triple has exactly six satisfying colourings;
3. `000` and `111` fail on one triple;
4. a valid disconnected colouring verifies;
5. the first monochromatic edge is deterministic;
6. every satisfying colouring's complement satisfies;
7. wrong-length colouring raises `ColoringError`;
8. nonbinary integer raises `ColoringError`;
9. Boolean and floating-point entries raise `ColoringError`;
10. strings and bytes are rejected as colouring containers;
11. `verify_coloring` and `first_violated_edge` agree on every colouring of the fixed small fixtures.

### Determinism

1. repeated runs produce identical canonical bytes and IDs;
2. input dictionary and edge iteration order do not affect output;
3. component and relabelling order is stable;
4. fixture IDs are pinned after the format is accepted and must change only under an explicit format-version migration.

## Input fixtures

Create parser and model fixtures for:

- `empty.json`: no vertices and no edges;
- `isolated-three.json`: vertices `0,1,2`, no edges;
- `single-edge.json`: edge `012`;
- `duplicate-unsorted.json`: noncanonical input normalizing to `single-edge.json`;
- `two-disconnected-edges.json`: edges `012` and `345`;
- `overlap-chain.json`: edges `012`, `234`, `456`;
- `fano-plane.json`: vertices `0` through `6` and edges `012`, `034`, `056`, `135`, `146`, `236`, `245`;
- malformed fixtures for duplicate keys, noncontiguous vertices, repeated edge vertices, unknown fields, wrong version, and invalid UTF-8.

`duplicate-unsorted.json` and malformed files are input fixtures, not canonical-output fixtures.

The Fano plane is only data in `VS-01`. Establishing its unsatisfiability belongs to `VS-02` and `VS-05`.

## Command-line validator

Provide:

```bash
python3 -m nae3sat.cli validate path/to/instance.json
```

Successful output is one compact JSON object:

```json
{"format":"nae3-v1-summary","id":"nae3-v1-sha256-...","n":7,"m":7,"components_total":1,"components_nontrivial":1,"encoded_bytes":...}
```

Definitions:

- `components_total` counts isolated singleton components;
- `components_nontrivial` counts components containing at least one hyperedge.

Output goes to standard output. Errors go to standard error with a nonzero exit status. The command validates and summarizes the instance but must not decide satisfiability.

## Reproducible commands

From `tools/monotone-nae-3sat/`:

```bash
python3 -m unittest discover -s tests -v
python3 -m nae3sat.cli validate tests/fixtures/fano-plane.json
```

The tool README must record the exact Python version used in the implementation audit in addition to the supported lower bound.

## Exit gate

`VS-01` becomes `COMPLETE` only when:

1. the package and all listed APIs exist;
2. every class invariant is enforced on all public construction paths;
3. all required tests pass from a clean checkout;
4. all fixtures are committed;
5. the validator command is reproducible;
6. the README records runtime requirements, commands, schemas, output, and limitations;
7. an implementation audit records concrete data structures and verifies the complexity obligations;
8. pinned fixture identifiers are recorded after format acceptance;
9. `VERTICAL-SLICES.md` and `STATUS.md` link the evidence and mark the slice complete.

## Explicit non-goals

This slice must not contain:

- a satisfiability solver;
- exhaustive instance generation;
- extension-profile computation;
- graph-isomorphism reduction;
- heuristic simplification that changes canonical identity;
- a claim that labelled canonical serialization is canonical up to isomorphism;
- silent acceptance of a future schema version.

## First implementation sequence

1. create the flat package layout and error hierarchy;
2. implement strict canonical-form validation in `Hypergraph3.__post_init__`;
3. implement `normalize_instance`;
4. implement strict versioned JSON parsing;
5. implement serialization, byte length, and stable identifiers;
6. implement colouring validation and verification;
7. implement components and relabelled subinstances;
8. add parser, model, malformed-input, and fixed-graph fixtures;
9. add unit tests and the command-line validator;
10. run the suite from a clean checkout;
11. record an implementation and complexity audit;
12. promote `VS-01` only after every exit condition is satisfied.
