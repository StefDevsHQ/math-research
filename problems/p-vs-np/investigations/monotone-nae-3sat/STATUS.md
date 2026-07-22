# Status — Monotone NAE-3SAT Investigation

**Phase:** `VS-01`, `VS-02`, and `VS-03` complete; controls and obstruction atlas ready  
**Updated:** 2026-07-22

## Current position

The investigation is open. The canonical instance layer, exact small-instance oracle, and exact extension-profile engine are `COMPLETE / CHECKED`. No universal polynomial-time mechanism is claimed.

Every vertical slice is governed by the mandatory [building-block quality gate](BUILDING-BLOCK-GATE.md). A dependent slice may begin only after each prerequisite is `COMPLETE / CHECKED` or stronger.

## Accepted baseline

1. Monotone NAE-3SAT is NP-complete — `ESTABLISHED / CHECKED`.
2. A deterministic polynomial-time algorithm for all instances would prove `P=NP` — `PROVED / CHECKED`.
3. Unary/binary fixed-template Boolean CSPs reduce to 2-SAT — `PROVED / CHECKED`.
4. Exact extension equivalence has well-defined one-variable transitions — `PROVED / CHECKED`.
5. Boundary width `w` gives a `2^{O(w)} poly(L)` exact algorithm — `PROVED / CHECKED`.
6. Bottom-up exact completion masks correctly construct the full semantic quotient for fixed instances and orderings — `PROVED / CHECKED`.

## Vertical-slice progress

- `VS-01` canonical instance model — `COMPLETE / CHECKED`.
- `VS-02` exact small-instance oracle — `COMPLETE / CHECKED`.
- `VS-03` exact extension-profile engine — `COMPLETE / CHECKED`.
- `VS-04` control calibration — `READY`.
- `VS-05` minimal obstruction atlas — `READY`.
- `VS-06` and `VS-07` — blocked on checked control and obstruction evidence.
- `VS-08` — blocked until failure structure supports one precise invariant.
- `VS-09` — `PARTIAL` through the existing bounded-boundary theorem only.
- `VS-10` through `VS-12` — blocked until an atomic invariant exists.

## VS-02 retained results

The first exhaustive domain contains all `1045` labelled 3-uniform hypergraphs on at most five vertices. Exactly `1044` are satisfiable and one is unsatisfiable: the complete 3-uniform hypergraph on five vertices. The Fano-plane control is unsatisfiable and edge-minimal unsatisfiable.

## VS-03 retained results

The first profile domain contains every ordering of every labelled instance through five vertices:

\[
123280
\]

instance-ordering profiles.

The exact census records:

- `7753542` raw prefixes;
- `2153049` exact semantic classes;
- `1818651` live exact classes;
- `2865585` processed-valid boundary states;
- maximum exact quotient size `8`;
- `120` unsatisfiable-root profiles, the orderings of the unique unsatisfiable five-vertex instance.

A pinned constrained live merge occurs for one edge under ordering `(0,1,2)`: prefixes `01` and `10` have the same nonzero completion set.

Evidence:

- [VS-03 implementation specification](VS-03-IMPLEMENTATION.md);
- [VS-03 proof and completion audit](VS-03-AUDIT.md);
- deterministic profile corpus under `tools/monotone-nae-3sat/profile-corpus/`;
- executable profile engine and independent tests;
- Python 3.11, 3.12, and 3.13 automated production gate;
- complete independent `123280`-profile reference census on the pinned runtime.

These are finite exact measurements. They do not establish a polynomial asymptotic quotient bound.

## Current obstruction

Exact future equivalence is now executable and measurable. The remaining issue is not semantic definition but asymptotic structure: exact quotients may grow, and even small quotients may be expensive to construct or encode. A universal route requires a new symbolic mechanism with globally polynomial construction, transitions, representation, and total state.

## Current open claim

`NAE-006` asks whether exact completion behaviour admits a universally polynomial symbolic representation with polynomial-time construction, transitions, equivalence, and acceptance. No representation language has yet been selected.

## Immediate next tasks

1. Execute `VS-04`: calibrate exact profiles on known easy controls and identify the actual tractability mechanism.
2. Execute `VS-05`: construct the checked minimal obstruction atlas using VS-02 and VS-03.
3. Only after those foundations, use `VS-06` and `VS-07` to attack summaries and measure nontrivial semantic merging.

## Stop conditions

Reject a proposed universal mechanism if it is only local or bounded-width, has superpolynomial construction or total state, merges unequal completion sets, succeeds only on a restricted subclass, relies on unsupported randomness, or avoids canonical hard families.
