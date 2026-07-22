# Status — Monotone NAE-3SAT Investigation

**Phase:** Vertical-slice execution prepared; executable laboratory not yet complete  
**Updated:** 2026-07-22

## Current position

The investigation is open. The object, encoding, primary sources, baseline theorems, mandatory controls, complete attack plan, and ordered vertical slices are prepared. No universal polynomial-time mechanism is claimed.

The selected object is Monotone NAE-3SAT, equivalently 2-colourability of a 3-uniform hypergraph. It is the symmetry-first counterpart to Positive 1-in-3 SAT.

## Accepted baseline

1. Monotone NAE-3SAT is NP-complete — `ESTABLISHED / CHECKED`.
2. A deterministic polynomial-time algorithm for all instances would prove `P=NP` — `PROVED / CHECKED`.
3. Unary/binary fixed-template Boolean CSPs reduce to 2-SAT — `PROVED / CHECKED`.
4. Exact extension equivalence has well-defined one-variable transitions — `PROVED / CHECKED`.
5. Boundary width `w` gives a `2^{O(w)} poly(L)` exact algorithm — `PROVED / CHECKED`.

These results establish the baseline, not a resolution.

## Vertical-slice progress

The authoritative operational tracker is [VERTICAL-SLICES.md](VERTICAL-SLICES.md).

Current state:

- `VS-01` canonical instance model — `PARTIAL`: mathematical specification complete; executable parser, normalizer, serializer, and verifier remain.
- `VS-02` exact small-instance oracle — `READY`.
- `VS-03` exact extension-profile engine — `READY`: semantics and transition theorem are proved; implementation remains.
- `VS-04` through `VS-08` — `BLOCKED` on the oracle and profile engine.
- `VS-09` restricted theorem — `PARTIAL`: the standard bounded-boundary theorem is complete, but no new invariant exists.
- `VS-10` through `VS-12` — `BLOCKED` until an atomic invariant is extracted.

No computational corpus, minimal-obstruction atlas, naive-summary collision, or semantic-growth dataset is yet recorded.

## Known structural boundaries

The programme must correctly separate:

- rank-two bipartiteness;
- planar NAE-3SAT;
- occurrence-at-most-three NAE;
- bounded-width instances;
- unrestricted NP-complete instances;
- linear 4-regular NP-complete instances.

## Current mathematical obstruction

Each constraint forbids only two of eight local assignments. Local feasibility is abundant, while incompatibility can remain distributed across overlapping hyperedges.

Ordinary dynamic programming stores boundary colourings and becomes exponential when all useful interfaces are large. Exact extension profiles define the correct semantic state, but the raw quotient may be large and deciding or manipulating a compact description may itself hide NP-hard work.

## Current open claim

`NAE-006` asks whether exact completion behaviour has a universally polynomial symbolic representation with polynomial-time construction, transitions, equivalence, and acceptance.

This is not yet a route-level conjecture because no representation language has been selected.

## Immediate next task

Execute the first three vertical slices:

1. finish the canonical executable instance model;
2. build and validate the exhaustive small-instance oracle;
3. build and cross-check the exact extension-profile engine.

Only then begin control calibration, obstruction enumeration, summary destruction, and invariant extraction.

## Stop conditions

Reject a candidate mechanism if it:

- is only bounded-width or local consistency without universal completeness;
- has superpolynomial construction, operations, or total representation;
- merges states with different completion sets;
- succeeds only on a restricted subclass;
- relies on randomness without the required deterministic consequence;
- avoids canonical reduction-generated or linear 4-regular hard instances.
