# Status — Monotone NAE-3SAT Investigation

**Phase:** `VS-07` complete; `VS-08` ready  
**Updated:** 2026-07-22

## Current position

The investigation remains open. `VS-01` through `VS-07` are `COMPLETE / CHECKED`. No universal polynomial-time mechanism or general representation lower bound is claimed.

The trusted laboratory now provides canonical instances, exact finite semantics, exact fixed-order completion profiles, tractable controls, obstruction and collision atlases, and a deterministic live semantic-merging census separated from dead collapse and complement symmetry.

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
10. The fan family has exponential live exact-state growth under one order and constant-width behaviour under an interleaved order — `PROVED / CHECKED`.
11. Genuine all-live exact merging beyond component-complement prefix orbits occurs in the complete labelled domain through four vertices — `COMPUTATIONAL / CHECKED`.

## Vertical-slice progress

- `VS-01` canonical instance model — `COMPLETE / CHECKED`.
- `VS-02` exact small-instance oracle — `COMPLETE / CHECKED`.
- `VS-03` exact extension-profile engine — `COMPLETE / CHECKED`.
- `VS-04` control calibration — `COMPLETE / CHECKED`.
- `VS-05` minimal obstruction atlas — `COMPLETE / CHECKED`.
- `VS-06` naive-summary destruction — `COMPLETE / CHECKED`.
- `VS-07` semantic-merging measurement — `COMPLETE / CHECKED`.
- `VS-08` atomic invariant extraction — `READY`.
- `VS-09` — `PARTIAL` through bounded-boundary and incidence-forest theorems.
- `VS-10` through `VS-12` — blocked until a VS-08 representation survives attack.

## VS-07 retained results

The measurement framework separately records:

- raw, live, and dead prefixes;
- exact live and dead semantic classes;
- component-complement prefix and semantic orbits;
- genuine exact merging across prefix-orbit boundaries;
- processed-valid and live boundary states;
- dense-mask, assignment-map, boundary, and profile byte sizes;
- ordering dependence.

The first all-live genuine merge occurs on the four-vertex instance with edges `{012,013}`, ordering `(0,2,3,1)`, and level three.

For the fan family `F_k`:

- the bad order has `2^(k+1)-1` live exact classes at level `k+1`;
- the reduction from raw prefixes is essentially only global complement symmetry;
- an interleaved order has boundary width at most two and at most four live exact classes.

Thus large fixed-order exact quotients are real, but one bad ordering is not an intrinsic obstruction.

## Current obstruction

`NAE-006` remains open because no concrete symbolic language has yet supplied all of:

- exact semantics;
- polynomial-time construction and canonical equality;
- exact restriction, transition, and merge;
- polynomial-time acceptance;
- a polynomial global bound on all generated representations.

VS-07 shows both sides of the problem: exact semantics can merge boundary assignments nontrivially, yet exact live quotients can also grow exponentially. Neither fact determines whether a richer symbolic representation remains polynomial.

## Immediate next task

Execute `VS-08` by defining one atomic representation language for the genuine merging observed in VS-07. The first candidate should normalize residual constraints under component complement and specify exact construction, transition, equality, acceptance, encoded size, hard controls, and a stop condition before implementation begins.
