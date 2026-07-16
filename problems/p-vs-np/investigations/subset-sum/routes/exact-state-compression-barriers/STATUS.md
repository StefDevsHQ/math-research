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
- The assignment-target family is polynomially representable in every model containing general polynomial-size Boolean circuits with access to the decoded assignment bits.

## Adversarial verdict

The ordered barrier is genuine but narrow.

It does not lower-bound arbitrary Subset Sum algorithms, fixed-target decision procedures, compact arithmetic programs, or representations with unrestricted polynomial-time query logic. The structured targets expose an assignment that can be decoded and checked against the formula directly.

The tree-state model is broader, but it still does not automatically contain succinct arithmetic summaries. A modulus \(q\) may be encoded in \(O(\log q)\) bits while an explicit residue transition table has \(q\) states or entries.

The opposite extreme also fails: a transition language containing arbitrary polynomial-size Boolean circuits can retain the original CNF and evaluate it directly. Therefore the desired model must be strictly weaker than general circuits.

## Smallest remaining gap

The route now needs a restricted **succinct transition language** between two extremes:

1. explicit tables, which admit knowledge-compilation lower bounds but may not express large binary-encoded arithmetic compactly;
2. general circuits or unrestricted polynomial-time programs, which are too powerful because they can evaluate the whole source formula or run any available decision procedure.

The required language must contain the interval, progression, residue, exception, and recursive summaries from structural compression and still support an unconditional superpolynomial lower bound.

## Next actions

1. Classify each retained structural-summary atom by the Boolean query representation it induces over target bits.
2. Test bounded-read branching programs and restricted arithmetic circuits as intermediate languages.
3. Separate final-representation size from bottom-up compilation cost; existing knowledge-compilation work shows that small final representations can coexist with exponentially large intermediate apply results.
4. Search for Tree Decision Diagram lower bounds on families not neutralized by balanced tree decomposition.
5. Audit target-specific pruning independently.

## Stop condition

Close the route as too model-specific unless a succinct transition model is found that formally subsumes the previous structural summaries and still admits a superpolynomial lower bound. Do not present ordered or explicit-tree hardness alone as a general Subset Sum obstruction.