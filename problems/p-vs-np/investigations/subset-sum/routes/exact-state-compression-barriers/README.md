# Exact-State Compression Barriers

**Route identifier:** `SS-ECB`  
**State:** Closed as a broad structural-compression barrier route  
**Opened:** 2026-07-16  
**Closed:** 2026-07-16

## Objective

This route asked whether one could formalize an exact-state model broad enough to contain the retained interval, progression, residue, exception, recursive, and target-relative mechanisms from structural compression while still proving a superpolynomial lower bound on reduction-generated Subset Sum families.

The route did not achieve that combined objective.

## Retained results

The route established:

- representation size alone is vacuous when query computation is unrestricted;
- polynomial compilation plus polynomial exact queries is equivalent to `P=NP`;
- an exact assignment-target Subset Sum embedding for width-three CNF evaluation;
- an ordered-binary-decision-diagram lower bound of `2^{Omega(L^{1/4})}` on square-grid assignment-query families;
- polynomial equivalence between explicit Boolean tree-state systems and deterministic Tree Decision Diagrams;
- exact Minkowski composition for disjoint item blocks;
- the semantic distinction between exact summaries, coverage certificates, and target-relative residual transformations;
- the linear-size unevaluated Minkowski-DAG boundary;
- the unrestricted-intersection escape;
- an exponential progression-union lower bound on easy ternary superincreasing instances;
- the residue-branching circuit escape.

## Final obstruction

The model search encountered three incompatible regimes:

1. unevaluated additive syntax remains small by retaining the original instance;
2. extensional progression normalization can be exponentially large even when target-relative decision is easy;
3. compact residue predicates combined with repeated branching or unrestricted intersection recover polynomial Boolean computation.

The proposed restricted arithmetic proof graph crossed the third boundary. It was therefore retracted.

## Scope

The ordered and arithmetic results are representation-model boundaries. They do not establish a lower bound for arbitrary Subset Sum algorithms, a hard fixed-target family, or `P != NP`.

## Reopening condition

Reopen only with a materially new mechanism that simultaneously provides:

1. exact item-block and target-relative semantics;
2. polynomial-overhead inclusion of every retained structural operation;
3. a proved restriction preventing polynomial Boolean simulation;
4. a superpolynomial lower bound for that same model;
5. complete intermediate construction and query accounting.

## Navigation

- [Closeout](CLOSEOUT.md)
- [Final status](STATUS.md)
- [Claim ledger](CLAIMS.md)
- [Item-block semantics](notes/item-block-semantics.md)
- [Ordered assignment-target embedding](proofs/assignment-target-obdd-transfer.md)
- [Grid-family ordered barrier](proofs/grid-family-state-barrier.md)
- [Tree-state and Tree Decision Diagram equivalence](proofs/tree-state-tdd-equivalence.md)
- [Unevaluated Minkowski-DAG boundary](proofs/minkowski-dag-boundary.md)
- [Intersection escape](proofs/binary-payload-intersection-escape.md)
- [Progression-union lower bound](proofs/progression-union-lower-bound.md)
- [Residue-branching escape](counterexamples/residue-branching-circuit-escape.md)
- [Route review](audits/2026-07-16-route-review.md)