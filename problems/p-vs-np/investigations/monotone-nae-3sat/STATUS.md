# Status — Monotone NAE-3SAT Investigation

**Phase:** `VS-01 COMPLETE / CHECKED`; `VS-02` unlocked  
**Updated:** 2026-07-22

## Current position

The investigation is open. The mathematical object, encoding discipline, source map, baseline theorems, attack plan, vertical-slice order, and canonical executable instance layer are prepared. No universal polynomial-time mechanism is claimed.

Every vertical slice is now governed by the mandatory [building-block quality gate](BUILDING-BLOCK-GATE.md). A dependent slice may begin only after each prerequisite is `COMPLETE / CHECKED` or stronger.

## Accepted baseline

1. Monotone NAE-3SAT is NP-complete — `ESTABLISHED / CHECKED`.
2. A deterministic polynomial-time algorithm for all instances would prove `P=NP` — `PROVED / CHECKED`.
3. Unary/binary fixed-template Boolean CSPs reduce to 2-SAT — `PROVED / CHECKED`.
4. Exact extension equivalence has well-defined one-variable transitions — `PROVED / CHECKED`.
5. Boundary width `w` gives a `2^{O(w)} poly(L)` exact algorithm — `PROVED / CHECKED`.

## Vertical-slice progress

The authoritative tracker is [VERTICAL-SLICES.md](VERTICAL-SLICES.md).

- `VS-01` canonical instance model — `COMPLETE / CHECKED`.
- `VS-02` exact small-instance oracle — `READY` and unlocked.
- `VS-03` exact extension-profile engine — formally ready, but may not consume VS-02 outputs until VS-02 passes its own quality gate.
- `VS-04` through `VS-08` — blocked on checked oracle/profile evidence.
- `VS-09` — `PARTIAL` through the existing bounded-boundary theorem only.
- `VS-10` through `VS-12` — blocked until an atomic invariant exists.

`VS-01` evidence:

- [implementation specification](VS-01-IMPLEMENTATION.md);
- [completion and quality audit](VS-01-AUDIT.md);
- [building-block gate](BUILDING-BLOCK-GATE.md);
- executable package under `tools/monotone-nae-3sat/`;
- automated Python 3.11, 3.12, and 3.13 workflow.

The gate includes all 1,045 labelled 3-uniform hypergraphs on at most five vertices, 33,047 colouring checks, 33,047 induced-subinstance checks, a separate 1,350-instance seeded reference cross-check, malformed-input tests, cross-process determinism, and CLI verification.

## Current obstruction

Ordinary boundary-state dynamic programming becomes exponential when useful interfaces are large. Exact extension profiles define the correct semantic state, but the quotient may itself be large or expensive to represent and manipulate.

## Current open claim

`NAE-006` asks whether exact completion behaviour admits a universally polynomial symbolic representation with polynomial-time construction, transitions, equivalence, and acceptance. No representation language has yet been selected.

## Immediate next task

Execute `VS-02` as a concrete building block:

1. specify the exact oracle contract and exported guarantees;
2. implement exhaustive binary-colouring search over the canonical model;
3. prove any component or complement-symmetry optimization before use;
4. return and independently verify witnesses;
5. declare and exhaust the first labelled instance domain;
6. add independent reference and adversarial tests;
7. audit encoding, runtime, complete search size, and memory;
8. require the cross-version automated gate before promotion.

Only after `VS-02` is `COMPLETE / CHECKED` may its outputs support VS-03, control calibration, or obstruction claims.

## Stop conditions

Reject a proposed universal mechanism if it is only local or bounded-width, has superpolynomial construction or total state, merges unequal completion sets, succeeds only on a restricted subclass, relies on unsupported randomness, or avoids canonical hard families.
