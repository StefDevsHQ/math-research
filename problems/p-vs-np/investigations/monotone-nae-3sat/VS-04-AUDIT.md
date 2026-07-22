# VS-04 Completion Audit — Control Calibration

**Slice:** `VS-04`  
**Status:** `COMPLETE / CHECKED`  
**Classification:** Proof, implementation, exhaustive finite computation, imported tractability boundaries, and complexity audit  
**Updated:** 2026-07-22

## Scope

VS-04 calibrates the exact VS-01 through VS-03 laboratory on five distinct tractability mechanisms:

1. graph parity propagation;
2. affine row reduction;
3. incidence-forest elimination;
4. bounded-boundary dynamic programming;
5. disconnected-component factorization.

Planar and occurrence-at-most-three Monotone NAE-3SAT are recorded as externally established tractable boundaries. This slice does not claim to reimplement or re-prove those full algorithms.

## Implemented artifacts

Under `tools/monotone-nae-3sat/`:

- `nae3sat/controls.py`: strict graph and XOR control models, exact solvers and generators, incidence-forest recognition and colouring, linearity, occurrence, and boundary utilities;
- `nae3sat/calibration.py`: deterministic calibration census and named-control report;
- `tests/test_vs04.py`: exhaustive independent graph and XOR references plus complete small NAE filtered-domain checks;
- `calibration/vs04-calibration.json`: committed deterministic semantic record;
- CLI command `calibrate`;
- Python 3.11, 3.12, and 3.13 automation.

## Graph parity theorem

For a graph component, fixing one root colour determines every other colour by path parity. A conflict occurs exactly when an edge joins equal parity labels, equivalently when an odd cycle exists. If the graph is bipartite and has `c` connected components, each component may be complemented independently, giving exactly `2^c` proper two-colourings. Choosing the orientation that gives each component's least-labelled vertex colour zero produces the lexicographically least full colouring.

**Status:** `PROVED / CHECKED`.

## Affine XOR theorem

A finite XOR system is a linear system over `GF(2)`. Gaussian elimination decides consistency and computes coefficient rank `r`. A consistent system on `n` variables has affine solution-space dimension `n-r` and exactly `2^(n-r)` solutions. The implementation obtains the lexicographically least solution by trying each variable as zero in order and retaining zero exactly when the augmented system remains consistent.

Iterable left sides are normalized over `GF(2)`: repeated variable occurrences cancel before the nonzero canonical row mask is stored.

**Status:** `PROVED / CHECKED`.

## Incidence-forest theorem

### Claim

Every finite 3-uniform hypergraph whose incidence graph is a forest has Property B, and a colouring is constructible in linear time.

### Proof

Consider one nontrivial incidence-tree component and choose a root hyperedge. Colour its three vertices non-monochromatically. Traverse hyperedge nodes away from the root. A newly visited hyperedge shares exactly one vertex with the processed part: it shares at least one through its parent incidence path, and sharing a second processed vertex would create a cycle in the incidence graph. Its other two vertices are uncoloured and may be assigned opposite colours. The new edge is therefore non-monochromatic regardless of the inherited colour. Continue until the component is exhausted. Assign isolated vertices colour zero.

Every incidence edge is inspected a constant number of times, so the construction uses `O(n+m)` incidence-graph time and space. The implementation re-verifies the returned colouring through the VS-01 verifier.

**Status:** `PROVED / CHECKED`.

## Exhaustive graph evidence

The declared domain contains

\[
\sum_{n=0}^{5}2^{\binom n2}=1100
\]

labelled simple graphs.

| Metric | Value |
|---|---:|
| Total | `1100` |
| Bipartite | `428` |
| Non-bipartite | `672` |

Production parity results, exact counts, and least witnesses agree with direct complete-colouring enumeration on every graph.

## Exhaustive XOR evidence

For `n<=3`, every subset of the `2(2^n-1)` possible canonical nonzero-mask equations is included:

\[
1+2^2+2^6+2^{14}=16453.
\]

| Metric | Value |
|---|---:|
| Total | `16453` |
| Consistent | `890` |
| Inconsistent | `15563` |

Gaussian elimination, ranks, solution counts, and least witnesses agree with direct assignment enumeration on every system.

## NAE filtered-domain evidence

All `1045` labelled 3-uniform hypergraphs through five vertices were checked.

- incidence-forest instances: `36`;
- incidence-forest unsatisfiable instances: `0`;
- maximum-occurrence-at-most-three instances: `344`;
- unsatisfiable instances in that finite occurrence filter: `0`.

Every forest witness passes VS-01 verification. Every profile acceptance agrees with VS-02, and every boundary utility agrees with the boundary recorded by VS-03.

The occurrence result is finite-domain evidence only. General tractability at occurrence at most three is imported from the cited literature.

## Mechanism calibration

- **Graph bipartiteness:** a component is represented by root-relative parity, not by enumerating all colourings.
- **XOR:** an exponential solution set is represented by a polynomial affine row space. Explicit semantic-state count and symbolic representation size are different questions.
- **Incidence forests:** compatibility cannot return through a second path, so processed subtrees may be eliminated irreversibly.
- **Bounded boundary:** all future-relevant information is retained explicitly on a small interface; exponential dependence is confined to interface width.
- **Disconnected components:** exact decision and counting factor because no edge crosses components.

These mechanisms are mathematically distinct. Success on one does not imply a universal mechanism for unrestricted Monotone NAE-3SAT.

## Imported boundaries

- Planar NAE3SAT tractability — `ESTABLISHED / CHECKED` from Darmann and Döcker.
- Occurrence-at-most-three tractability — `ESTABLISHED / CHECKED` from Porschen, Randerath, and Speckenmeyer and the restricted-hardness literature.

The calibration report contains source identifiers rather than claiming these as project-original proofs.

## Complexity audit

- graph parity solver: `O(n+m)` time and space;
- graph solution count: an integer with at most `n+1` bits;
- direct XOR elimination: `O(r n^2)` bit operations for `r` input rows, with polynomially bounded row masks;
- least XOR witness: at most `n+1` consistency eliminations, hence polynomial;
- incidence-forest recognition and colouring: `O(n+m)` incidence work;
- one ordering's direct boundary-width computation: `O(n(n+m))`;
- exhaustive minimum ordering width: factorial and guarded by an explicit vertex bound;
- report construction: finite exhaustive computation over fixed declared domains, not a general polynomial algorithm.

## Break pass

The attack checked:

- zero-vertex graph and XOR boundaries;
- isolated graph components;
- odd cycles and disconnected odd-cycle instances;
- contradictory equal-left-side XOR equations;
- dependent affine systems and free variables;
- least-witness semantics;
- cyclic incidence rejection;
- incidence forests with multiple components and isolates;
- boundary agreement with VS-03;
- constructor and public-API type rejection;
- report hashing and cross-version determinism;
- arithmetic consistency of all aggregate census totals.

The first CI pass caught an incorrect hand-summed graph aggregate (`427/673` instead of `428/672`). The per-size exhaustive results and both solvers were correct; the assertion and report expectation were corrected. No unresolved mathematical defect remains.

## Reproducibility

The complete VS-01 through VS-04 suite, inherited VS-03 independent reference gate, CLI controls, and byte reproduction of the VS-02, VS-03, and VS-04 committed records pass on the documented Python runtime matrix. The VS-04 semantic payload digest is:

```text
be8a013fdf80c7fd252581e975b07aa18eebda916fb714fbaca404ce8fb137bb
```

## Final determination

`VS-04` is `COMPLETE / CHECKED`.

The retained lesson is negative as well as positive: tractable controls succeed through identifiable parity, affine, acyclic, bounded-interface, or product structure. None supplies a universal unrestricted compression theorem.
