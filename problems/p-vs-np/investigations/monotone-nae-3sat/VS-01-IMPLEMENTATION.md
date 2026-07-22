# VS-01 Implementation Specification — Canonical Instance Model

**Slice:** `VS-01`  
**Status:** `PARTIAL` — implementation-ready; executable model and tests remain  
**Updated:** 2026-07-22

## Purpose

Create the single executable representation used by every later Monotone NAE-3SAT proof, experiment, oracle, profile engine, and corpus.

This slice does not solve satisfiability. It establishes what an instance is, how it is normalized, how it is serialized, how components are computed, and how a proposed colouring is verified.

## Implementation decision

Use **Python 3.12 or later** and the standard library only.

Reasons:

- exhaustive small-instance work benefits from direct integer and bit operations;
- standard-library-only execution keeps the laboratory portable and reproducible;
- Python is sufficient for the initial finite domains;
- performance-critical components can later be replaced without changing the canonical format or mathematical semantics.

Tests use `unittest`; no third-party test framework is required.

## Repository layout

```text
tools/monotone-nae-3sat/
├── README.md
├── pyproject.toml
├── src/
│   └── nae3sat/
│       ├── __init__.py
│       ├── errors.py
│       ├── model.py
│       └── serialization.py
├── tests/
│   ├── fixtures/
│   ├── test_model.py
│   ├── test_serialization.py
│   ├── test_components.py
│   └── test_verifier.py
└── scripts/
    └── validate_instance.py
```

Generated experimental results do not belong under `tools/`; they belong under the investigation's future `experiments/` directory.

## Canonical mathematical object

An instance is a pair

\[
H=(V,E),
\]

where

\[
V=\{0,1,\ldots,n-1\}
\]

and every edge is a 3-element subset of `V`.

The executable model preserves `n`, including isolated vertices. Removing isolated vertices is an optional derived operation, not part of canonical parsing. This prevents two explicitly different inputs from becoming silently identical and makes empty and isolated-vertex boundary cases unambiguous.

## Core data types

```python
from dataclasses import dataclass
from typing import Iterable, Mapping, Sequence, TypeAlias

Vertex: TypeAlias = int
Edge: TypeAlias = tuple[Vertex, Vertex, Vertex]
Coloring: TypeAlias = tuple[int, ...]

@dataclass(frozen=True, slots=True)
class Hypergraph3:
    n: int
    edges: tuple[Edge, ...]
```

### Class invariants

Every constructed `Hypergraph3` must satisfy:

1. `n >= 0`;
2. vertices are exactly `0, ..., n-1`;
3. every edge has length three;
4. edge entries are integers, not booleans;
5. all three vertices in an edge are distinct;
6. every vertex lies in `[0, n)`;
7. each edge is internally sorted;
8. the edge tuple is lexicographically sorted;
9. duplicate edges are absent.

No public constructor may create a value violating these invariants.

## Public API

```python
def normalize_instance(n: int, edges: Iterable[Sequence[int]]) -> Hypergraph3:
    """Validate, sort, deduplicate, and construct a canonical instance."""


def parse_canonical_json(data: str | bytes) -> Hypergraph3:
    """Parse the canonical JSON schema and return the normalized instance."""


def to_canonical_json(instance: Hypergraph3) -> str:
    """Return the unique compact JSON serialization."""


def canonical_bytes(instance: Hypergraph3) -> bytes:
    """UTF-8 bytes of the canonical JSON serialization."""


def instance_id(instance: Hypergraph3) -> str:
    """Return 'nae3-sha256-' followed by the SHA-256 digest of canonical bytes."""


def encoded_size_bytes(instance: Hypergraph3) -> int:
    """Length of canonical bytes; an operational encoding measure, not a new complexity theorem."""


def incidence_components(instance: Hypergraph3) -> tuple[tuple[int, ...], ...]:
    """Return all components, including singleton isolated vertices, canonically ordered."""


def induced_subinstance(instance: Hypergraph3, vertices: Iterable[int]) -> Hypergraph3:
    """Return the induced subhypergraph, relabelled increasingly to 0..k-1."""


def active_core(instance: Hypergraph3) -> Hypergraph3:
    """Remove isolated vertices and relabel; satisfiability-preserving but not identity-preserving."""


def verify_coloring(instance: Hypergraph3, coloring: Sequence[int]) -> bool:
    """Accept exactly total 0/1 colourings making every edge non-monochromatic."""


def first_violated_edge(instance: Hypergraph3, coloring: Sequence[int]) -> Edge | None:
    """Return the first canonical monochromatic edge, or None when valid."""
```

## Canonical JSON schema

The only canonical serialized form is:

```json
{"n":4,"edges":[[0,1,2],[1,2,3]]}
```

Rules:

- top-level object has exactly the keys `n` and `edges`;
- `n` is a nonnegative integer and not a Boolean;
- `edges` is an array of arrays of exactly three integers;
- whitespace is omitted in canonical output;
- keys are emitted in the order `n`, then `edges`;
- input edges may be unsorted or repeated, but parsed output is normalized;
- unknown keys are rejected rather than ignored;
- malformed JSON and malformed mathematical instances raise explicit errors.

Canonical output uses `json.dumps(..., separators=(",", ":"), ensure_ascii=True)` over an insertion-ordered object.

## Error model

Define a small explicit hierarchy:

```python
class NAE3Error(Exception): ...
class ParseError(NAE3Error): ...
class ValidationError(NAE3Error): ...
class ColoringError(NAE3Error): ...
```

`verify_coloring` returns `False` only for a total binary colouring that violates an edge. It raises `ColoringError` for malformed colourings, such as wrong length or nonbinary entries. This separates an invalid witness from a valid but unsuccessful witness.

## Component semantics

The incidence graph has one node for every vertex and one node for every hyperedge, with incidence edges connecting them.

For simple 3-uniform hypergraphs, two vertices lie in the same nontrivial component exactly when they are connected through a sequence of overlapping hyperedges.

`incidence_components` must:

- include every isolated vertex as a singleton component;
- sort vertices within each component;
- sort components by their least vertex;
- return the empty tuple for `n = 0`.

The satisfiability factorization theorem used later is:

> An instance is satisfiable exactly when every nontrivial incidence component is satisfiable; isolated vertices are unconstrained.

The implementation of this theorem belongs to `VS-02`, not `VS-01`.

## Colouring semantics

A colouring is represented as a sequence of length `n` whose entries are exactly integers `0` or `1`.

For an edge `(u, v, w)`, the edge is satisfied exactly when:

```python
not (coloring[u] == coloring[v] == coloring[w])
```

Boundary cases:

- `n = 0`, no edges: the empty colouring is valid;
- isolated vertices may take either colour;
- an edge ordering never affects verification;
- duplicate input edges disappear during normalization and do not affect verification;
- complementing every bit preserves verification.

## Determinism requirements

For identical mathematical input, all supported construction paths must produce:

- equal `Hypergraph3` values;
- byte-identical canonical serialization;
- the same SHA-256 identifier;
- identically ordered components;
- the same first violated edge.

No result may depend on hash-table iteration order, process identity, machine architecture, or locale.

## Complexity obligations

For `n` vertices and `m` input edges:

- validation and normalization: `O(m log m)` comparisons after constant-size edge normalization;
- serialization: linear in serialized output size;
- witness verification: `O(n + m)` including colouring validation;
- component computation: `O(n + m)` using adjacency or union-find;
- memory: `O(n + m)` excluding input and output strings.

These are implementation targets to verify by inspection and tests. They do not alter the investigation's complexity claims.

## Required tests

### Construction and normalization

1. `n = 0`, no edges;
2. positive `n`, no edges;
3. unsorted edge becomes sorted;
4. repeated edges are deduplicated;
5. edge list becomes lexicographically sorted;
6. repeated vertex inside one edge is rejected;
7. negative vertex is rejected;
8. out-of-range vertex is rejected;
9. negative `n` is rejected;
10. Boolean values are rejected where integers are required;
11. edge with length other than three is rejected.

### Serialization

1. round trip preserves equality;
2. two differently ordered inputs serialize identically;
3. canonical serialization has no insignificant whitespace;
4. unknown top-level fields are rejected;
5. malformed JSON is rejected;
6. IDs are stable across round trips.

### Components

1. empty instance has no components;
2. isolated vertices are singleton components;
3. one edge forms one component;
4. overlapping edges form one component;
5. disjoint edges form separate components;
6. mixed isolated and nontrivial components are ordered canonically;
7. `active_core` removes only isolated vertices and relabels correctly.

### Witness verification

1. empty colouring verifies the empty instance;
2. one triple has exactly six valid colourings when exhaustively checked in the test;
3. `000` and `111` fail on one triple;
4. a valid disconnected colouring verifies;
5. a monochromatic edge is returned deterministically;
6. every valid colouring's complement is valid;
7. wrong-length colouring raises `ColoringError`;
8. nonbinary colour raises `ColoringError`;
9. Boolean entries are rejected for type discipline.

## Fixed fixtures

Create canonical fixtures for:

- `empty.json`: `n = 0`;
- `isolated-three.json`: `n = 3`, no edges;
- `single-edge.json`: edge `012`;
- `duplicate-unsorted.json`: parses to the single-edge fixture;
- `two-disconnected-edges.json`: edges `012` and `345`;
- `overlap-chain.json`: edges `012`, `234`, `456`;
- `fano-plane.json`: seven vertices and edges `012`, `034`, `056`, `135`, `146`, `236`, `245`.

The Fano plane fixture is only a data fixture in `VS-01`; proving or computing its unsatisfiability belongs to `VS-02` and `VS-05`.

## Command-line validator

Provide:

```bash
python -m nae3sat.scripts.validate_instance path/to/instance.json
```

Output on success:

```json
{"id":"nae3-sha256-...","n":7,"m":7,"components":1,"encoded_bytes":...}
```

Output goes to standard output. Errors go to standard error and return a nonzero exit code. The command must not decide satisfiability.

## Reproducible commands

From `tools/monotone-nae-3sat/`:

```bash
python3.12 -m unittest discover -s tests -v
python3.12 -m nae3sat.scripts.validate_instance tests/fixtures/fano-plane.json
```

The package configuration must allow the commands without manually editing `PYTHONPATH`, for example through an editable standard-library-compatible installation command documented in the tool README.

## Exit gate

`VS-01` becomes `COMPLETE` only when:

1. the package and all listed APIs exist;
2. all required tests pass;
3. canonical fixtures are committed;
4. the validator command is reproducible from a clean checkout;
5. the README states Python version, commands, input/output formats, and limitations;
6. an implementation audit confirms all class invariants and asymptotic targets;
7. `VERTICAL-SLICES.md` and `STATUS.md` link the evidence and mark the slice complete.

## Explicit non-goals

This slice must not contain:

- a satisfiability solver;
- exhaustive instance generation;
- extension-profile computation;
- graph isomorphism reduction;
- heuristic simplification that changes the canonical identity;
- a claim that canonical serialization is a canonical form up to hypergraph isomorphism.

The last distinction is important: serialization is canonical for a fixed vertex labelling, not for an unlabeled isomorphism class.

## First implementation sequence

1. create package layout and error hierarchy;
2. implement `Hypergraph3` construction and invariants;
3. implement serialization and stable IDs;
4. implement colouring verification;
5. implement components and derived subinstances;
6. add fixtures and unit tests;
7. add command-line validator;
8. run the full test suite from a clean environment;
9. record the implementation audit and promote `VS-01` only after the exit gate is satisfied.
