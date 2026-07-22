# P versus NP

This directory contains a disciplined investigation of the P versus NP problem and selected computational problems used as concrete research environments.

The repository does not claim a resolution. It preserves exact statements, established results, proof attempts, failed routes, counterexamples, computational evidence, canonical literature landscapes, and current research state without conflating them.

## Current phase

The project has opened a **Monotone NAE-3SAT investigation in formalization and route-selection mode**. No proof route is active.

The first concrete investigation, Subset Sum, completed and closed two universal routes:

1. **Structural compression** — closed as a universal polynomial-time strategy; the residue-completion lemma and a restricted polynomially bounded decomposition theorem remain valid.
2. **Exact-state compression barriers** — closed as a broad model-barrier strategy; ordered Boolean lower bounds and arithmetic representation-boundary theorems remain valid only in their recorded models.

The programme maintains three canonical orientation artifacts:

- [Research-programme landscape](references/research-programme-landscape.md) — major positive, structural, circuit, proof, meta-complexity, conditional, and barrier programmes, with the exact class consequence of each target.
- [Problem-testbed landscape](references/problem-testbed-landscape.md) — candidate testbeds and controls organized by native obstruction and research objective.
- [Canonical source map](references/top-level-landscape-sources.md) — the authoritative bibliography supporting both landscapes.

The detailed [Subset Sum algorithmic landscape](investigations/subset-sum/references/algorithmic-landscape.md) remains investigation-specific rather than the top-level project map.

## Current candidate tracks

### Symmetry-first positive investigation

The active investigation is [Monotone NAE-3SAT](investigations/monotone-nae-3sat/README.md), equivalently 2-colourability of a 3-uniform hypergraph. It uses one self-dual ternary relation, no negations, no constants, and no weights.

A deterministic polynomial-time algorithm correct on every Monotone NAE-3SAT instance would prove `P=NP`. The current phase prepares the object, controls, claim ledger, and proof obligations; it does not assert such an algorithm.

### Exactness-first sibling

Positive 1-in-3 SAT remains the strongest exactness-first candidate, with X3C and 3-Dimensional Matching as paired hard controls. It is not currently an active investigation.

### Lower-bound sibling track

The strongest current sibling candidate is **Circuit-SAT and restricted-circuit satisfiability**, because nontrivial algorithms for sufficiently expressive restricted circuit classes can sometimes be converted into circuit lower bounds.

A lower-bound route must state the exact computation or proof model and the class separation implied by the desired theorem. Failure of one model is not evidence for `P!=NP`.

## Structure

- [Foundations](foundations/README.md) — shared definitions, models, and established results
- [References and landscapes](references/README.md) — canonical cross-investigation programme, testbed, and source maps
- [Reductions](reductions/README.md) — reusable reduction infrastructure
- [Investigations](investigations/README.md) — concrete research environments
  - [Monotone NAE-3SAT](investigations/monotone-nae-3sat/README.md)
  - [Subset Sum](investigations/subset-sum/README.md)

## Navigation

- [Current status](STATUS.md)
- [Claim ledger](CLAIMS.md)
- [Research-programme landscape](references/research-programme-landscape.md)
- [Problem-testbed landscape](references/problem-testbed-landscape.md)
- [Canonical source map](references/top-level-landscape-sources.md)
- [Repository research standards](../../RESEARCH_STANDARDS.md)

## Scope restraint

No retained result proves `P=NP`, `P!=NP`, a general Boolean circuit lower bound, or a lower bound for arbitrary Subset Sum algorithms.

Landscape rankings and investigation choices are project strategy decisions, not mathematical claims that one problem is intrinsically easier or that one programme is exhaustive.

## Identifiers

Problem-wide claims use `PNP-###`. Investigation claims use stable prefixes such as `NAE-###` and `SS-###`. Route-local identifiers must link upward when they alter the accepted investigation state.
