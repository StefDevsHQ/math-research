# Status — Exact-State Compression Barriers

**State:** Active; model-specific Boolean barriers established, structural-summary transfer absent  
**Updated:** 2026-07-16

## Current position

The route has established two precise Boolean representation results.

First, the assignment-target construction converts formula evaluation into membership queries for a fixed Subset Sum item multiset. Under the route's ordered query-graph definition, the resulting representation is exactly an ordered binary decision diagram. On square-grid monotone two-CNF formulas, every such graph has size

\[
2^{\Omega(L^{1/4})},
\]

where \(L\) is the binary length of the encoded item multiset and target.

Second, an explicit deterministic bottom-up tree-state model over assignment-variable blocks has been defined and proved polynomially equivalent to deterministic Tree Decision Diagrams respecting the same variable tree.

Neither result currently compiles or lower-bounds the interval, progression, residue, exception, or recursive item-block summaries from the closed structural-compression route.

## Accepted route results

- Unrestricted representation-size lower bounds are impossible: the original instance is already a linear-size exact representation when query computation is unrestricted.
- Universal polynomial-time preprocessing and polynomial-time exact target queries exist if and only if Subset Sum is in polynomial time, equivalently if and only if \(P=NP\).
- The assignment-target no-carry embedding is exact and polynomially bounded.
- Ordered assignment-target query graphs are, by definition and semantics, ordered binary decision diagrams for the source formula.
- Square-grid families force superpolynomial complete graph size in that ordered Boolean model.
- Explicit deterministic tree-state systems with fully counted transition tables are polynomially equivalent to deterministic Tree Decision Diagrams for Boolean query functions.
- The assignment-target family is polynomially representable in every model containing general polynomial-size Boolean circuits with unrestricted access to the decoded assignment bits.

## Adversarial verdict

The ordered lower bound is genuine but narrow.

It does not lower-bound arbitrary Subset Sum algorithms, fixed-target decision procedures, compact arithmetic programs, or representations with unrestricted polynomial-time query logic. The structured targets expose an assignment that can be decoded and checked against the formula directly.

The tree-state equivalence is also correct, but its tree decomposes assignment variables rather than Subset Sum item blocks or reachable-sum structure. Calling it a successor to structural compression requires a further subsumption theorem that has not been proved.

Explicit tables are too weak to represent a binary-encoded modulus \(q\) without potentially expanding to \(q\) states or entries. At the opposite extreme, unrestricted circuits or programs can retain the original CNF and evaluate it directly. A viable intermediate model may use circuit-like local operations only if access, locality, composition, and complete construction cost are restricted enough to block this escape.

## Smallest remaining gap

No current theorem establishes both:

1. polynomial-overhead expression of the retained structural-summary operations;
2. a superpolynomial lower bound on the resulting complete representation or construction graph.

The route should not claim a barrier against structural compression until both parts are proved in the same formal model.

## Next actions — not yet started

1. Define candidate restricted transition languages only after fixing their item-block semantics, target access, locality, sharing, and total construction-cost measure.
2. Require an explicit compilation theorem for every retained structural-summary atom.
3. Attack each candidate for circuit simulation before seeking a lower bound.
4. Separate final-representation size from intermediate bottom-up compilation cost.

## Stop condition

Close the route as too model-specific unless a model is found that formally subsumes the previous structural summaries and still admits a superpolynomial lower bound. Do not present ordered or explicit-tree Boolean hardness alone as a general Subset Sum obstruction.
