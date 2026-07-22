# R2.3 — Beyond-Width Exact Decomposition

**Subroute:** `R2.3`  
**Status:** `READY / OPEN`

## Objective

Find an exact decomposition or processing order whose interface state is smaller than raw boundary assignment while retaining all cross-component compatibility.

## Candidate directions

- PCRNF state bounds on bounded incidence treewidth;
- bounded residual-component interaction;
- exact component-interface quotients;
- hybrid decomposition plus semantic state sharing;
- orderings chosen by semantic-state growth rather than boundary size alone.

## Required theorem form

For a precisely defined class `C`, prove that every encoded instance in `C` has an efficiently constructible decomposition or ordering for which:

- every interface representation is exact;
- the number of reachable states is polynomial;
- maximum and total encoded state are polynomial;
- transition, merge and acceptance are polynomial.

## Mandatory attacks

- cross-component compatibility collisions from VS-06;
- the five-vertex PCRNF semantic merge;
- both fan orderings;
- high-width satisfiable instances;
- reduction-generated instances.

## Stop conditions

Restrict or close a candidate when it collapses to ordinary `2^w` boundary dynamic programming, loses compatibility, requires an intractable decomposition, or has superpolynomial total generated state.