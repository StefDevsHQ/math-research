# VS-04 Post-Merge Independent Review

**Slice:** `VS-04`  
**Review result:** `COMPLETE / CHECKED` after corrective PR  
**Date:** 2026-07-22

## Review scope

This review re-audited the merged implementation rather than relying on the completion summary. It checked:

- theorem statements and quantifiers;
- graph and XOR solver correctness;
- incidence-forest construction;
- boundary definitions;
- exhaustive finite-domain claims;
- complexity accounting;
- deterministic report generation;
- imported planar and bounded-occurrence sources;
- synchronization of code, tests, records, and claims.

## Findings

### 1. Incidence-forest theorem

The theorem and proof remain correct:

> Every finite 3-uniform hypergraph whose incidence graph is a forest is two-colourable, and a colouring is constructible in linear incidence-graph time.

However, the merged implementation first constructed all pairs of hyperedges incident to each vertex. At a vertex of degree `d`, this creates `binom(d,2)` adjacency entries. Therefore the shipped implementation could take quadratic time even though the theorem promised a linear construction.

**Classification:** implementation-complexity defect; mathematical theorem unaffected.

**Correction:** traverse the bipartite incidence forest directly. Each incidence edge is now visited a constant number of times, giving `O(n+m)` time and space for 3-uniform input.

### 2. Boundary-width implementation

The merged direct implementation repeatedly scanned every hyperedge for every processed vertex and level. It was correct, but slower than necessary.

**Correction:** for a fixed ordering, compute each vertex's last incident-edge position. A processed vertex is live at level `k` exactly when its position is below `k` and its expiry is at least `k`. Boundary extraction is linear after preprocessing, and width is computed by interval differences.

### 3. Planar-source provenance

The planar tractability statement was correct, but the source ledger incorrectly attributed it to Darmann and Döcker and linked arXiv `1904.07825`, which is unrelated.

The correct primary result is:

- Bernard M. E. Moret, “Planar NAE3SAT is in P,” *ACM SIGACT News* 19(2):51–54, 1988, DOI `10.1145/49097.49099`.

**Classification:** provenance defect; imported theorem unaffected.

### 4. Finite computations

The following values were rechecked against the executable definitions and remain unchanged:

- labelled graphs through five vertices: `1100`, of which `428` are bipartite;
- canonical XOR systems through three variables: `16453`, of which `890` are consistent;
- labelled 3-uniform hypergraphs through five vertices: `1045`;
- incidence forests in that domain: `36`, all satisfiable;
- maximum-occurrence-at-most-three instances in that domain: `344`, all satisfiable.

These remain `COMPUTATIONAL / CHECKED` finite evidence only.

## Regression gates

The corrective gate adds:

1. a high-degree incidence-tree control that would trigger the old quadratic adjacency construction;
2. independent direct-boundary comparison for both natural and reverse orderings of every labelled instance through five vertices;
3. a pinned Moret source identifier;
4. full VS-01 through VS-04 testing and byte-identical calibration reproduction on Python 3.11, 3.12, and 3.13.

## Final claim status

- graph parity theorem and solver — `PROVED / CHECKED`;
- affine XOR theorem and solver — `PROVED / CHECKED`;
- incidence-forest theorem — `PROVED / CHECKED`;
- incidence-forest implementation runtime — corrected to match the theorem;
- bounded-boundary theorem — `PROVED / CHECKED`;
- planar tractability — `ESTABLISHED / CHECKED`, correctly attributed to Moret;
- occurrence-at-most-three tractability — `ESTABLISHED / CHECKED`;
- finite control census — `COMPUTATIONAL / CHECKED`.

No finite result or theorem was disproved. Two release defects were found and isolated: one complexity mismatch and one incorrect citation.

## Strategic conclusion

VS-04's central conclusion survives stronger review: the tractable controls do not collapse to one generic compression rule. They use parity, affine span, acyclic elimination, bounded interfaces, or exact products. Any universal proposal must either subsume these mechanisms with polynomial overhead or explain why it needs a different invariant.
