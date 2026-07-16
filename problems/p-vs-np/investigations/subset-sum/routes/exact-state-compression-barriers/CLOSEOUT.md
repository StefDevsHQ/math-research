# Closeout — Exact-State Compression Barriers

**Route:** `SS-ECB`  
**State:** Closed as a path to a broad structural-compression barrier  
**Closed:** 2026-07-16

## Original objective

The route sought a formal exact-state model broad enough to contain the interval, progression, residue, exception, recursive, and target-relative mechanisms retained from structural compression, while still supporting an unconditional superpolynomial lower bound on reduction-generated Subset Sum families.

## Final determination

The route did not achieve that objective.

It established correct model-specific results and isolated a three-way obstruction:

1. **Too syntactic:** unevaluated Minkowski-sum DAGs represent every reachable set in linear size while leaving membership as the original Subset Sum problem.
2. **Too extensional:** normalized unions of bounded arithmetic progressions can require exponentially many atoms even on easy ternary superincreasing instances solved by forced target-relative reductions.
3. **Too expressive:** compact interval, progression, and bounded residue-range predicates combined with unrestricted intersection or unrestricted repeated branching evaluate arbitrary width-three CNF assignment slices with polynomial representations or proof graphs.

The proposed restricted arithmetic proof graph did not specify its branch grammar tightly enough to prove non-universality. Its natural completion with compact bounded residue-range tests crossed the third boundary: binary-payload target bits become readable, and repeated branch nodes evaluate a width-three CNF with one short literal-test chain per clause.

No natural repair survived:

- bounded residue-range branching with unrestricted reuse recovers polynomial Boolean computation;
- fixed ordered access collapses back toward the established OBDD model and does not subsume general binary-encoded residue summaries;
- explicit state tables exclude compact large-modulus arithmetic;
- forbidding target-dependent branching excludes forced separation and other target-relative mechanisms;
- informal locality restrictions do not prevent repeated clause-style computation.

Pure residue-equality branching alone was not proved sufficient for the escape, but no complete narrower model using only equality tests was formalized or shown to subsume the retained framework.

Accordingly, the route is closed rather than preserved as an indefinite model-design program.

## Retained results

The following remain valid:

- `SS-ECB-001`: representation bytes alone are a vacuous measure.
- `SS-ECB-002`: polynomial preprocessing plus polynomial exact queries is equivalent to `P=NP`.
- `SS-ECB-003`: exact assignment-target Subset Sum embedding.
- `SS-ECB-004`–`SS-ECB-006`: ordered assignment-query graphs are OBDDs and square-grid families force size `2^{Omega(L^{1/4})}` in that model.
- `SS-ECB-007`: the ordered result does not lower-bound unrestricted algorithms.
- `SS-ECB-009`: explicit Boolean tree-state systems are polynomially equivalent to deterministic Tree Decision Diagrams.
- `SS-ECB-010`: general Boolean circuits defeat the assignment-target barrier.
- `SS-ECB-011`: exact item-block summaries compose by Minkowski sum.
- `SS-ECB-012`: the retained framework requires separate exact-summary, coverage-certificate, and residual-transformation semantics.
- `SS-ECB-013`: unevaluated Minkowski DAGs are universally small.
- `SS-ECB-014`: unrestricted intersection of compact arithmetic sets restores compact CNF conjunction.
- `SS-ECB-015`: progression-union normalization can be exponentially large on easy instances.
- `SS-ECB-017`: compact bounded residue-range tests plus unrestricted repeated branching simulate width-three CNF assignment evaluation in polynomial graph size.

These are representation-model boundaries and design constraints. They do not imply a general lower bound for Subset Sum or evidence sufficient for `P != NP`.

## Failed candidate

`SS-ECB-016`, the restricted arithmetic proof graph, is retracted. Its branch syntax was under-specified, and its natural bounded-residue completion failed the non-universality requirement.

## Reopening condition

Reopen this route only with a materially new theorem or mechanism satisfying all of:

1. fully specified item-block and target-relative semantics;
2. polynomial-overhead inclusion of every retained structural operation;
3. a proved restriction preventing polynomial Boolean simulation;
4. an explicit hard-family lower bound for the same model;
5. full accounting of intermediate construction and query graphs.

A new name for ordered access, bounded tables, or unspecified local arithmetic does not meet the reopening condition.

## Recommended pivot

Do not continue searching for a universal compression language by interpolation between explicit tables and general circuits.

The next Subset Sum route should pursue either:

- a separately justified tractable subclass with a positive exact algorithm and globally polynomial state bound; or
- a different P-versus-NP investigation not centered on exact-state compression.

The route has completed its useful role by defining the boundaries future proposals must cross. See the [final audit](audits/2026-07-16-final-audit.md).