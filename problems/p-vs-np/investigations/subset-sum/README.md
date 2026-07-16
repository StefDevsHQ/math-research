# Subset Sum Investigation

Subset Sum is the first concrete exact-algorithm testbed in the P versus NP program.

Given positive integers

\[
A=\{a_1,\ldots,a_n\}
\]

and a target \(T\), determine whether some subset of \(A\) sums exactly to \(T\).

## Current phase

The investigation is in route selection after closing two universal strategies:

- [Structural compression](routes/structural-compression/README.md) — closed as a universal algorithmic route; local residue completion and the polynomially bounded exact-decomposition theorem remain valid.
- [Exact-state compression barriers](routes/exact-state-compression-barriers/README.md) — closed as a broad barrier route; ordered Boolean lower bounds and arithmetic model-boundary theorems remain valid.

No active Subset Sum route is currently selected.

## Navigation

- [Current status](STATUS.md)
- [Claim ledger](CLAIMS.md)
- [Research routes](routes/README.md)
- [Structural-compression closeout](routes/structural-compression/README.md)
- [Exact-state barrier closeout](routes/exact-state-compression-barriers/CLOSEOUT.md)
- [References](references/README.md)
- [Session handoffs](journal/README.md)
- [Shared reductions](../../reductions/README.md)
- [P versus NP overview](../../README.md)
- [Research standards](../../../../RESEARCH_STANDARDS.md)

## Scope

The retained results do not prove `P=NP`, `P!=NP`, or a lower bound for arbitrary Subset Sum algorithms. Reopen a closed route only under its recorded reopening conditions.

## Identifier policy

Investigation-wide claims use `SS-###`. Route-local records may use a route prefix while linking to the authoritative investigation ledger when they change the accepted project state.