# P versus NP

This directory contains a disciplined investigation of the P versus NP problem and selected NP-complete problems used as concrete research environments.

The repository does not claim a resolution. It preserves exact statements, established results, proof attempts, failed routes, counterexamples, computational evidence, and current research state without conflating them.

## Working scope

The current program studies whether exact algorithms for NP-complete problems admit structural compression polynomial in the binary input length, and what information prevents exact states from being merged.

## Structure

- [Foundations](foundations/README.md) — shared definitions, models, and established results
- [Reductions](reductions/README.md) — reusable reduction infrastructure
- [Investigations](investigations/README.md) — concrete research environments
  - [Subset Sum](investigations/subset-sum/README.md)

## Navigation

- [Current status](STATUS.md)
- [Claim ledger](CLAIMS.md)
- [Repository research standards](../../RESEARCH_STANDARDS.md)

## Identifiers

Problem-wide claims use `PNP-###`. Investigation claims use stable prefixes such as `SS-###`. Route-local identifiers must link upward when they alter the accepted investigation state.