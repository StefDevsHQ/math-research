# Literature Map — Exact-State Compression Barriers

**Status:** Research note  
**Updated:** 2026-07-16

This note records primary sources relevant to exact-state representation lower bounds. External results are not promoted beyond their stated models.

## 1. Ordered binary decision diagrams

### Igor Razgon, 2021

“Classification of OBDD size for monotone 2-CNFs,” arXiv:2103.09115v2.

Primary result used by this route:

- Theorem 2 proves

  \[
  2^{lu(G)}\le \operatorname{obdd}(\varphi(G))\le n^{O(lu(G))}
  \]

  for the monotone two-CNF induced by a graph \(G\).

Use here:

- supplies the imported lower bound in `SS-ECB-005`;
- combines with the project grid-width proof and the assignment-target embedding.

Limitation:

- applies to ordered binary decision diagrams;
- does not cover free ordering, arithmetic programs, or general exact query algorithms.

Source: https://arxiv.org/abs/2103.09115

## 2. Non-deterministic read-once branching programs

### Igor Razgon, 2015

“On the read-once property of branching programs and CNFs of bounded treewidth,” arXiv:1411.0264v3.

Reported result:

- non-deterministic syntactic read-once branching programs require size \(n^{\Omega(k)}\) on certain CNFs of primal treewidth at most \(k\);
- the paper derives a separation involving free binary decision diagrams and decision decomposable negation normal form.

Potential route use:

- a broader residual-state model may naturally induce a non-deterministic read-once branching program rather than an ordered one;
- monotone two-CNF instances remain compatible with no-carry embeddings.

Unresolved work:

- define the exact Subset Sum state model;
- prove a transfer preserving read-once syntax, graph size, and binary encoding;
- verify a hard family with the required parameter growth.

Source: https://arxiv.org/abs/1411.0264

## 3. Bounded-read non-deterministic branching programs

### Oded Lachish and Igor Razgon, 2016

“Non-deterministic branching programs with logarithmic repetition cannot efficiently compute small monotone CNFs,” arXiv:1604.01560.

Reported result:

- exponential lower bounds for syntactic non-deterministic read-\(d\) branching programs when \(d\le \log n/10^5\), on constructible monotone CNFs with a linear number of clauses.

Potential route use:

- permits bounded repeated access rather than a strict read-once order;
- may capture recursive state refinement more naturally than OBDD.

Obstruction:

- the hard formulas are not immediately the normalized width-three family used by the existing reduction;
- clause-width conversion must preserve the branching-program lower bound or a generalized no-carry target embedding must be proved.

Source: https://arxiv.org/abs/1604.01560

## 4. Decomposable negation normal form

### Stefan Mengel, 2016

“Parameterized Compilation Lower Bounds for Restricted CNF-formulas,” arXiv:1604.06715.

Reported result:

- unconditional parameterized lower bounds for decomposable negation normal form representations of CNFs under structural width restrictions.

Potential route use:

- decomposable conjunction resembles exact composition over disjoint item blocks;
- a structured variant may be a better target for tree-shaped Subset Sum summaries.

Obstruction:

- unrestricted DNNF may allow operations not present in the previous route;
- the transfer must preserve determinism, decomposability, target semantics, and total circuit size.

Source: https://arxiv.org/abs/1604.06715

### Andrea Calì, Florent Capelli, and Igor Razgon, 2017

“Non-FPT lower bounds for structural restrictions of decision DNNF,” arXiv:1708.07767.

Reported result:

- non-fixed-parameter lower bounds for structured decision DNNF and OBDD with decomposable conjunction nodes on CNFs of bounded incidence treewidth.

Potential route use:

- closer to a compositional state graph with branching and independent subproblems;
- candidate for a formal tree-structured successor to the ordered model.

Source: https://arxiv.org/abs/1708.07767

## 5. Tree Decision Diagrams

### Florent Capelli, YooJung Choi, Stefan Mengel, Martín Muñoz, and Guy Van den Broeck, 2026

“A canonical generalization of OBDD,” arXiv:2604.05537.

The paper introduces Tree Decision Diagrams:

- a tree-structured generalization of OBDD;
- a restriction of structured deterministic decomposable negation normal form;
- a model supporting efficient apply, conditioning, minimization, and canonical representations;
- a model that can compile bounded-treewidth CNFs with fixed-parameter-size representations.

Why this is the leading next candidate:

- the vtree provides an explicit composition tree;
- node sets at each vtree position behave like context-independent local states;
- apply and minimization resemble bottom-up exact state construction;
- the model is broader than ordered linear processing.

Risk:

- the model may be too powerful for the square-grid OBDD family, because it can be exponentially more succinct than OBDD;
- a new hard family or a new lower-bound theorem may be necessary;
- no transfer from interval, progression, or residue summaries has been proved.

Source: https://arxiv.org/abs/2604.05537

## 6. Route decision from the literature

### Retained

- OBDD gives a complete first barrier and a proof template.
- Branching-program and knowledge-compilation lower bounds show that broader model-specific barriers are mathematically plausible.
- Tree Decision Diagrams provide the most natural current formal language for tree-shaped context-independent composition.

### Rejected as insufficient

- communication complexity alone generally yields a bit lower bound, not automatically a superpolynomial total-state lower bound;
- counting reachable sums does not imply representation size;
- OBDD lower bounds alone do not contain binary-encoded modular arithmetic;
- unrestricted representation lower bounds are impossible because the source instance can be stored directly.

## 7. Next literature task

Determine whether one of the following is already known:

1. a superpolynomial lower bound for Tree Decision Diagrams on an explicit polynomial-size CNF family;
2. a lower bound for structured deterministic decomposable negation normal form that survives the assignment-target embedding;
3. a characterization of interval, congruence, or semilinear membership programs inside a knowledge-compilation class;
4. a lower bound for bottom-up apply-based compilation that counts all intermediate representations even when the final representation is small.

No novelty claim is made for the project transfer framework until these connections are searched more thoroughly.
