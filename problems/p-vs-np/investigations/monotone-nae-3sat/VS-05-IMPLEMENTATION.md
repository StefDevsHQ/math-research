# VS-05 Implementation Specification — Minimal Obstruction Atlas

**Slice:** `VS-05`  
**Status:** `ACTIVE`  
**Depends on:** `VS-01` through `VS-04 — COMPLETE / CHECKED`  
**Updated:** 2026-07-22

## Purpose

Construct a deterministic, independently checked atlas of the first exact obstructions to two-colourability in 3-uniform hypergraphs. The atlas separates edge-minimality from vertex-minimality, stores complete deletion certificates, and records exact VS-03 profile evidence across every ordering of each named obstruction.

This slice is finite structural calibration. It does not classify all minimal non-two-colourable 3-uniform hypergraphs.

## Definitions

Let `H=(V,E)` be a canonical `Hypergraph3`.

- `H` is **edge-minimal unsatisfiable** when `H` is not two-colourable and `H-e` is two-colourable for every `e in E`.
- `H` is **vertex-minimal unsatisfiable** when `H` is not two-colourable and the induced hypergraph `H-v` is two-colourable for every `v in V`.
- `H` is **proper-edge-critical** when every proper edge-subhypergraph is two-colourable.
- `H` is **proper-induced-critical** when every proper induced vertex subhypergraph is two-colourable.

### Single-deletion sufficiency

For an unsatisfiable hypergraph, checking every single edge deletion is sufficient for proper-edge-criticality: every proper edge-subhypergraph is contained in some `H-e`, and two-colourability is preserved under edge deletion. The analogous statement holds for induced vertex subhypergraphs by choosing any omitted vertex.

Every object called minimal in the atlas must include all relevant single-deletion checks and their least witnesses.

## Required API

```python
@dataclass(frozen=True, slots=True)
class EdgeDeletionCertificate:
    edge: Edge
    witness: Coloring

@dataclass(frozen=True, slots=True)
class VertexDeletionCertificate:
    vertex: int
    new_to_old: tuple[int, ...]
    witness: Coloring


def complete_three_graph(n: int) -> Hypergraph3: ...
def fano_plane() -> Hypergraph3: ...
def delete_edge(instance: Hypergraph3, edge: Sequence[int]) -> Hypergraph3: ...
def delete_vertex(instance: Hypergraph3, vertex: int) -> RelabeledHypergraph3: ...
def is_vertex_minimal_unsatisfiable(instance: Hypergraph3) -> bool: ...
def edge_deletion_certificates(instance: Hypergraph3) -> tuple[EdgeDeletionCertificate, ...]: ...
def vertex_deletion_certificates(instance: Hypergraph3) -> tuple[VertexDeletionCertificate, ...]: ...
def obstruction_record(name: str, instance: Hypergraph3) -> dict[str, object]: ...

def obstruction_atlas_payload() -> dict[str, object]: ...
def obstruction_atlas_record() -> dict[str, object]: ...
def obstruction_atlas_bytes() -> bytes: ...
def verify_obstruction_atlas_record(record: object) -> bool: ...
```

All public functions use strict existing model validation. Certificate constructors validate shape, strict binary witnesses, and canonical labels. Certificate-producing functions reject satisfiable or nonminimal inputs rather than returning partial evidence.

## Declared exhaustive domain

Enumerate every labelled 3-uniform hypergraph through five vertices:

\[
\sum_{n=0}^{5}2^{\binom n3}=1045.
\]

Record by `n`:

- total and unsatisfiable instances;
- edge-minimal unsatisfiable instances;
- vertex-minimal unsatisfiable instances;
- instances satisfying both notions;
- canonical identifiers of every obstruction.

The expected first obstruction is the complete 3-uniform hypergraph `K_5^(3)`. The census is exhaustive only through five vertices.

## Named obstructions

### Dense control: `K_5^(3)`

Record the complete five-vertex hypergraph with all ten triples. Verify unsatisfiability, all ten edge deletions, all five vertex deletions, and all 120 vertex orderings.

### Sparse control: Fano plane

Record the seven-edge Fano plane on seven vertices:

```text
012, 034, 056, 135, 146, 236, 245
```

Verify unsatisfiability, all seven edge deletions, all seven vertex deletions, and all 5040 vertex orderings. This is a named control, not part of an exhaustive seven-vertex census.

## Structural evidence

Each obstruction record contains:

- canonical identifier, vertices, edges, and encoded instance size;
- degree sequence and pair-codegree distribution;
- component count, regularity, linearity, incidence-forest status, and boundary width under natural order;
- exact edge- and vertex-minimality flags;
- complete edge-deletion least-witness certificates;
- complete vertex-deletion least-witness certificates with old/new label maps;
- exact all-ordering profile aggregate.

## All-ordering profile aggregate

For every permutation of the obstruction vertices, build the exact VS-03 profile and record:

- ordering count;
- distributions of maximum class count, total class count, boundary width, and encoded profile bytes;
- minima and maxima of those measurements;
- an ordered SHA-256 digest over a canonical signature containing the ordering, every level's class masks, assignment partition, transitions, and processed boundary count.

This is exact finite evidence. A small quotient does not imply efficient construction.

## Deterministic atlas record

The canonical JSON format is `nae3-vs05-obstruction-atlas-v1`. It contains:

- definitions and monotonicity lemma;
- complete `n<=5` census;
- dense and sparse named obstruction records;
- source identifiers for established Fano terminology/results;
- explicit limitations;
- non-self-referential SHA-256 payload digest.

`obstruction_atlas_bytes()` emits compact UTF-8 JSON with fixed insertion order and no terminal newline.

## Command-line interface

```bash
python3 -m nae3sat.cli obstruction-atlas --output path/to/vs05-obstruction-atlas.json
```

The command writes atomically and must reproduce the committed atlas byte for byte on Python 3.11, 3.12, and 3.13.

## Independent verification

Tests must contain a logically separate direct-colouring reference that does not call the production minimality or certificate functions.

Required gates:

1. strict deletion and certificate validation;
2. complete production/reference agreement on all `1045` labelled instances through five vertices;
3. exact uniqueness of `K_5^(3)` as the unsatisfiable, edge-minimal, and vertex-minimal object in that domain;
4. independent unsatisfiability checks for `K_5^(3)` and Fano;
5. every deletion certificate independently verifies and is the true lexicographically least witness;
6. structural invariants match independent calculations;
7. all 120 and 5040 orderings are represented exactly once;
8. independent recomputation of all-ordering profile digests;
9. deterministic atlas digest and committed byte reproduction;
10. CLI error and atomic-output behaviour;
11. complete VS-01 through VS-05 matrix on Python 3.11–3.13.

## Complexity accounting

For `n` vertices and `m` edges:

- exact decision and certificate generation inherit the exponential VS-02 oracle;
- edge certificates require `m` exact solves on `m-1` edges;
- vertex certificates require `n` exact solves on induced instances;
- all-ordering profile evidence requires `n!` exact profiles and is factorial-exponential;
- the complete `n<=5` census enumerates exactly `1045` inputs;
- the Fano control is one explicitly declared seven-vertex instance, not an exhaustive seven-vertex domain;
- output size includes every deletion certificate and aggregate profile statistics, not every full profile.

No part of atlas construction is claimed polynomial on unrestricted input.

## Quality gate

`VS-05` becomes `COMPLETE / CHECKED` only when:

1. corrected VS-04 is merged and green;
2. all APIs, CLI, records, and tests exist;
3. minimality definitions and single-deletion sufficiency are proved;
4. the full `n<=5` census agrees with an independent reference;
5. both named obstruction certificate sets are complete and independently verified;
6. every named ordering is included in deterministic profile evidence;
7. the committed atlas reproduces byte for byte across supported runtimes;
8. complexity and finite-domain limits are explicit;
9. an independent break pass finds no unresolved substantive defect;
10. status, claims, README, workflow, specification, audit, and generated record agree.

## Non-goals

VS-05 does not:

- classify all critical 3-uniform hypergraphs;
- exhaust all six- or seven-vertex instances;
- infer asymptotic state growth from two named obstructions;
- prove a universal compression barrier;
- establish either `P=NP` or `P!=NP`.
