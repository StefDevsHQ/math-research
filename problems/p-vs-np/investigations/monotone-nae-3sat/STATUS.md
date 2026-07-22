# Status — Monotone NAE-3SAT Investigation

**Phase:** `VS-01` through `VS-04` complete; obstruction atlas next  
**Updated:** 2026-07-22

## Current position

The investigation is open. The canonical instance layer, exact small-instance oracle, exact extension-profile engine, and tractable-control calibration are `COMPLETE / CHECKED`. No universal polynomial-time mechanism is claimed.

Every vertical slice is governed by the mandatory [building-block quality gate](BUILDING-BLOCK-GATE.md). A dependent slice may begin only after each prerequisite is `COMPLETE / CHECKED` or stronger.

## Accepted baseline

1. Monotone NAE-3SAT is NP-complete — `ESTABLISHED / CHECKED`.
2. A deterministic polynomial-time algorithm for all instances would prove `P=NP` — `PROVED / CHECKED`.
3. Unary/binary fixed-template Boolean CSPs reduce to 2-SAT — `PROVED / CHECKED`.
4. Exact extension equivalence has well-defined one-variable transitions — `PROVED / CHECKED`.
5. Boundary width `w` gives a `2^{O(w)} poly(L)` exact algorithm — `PROVED / CHECKED`.
6. Bottom-up exact completion masks correctly construct the full semantic quotient for fixed instances and orderings — `PROVED / CHECKED`.
7. Every incidence-forest 3-uniform hypergraph is constructively two-colourable in linear incidence time — `PROVED / CHECKED`.

## Vertical-slice progress

- `VS-01` canonical instance model — `COMPLETE / CHECKED`.
- `VS-02` exact small-instance oracle — `COMPLETE / CHECKED`.
- `VS-03` exact extension-profile engine — `COMPLETE / CHECKED`.
- `VS-04` control calibration — `COMPLETE / CHECKED`.
- `VS-05` minimal obstruction atlas — `READY`.
- `VS-06` and `VS-07` — blocked on checked obstruction evidence.
- `VS-08` — blocked until failure structure supports one precise invariant.
- `VS-09` — `PARTIAL` through bounded-boundary and incidence-forest restricted theorems.
- `VS-10` through `VS-12` — blocked until an atomic invariant exists.

## Retained finite evidence

### VS-02

All `1045` labelled 3-uniform hypergraphs through five vertices are classified exactly. Exactly `1044` are satisfiable and one is unsatisfiable: the complete 3-uniform hypergraph on five vertices. The Fano plane is unsatisfiable and edge-minimal unsatisfiable.

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

The calibrated mechanisms are distinct: graph parity, affine row space, acyclic elimination, bounded interface, and disconnected product decomposition. Planar and occurrence-at-most-three tractability remain externally established broader boundaries.

## Current obstruction

The easy controls do not reveal one common universal compression rule. Their tractability comes from different exact structures. Unrestricted Monotone NAE-3SAT still requires a symbolic mechanism with globally polynomial construction, transitions, representation, and total generated state.

## Current open claim

`NAE-006` asks whether exact completion behaviour admits a universally polynomial symbolic representation with polynomial-time construction, transitions, equivalence, and acceptance. No representation language has yet survived formulation and attack.

## Immediate next tasks

1. Execute `VS-05`: construct the checked minimal obstruction atlas using VS-02 and VS-03.
2. Use the atlas in `VS-06` to destroy naive summaries.
3. Use `VS-07` to separate genuine live merging from symmetry, dead-state collapse, and bounded-interface effects.

## Stop conditions

Reject a proposed universal mechanism if it is only local or bounded-width, has superpolynomial construction or total state, merges unequal completion sets, succeeds only on a restricted subclass, relies on unsupported randomness, or avoids canonical hard families.
