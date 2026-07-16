# Exact-State Compression Barriers

**Route identifier:** `SS-ECB`  
**State:** Active  
**Opened:** 2026-07-16

## Objective

This route asks which exact-state representation models necessarily retain superpolynomially many compatibility states on structured Subset Sum families.

The route is not a direct attempt to prove a lower bound for every Subset Sum algorithm. It fixes a representation or computation model, proves an exact transfer to a known Boolean representation model where possible, and records only model-specific conclusions.

## Boundary established first

Representation size alone is not a meaningful obstruction. The original binary instance is already a polynomial-size exact representation if unrestricted computation is permitted at query time. A useful barrier must therefore restrict at least one of:

- construction time;
- query time;
- merge or composition operations;
- variable or item access order;
- decomposition structure;
- complete computation-graph size.

See [Unrestricted representation boundary](proofs/unrestricted-representation-boundary.md).

## First formal model

The initial model is an **ordered assignment-target query graph**.

For a CNF formula \(\varphi\), a fixed Subset Sum item multiset \(A_\varphi\) is constructed together with an injective target map

\[
\alpha\longmapsto \tau_\varphi(\alpha)
\]

such that

\[
\tau_\varphi(\alpha)\in\Sigma(A_\varphi)
\quad\Longleftrightarrow\quad
\alpha\models\varphi.
\]

A deterministic graph that reads the bits of \(\alpha\) in a fixed order and answers this membership query is, by the model definition, an ordered binary decision diagram for \(\varphi\). This is an exact Boolean-model equivalence, not yet a compilation theorem from a pre-existing Subset Sum summary language.

## First barrier

For monotone two-CNF formulas induced by square grids, Razgon's ordered-binary-decision-diagram lower bound together with a project proof that the grid has linear upper induced-matching width gives a complete graph-size lower bound

\[
2^{\Omega(r)}
\]

for an \(r\times r\) grid. The corresponding assignment-target query family has binary encoding length \(L=O(r^4)\), so the lower bound is

\[
2^{\Omega(L^{1/4})}.
\]

This rules out polynomial-size ordered assignment-target query graphs. It does not yet rule out any representation used by the closed structural-compression route.

## Broader formal model

The second model is an **explicit deterministic tree-state system**. Assignment variables are partitioned by a binary variable tree, local states are computed bottom-up, and every child-state transition is explicitly counted.

This model is polynomially equivalent to deterministic Tree Decision Diagrams respecting the same variable tree. It is a precise tree-structured Boolean query model, but it is not yet a tree decomposition of Subset Sum item blocks or reachable-sum summaries.

The inclusion boundary is therefore:

- explicit transition tables over assignment-variable blocks are covered;
- arbitrary polynomial-time transition programs are not covered;
- compact binary-encoded arithmetic atoms are not proved to compile with polynomial overhead;
- no transfer from the interval, progression, residue, exception, or recursive summaries of the previous route has been proved.

## Scope limitation

The ordered result does **not** imply a lower bound for arbitrary fixed-target Subset Sum algorithms. The target family explicitly encodes assignments, and a general algorithm may decode the assignment and evaluate the CNF directly in polynomial time. The result is therefore a Boolean representation-model barrier, not an algorithmic lower bound and not evidence that \(P\ne NP\).

The decisive remaining task is to identify a restricted succinct transition model that:

1. contains the interval, progression, residue, exception, and recursive summaries used by the closed structural-compression route;
2. still admits a valid transfer to a representation model with a proven superpolynomial lower bound;
3. restricts access or composition enough that the original source formula cannot simply be retained as an unrestricted circuit.

## Navigation

- [Operational status](STATUS.md)
- [Claim ledger](CLAIMS.md)
- [Route re-audit](audits/2026-07-16-route-review.md)
- [Unrestricted representation boundary](proofs/unrestricted-representation-boundary.md)
- [Assignment-target embedding and OBDD equivalence](proofs/assignment-target-obdd-transfer.md)
- [Grid-family ordered barrier](proofs/grid-family-state-barrier.md)
- [Tree-state and Tree Decision Diagram equivalence](proofs/tree-state-tdd-equivalence.md)
- [Ordered-model scope audit](audits/ordered-model-scope.md)
- [Literature map](notes/literature-map.md)
- [Opening journal record](journal/2026-07-16-route-opened.md)
