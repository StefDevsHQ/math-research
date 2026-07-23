# Status — P versus NP

**Phase:** Circuit-SAT consequence-map construction and model selection  
**Updated:** 2026-07-23

## Current position

The project has opened a Circuit-SAT algorithms-to-lower-bounds investigation.

`CS-VS-01 — Exact consequence map` is active. No circuit class, algorithmic mechanism or lower-bound target has yet been selected.

The immediate objective is to identify one precise statement of the form:

```text
specified SAT or #SAT improvement for circuit class C
implies
specified nonuniform circuit lower bound
```

and verify every theorem hypothesis before activating an algorithm route.

## Retained prior results

The Monotone NAE-3SAT investigation completed two universal exact-representation barriers on one central-lift expander family:

- `NAE-020` forces exponentially many distinct live residual completion functions under every variable ordering;
- `NAE-021` proves exponential size for every DNNF representing the exact satisfying-assignment function.

The Subset Sum investigation remains closed after its universal structural-compression and broad exact-state-barrier strategies failed within their stated models.

## Current investigation state

- `CS-001 — OPEN / CHECKED`: consequence-map construction; no circuit model selected.
- `CS-002 — ESTABLISHED / DRAFT`: class-specific algorithms-to-lower-bounds transfer results exist and require exact source verification.

## Active gate

Complete `CS-VS-01` with:

1. exact circuit-class definitions;
2. exact SAT, #SAT or counting improvement thresholds;
3. primary transfer theorem statements;
4. closure, uniformity, size and randomness hypotheses;
5. exact lower-bound consequences;
6. best known algorithms and remaining gaps;
7. one recommended model and one decisive stop condition.

Implementation and algorithm design remain blocked until this gate is passed.

## Scope boundary

The active investigation does not yet claim:

- a faster Circuit-SAT algorithm;
- a new circuit lower bound;
- a lower bound for unrestricted Boolean circuits;
- `P=NP` or `P!=NP`.

## Navigation

- [Circuit-SAT investigation](investigations/circuit-sat/README.md)
- [Circuit-SAT vertical slices](investigations/circuit-sat/VERTICAL-SLICES.md)
- [Monotone NAE-3SAT retained results](investigations/monotone-nae-3sat/STATUS.md)
- [Subset Sum retained results](investigations/subset-sum/STATUS.md)
