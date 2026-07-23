# Status — Monotone NAE-3SAT Investigation

**Phase:** exact-representation barrier package complete; universal route selection closed  
**Updated:** 2026-07-23

## Current position

`VS-01` through `VS-09A` remain `COMPLETE / CHECKED`. The DNNF barrier continuation is also complete.

The central-lift expander family now supplies two complementary lower bounds:

- `NAE-020`: every variable ordering exposes `2^{Omega(n)}` distinct live residual completion functions;
- `NAE-021`: every DNNF for the exact satisfying-assignment function has size `2^{Omega(n)}`.

The universal ordered PCRNF and decomposable-circuit routes are closed. The broader Monotone NAE-3SAT problem remains open.

## Accepted results

- `NAE-016 — DISPROVED / CHECKED`.
- `NAE-017 — PROVED / CHECKED`.
- `NAE-018 — DISPROVED / CHECKED`.
- `NAE-019 — PROVED / CHECKED`.
- `NAE-020 — PROVED / CHECKED`.
- `NAE-021 — PROVED / CHECKED`.
- `NAE-006 — CONJECTURE / DRAFT` remains unresolved and dormant.

## Route position

- `R1.1 — PCRNF`: closed universally; exact and restricted results retained.
- `R1.2 — Collective representation`: dormant; no fixed surviving model.
- `R1.3 — Decision diagrams`: reduced ordered variants blocked.
- `R1.4 — Decomposable circuits`: closed universally by `NAE-021`; restricted bounded-width compilation retained.
- `R2`: restricted decomposition and ordering results remain valid as a secondary theorem programme.
- `R6`: retains the ordered-state and DNNF model-specific barriers.

## Exact determination

```text
PCRNF exactness                                  RETAINED
PCRNF byte equality as semantic equality         DISPROVED
polynomial PCRNF state under some ordering        DISPROVED
ordered state per residual function               BLOCKED
polynomial DNNF exact representation              DISPROVED
unrestricted exact symbolic representation        OPEN / DORMANT
restricted PCRNF and decomposition classes        OPEN
```

## Scope boundary

The lower bounds do not prove `P!=NP`, do not disprove `NAE-006`, and do not lower-bound unrestricted Boolean circuits, algebraic methods, arbitrary non-DNNF structures, or arbitrary algorithms.

## Next decision

Close the universal exact-representation programme at this point. Preserve restricted-class work separately. Reopen only for a precisely defined representation model with an explicit reason it escapes both `NAE-020` and `NAE-021`.

Evidence:

- [NAE-016 expander disproof](routes/exact-state-representations/pcrnf/proofs/NAE-016-expander-disproof.md)
- [NAE-021 DNNF lower bound](routes/exact-state-representations/decomposable-circuits/proofs/NAE-021-dnnf-expander-lower-bound.md)