# Status — Exact-State Compression Barriers

**State:** Active; ordered barrier and explicit tree-state model established  
**Updated:** 2026-07-16

## Current position

The route has passed two formalization tests.

First, a precise ordered target-query state model was transferred exactly to ordered binary decision diagrams. On square-grid monotone two-CNF formulas, the resulting Subset Sum target-query families require complete ordered state graphs of size

\[
2^{\Omega(L^{1/4})},
\]

where \(L\) is the binary length of the encoded item multiset and target.

Second, an explicit deterministic bottom-up tree-state model has been defined and proved polynomially equivalent to deterministic Tree Decision Diagrams respecting the same variable tree.

## Accepted route results

- Unrestricted representation-size lower bounds are impossible: the original instance is already a linear-size exact representation when query computation is unrestricted.
- Universal polynomial-time preprocessing and polynomial-time exact target queries exist if and only if Subset Sum is in polynomial time, equivalently if and only if \(P=NP\).
- The assignment-target no-carry embedding is exact and polynomially bounded.
- Ordered assignment-target query graphs transfer to ordered binary decision diagrams.
- Square-grid families force superpolynomial complete state graphs in that ordered model.
- Explicit deterministic tree-state systems with fully counted transition tables are polynomially equivalent to deterministic Tree Decision Diagrams.

## Adversarial verdict

The ordered barrier is genuine but narrow.

It does not lower-bound arbitrary Subset Sum algorithms, fixed-target decision procedures, compact arithmetic programs, or representations with unrestricted polynomial-time query logic. The structured targets expose an assignment that can be decoded and checked against the formula directly.

The tree-state model is broader, but it still does not automatically contain succinct arithmetic summaries. A modulus \(q\) may be encoded in \(O(\log q)\) bits while an explicit residue transition table has \(q\) states or entries.

## Smallest remaining gap

The route now needs a restricted **succinct transition language** between two extremes:

1. explicit tables, which admit knowledge-compilation lower bounds but may not express large binary-encoded arithmetic compactly;
2. unrestricted polynomial-time programs, which are too powerful because they can evaluate the whole source formula or run any available decision procedure.

The required language must contain the interval, progression, residue, exception, and recursive summaries from structural compression and still support an unconditional superpolynomial lower bound.

## Next actions

1. Classify each retained structural-summary atom by the Boolean query representation it induces over target bits.
2. Test bounded-read branching programs and structured decision decomposable negation normal form as intermediate languages.
3. Search for explicit Tree Decision Diagram lower bounds or derive one through subfunction counts for a family not neutralized by tree decomposition.
4. Separate final-representation size from bottom-up compilation cost; a small final diagram may still require large intermediate apply states.
5. Audit target-specific pruning independently.

## Stop condition

Close the route as too model-specific unless a succinct transition model is found that formally subsumes the previous structural summaries and still admits a superpolynomial lower bound. Do not present ordered or explicit-tree hardness alone as a general Subset Sum obstruction.
