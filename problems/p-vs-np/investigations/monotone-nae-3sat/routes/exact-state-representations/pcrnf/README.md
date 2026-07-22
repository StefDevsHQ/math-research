# R1.1 — Propagation-Closed Signed Residual Normal Form

**Subroute:** `R1.1`  
**Status:** `RETAINED / OPEN CLAIM`  
**Primary claim:** `NAE-016 — CONJECTURE / CHECKED`  
**Completed slice:** `VS-08`

## Thesis

Process variables in an ordering and represent every residual instance by a propagation-closed signed residual normal form containing:

- labelled remaining vertices;
- unary colour requirements;
- signed binary constraints;
- residual ternary NAE constraints;
- residual incidence components;
- explicit component orientation bits.

Memoize identical residual states and attempt to bound the complete generated state graph polynomially.

## What was proved

`NAE-017 — PROVED / CHECKED`:

- direct residualization is exact;
- deterministic closure terminates;
- component complement is exact when orientation is recorded;
- next-variable restriction and re-closure are exact transitions.

## What was disproved

`NAE-018 — DISPROVED / CHECKED`:

> Byte equality of oriented PCRNF is exact completion equivalence.

The five-vertex witness has two different PCRNFs with the same exact completion mask.

Orientation-free normalization was also disproved independently on a single edge.

## What remains open

`NAE-016` asks whether every instance has a polynomial-time constructible ordering whose complete reachable PCRNF state graph has polynomial state count and polynomial total encoded size.

This was not disproved. The fan family gives exponential growth under a bad order but bounded growth under an interleaved order.

## Current subroute split

### `R1.1-A` — Direct state-count theorem

Try to prove a polynomial global state bound despite incomplete semantic merging.

### `R1.1-B` — Restricted PCRNF classes

Prove polynomial reachable-state bounds under explicit hypotheses such as bounded boundary width, bounded incidence treewidth, bounded residual component size, or another exact structural parameter.

### Handoff to `R1.2`

When stronger semantic merging is required, use PCRNF as the exact substrate and move to [semantic quotient over PCRNF](../semantic-quotient/README.md).

## Evidence

- [VS-08 preparation](../../../VS-08-PREPARATION.md)
- [VS-08 implementation](../../../VS-08-IMPLEMENTATION.md)
- [VS-08 completion and status-correction audit](../../../VS-08-AUDIT.md)
- executable modules under `tools/monotone-nae-3sat/nae3sat/pcrnf*.py`
- deterministic record under `tools/monotone-nae-3sat/pcrnf/`

## Reopening and continuation rule

Do not restate byte equality as a complete quotient. Continue only through a direct all-state theorem, a restricted theorem, or the stronger quotient subroute.