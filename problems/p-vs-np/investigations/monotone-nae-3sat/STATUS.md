# Status — Monotone NAE-3SAT Investigation

**Phase:** Phase I (`VS-01` through `VS-05`) complete; `VS-06` formalization next  
**Updated:** 2026-07-22

## Current position

The investigation remains open. The trusted laboratory phase consisting of the canonical instance layer, exact small-instance oracle, exact extension-profile engine, tractable-control calibration, and minimal-obstruction atlas is `COMPLETE / CHECKED`. No universal polynomial-time mechanism is claimed.

The phase closeout is recorded in [VS-01-05-PHASE-AUDIT.md](VS-01-05-PHASE-AUDIT.md). `VS-06` may begin only from the exported contracts and limitations recorded there.

## Accepted baseline

1. Monotone NAE-3SAT is NP-complete — `ESTABLISHED / CHECKED`.
2. A deterministic polynomial-time algorithm for all instances would prove `P=NP` — `PROVED / CHECKED`.
3. Unary/binary fixed-template Boolean CSPs reduce to 2-SAT — `PROVED / CHECKED`.
4. Exact extension equivalence has well-defined one-variable transitions — `PROVED / CHECKED`.
5. Boundary width `w` gives a `2^{O(w)} poly(L)` exact algorithm — `PROVED / CHECKED`.
6. Bottom-up exact completion masks correctly construct the full semantic quotient for fixed instances and orderings — `PROVED / CHECKED`.
7. Every incidence-forest 3-uniform hypergraph is constructively two-colourable in linear incidence time — `PROVED / CHECKED`.
8. Single edge or vertex deletion checks suffice for the corresponding proper-subinstance minimality notions — `PROVED / CHECKED`.
9. Every unsatisfiable instance collapses the successful-completion quotient to one dead class at every level under every ordering — `PROVED / CHECKED`.

## Vertical-slice progress

- `VS-01` canonical instance model — `COMPLETE / CHECKED`.
- `VS-02` exact small-instance oracle — `COMPLETE / CHECKED`.
- `VS-03` exact extension-profile engine — `COMPLETE / CHECKED`.
- `VS-04` control calibration — `COMPLETE / CHECKED`.
- `VS-05` minimal obstruction atlas — `COMPLETE / CHECKED`.
- `VS-06` naive-summary destruction — `READY FOR FORMALIZATION`.
- `VS-07` — blocked on checked VS-06 failure evidence.
- `VS-08` — blocked until failure structure supports one precise invariant.
- `VS-09` — `PARTIAL` through bounded-boundary and incidence-forest restricted theorems.
- `VS-10` through `VS-12` — blocked until an atomic invariant exists.

## Retained finite evidence

### VS-02

All `1045` labelled 3-uniform hypergraphs through five vertices are classified exactly. Exactly `1044` are satisfiable and one is unsatisfiable: `K_5^(3)`. The Fano plane is independently verified unsatisfiable and edge-minimal unsatisfiable.

### VS-03

All `123280` instance-ordering profiles through five vertices are measured exactly:

- `7753542` raw prefixes;
- `2153049` exact semantic classes;
- `1818651` live exact classes;
- `2865585` processed-valid boundary states;
- maximum exact quotient size `8`.

### VS-04

Control calibration exhaustively checked:

- `1100` labelled graphs through five vertices: `428` bipartite and `672` non-bipartite;
- `16453` canonical XOR systems through three variables: `890` consistent and `15563` inconsistent;
- `36` incidence-forest NAE instances through five vertices, all constructively colourable;
- `344` maximum-occurrence-at-most-three NAE instances in the same finite domain, all satisfiable.

### VS-05

The complete `n<=5` obstruction census contains exactly one unsatisfiable object, `K_5^(3)`, and it is both edge-minimal and vertex-minimal. Complete least-witness certificates are stored for every edge and vertex deletion of `K_5^(3)` and the Fano plane.

All `120` orderings of `K_5^(3)` and all `5040` orderings of the Fano plane were profiled. Both have exactly one successful-completion class at every level because every prefix has the empty set of satisfying full completions.

## Current obstruction

The easy controls do not reveal one common universal compression rule. Successful-completion semantics becomes completely uninformative inside globally unsatisfiable instances. Dense `K_5^(3)` and sparse linear Fano collapse to the same one-dead-class pattern at every level despite radically different structure.

A useful next representation must therefore preserve failure information, residual constraints, or another exact observable beyond successful full completions.

## Current open claim

`NAE-006` asks whether exact completion behaviour admits a universally polynomial symbolic representation with polynomial-time construction, transitions, equivalence, and acceptance. No representation language has yet survived formulation and attack. `NAE-011` shows only that accepting-completion equivalence is too coarse to explain rejection structure; it is not a general compression lower bound.

## Immediate next tasks

1. Formalize `VS-06` summaries, semantic targets, collision criteria, and finite search domains.
2. Attack degree, incidence, pair-codegree, parity, bounded-radius, local-consistency, spectral, boundary-only, and low-moment summaries.
3. Use `VS-07` to separate genuine live merging from symmetry, dead-state collapse, bounded-interface effects, and globally dead instances.

## Stop conditions

Reject a proposed universal mechanism if it is only local or bounded-width, has superpolynomial construction or total state, merges unequal exact semantics, succeeds only on a restricted subclass, relies on unsupported randomness, ignores globally dead-state collapse, or avoids canonical hard families.
