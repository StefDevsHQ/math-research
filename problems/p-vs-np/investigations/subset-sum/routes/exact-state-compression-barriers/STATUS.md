# Status — Exact-State Compression Barriers

**State:** Active; first model-specific barrier established  
**Updated:** 2026-07-16

## Current position

The route has passed its first formalization test.

A precise ordered target-query state model has been defined, a no-carry assignment-target embedding has been proved, and the model has been transferred exactly to ordered binary decision diagrams. On square-grid monotone two-CNF formulas, the resulting Subset Sum target-query families require complete ordered state graphs of size

\[
2^{\Omega(L^{1/4})}
\]

where \(L\) is the binary length of the encoded item multiset and target.

## Accepted route results

- Unrestricted representation-size lower bounds are impossible: the original instance is already a linear-size exact representation when query computation is unrestricted.
- Universal polynomial-time preprocessing and polynomial-time exact target queries exist if and only if Subset Sum is in polynomial time, equivalently if and only if \(P=NP\).
- The assignment-target no-carry embedding is exact and polynomially bounded.
- Ordered assignment-target query graphs transfer to ordered binary decision diagrams.
- Square-grid families force superpolynomial complete state graphs in that ordered model.

## Adversarial verdict

The first barrier is genuine but narrow.

It does not lower-bound arbitrary Subset Sum algorithms, fixed-target decision procedures, compact arithmetic programs, or representations with unrestricted polynomial-time query logic. In fact, the structured targets expose an assignment that can be decoded and checked against the formula directly.

The result closes ordered decision-diagram compression as a universal exact-state mechanism. It does not yet close the former interval/progression/residue framework because compact modular arithmetic need not compile into a small ordered decision diagram.

## Main blocker

No formal model has yet been proved to satisfy both requirements:

1. it contains the full structural-compression operation set, including large moduli encoded in binary and recursive composition;
2. it has a known or project-proved superpolynomial lower bound on reduction-generated families.

## Next actions

1. Define a tree-structured exact composition model with explicit state syntax, merge semantics, sharing, target access, and total computation-graph accounting.
2. Test whether Tree Decision Diagrams, structured deterministic decomposable negation normal form, or bounded-read branching programs provide the correct transfer target.
3. Prove or refute that polynomially many interval, progression, residue, and exception atoms induce polynomial representations in one of those models.
4. Audit target-specific pruning separately; do not infer a decision lower bound from a compilation lower bound.

## Stop condition

Close the route as too model-specific unless a broader model is found that formally subsumes the previous structural summaries and still admits a superpolynomial lower bound. Do not present ordered-binary-decision-diagram hardness alone as a general Subset Sum obstruction.
