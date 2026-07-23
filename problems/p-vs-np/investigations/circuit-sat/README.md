# Circuit-SAT Algorithms to Lower Bounds

This investigation studies whether nontrivial satisfiability or counting algorithms for precisely defined circuit classes can be converted, through verified transfer theorems, into explicit nonuniform circuit lower bounds.

## Current phase

`CS-VS-01 — Exact consequence map` is active.

No circuit class, algorithmic mechanism or lower-bound target has yet been selected. The investigation begins by fixing the theorem dependency:

```text
circuit class C
+ exact SAT or #SAT improvement
+ verified transfer hypotheses
= exact lower-bound consequence
```

The project will not infer lower bounds merely from an apparently fast special-case algorithm.

## Governing question

Find a circuit class `C` and an exact algorithmic statement strong enough to activate a known algorithms-to-lower-bounds theorem, while retaining a realistic atomic mechanism and a decisive stop condition.

## Structure

- [Vertical slices](VERTICAL-SLICES.md) — authoritative execution order
- [Status](STATUS.md) — operational state
- [Claims](CLAIMS.md) — authoritative mathematical ledger
- [Sources](references/SOURCES.md) — primary literature map

Planned record directories:

```text
proofs/
audits/
experiments/
notes/
routes/
journal/
```

## Investigation boundaries

This investigation distinguishes:

- unrestricted Circuit-SAT;
- SAT for a restricted circuit class;
- #SAT and approximate counting;
- formula satisfiability;
- uniform algorithms;
- nonuniform circuit lower bounds.

These terms are not interchangeable.

A result for `AC0`, `ACC0`, formulas, threshold circuits or another restricted class establishes only the consequence justified for that class.

## Activation gate

No algorithm route becomes active until `CS-VS-01` records:

1. the exact circuit model;
2. the exact required runtime improvement;
3. the primary transfer theorem;
4. every theorem hypothesis;
5. the exact resulting separation;
6. the current best algorithm;
7. the remaining technical gap;
8. a decisive stop condition.

## Scope restraint

No repository result in this investigation currently proves a new SAT algorithm, a new circuit lower bound, `P=NP`, or `P!=NP`.