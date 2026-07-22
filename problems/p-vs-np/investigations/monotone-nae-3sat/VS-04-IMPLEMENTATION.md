# VS-04 Implementation Specification — Control Calibration

**Slice:** `VS-04`  
**Status:** `COMPLETE / CHECKED`  
**Depends on:** `VS-01`, `VS-02`, and `VS-03` — `COMPLETE / CHECKED`  
**Updated:** 2026-07-22

## Purpose

Calibrate the shared laboratory on problems and subclasses whose tractability mechanisms are understood. VS-04 separates five exact mechanisms rather than treating all positive controls as one vague easy class:

1. parity propagation for graph bipartiteness;
2. affine row reduction for XOR systems;
3. leaf/subtree elimination for incidence-forest NAE instances;
4. finite-interface dynamic programming for bounded-boundary NAE instances;
5. exact product decomposition for disconnected instances.

Planar and occurrence-at-most-three Monotone NAE-3SAT remain externally established tractable boundaries. The finite controls here do not re-prove those full algorithms.

## Mathematical status

- graph bipartiteness decision, least witness, and count formula — `PROVED / CHECKED`;
- XOR consistency, least witness, rank, and count formula — `PROVED / CHECKED`;
- incidence-forest NAE colouring theorem — `PROVED / CHECKED` as `NAE-008`;
- bounded-boundary algorithm — retained `NAE-005`, `PROVED / CHECKED`;
- disconnected factorization — retained VS-02 result, `PROVED / CHECKED`;
- planar and occurrence-at-most-three tractability — `ESTABLISHED / CHECKED`;
- finite census values — `COMPUTATIONAL / CHECKED` with complete declared-domain enumeration.

## Exported APIs

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

normalize_graph2(...)
solve_graph2(...)
verify_graph2_coloring(...)
labelled_graphs(...)
```

For a bipartite graph with `c` connected components, including isolated vertices, the exact number of proper two-colourings is `2^c`. The solver returns the true lexicographically least colouring by orienting each component so its least-labelled vertex is zero.

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

normalize_xor_system(...)
solve_xor(...)
verify_xor_assignment(...)
labelled_xor_systems(...)
```

A row mask uses bit `i` for variable `i`. Iterable left sides are interpreted over `GF(2)`, so repeated variable occurrences cancel; the canonical stored row is a nonzero bitmask. The exhaustive generator independently includes or excludes each canonical equation `(mask,rhs)` for every nonzero mask and both right-hand sides.

A consistent rank-`r` system on `n` variables has exactly `2^(n-r)` assignments. The least witness is found by fixing variables in increasing order to zero whenever the augmented system remains consistent.

### NAE structural controls

```python
is_incidence_forest(...)
color_incidence_forest(...)
vertex_occurrences(...)
is_linear(...)
processed_boundary(...)
boundary_width(...)
minimum_boundary_width(...)
```

`color_incidence_forest` rejects cyclic incidence graphs and returns a VS-01-verified colouring for every incidence forest. `minimum_boundary_width` is exhaustive over permutations and guarded by an explicit small-vertex limit.

## Incidence-forest theorem

Every finite 3-uniform hypergraph whose incidence graph is a forest is two-colourable in linear incidence-graph time.

Choose a root hyperedge in each nontrivial incidence-tree component and colour it non-monochromatically. Every newly visited hyperedge meets the processed part in exactly one vertex; otherwise the incidence graph contains a cycle. Colour its two new vertices oppositely. Isolated vertices receive zero. Every incidence edge is processed only constantly many times.

The full proof and implementation audit are recorded in [VS-04-AUDIT.md](VS-04-AUDIT.md).

## Exhaustive finite domains

### Graph census

Every labelled simple graph through five vertices:

\[
\sum_{n=0}^{5}2^{\binom n2}=1100.
\]

Production parity decision, exact count, and least witness agree with direct complete-colouring enumeration on every graph.

### XOR census

For `n<=3`, every subset of the `2(2^n-1)` possible canonical nonzero-mask equations:

\[
1+2^2+2^6+2^{14}=16453.
\]

Gaussian elimination, rank, exact count, and least witness agree with direct assignment enumeration on every system.

### NAE calibration domain

Every one of the `1045` labelled 3-uniform hypergraphs through five vertices is checked and filtered for:

- incidence-forest structure;
- maximum occurrence at most three.

VS-02 supplies exact satisfiability and VS-03 supplies exact profiles and boundary data. Forest instances additionally receive a constructive checked witness.

## Named controls

The deterministic report contains:

- graph path, even cycle, odd cycle, and disconnected odd-cycle instance;
- independent, dependent-consistent, contradictory, and free-variable XOR systems;
- single edge, loose incidence-tree paths, a cyclic low-occurrence loose cycle, disconnected edges, and the complete five-vertex obstruction.

Every NAE control records exact count, components, maximum occurrence, linearity, incidence-forest status, ordering, boundary width, raw prefixes, exact/live classes, maximum classes, and profile bytes.

## Calibration interpretation

- **Graph bipartiteness:** one root-relative parity label per vertex.
- **XOR:** a polynomial affine row space can represent exponentially many assignments.
- **Incidence forests:** processed compatibility cannot return through a second path.
- **Bounded boundary:** retain the complete future interface explicitly, with exponential dependence confined to width.
- **Disconnected components:** exact conjunction and counting product because no constraint crosses the cut.

These are different mechanisms. Their coexistence does not imply one universal compression rule.

## Canonical report and CLI

```bash
python3 -m nae3sat.cli calibrate --output path/to/vs04-calibration.json
```

The command writes compact deterministic JSON atomically. The report contains fixed mechanism descriptions, exhaustive census rows, named controls, external source identifiers, explicit limitations, and a non-self-referential SHA-256 payload digest.

The committed report is:

```text
 tools/monotone-nae-3sat/calibration/vs04-calibration.json
```

and must reproduce byte for byte on Python 3.11, 3.12, and 3.13.

## Checked tests

- strict graph and XOR construction and API rejection;
- all `1100` graph production/reference comparisons;
- all `16453` XOR production/reference comparisons;
- least witnesses and exact counts throughout both domains;
- all `1045` small NAE instances checked against VS-02 and VS-03;
- all incidence-forest witnesses verified;
- boundary utilities compared with VS-03 at every level;
- cyclic-incidence rejection and exhaustive-order guard boundaries;
- report digest validation, CLI generation, and byte reproduction;
- full VS-01 through VS-04 suite on Python 3.11, 3.12, and 3.13.

## Complexity accounting

- graph normalization: `O(m log m)` under canonical sorting;
- graph parity solver: `O(n+m)` time and space;
- XOR normalization: polynomial in input row count and row bit length;
- direct Gaussian elimination: `O(r n^2)` bit operations for `r` rows;
- least XOR witness: at most `n+1` consistency eliminations;
- incidence-forest recognition and colouring: `O(n+m)` incidence work;
- one ordering's boundary width: `O(n(n+m))` in the direct implementation;
- exhaustive minimum boundary width: `O(n! n(n+m))`, explicitly guarded and never described as polynomial;
- report construction: finite exhaustive computation over fixed declared domains.

## Claim boundary

VS-04 does not provide a new planar or occurrence-at-most-three algorithm, infer universal tractability from finite controls, prove a polynomial exact quotient, replace hard-family testing, or establish either `P=NP` or `P!=NP`.
