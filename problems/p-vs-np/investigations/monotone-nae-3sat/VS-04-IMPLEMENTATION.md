# VS-04 Implementation Specification — Control Calibration

**Slice:** `VS-04`  
**Status:** `ACTIVE` — reviewed contract and implementation in progress  
**Depends on:** `VS-01`, `VS-02`, and `VS-03` — `COMPLETE / CHECKED`  
**Updated:** 2026-07-22

## Purpose

Calibrate the shared laboratory on problems and subclasses whose tractability mechanisms are already understood. The goal is not to collect vaguely “easy” examples. It is to separate five exact mechanisms that later representation proposals must recover without conflation:

1. parity propagation for graph bipartiteness;
2. affine row reduction for XOR systems;
3. leaf elimination for incidence-forest NAE instances;
4. finite-interface dynamic programming for bounded-boundary NAE instances;
5. exact product decomposition for disconnected instances.

Planar and occurrence-at-most-three Monotone NAE-3SAT remain externally established tractable boundaries. VS-04 records checked finite controls inside those classes but does not re-prove the full literature algorithms.

## Claim classification

- graph bipartiteness solver and count formula — `PROVED / CHECKED` project proof;
- XOR row-reduction solver and count formula — `PROVED / CHECKED` project proof;
- incidence-forest NAE colouring algorithm — new project theorem, to be `PROVED / CHECKED`;
- bounded-boundary algorithm — retained `NAE-005`, `PROVED / CHECKED`;
- disconnected factorization — retained VS-02 result, `PROVED / CHECKED`;
- planar and occurrence-at-most-three tractability — `ESTABLISHED / CHECKED` from primary literature;
- finite control census values — `COMPUTATIONAL / CHECKED`.

## Required APIs

### Rank-two graph control

```python
@dataclass(frozen=True, slots=True)
class Graph2:
    n: int
    edges: tuple[tuple[int, int], ...]

@dataclass(frozen=True, slots=True)
class Graph2Result:
    bipartite: bool
    witness: tuple[int, ...] | None
    components: int
    solution_count: int
    conflict_edge: tuple[int, int] | None


def normalize_graph2(n: int, edges: Iterable[Sequence[int]]) -> Graph2: ...
def solve_graph2(graph: Graph2) -> Graph2Result: ...
def verify_graph2_coloring(graph: Graph2, coloring: Sequence[int]) -> bool: ...
def labelled_graphs(n: int) -> Iterator[Graph2]: ...
```

The solver returns the lexicographically least proper two-colouring when one exists. Isolated vertices count as components, so a bipartite graph with `c` components has exactly `2^c` colourings; the empty graph on zero vertices has one colouring.

### XOR control

```python
@dataclass(frozen=True, slots=True)
class XorSystem:
    n: int
    equations: tuple[tuple[int, int], ...]

@dataclass(frozen=True, slots=True)
class XorResult:
    consistent: bool
    rank: int
    free_variables: int
    witness: tuple[int, ...] | None
    solution_count: int
    reduced_rows: tuple[tuple[int, int], ...]


def normalize_xor_system(
    n: int,
    equations: Iterable[tuple[Iterable[int] | int, int]],
) -> XorSystem: ...
def solve_xor(system: XorSystem) -> XorResult: ...
def verify_xor_assignment(system: XorSystem, assignment: Sequence[int]) -> bool: ...
def labelled_xor_systems(n: int) -> Iterator[XorSystem]: ...
```

A row mask uses bit `i` for variable `i`. The canonical equation order is increasing `(mask, rhs)`. The exhaustive generator includes or excludes each equation `(mask, rhs)` independently for every nonzero mask and both right-hand sides.

The returned witness is the true lexicographically least solution. It may be found by greedily fixing variables to zero whenever the augmented system remains consistent.

### NAE structural controls

```python
def is_incidence_forest(instance: Hypergraph3) -> bool: ...
def color_incidence_forest(instance: Hypergraph3) -> tuple[int, ...]: ...
def vertex_occurrences(instance: Hypergraph3) -> tuple[int, ...]: ...
def is_linear(instance: Hypergraph3) -> bool: ...
def processed_boundary(instance: Hypergraph3, ordering: Sequence[int], level: int) -> tuple[int, ...]: ...
def boundary_width(instance: Hypergraph3, ordering: Sequence[int]) -> int: ...
def minimum_boundary_width(instance: Hypergraph3, *, max_vertices: int = 8) -> int: ...
```

`color_incidence_forest` rejects cyclic incidence graphs and returns a verified colouring for every incidence forest, including empty instances and isolated vertices.

## Incidence-forest theorem

### Claim

Every finite 3-uniform hypergraph whose incidence graph is a forest is two-colourable. A colouring can be constructed in linear time.

### Proof obligation

In each nontrivial incidence-tree component, choose a root hyperedge. Colour its three vertices non-monochromatically. Traverse hyperedges away from the root. Every new hyperedge meets the processed part in exactly one vertex; otherwise the incidence graph would contain a cycle. Its two uncoloured vertices can be assigned opposite colours, so the edge is non-monochromatic regardless of the inherited colour. Isolated vertices receive zero. Every incidence edge is processed a constant number of times.

The implementation must check the forest hypothesis and re-verify the returned colouring through VS-01.

## Exact finite domains

### Graph census

Enumerate every labelled simple graph through five vertices:

\[
\sum_{n=0}^{5}2^{\binom n2}=1100.
\]

Record by `n` the total, bipartite, non-bipartite, and bipartite component-count distribution. Production BFS/parity results must agree with independent colouring enumeration on every graph.

### XOR census

For `n<=3`, independently include or exclude every equation `(a,b)` with nonzero `a in GF(2)^n` and `b in GF(2)`. The domain size is

\[
1+2^2+2^6+2^{14}=16453.
\]

Record consistency and rank distributions. Gaussian elimination, exact counts, and least witnesses must agree with independent assignment enumeration on every system.

### NAE calibration domain

Use every labelled 3-uniform hypergraph through five vertices and record two filtered subdomains:

- incidence-forest instances;
- instances of maximum vertex occurrence at most three.

For each filtered instance:

- obtain exact satisfiability and counts from VS-02;
- construct and verify the forest colouring where applicable;
- compute the natural-order exact profile through VS-03;
- record quotient and boundary metrics.

The finite occurrence filter is evidence about the declared small domain only. The unrestricted occurrence-at-most-three theorem remains external.

## Named controls

The deterministic report must include:

### Graph

- a path;
- an even cycle;
- an odd cycle;
- a disconnected graph containing an odd cycle.

### XOR

- independent equations;
- a dependent consistent system;
- an inconsistent pair of equal left-hand sides;
- a system with free variables and exponentially many assignments.

### Monotone NAE-3SAT

- a single edge;
- a loose incidence-tree path;
- a cyclic planar low-occurrence loose cycle;
- two disconnected edges;
- a longer bounded-boundary loose path;
- the complete five-vertex obstruction as a negative comparison.

Every NAE control records exact count, components, maximum occurrence, linearity, incidence-forest status, chosen ordering, boundary width, raw prefixes, exact/live classes, and encoded profile bytes.

## Calibration interpretation

The completion report must state the mechanism, not merely the outcome:

- graph 2-colouring compresses to one parity label per vertex relative to a component root;
- XOR compresses to a polynomial-size affine row space even when the explicit solution set is exponential;
- incidence forests permit irreversible leaf/subtree elimination because no compatibility can return through a second path;
- bounded boundary retains the complete interface explicitly and is exponential only in interface width;
- disconnected components factor because no constraint crosses the cut;
- planarity and occurrence bounds are genuine broader tractable theorems, but finite controls do not explain those algorithms by themselves.

## Canonical report

`calibration_record()` returns compact deterministic semantic JSON with:

- format `nae3-vs04-calibration-v1`;
- mechanism descriptions;
- graph census and named controls;
- XOR census and named controls;
- NAE filtered census and named controls;
- primary-source identifiers for planar and bounded-occurrence boundaries;
- finite-computation limitations;
- a non-self-referential SHA-256 payload digest.

`calibration_bytes()` emits compact UTF-8 JSON with fixed key order and no terminal newline. Interpreter versions and timestamps belong in the audit, not the semantic payload.

## Command-line interface

```bash
python3 -m nae3sat.cli calibrate --output path/to/vs04-calibration.json
```

The command writes atomically and reproduces the committed report byte for byte.

## Required tests

1. strict constructor and public-API validation for graph and XOR controls;
2. exhaustive graph solver/reference agreement on all `1100` graphs;
3. exhaustive XOR solver/reference agreement on all `16453` systems;
4. least-witness and exact-count agreement throughout both domains;
5. exhaustive incidence-forest recognition and constructive colouring through five vertices;
6. all filtered NAE results agree with VS-02 and VS-03;
7. boundary functions agree with the VS-03 level boundaries;
8. named controls exhibit their declared mechanism and expected positive/negative behaviour;
9. report digest validation and byte reproduction;
10. hash-seed determinism;
11. Python 3.11, 3.12, and 3.13 full-suite and CLI reproduction;
12. independent break pass over constructor bypasses, zero-variable cases, contradictory XOR rows, odd cycles, disconnected instances, and cyclic incidence graphs.

## Complexity accounting

- graph normalization: `O(m log m)` under canonical sorting;
- graph parity solver: `O(n+m)` time and space;
- graph exact solution count: one integer of at most `n+1` bits;
- XOR normalization: polynomial in row count and mask bit length;
- Gaussian elimination: `O(r n^2)` bit operations in the direct row representation, with polynomially bounded intermediate masks;
- lexicographically least XOR witness: at most `n+1` consistency eliminations, still polynomial;
- incidence-forest recognition and colouring: `O(n+m)` incidence-graph work;
- one ordering's boundary width: `O(n(n+m))` in the direct implementation;
- minimum boundary width by exhaustive permutations: `O(n! n(n+m))`, restricted by an explicit small-`n` guard and never called polynomial;
- calibration report generation is finite exhaustive computation over the declared fixed domains, not a general polynomial solver.

## Quality gate

`VS-04` becomes `COMPLETE / CHECKED` only when:

1. VS-01 through VS-03 remain green;
2. all required graph, XOR, NAE structural, report, and CLI APIs exist;
3. parity, affine, incidence-forest, bounded-boundary, and component mechanisms are proved or correctly imported;
4. graph and XOR exhaustive reference comparisons pass;
5. the complete declared NAE filtered domain passes exact checks;
6. the committed report is byte-reproducible across supported runtimes;
7. all complexity and finite-domain boundaries are explicit;
8. an independent attack leaves no unresolved substantive defect;
9. status, vertical-slice, claim, README, source, and audit records agree.

## Non-goals

VS-04 does not:

- provide a new planar or occurrence-at-most-three algorithm;
- infer universal tractability from control behaviour;
- claim that few exact classes imply efficient construction;
- claim a polynomial bound for unrestricted NAE instances;
- replace later hard-family and obstruction testing;
- establish either `P=NP` or `P!=NP`.
