# Status — R1 Exact-State Representations

**Route:** `R1`  
**Status:** `ACTIVE, WITH ORDERED STATE ENUMERATION CLOSED`  
**Updated:** 2026-07-23

## Current position

The route remains open, but its first universal state-enumeration subroute is closed.

Central lifts of constant-degree expanders force `2^{Omega(n)}` pairwise distinct live exact completion functions under every variable ordering. Since exact PCRNF states cannot identify distinct completion functions, every ordering has exponentially many PCRNF states.

## Accepted results

- `NAE-004 — PROVED / CHECKED`: exact extension equivalence is transition-compatible.
- `NAE-017 — PROVED / CHECKED`: oriented PCRNF exactly represents labelled residual semantics and transitions.
- `NAE-018 — DISPROVED / CHECKED`: PCRNF byte equality is not exact semantic equivalence.
- `NAE-019 — PROVED / CHECKED`: PCRNF state count dominates exact residual-function count.
- `NAE-020 — PROVED / CHECKED`: central lifts of bounded-degree expanders have exponentially many exact residual functions under every ordering.
- `NAE-016 — DISPROVED / CHECKED`: no variable ordering gives a universal polynomial PCRNF state graph.

## Closed subroute

`R1.1 — PCRNF` is closed as a universal ordered state-enumeration route. Its exact machinery and restricted-class programme are retained.

## Effect on semantic quotients

A quotient that merely merges semantically equal residuals cannot restore polynomial state on the `NAE-020` family, because the residual functions are already pairwise semantically distinct.

Therefore `R1.2` must be narrowed or replaced by a materially different collective representation that can share structure across many distinct functions without enumerating each function as one traversal state.

## Surviving candidates

- `R1.4 — Decomposable circuits` or another collective circuit representation;
- non-ordered decompositions;
- algebraic global representations;
- restricted PCRNF classes.

Decision diagrams that obey a single global variable order inherit the same residual-subfunction obstruction on the central-lift family.

## Route boundary

This lower bound is representation-specific. It does not disprove `NAE-006`, arbitrary circuits, arbitrary algorithms, `P=NP`, or prove `P!=NP`.