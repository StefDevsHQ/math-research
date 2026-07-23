# Status — P versus NP

**Phase:** Monotone NAE-3SAT exact-representation closeout complete; top-level route selection  
**Updated:** 2026-07-23

## Current position

The Monotone NAE-3SAT investigation has completed two universal exact-representation barriers on one central-lift expander family.

- `NAE-020` forces exponentially many distinct live residual completion functions under every variable ordering.
- `NAE-021` proves exponential size for every DNNF representing the exact satisfying-assignment function.

No universal polynomial-time algorithm or general circuit lower bound is claimed.

The Subset Sum investigation remains closed after its universal structural-compression and broad exact-state-barrier strategies failed within their stated models.

## Accepted determination

- `NAE-016 — DISPROVED / CHECKED`.
- `NAE-017 — PROVED / CHECKED`.
- `NAE-018 — DISPROVED / CHECKED`.
- `NAE-019 — PROVED / CHECKED`.
- `NAE-020 — PROVED / CHECKED`.
- `NAE-021 — PROVED / CHECKED`.
- `NAE-006 — CONJECTURE / DRAFT` remains unresolved but dormant pending a materially new exact representation model.

## Route determination

Within `R1 — Exact-state representations`:

- ordered PCRNF state enumeration is closed universally;
- one-state-per-residual-function semantic quotients are blocked;
- reduced ordered decision diagrams inherit the residual-function obstruction;
- DNNF and all of its subclasses are exponentially large on the central-lift expander family;
- restricted PCRNF and bounded-width compilation results remain valid.

Generic collective representation is not an active route. It may be reopened only with a fixed representation language, exact operations, polynomial total-size target, and a mechanism not subsumed by the current lower bounds.

## Scope boundary

The retained barriers do not lower-bound:

- unrestricted Boolean circuits;
- arbitrary non-DNNF data structures;
- algebraic global methods;
- arbitrary polynomial-time algorithms.

They therefore prove neither `P=NP` nor `P!=NP`.

## Retained project results

- Subset Sum residue-completion lemma and restricted exact-decomposition theorem;
- Monotone NAE-3SAT exact quotient and bounded-boundary theorems;
- incidence-forest constructive colouring;
- obstruction, locality-failure, summary-collision and semantic-merging evidence;
- exact oriented PCRNF residualization;
- all-ordering expander lower bound for ordered residual-state enumeration;
- exponential DNNF lower bound for central-lift expanders.

## Next decision

Return to top-level route selection. Keep restricted PCRNF and decomposition classification as a secondary theorem programme, but do not activate another universal exact-representation subroute without a materially new model and a precise survival argument.

Evidence:

- [NAE-016 expander disproof](investigations/monotone-nae-3sat/routes/exact-state-representations/pcrnf/proofs/NAE-016-expander-disproof.md)
- [NAE-021 DNNF lower bound](investigations/monotone-nae-3sat/routes/exact-state-representations/decomposable-circuits/proofs/NAE-021-dnnf-expander-lower-bound.md)