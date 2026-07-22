# R1.3 — Canonical Decision Diagrams

**Subroute:** `R1.3`  
**Status:** `CANDIDATE / NOT ACTIVATED`

## Thesis

Represent each residual completion function by a reduced canonical decision diagram under an explicit variable order.

Unlike PCRNF byte equality, equality of reduced diagrams under fixed conventions is intended to mean equality of the represented Boolean function.

## Candidate models

- reduced ordered binary decision diagrams;
- zero-suppressed decision diagrams where semantically appropriate;
- other explicitly canonical decision-diagram variants.

Do not merge these models without a polynomial-overhead equivalence theorem.

## Required distinctions

Track separately:

1. processing order of the original variables;
2. variable order inside the decision diagram;
3. number of residual states;
4. number of shared diagram nodes;
5. maximum and total encoded diagram size;
6. cost of reduction, restriction and conjunction.

## First attacks

- reproduce the VS-07 genuine merge;
- merge the VS-08 five-vertex PCRNF witness exactly;
- measure both fan orderings;
- search for ordering-sensitive exponential diagram growth;
- test reduction-generated instances.

## Main risk

Canonical equality does not imply compactness. General Boolean functions and structured constraint families can require exponentially large ordered decision diagrams.

The route survives only if Monotone NAE-3SAT residual structure plus efficiently constructible ordering yields a new polynomial bound.

## Activation gate

Before implementation, state one exact model, one ordering algorithm or ordering conjecture, complete size accounting, and one explicit stop family.