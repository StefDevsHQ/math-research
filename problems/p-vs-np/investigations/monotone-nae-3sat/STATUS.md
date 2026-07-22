# Status — Monotone NAE-3SAT Investigation

**Phase:** Formalization complete; first route mechanism not yet activated  
**Updated:** 2026-07-22

## Current position

The investigation is open. The object, encoding, primary sources, baseline theorems, mandatory controls, and complete attack plan are prepared. No universal polynomial-time mechanism is claimed.

The selected object is Monotone NAE-3SAT, equivalently 2-colourability of a 3-uniform hypergraph. It is the symmetry-first counterpart to Positive 1-in-3 SAT.

## Accepted baseline

1. Monotone NAE-3SAT is NP-complete — `ESTABLISHED / CHECKED`.
2. A deterministic polynomial-time algorithm for all instances would prove `P=NP` — `PROVED / CHECKED`.
3. Unary/binary fixed-template Boolean CSPs reduce to 2-SAT — `PROVED / CHECKED`.
4. Exact extension equivalence has well-defined one-variable transitions — `PROVED / CHECKED`.
5. Boundary width `w` gives a `2^{O(w)} poly(L)` exact algorithm — `PROVED / CHECKED`.

These results establish the baseline, not a resolution.

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

Execute the first stage of [the complete attack plan](PLAN.md):

1. construct the exact small-instance and extension-profile harness;
2. establish the first semantic merges beyond raw boundary assignments;
3. falsify pairwise, affine, and other low-order summaries where possible;
4. isolate the smallest missing compatibility relation;
5. state and attack the first atomic route conjecture.

## Stop conditions

Reject a candidate mechanism if it:

- is only bounded-width or local consistency without universal completeness;
- has superpolynomial construction, operations, or total representation;
- merges states with different completion sets;
- succeeds only on a restricted subclass;
- relies on randomness without the required deterministic consequence;
- avoids canonical reduction-generated or linear 4-regular hard instances.
