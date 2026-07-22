# R1.3 — Decision Diagrams

**Subroute:** `R1.3`  
**Status:** `ORDERED VARIANT BLOCKED / BROADER VARIANTS UNASSESSED`

## Thesis

Represent residual completion behaviour by a canonical decision structure.

## Ordered variant

For reduced ordered binary decision diagrams, node width at a level is at least the number of distinct residual Boolean functions induced by assignments to the processed prefix.

`NAE-020` gives central-lift instances with `2^{Omega(n)}` pairwise distinct live residual functions at one level for every variable ordering. Therefore every ordered decision diagram using one global variable order has exponential size on this family.

This closes the straightforward reduced ordered binary decision-diagram candidate as a universal polynomial representation.

## What remains unassessed

The theorem does not automatically cover:

- free binary decision diagrams;
- sentential decision diagrams under unrestricted vtrees;
- zero-suppressed variants with a different represented semantics;
- non-ordered branching programs;
- circuits sharing many residual functions collectively.

Each requires a separate model statement and subsumption analysis.

## Required distinctions

Track separately:

1. processing order of original variables;
2. decision-diagram ordering or decomposition structure;
3. number of residual functions;
4. total shared nodes;
5. maximum and total encoded size;
6. construction, reduction, restriction, and conjunction cost.

## Main boundary

Canonicity does not imply compactness. `NAE-020` is an all-order residual-subfunction lower bound for ordered diagrams, not a lower bound for arbitrary circuits or decision structures.

## Reopening gate

Activate another decision-diagram model only after stating:

- its exact semantics;
- its structural restriction;
- why `NAE-020` does not already subsume it;
- a complete size measure;
- one hard family and stop condition.