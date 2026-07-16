# P versus NP

This directory contains a disciplined investigation of the P versus NP problem and selected NP-complete problems used as concrete research environments.

The repository does not claim a resolution. It preserves exact statements, established results, proof attempts, failed routes, counterexamples, computational evidence, and current research state without conflating them.

## Current phase

The first Subset Sum investigation has completed two universal routes:

1. **Structural compression** — closed as a universal polynomial-time strategy; the residue-completion lemma and a restricted polynomially bounded decomposition theorem remain valid.
2. **Exact-state compression barriers** — closed as a broad model-barrier strategy; ordered Boolean lower bounds and arithmetic representation-boundary theorems remain valid only in their recorded models.

No active Subset Sum route is currently selected. The program is in route selection.

## Working scope

Future work must choose one of the following before becoming active:

- a positive exact algorithm for a separately justified tractable subclass with complete binary-length and global-state accounting; or
- a different P-versus-NP investigation not centered on universal exact-state compression.

The two closed routes must not be reopened without satisfying their recorded reopening conditions.

## Structure

- [Foundations](foundations/README.md) — shared definitions, models, and established results
- [Reductions](reductions/README.md) — reusable reduction infrastructure
- [Investigations](investigations/README.md) — concrete research environments
  - [Subset Sum](investigations/subset-sum/README.md)

## Navigation

- [Current status](STATUS.md)
- [Claim ledger](CLAIMS.md)
- [Repository research standards](../../RESEARCH_STANDARDS.md)

## Scope restraint

No retained result proves `P=NP`, `P!=NP`, or a lower bound for arbitrary Subset Sum algorithms.

## Identifiers

Problem-wide claims use `PNP-###`. Investigation claims use stable prefixes such as `SS-###`. Route-local identifiers must link upward when they alter the accepted investigation state.