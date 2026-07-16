# Exact-State Compression Barriers

**Route identifier:** `SS-ECB`  
**State:** Closed as a broad structural-compression barrier route  
**Opened:** 2026-07-16  
**Closed:** 2026-07-16

## Objective

This route asked whether an exact-state model could simultaneously:

1. contain the retained interval, progression, residue, exception, recursive, and target-relative mechanisms from structural compression;
2. exclude compact simulation of general Boolean computation;
3. support a superpolynomial lower bound on an explicit Subset Sum family.

No model satisfying all three requirements was established.

## Retained results

The route established:

- unrestricted representation size is a vacuous complexity measure;
- polynomial compilation plus polynomial exact queries is equivalent to `P=NP`;
- an exact assignment-target embedding for width-three CNF evaluation;
- an ordered query-representation lower bound of `2^{Omega(L^{1/4})}` on square-grid assignment slices;
- a polynomial equivalence between explicit Boolean tree-state systems and deterministic Tree Decision Diagrams;
- exact Minkowski composition for disjoint item blocks;
- a semantic separation between exact summaries, coverage certificates, and target-relative residual transformations;
- a linear-size unevaluated Minkowski-DAG boundary;
- an unrestricted-intersection escape;
- an exponential progression-union lower bound on easy ternary superincreasing instances;
- a bounded-residue branching escape.

## Final obstruction

The model search encountered three incompatible regimes:

1. unevaluated additive syntax remains small by retaining the original instance;
2. extensional arithmetic normalization can be exponentially large even when target-relative decision is easy;
3. compact residue-range predicates combined with repeated branching or unrestricted intersection recover polynomial Boolean computation.

The proposed restricted arithmetic proof graph was under-specified. Its natural bounded-residue completion crossed the third boundary and was retracted.

## Scope

The retained results are representation-model boundaries. They do not establish a lower bound for arbitrary Subset Sum algorithms, a hard fixed-target family, or `P != NP`.

## Reopening condition

Reopen only with a materially new mechanism providing all of:

1. exact item-block and target-relative semantics;
2. polynomial-overhead inclusion of every retained structural operation;
3. a proved restriction preventing polynomial Boolean simulation;
4. a superpolynomial lower bound for that same model;
5. complete intermediate construction and query accounting.

## Navigation

- [Closeout](CLOSEOUT.md)
- [Final audit](audits/2026-07-16-final-audit.md)
- [Final status](STATUS.md)
- [Claim ledger](CLAIMS.md)
- [Item-block semantics](notes/item-block-semantics.md)
- [Retracted arithmetic proof-graph candidate](notes/restricted-arithmetic-proof-graph.md)
- [Ordered assignment-target embedding](proofs/assignment-target-obdd-transfer.md)
- [Grid-family ordered barrier](proofs/grid-family-state-barrier.md)
- [Tree-state and Tree Decision Diagram equivalence](proofs/tree-state-tdd-equivalence.md)
- [Unevaluated Minkowski-DAG boundary](proofs/minkowski-dag-boundary.md)
- [Intersection escape](proofs/binary-payload-intersection-escape.md)
- [Progression-union lower bound](proofs/progression-union-lower-bound.md)
- [Bounded-residue branching escape](counterexamples/residue-branching-circuit-escape.md)
