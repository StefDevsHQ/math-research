# Status — Monotone NAE-3SAT Investigation

**Phase:** `VS-01` complete; exact small-instance oracle ready to implement  
**Updated:** 2026-07-22

## Current position

The investigation is open. The mathematical object, encoding discipline, source map, baseline theorems, attack plan, vertical-slice order, and canonical executable instance layer are prepared. No universal polynomial-time mechanism is claimed.

## Accepted baseline

1. Monotone NAE-3SAT is NP-complete — `ESTABLISHED / CHECKED`.
2. A deterministic polynomial-time algorithm for all instances would prove `P=NP` — `PROVED / CHECKED`.
3. Unary/binary fixed-template Boolean CSPs reduce to 2-SAT — `PROVED / CHECKED`.
4. Exact extension equivalence has well-defined one-variable transitions — `PROVED / CHECKED`.
5. Boundary width `w` gives a `2^{O(w)} poly(L)` exact algorithm — `PROVED / CHECKED`.

## Vertical-slice progress

The authoritative tracker is [VERTICAL-SLICES.md](VERTICAL-SLICES.md).

- `VS-01` canonical instance model — `COMPLETE`.
- `VS-02` exact small-instance oracle — `READY`.
- `VS-03` exact extension-profile engine — `READY`.
- `VS-04` through `VS-08` — blocked on oracle/profile evidence.
- `VS-09` — `PARTIAL` through the existing bounded-boundary theorem only.
- `VS-10` through `VS-12` — blocked until an atomic invariant exists.

`VS-01` evidence:

- [implementation specification](VS-01-IMPLEMENTATION.md);
- [completion audit](VS-01-AUDIT.md);
- executable package under `tools/monotone-nae-3sat/`.

## Current obstruction

Ordinary boundary-state dynamic programming becomes exponential when useful interfaces are large. Exact extension profiles define the correct semantic state, but the quotient may itself be large or expensive to represent and manipulate.

## Current open claim

`NAE-006` asks whether exact completion behaviour admits a universally polynomial symbolic representation with polynomial-time construction, transitions, equivalence, and acceptance. No representation language has yet been selected.

## Immediate next task

Execute `VS-02`:

1. implement exhaustive binary-colouring search over the canonical model;
2. use component and complement symmetry only with proved correctness;
3. return and independently verify witnesses;
4. generate the first explicitly declared labelled instance domain;
5. record the exhaustiveness argument, commands, counts, environment, and limitations.

Only then use the oracle to calibrate controls and enumerate minimal obstructions.

## Stop conditions

Reject a proposed universal mechanism if it is only local or bounded-width, has superpolynomial construction or total state, merges unequal completion sets, succeeds only on a restricted subclass, relies on unsupported randomness, or avoids canonical hard families.
