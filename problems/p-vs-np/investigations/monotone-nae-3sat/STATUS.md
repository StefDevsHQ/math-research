# Status — Monotone NAE-3SAT Investigation

**Phase:** `VS-07` reviewed; `VS-08` prepared  
**Updated:** 2026-07-22

## Current position

`VS-01` through `VS-07` are `COMPLETE / CHECKED`. The post-merge VS-07 review preserves `NAE-014` and `NAE-015`, sharpens the good-fan live bound to four in executable assertions, adds explicit unsatisfiable controls, and removes repeated exact-profile reconstruction.

No universal polynomial-time mechanism or general representation lower bound is claimed.

## Accepted baseline

1. Monotone NAE-3SAT is NP-complete — `ESTABLISHED / CHECKED`.
2. A deterministic polynomial-time algorithm for all instances would prove `P=NP` — `PROVED / CHECKED`.
3. Exact extension equivalence has well-defined transitions — `PROVED / CHECKED`.
4. Boundary width `w` gives a `2^{O(w)} poly(L)` exact algorithm — `PROVED / CHECKED`.
5. Incidence-forest instances are constructively two-colourable in linear incidence time — `PROVED / CHECKED`.
6. Every globally unsatisfiable instance collapses successful-completion semantics to one dead class at every level — `PROVED / CHECKED`.
7. Fixed-radius local views can miss conditioned residual satisfiability — `PROVED / CHECKED`.
8. Ten explicit naive summaries have checked collisions — `COMPUTATIONAL / CHECKED`.
9. The fan family has exponential live exact-state growth under one order and constant-width behaviour under an interleaved order — `PROVED / CHECKED`.
10. Genuine all-live merging beyond component-complement prefix orbits occurs through four vertices — `COMPUTATIONAL / CHECKED`.

## Vertical-slice progress

- `VS-01` through `VS-07` — `COMPLETE / CHECKED`.
- `VS-08` propagation-closed signed residual normal form — `PREPARED`.
- `VS-09` — `PARTIAL` through bounded-boundary and incidence-forest theorems.
- `VS-10` through `VS-12` — blocked until `NAE-016` survives VS-08.

## VS-07 review findings

- The mathematical claims survive.
- The version-one record stores the conservative value five in a field named as a live bound; the sharp live bound is four and five is only the possible total-class bound including one dead class.
- Version-one record bytes are preserved for reproducibility; core assertions and tests enforce four.
- `K_5^(3)` and Fano now explicitly test pure dead-state collapse.
- Profile measurement now reuses one exact profile across all levels.
- Per-level byte counters are raw payload measures, not complete self-delimiting encodings.

Evidence: [VS-07 post-merge review](VS-07-REVIEW.md).

## Prepared VS-08 candidate

`NAE-016 — CONJECTURE / DRAFT` proposes memoized traversal by **propagation-closed signed residual normal forms**.

The representation contains:

- contradiction;
- labelled unprocessed vertices;
- unary colour requirements;
- signed binary constraints forbidding both endpoints from one colour;
- remaining ternary NAE constraints;
- deterministic propagation closure;
- residual-component normalization under simultaneous colour complement.

The universal claim is not that one residual is small. It is that some polynomial-time constructible ordering yields polynomially many reachable normalized residuals of polynomial maximum and total encoded size, with polynomial-time exact transitions, equality, and acceptance.

Evidence: [VS-08 preparation](VS-08-PREPARATION.md).

## Immediate next task

Execute `VS-08A`: implement and prove the exact labelled residual object and direct edge residualization. Do not assume the polynomial global state bound. Attack correctness and canonicality before measuring compression.
