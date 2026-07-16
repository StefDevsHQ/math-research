# Status — Exact-State Compression Barriers

**State:** Closed as a broad structural-compression barrier route  
**Updated:** 2026-07-16

## Final position

The route produced correct model-specific results but did not find a formal model satisfying all required properties.

Retained results include:

- the assignment-target embedding and ordered-binary-decision-diagram lower bound;
- the explicit tree-state and Tree Decision Diagram equivalence;
- exact item-block Minkowski semantics;
- the proof that the retained framework needs separate exact-summary, coverage-certificate, and target-relative residual layers;
- the unevaluated Minkowski-DAG boundary;
- the unrestricted-intersection escape;
- the exponential progression-union lower bound on easy ternary superincreasing instances;
- the residue-branching circuit escape.

## Decisive obstruction

Candidate models fall into three regimes:

1. **Too syntactic:** unevaluated additive DAGs are linearly small for every instance but leave membership unresolved.
2. **Too extensional:** normalized progression unions can be exponentially large even on instances solved efficiently by forced residual reductions.
3. **Too expressive:** compact congruence access combined with unrestricted repeated branching or intersection evaluates arbitrary CNF assignment slices in polynomial size.

The restricted arithmetic proof-graph candidate crossed the third boundary. Repeated local residue tests can recover payload bits and evaluate one clause after another. `SS-ECB-016` is therefore retracted and `SS-ECB-017` records the escape theorem.

## Scope

The retained lower bounds are representation-model results. They do not imply a lower bound for arbitrary Subset Sum algorithms, a hard fixed-target family, or `P != NP`.

## Reopening condition

Reopen only with a materially new mechanism that provides:

1. exact item-block and target-relative semantics;
2. polynomial-overhead inclusion of every retained structural operation;
3. a proved restriction preventing polynomial Boolean simulation;
4. a superpolynomial lower bound for the same model;
5. complete intermediate construction and query accounting.

## Recommendation

Do not continue interpolating between explicit tables and general circuits. Select either a separately justified tractable Subset Sum subclass or another P-versus-NP investigation.

See [Closeout](CLOSEOUT.md) and the [claim ledger](CLAIMS.md).