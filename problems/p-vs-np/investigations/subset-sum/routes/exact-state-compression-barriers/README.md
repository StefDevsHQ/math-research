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

A deterministic layered graph that reads the bits of \(\alpha\) in a fixed order and answers this membership query is exactly an ordered binary decision diagram for \(\varphi\), up to terminal and layering conventions.

## First barrier

For monotone two-CNF formulas induced by square grids, Razgon's ordered-binary-decision-diagram lower bound together with a project proof that the grid has linear upper induced-matching width gives a complete state-graph lower bound

\[
2^{\Omega(r)}
\]

for an \(r\times r\) grid. The corresponding Subset Sum query family has binary encoding length \(L=O(r^4)\), so the lower bound is

\[
2^{\Omega(L^{1/4})}.
\]

This rules out polynomial complete state graphs for the ordered query model.

## Scope limitation

The result does **not** imply a lower bound for arbitrary fixed-target Subset Sum algorithms. The target family explicitly encodes assignments, and a general algorithm may decode the assignment and evaluate the CNF directly in polynomial time. The result is therefore a representation-model barrier, not an algorithmic lower bound and not evidence that \(P\ne NP\).

The decisive remaining task is to formalize a broader compositional model that:

1. contains the interval, progression, residue, and recursive summaries used by the closed structural-compression route;
2. still admits a valid transfer to a representation model with a proven superpolynomial lower bound.

## Navigation

- [Operational status](STATUS.md)
- [Claim ledger](CLAIMS.md)
- [Unrestricted representation boundary](proofs/unrestricted-representation-boundary.md)
- [Assignment-target embedding and OBDD transfer](proofs/assignment-target-obdd-transfer.md)
- [Grid-family state barrier](proofs/grid-family-state-barrier.md)
- [Model-scope audit](audits/ordered-model-scope.md)
- [Literature map](notes/literature-map.md)
- [Opening journal record](journal/2026-07-16-route-opened.md)
