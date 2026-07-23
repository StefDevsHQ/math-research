# P versus NP

This directory contains a disciplined investigation of the P versus NP problem and selected computational problems used as concrete research environments.

The repository does not claim a resolution. It preserves exact statements, established results, proof attempts, failed routes, counterexamples, computational evidence, canonical literature landscapes, and current research state without conflating them.

## Current phase

The project is in **top-level route selection** after completing the universal exact-representation closeout for the Monotone NAE-3SAT investigation.

Two concrete investigations have now produced retained results and justified route closures:

1. **Subset Sum**
   - structural compression closed universally;
   - broad exact-state compression barriers closed within their stated models;
   - residue-completion and restricted exact-decomposition results retained.
2. **Monotone NAE-3SAT**
   - exact PCRNF residualization retained;
   - universal ordered PCRNF state enumeration disproved;
   - reduced ordered decision diagrams inherit the residual-function obstruction;
   - universal DNNF exact representation disproved on central-lift expanders;
   - restricted decomposition and compilation results retained.

No proof route is currently active.

## Canonical orientation artifacts

- [Research-programme landscape](references/research-programme-landscape.md)
- [Problem-testbed landscape](references/problem-testbed-landscape.md)
- [Canonical source map](references/top-level-landscape-sources.md)

## Current candidate tracks

### New positive investigation

Select a testbed and one atomic polynomial-time mechanism with a falsifiable promotion gate. Positive 1-in-3 SAT, X3C, and 3-Dimensional Matching remain available exactness-first candidates, but none is active.

### Lower-bound sibling

Circuit-SAT and restricted-circuit satisfiability remain the strongest sibling candidate only after fixing the exact circuit model and the theorem that would transfer an algorithmic improvement into a lower bound.

### Restricted theorem programme

Monotone NAE-3SAT restricted PCRNF and decomposition classification may continue as a secondary programme. Success there does not establish a universal algorithm.

## Structure

- [Foundations](foundations/README.md)
- [References and landscapes](references/README.md)
- [Reductions](reductions/README.md)
- [Investigations](investigations/README.md)
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

No retained result proves `P=NP`, `P!=NP`, a general Boolean circuit lower bound, or a lower bound for arbitrary algorithms.

Landscape rankings and investigation choices are project strategy decisions, not mathematical claims that one problem is intrinsically easier or that one programme is exhaustive.

## Identifiers

Problem-wide claims use `PNP-###`. Investigation claims use stable prefixes such as `NAE-###` and `SS-###`. Route-local identifiers must link upward when they alter the accepted investigation state.