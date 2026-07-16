# Second-Pass Audit — P versus NP Top-Level Landscapes

**Mode:** VERIFY / RECORD  
**Date:** 2026-07-16  
**Verdict:** Landscapes expanded and corrected; no mathematical claim state changed

## Audit objective

Recheck the top-level research-programme and problem-testbed landscapes for:

- omitted major paradigms;
- incorrect complexity-class implications;
- conflation of uniform and nonuniform computation;
- conflation of decision, counting, promise, total-search, and quantum models;
- unsupported problem rankings;
- source mismatch;
- accidental activation of an investigation or promotion of literature to a repository proof.

## Material corrections

1. Added an explicit consequence map distinguishing:
   - \(P=NP\);
   - \(NP\not\subseteq P/\mathrm{poly}\);
   - \(NP\ne coNP\);
   - \(VP\ne VNP\);
   - conditional ETH or SETH consequences;
   - restricted-model lower bounds;
   - quantum containment statements.
2. Added or expanded major programmes:
   - hierarchy and diagonalization methods;
   - restricted formula and bounded-depth lower bounds;
   - algebraic and semialgebraic proof systems;
   - polyhedral extension complexity;
   - learning-to-lower-bounds;
   - PIT derandomization;
   - sparse complete sets;
   - advice and nonuniform complexity;
   - instance compression;
   - total-search complexity.
3. Added strategic objects and controls:
   - Unique-SAT as a promise problem;
   - QBF as a PSPACE boundary control;
   - factoring as an intermediate and quantum-model control;
   - TFNP, PPAD, and PLS as total-search classes;
   - sparse languages and compression as representation boundaries.
4. Marked all rankings as project strategy rankings rather than literature consensus.
5. Corrected incidence language so Positive 1-in-3 SAT, X3C, and 3-Dimensional Matching are treated as related orientations, not as automatically theorem-equivalent formulations.
6. Added explicit warnings about promise, totality, uniformity, counting, and conditional assumptions.

## Repository-integrity incident

A large replacement write temporarily truncated `research-programme-landscape.md`. The integrity pass detected the truncation before publication. The complete file was restored and re-fetched through its final status section.

## Final disposition

- No P-versus-NP claim was added or promoted.
- No investigation or route was activated.
- Subset Sum remains closed as a universal route family and retained as an adversarial arithmetic control.
- Positive 1-in-3 SAT remains the leading project candidate for a future positive testbed, subject to selection of a concrete mechanism.
- Circuit-SAT remains the leading lower-bound sibling, subject to an explicit restricted model and transfer theorem.

## Remaining limitation

The landscapes are complete at the level of major paradigms and natural obstruction families, not exhaustive bibliographies of every complete problem, circuit class, proof system, or parameterized restriction.