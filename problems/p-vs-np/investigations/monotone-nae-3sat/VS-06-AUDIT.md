# VS-06 Completion Audit — Naive Summary Collisions

**Slice:** `VS-06`  
**Status:** `COMPLETE / CHECKED`  
**Classification:** Explicit counterexamples, constructive theorem, finite computation, and complexity audit  
**Updated:** 2026-07-22

## Exact result

The following explicitly defined summaries do not determine exact Monotone NAE-3SAT semantics:

- sorted degree sequence;
- hyperedge-intersection multiset;
- pair-codegree multiset;
- parity data;
- first and second incidence moments;
- the full incidence-Gram characteristic polynomial;
- root generalized arc-consistency;
- satisfiability of every proper induced vertex subinstance;
- boundary Hamming weight;
- boundary Hamming parity.

Each failure is witnessed by a complete pair in the committed atlas. Whole-instance collisions have equal summaries and opposite satisfiability. Prefix collisions occur inside one fixed instance and ordering and have equal summaries but different exact completion masks.

**Status:** `COMPUTATIONAL / CHECKED` as `NAE-013`.

## Bounded-radius theorem — `NAE-012`

For every fixed `r>=1`, let

- `G_r^- = C_(2r+3) disjoint-union C_(2r+3)`;
- `G_r^+ = C_(2r+2) disjoint-union C_(2r+4)`.

Every rooted radius-`r` neighbourhood in both graphs is the same rooted path on `2r+1` vertices. Both graphs have `4r+6` roots, so their rooted-neighbourhood multisets agree exactly.

`G_r^-` contains odd cycles and is not bipartite. `G_r^+` contains only even cycles and is bipartite.

Under the anchored NAE encoding with anchors fixed to opposite colours, every graph edge is forced bichromatic. Therefore the two conditioned NAE residuals have equal fixed-radius local summaries and opposite satisfiability.

**Status:** `PROVED / CHECKED`.

## Explicit collision audit

### Shared six-vertex pair

The hypergraph consisting of all triples `{0,u,v}` with `1<=u<v<=5` is satisfiable. The complete three-uniform hypergraph on vertices `0,...,4` plus isolated vertex `5` is unsatisfiable. They have equal:

- edge-intersection multisets;
- parity summaries;
- second-moment summaries;
- incidence-Gram characteristic polynomials.

### Degree and pair-codegree pairs

Separate six-vertex ten-edge pairs are stored for degree sequence and pair-codegree multiset. Exact enumeration checks one side satisfiable and the other unsatisfiable.

### Local-consistency pair

The Fano plane and a seven-edge satisfiable star instance both leave all root GAC domains equal to `{0,1}`. Every proper induced vertex subinstance of each is satisfiable, yet the Fano plane itself is not.

### Prefix pairs

- a four-vertex two-edge instance contains two prefixes with the same boundary width and Hamming weight but different completion masks;
- a single-edge instance contains two prefixes with the same boundary width and Hamming parity but opposite one-bit completion masks.

## Retained exact control

For a fixed instance, ordering, and processing level, processed consistency plus the exact assignment on the processed boundary determines the remaining completion set. This is the standard exact-interface fact behind `NAE-005` and is exhaustively cross-checked through four vertices.

It is not a universal compression theorem: the boundary can have linear size and therefore expose `2^w` states.

## Independent attack

The slice was attacked for:

- comparing globally unsatisfiable instances through the already-collapsed `VS-03` observable;
- silently treating sorted summaries as labelled matrices;
- using numerical eigenvalue approximations rather than exact characteristic polynomials;
- confusing local consistency with exact satisfiability;
- claiming a bounded-radius theorem only from finite samples;
- overlooking component counts or total vertex counts in the radius family;
- inferring a lower bound for arbitrary algorithms;
- hiding factorial work in rooted-neighbourhood canonicalization;
- weakening the semantic discriminator from exact completion masks to mere processed consistency.

The bounded-radius claim is proved symbolically for every fixed radius. The canonicalizer is used only to verify small samples and is not part of the theorem or a proposed algorithm.

## Post-merge implementation review

The first `main` run after the VS-06 merge, workflow run `29954395327`, failed on Python 3.11, 3.12, and 3.13. The review found a stale committed collision record rather than a failed mathematical collision.

The committed JSON had retained an advertised digest from the final generator while containing values from an earlier prototype. The first repair corrected the initially visible counts and moments, but workflow run `29955640016` still failed because the record had broader drift. Exact regeneration exposed and corrected all stale fields, including:

- every noncanonical instance identifier inherited from the prototype;
- the satisfiable degree-sequence count and least witness;
- the satisfiable pair-codegree count and least witness;
- the seven-vertex star count, `42` rather than `54`;
- the degree second moment, `180` rather than `270`;
- the boundary-weight width, `3` rather than `2`;
- the boundary-weight completion masks, `3` and `2` rather than `2` and `3`.

The final record is the exact byte output of the canonical serializer and `summary_collision_bytes()`, not a field-by-field repair. The semantic collision claims did not change.

The review also strengthened the gate by:

- independently enumerating all assignments for every named whole-instance witness;
- comparing stored solution counts and least witnesses with that independent enumeration;
- checking the anchored graph-to-NAE reduction in both directions on odd-cycle, even-cycle, and radius-one controls;
- checking the characteristic-polynomial routine on exact known matrices;
- adding VS-06 to the generic strict-envelope adversarial tests;
- making the test directory an explicit Python package for dotted unittest targets.

## Complexity and scope

The atlas is a falsification instrument, not a decision algorithm. The finite witnesses are tiny, but finding collisions by exhaustive search can be exponential. The generic local-neighbourhood canonicalizer can be factorial in ball size. No such cost is described as polynomial.

The results are summary-specific. They do not prove that every local, algebraic, spectral, or symbolic representation fails. They do not establish `P!=NP` or refute `NAE-006`.

## Final determination

`VS-06` remains `COMPLETE / CHECKED` after exact regeneration of its reproducibility artifact and strengthening of its independent verification boundary.

The legitimate next slice is `VS-07`: measure genuine live semantic merging, separating dead-state collapse, complement symmetry, exact quotient count, boundary-state count, and encoded representation size.
