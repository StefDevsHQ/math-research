# Status — Monotone NAE-3SAT Investigation

**Phase:** `VS-01` and `VS-02` complete; exact extension-profile engine ready  
**Updated:** 2026-07-22

## Current position

The investigation is open. The canonical instance layer and the exact small-instance oracle are both `COMPLETE / CHECKED`. No universal polynomial-time mechanism is claimed.

Every vertical slice is governed by the mandatory [building-block quality gate](BUILDING-BLOCK-GATE.md). A dependent slice may begin only after each prerequisite is `COMPLETE / CHECKED` or stronger.

## Accepted baseline

1. Monotone NAE-3SAT is NP-complete — `ESTABLISHED / CHECKED`.
2. A deterministic polynomial-time algorithm for all instances would prove `P=NP` — `PROVED / CHECKED`.
3. Unary/binary fixed-template Boolean CSPs reduce to 2-SAT — `PROVED / CHECKED`.
4. Exact extension equivalence has well-defined one-variable transitions — `PROVED / CHECKED`.
5. Boundary width `w` gives a `2^{O(w)} poly(L)` exact algorithm — `PROVED / CHECKED`.

## Vertical-slice progress

- `VS-01` canonical instance model — `COMPLETE / CHECKED`.
- `VS-02` exact small-instance oracle — `COMPLETE / CHECKED`.
- `VS-03` exact extension-profile engine — `READY` and unlocked.
- `VS-04` and `VS-05` — blocked on checked VS-03 profile outputs, though VS-02 ground truth is now available.
- `VS-06` through `VS-08` — blocked on checked obstruction and profile evidence.
- `VS-09` — `PARTIAL` through the existing bounded-boundary theorem only.
- `VS-10` through `VS-12` — blocked until an atomic invariant exists.

## VS-02 retained results

The exact oracle provides decision, least witness, complete solution listing, exact counting, component-factorized counting, edge-minimal-unsatisfiability testing, labelled generation, and deterministic census output.

The first exhaustive domain contains all `1045` labelled 3-uniform hypergraphs on at most five vertices. Exactly `1044` are satisfiable and one is unsatisfiable: the complete 3-uniform hypergraph on five vertices. The census evaluated `33047` complete colourings.

The Fano-plane control is unsatisfiable and edge-minimal unsatisfiable by committed exhaustive computation.

Evidence:

- [VS-02 implementation specification](VS-02-IMPLEMENTATION.md);
- [VS-02 completion audit](VS-02-AUDIT.md);
- deterministic corpus under `tools/monotone-nae-3sat/corpus/`;
- executable package and exhaustive tests under `tools/monotone-nae-3sat/`;
- Python 3.11, 3.12, and 3.13 automated gate.

These are finite exact results, not a universal algorithm.

## Current obstruction

Ordinary boundary-state dynamic programming becomes exponential when useful interfaces are large. Exact extension profiles define the correct semantic state, but the quotient may itself be large or expensive to represent and manipulate.

## Current open claim

`NAE-006` asks whether exact completion behaviour admits a universally polynomial symbolic representation with polynomial-time construction, transitions, equivalence, and acceptance. No representation language has yet been selected.

## Immediate next task

Execute `VS-03` as the next concrete building block:

1. implement exact completion sets for fixed instances and orderings;
2. quotient prefix assignments only by identical completion sets;
3. construct and verify both colour transitions;
4. compare final acceptance with checked VS-02 ground truth;
5. record raw, boundary, quotient, and encoded-profile sizes;
6. pass the full building-block quality gate before downstream use.

## Stop conditions

Reject a proposed universal mechanism if it is only local or bounded-width, has superpolynomial construction or total state, merges unequal completion sets, succeeds only on a restricted subclass, relies on unsupported randomness, or avoids canonical hard families.
