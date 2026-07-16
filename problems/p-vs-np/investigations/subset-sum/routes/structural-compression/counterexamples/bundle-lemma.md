# Bundle Lemma — Retraction Record

**Claim:** `SS-SC-001`  
**Mathematical status:** `RETRACTED`  
**Review maturity:** `CHECKED`  
**Recorded:** 2026-07-16

## Withdrawn claim

The exploratory route proposed that every Subset Sum instance could be partitioned into polynomially many bundles whose local density or separation would compose into a polynomial-size exact representation of the global reachable-sum state.

## Reason for withdrawal

The proposed composition step did not preserve enough exact information. In particular:

- a locally dense set may occupy only selected residue classes;
- interval summaries may include unreachable totals;
- choices in different bundles may have nonlocal compatibility constraints;
- a bundle that appears separated in isolation may not produce a forced decision in the combined instance.

These gaps invalidate the lemma as a foundation for a universal exact algorithm.

## Evidence status

The original exploratory session treated the lemma as disproved by counterexample, but the exact numerical instance and the final formal wording were not preserved.

Under the repository counterexample standard, this record therefore uses `RETRACTED` rather than `DISPROVED`. Promotion to `DISPROVED` requires a complete instance that verifies the hypotheses and directly falsifies the conclusion.

## Consequence

The dense-or-separated route is closed in its original form. Any replacement composition theorem must explicitly preserve residue coverage and cross-bundle compatibility, and must prove a polynomial bound in the binary input length.
