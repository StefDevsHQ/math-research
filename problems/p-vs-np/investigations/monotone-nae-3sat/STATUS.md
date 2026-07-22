# Status — Monotone NAE-3SAT Investigation

**Phase:** `VS-06` complete; `VS-07` ready  
**Updated:** 2026-07-22

## Current position

The investigation remains open. `VS-01` through `VS-06` are `COMPLETE / CHECKED`. No universal polynomial-time mechanism is claimed.

The trusted laboratory provides canonical instances, exact finite semantics, exact fixed-order completion profiles, calibrated tractable controls, a minimal-obstruction atlas, and a checked atlas of failures for explicitly defined naive summaries.

## Accepted baseline

1. Monotone NAE-3SAT is NP-complete — `ESTABLISHED / CHECKED`.
2. A deterministic polynomial-time algorithm for all instances would prove `P=NP` — `PROVED / CHECKED`.
3. Exact extension equivalence has well-defined transitions — `PROVED / CHECKED`.
4. Boundary width `w` gives a `2^{O(w)} poly(L)` exact algorithm — `PROVED / CHECKED`.
5. Exact completion masks correctly construct fixed-order semantic profiles — `PROVED / CHECKED`.
6. Incidence-forest instances are constructively two-colourable in linear incidence time — `PROVED / CHECKED`.
7. Every globally unsatisfiable instance collapses successful-completion semantics to one dead class at every level — `PROVED / CHECKED`.
8. For every fixed radius, equal rooted-radius neighbourhood multisets can coexist with opposite conditioned residual satisfiability — `PROVED / CHECKED`.
9. Ten explicit naive summaries have checked same-summary/different-semantics collisions — `COMPUTATIONAL / CHECKED`.

## Vertical-slice progress

- `VS-01` canonical instance model — `COMPLETE / CHECKED`.
- `VS-02` exact small-instance oracle — `COMPLETE / CHECKED`.
- `VS-03` exact extension-profile engine — `COMPLETE / CHECKED`.
- `VS-04` control calibration — `COMPLETE / CHECKED`.
- `VS-05` minimal obstruction atlas — `COMPLETE / CHECKED`.
- `VS-06` naive-summary destruction — `COMPLETE / CHECKED`.
- `VS-07` semantic-merging measurement — `READY`.
- `VS-08` — blocked until VS-07 isolates a candidate invariant.
- `VS-09` — `PARTIAL` through bounded-boundary and incidence-forest theorems.
- `VS-10` through `VS-12` — blocked until an atomic invariant exists.

## VS-06 retained results

The committed collision atlas separates whole-instance satisfiability from prefix completion semantics.

Disproved summaries:

- degree sequence;
- edge-intersection multiset;
- pair-codegree multiset;
- parity data;
- second moments;
- incidence-Gram spectrum;
- root generalized arc consistency;
- satisfiability of all proper induced subinstances;
- boundary Hamming weight;
- boundary Hamming parity.

The exact boundary assignment remains a complete control but can expose `2^w` states. The fixed-radius family rules out every constant locality radius, not radii growing with input size.

## Current obstruction

Easy global statistics, fixed local views, weak local consistency, and coarse boundary aggregates can preserve unresolved logical compatibility. Their failure does not lower-bound richer representations.

`NAE-006` remains open because no concrete symbolic language with polynomial construction, transition, equivalence, acceptance, and total generated size has yet been selected and survived attack.

## Immediate next task

Run `VS-07` to measure genuine live semantic merging separately from:

- dead-state collapse;
- componentwise complement symmetry;
- exact boundary-state count;
- quotient-state count;
- representation byte size;
- ordering effects.

The slice must end with reproducible first merges, first substantial growth families, and an exact distinction between semantic compression and compact symbolic representation.
