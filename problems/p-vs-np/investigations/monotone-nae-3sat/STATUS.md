# Status — Monotone NAE-3SAT Investigation

**Phase:** Formalization and route selection  
**Updated:** 2026-07-22

## Current position

The investigation is open, but no proof route is active.

The selected object is Monotone NAE-3SAT, equivalently 2-colourability of a 3-uniform hypergraph. It is used as a symmetry-first complement to Positive 1-in-3 SAT.

## Established external facts

1. Monotone NAE-3SAT is in `NP`.
2. Monotone NAE-3SAT is NP-complete.
3. Therefore a deterministic polynomial-time algorithm for all instances would imply `P=NP`.
4. Boolean CSPs restricted to unary and binary relations reduce to 2-SAT, so arity three is minimal for NP-completeness within fixed-template Boolean CSPs.

These are established results or direct consequences, not project-original resolutions.

## Current mathematical obstruction

Each constraint forbids only two of eight local assignments and is invariant under global colour complementation. Local feasibility is therefore abundant, while unsatisfiability can arise from incompatibility distributed across cycles and overlapping hyperedges.

The candidate abstract object is exact global witness compatibility: partial colourings should be identified only when they admit exactly the same completions. This semantic quotient is exact but may be exponentially large and may be intractable to construct.

## Required next result

Before a route is activated, produce one precise candidate invariant or composition theorem with:

- exact soundness and completeness statements;
- an explicit finite representation;
- polynomial construction and update algorithms;
- a polynomial bound on the complete computation graph and encoded intermediate state;
- successful tests against graph 2-colouring, XOR-SAT, Positive 1-in-3 SAT, and reduction-generated hard instances.

## Stop conditions

Close or reject a candidate mechanism if any of the following occurs:

1. it is only a bounded-width or local-consistency method with no universal completeness theorem;
2. exact state generation is exponential on a polynomial-size family;
3. it merges partial assignments that have different possible completions;
4. it succeeds only on a restricted subclass;
5. it relies on randomized correctness without an explicit deterministic consequence;
6. it survives only because tested instances omit canonical hard reductions.

## Next decision

Select the first route mechanism. The leading candidate family is global-compatibility geometry: local solution systems, restriction maps, and exact future-equivalence classes. It remains an `OPEN` research proposal, not an established algorithm.
