# Status — Monotone NAE-3SAT Investigation

**Phase:** `VS-08` complete; `NAE-016` open; VS-09 route selection organized  
**Updated:** 2026-07-23

## Current position

`VS-01` through `VS-08` are `COMPLETE / CHECKED`.

VS-08 implemented propagation-closed signed residual normal forms, repaired an orientation defect, proved exact oriented residualization, and found the first strict semantic-incompleteness witness for byte equality.

The Monotone NAE-3SAT programme remains open. The byte-equality merge strategy is closed; the existential polynomial-state conjecture `NAE-016` remains open.

No universal polynomial-time mechanism or general representation lower bound is claimed.

## Route position

The programme now has an explicit [route registry](routes/README.md) and [route dashboard](routes/STATUS.md).

Current hierarchy:

- [`R1 — Exact-state representations`](routes/exact-state-representations/README.md) — `ACTIVE`;
  - [`R1.1 — PCRNF`](routes/exact-state-representations/pcrnf/README.md) — exact substrate retained, `NAE-016` open;
  - [`R1.2 — Semantic quotient over PCRNF`](routes/exact-state-representations/semantic-quotient/README.md) — `READY`, recommended next subroute;
  - `R1.3` decision diagrams and `R1.4` decomposable circuits — registered candidates.
- [`R2 — Decomposition and ordering`](routes/decomposition-and-ordering/README.md) — restricted results and open candidates.
- `R3` through `R6` — registered algebraic, gluing, branching and barrier families.

## Accepted VS-08 results

1. Orientation-free component-complement normalization is unsound for exact labelled completion semantics — `DISPROVED / CHECKED`.
2. Direct substitution, propagation closure, and component normalization with an explicit orientation bit preserve exact labelled completion sets and exact transitions — `NAE-017, PROVED / CHECKED`.
3. PCRNF byte equality is strictly finer than exact completion equivalence — `NAE-018, DISPROVED / CHECKED`.
4. PCRNF equality coincides with exact completion classes throughout the exhaustive domain through four vertices — `COMPUTATIONAL / CHECKED`.
5. The first strict gap occurs on a five-vertex six-edge instance at ordering `(0,4,1,2,3)` and level two.
6. The fan family retains exponential bad-order PCRNF growth and bounded good-order growth.

## Claim status

- `NAE-016` — `CONJECTURE / CHECKED`.
- `NAE-017` — `PROVED / CHECKED`.
- `NAE-018` — `DISPROVED / CHECKED`.
- `NAE-006` — `CONJECTURE / DRAFT`.

Operationally:

```text
mathematical conjecture NAE-016       OPEN
exact oriented PCRNF substrate        RETAINED
byte equality as complete quotient    CLOSED
recommended next subroute             R1.2
parallel restricted theorem track     R1.1-B / R2.3
```

## Vertical-slice progress

- `VS-01` through `VS-08` — `COMPLETE / CHECKED`.
- `VS-09` — `PARTIAL / READY`:
  - `Track A`: prove restricted polynomial PCRNF state bounds through `R1.1-B` and `R2.3`;
  - `Track B`: define a stronger exact merge layer through `R1.2`.
- `VS-10` through `VS-12` remain blocked until VS-09 produces a precise surviving candidate.

## Current obstruction

```text
exact residual syntax != exact semantic equivalence
```

A stronger merge rule must identify semantically equal but syntactically different residuals without invoking satisfiability, exact completion enumeration, or another intractable semantic oracle. Alternatively, a direct theorem may bound the number of reachable PCRNFs despite incomplete merging.

Either continuation must bound the complete generated state graph, not only each individual state.

## Continuation conditions

Continue from `NAE-017` through one of two precise routes:

1. prove polynomial reachable-state and total-encoding bounds on the largest identifiable structural class, then test whether the proof extends;
2. define a polynomial-time exact merge criterion strictly stronger than byte equality and attack it on the five-vertex witness, fan family, Fano, linear four-regular instances, and canonical reduction outputs.

A disproof of `NAE-016` requires an every-ordering superpolynomial family or another complete contradiction to its quantified statement.

Evidence: [VS-08 completion and status-correction audit](VS-08-AUDIT.md), the deterministic PCRNF attack record, and the new route hierarchy.