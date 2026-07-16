# P versus NP

This directory contains a disciplined investigation of the P versus NP problem and selected computational problems used as concrete research environments.

The repository does not claim a resolution. It preserves exact statements, established results, proof attempts, failed routes, counterexamples, computational evidence, literature landscapes, and current research state without conflating them.

## Current phase

The first concrete investigation, Subset Sum, has completed and closed two universal routes:

1. **Structural compression** — closed as a universal polynomial-time strategy; the residue-completion lemma and a restricted polynomially bounded decomposition theorem remain valid.
2. **Exact-state compression barriers** — closed as a broad model-barrier strategy; ordered Boolean lower bounds and arithmetic representation-boundary theorems remain valid only in their recorded models.

The project has now completed two route-selection audits:

- a detailed [Subset Sum algorithmic landscape](investigations/subset-sum/references/algorithmic-landscape.md);
- a cross-investigation [P-versus-NP research-programme landscape](references/research-programme-landscape.md) and [problem-testbed landscape](references/problem-testbed-landscape.md).

No new investigation or route is active. The program is in top-level route selection.

## Current candidate tracks

The top-level landscape separates two distinct tracks.

### Positive investigation track

The strongest next positive candidate is the **exact-incidence constraint cluster** centred on Positive 1-in-3 SAT, with X3C and 3-Dimensional Matching as paired controls.

A route is not active until it states a concrete mechanism, exact success criterion, tractable neighbours, canonical adversarial reductions, and complete complexity accounting.

### Lower-bound sibling track

The strongest lower-bound sibling candidate is **Circuit-SAT and restricted-circuit satisfiability**, because nontrivial algorithms for sufficiently expressive restricted circuit classes can sometimes be converted into circuit lower bounds.

A lower-bound route must state the exact computation or proof model and the class separation implied by the desired theorem. Failure of one model is not evidence for `P!=NP`.

## Structure

- [Foundations](foundations/README.md) — shared definitions, models, and established results
- [References and landscapes](references/README.md) — cross-investigation programme and testbed maps
- [Reductions](reductions/README.md) — reusable reduction infrastructure
- [Investigations](investigations/README.md) — concrete research environments
  - [Subset Sum](investigations/subset-sum/README.md)

## Navigation

- [Current status](STATUS.md)
- [Claim ledger](CLAIMS.md)
- [Research-programme landscape](references/research-programme-landscape.md)
- [Problem-testbed landscape](references/problem-testbed-landscape.md)
- [Top-level primary-source map](references/top-level-landscape-sources.md)
- [Repository research standards](../../RESEARCH_STANDARDS.md)

## Scope restraint

No retained result proves `P=NP`, `P!=NP`, a general Boolean circuit lower bound, or a lower bound for arbitrary Subset Sum algorithms.

Landscape rankings are strategic recommendations, not mathematical claims that one problem is intrinsically easier or that one programme is complete.

## Identifiers

Problem-wide claims use `PNP-###`. Investigation claims use stable prefixes such as `SS-###`. Route-local identifiers must link upward when they alter the accepted investigation state.