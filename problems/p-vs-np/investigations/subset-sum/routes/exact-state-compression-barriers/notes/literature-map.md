# Literature Map — Exact-State Compression Barriers

**Status:** Archived route research note  
**Updated:** 2026-07-16

This note records primary literature considered during the closed `SS-ECB` route. External results are retained only within their stated representation models.

## Ordered binary decision diagrams

### Igor Razgon, 2021

“Classification of OBDD size for monotone 2-CNFs,” arXiv:2103.09115v2.

Theorem 2 gives, for the monotone two-CNF induced by a graph `G`,

\[
2^{lu(G)}\le \operatorname{obdd}(\varphi(G))\le n^{O(lu(G))}.
\]

Route use:

- imported lower bound in `SS-ECB-005`;
- combined with the project grid-width proof and assignment-target embedding.

Limitation:

- applies to OBDDs;
- does not cover arithmetic programs, free access order, or general exact query algorithms.

Source: https://arxiv.org/abs/2103.09115

## Read-once and bounded-read branching programs

### Igor Razgon, 2015

“On the read-once property of branching programs and CNFs of bounded treewidth,” arXiv:1411.0264v3.

Relevant result:

- non-deterministic syntactic read-once branching programs require large size on certain bounded-treewidth CNFs.

Source: https://arxiv.org/abs/1411.0264

### Oded Lachish and Igor Razgon, 2016

“Non-deterministic branching programs with logarithmic repetition cannot efficiently compute small monotone CNFs,” arXiv:1604.01560.

Relevant result:

- exponential lower bounds for certain bounded-read non-deterministic branching programs.

Source: https://arxiv.org/abs/1604.01560

Route limitation:

No transfer was proved from the retained structural-compression operations to these branching-program models.

## Decomposable negation normal form

### Stefan Mengel, 2016

“Parameterized Compilation Lower Bounds for Restricted CNF-formulas,” arXiv:1604.06715.

Relevant result:

- parameterized lower bounds for DNNF representations under structural restrictions.

Source: https://arxiv.org/abs/1604.06715

### Andrea Calì, Florent Capelli, and Igor Razgon, 2017

“Non-FPT lower bounds for structural restrictions of decision DNNF,” arXiv:1708.07767.

Relevant result:

- lower bounds for structured decision DNNF and OBDD variants with decomposable conjunction nodes.

Source: https://arxiv.org/abs/1708.07767

Route limitation:

No polynomial-overhead compilation of the retained item-block arithmetic summaries into these models was established.

## Tree Decision Diagrams

### Florent Capelli, YooJung Choi, Stefan Mengel, Martín Muñoz, and Guy Van den Broeck, 2026

“A canonical generalization of OBDD,” arXiv:2604.05537.

Relevant features:

- tree-structured generalization of OBDD;
- restriction of structured deterministic decomposable negation normal form;
- canonical and algorithmically tractable operations under its model assumptions.

Source: https://arxiv.org/abs/2604.05537

Route use:

- supplied the formal target for `SS-ECB-009`, the equivalence with explicit deterministic tree-state systems.

Route limitation:

- the model decomposes Boolean variables;
- no transfer from binary-encoded interval, progression, residue, exception, or recursive item-block summaries was proved.

## Bottom-up compilation

Work on large intermediate results in bottom-up knowledge compilation was considered relevant because a compact final representation need not imply a polynomial construction graph.

The route retained this distinction in its cost accounting but did not derive a Subset Sum lower bound from it.

## Final literature determination

The literature supports strong lower bounds for several restricted Boolean representation models. It did not supply the missing bridge required by this route:

1. formal polynomial-overhead inclusion of all retained structural-compression operations;
2. exclusion of polynomial Boolean simulation;
3. a superpolynomial lower bound for the same resulting model.

Further literature work is inactive unless the route is reopened under `CLOSEOUT.md`. No novelty claim is made for the project constructions or model boundaries.