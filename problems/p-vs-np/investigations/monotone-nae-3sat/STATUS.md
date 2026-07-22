# Status — Monotone NAE-3SAT Investigation

**Phase:** `VS-08` complete; `NAE-016` open; select VS-09 continuation  
**Updated:** 2026-07-23

## Current position

`VS-01` through `VS-08` are `COMPLETE / CHECKED`.

VS-08 implemented propagation-closed signed residual normal forms, repaired an orientation defect, proved exact oriented residualization, and found the first strict semantic-incompleteness witness for byte equality.

The Monotone NAE-3SAT programme remains open. The specific byte-equality merge strategy is closed; the existential polynomial-state conjecture `NAE-016` is not disproved and remains open.

No universal polynomial-time mechanism or general representation lower bound is claimed.

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
- `NAE-006` remains `CONJECTURE / DRAFT` and unresolved.

The former `RETRACTED` classification of `NAE-016` was too strong. VS-08 refuted semantic completeness of byte equality and failed to prove a global polynomial bound; it did not refute the existence of a polynomial-state ordering for every instance.

Operationally:

```text
mathematical conjecture NAE-016       OPEN
exact oriented PCRNF substrate        RETAINED
byte equality as complete quotient    CLOSED
next proof mechanism                  NOT YET SELECTED
```

## Retained implementation

The tool now provides:

- immutable oriented residual components;
- unary, signed-binary, and ternary residual constraints;
- deterministic propagation closure;
- exact next-variable restriction;
- exact residual evaluation and completion masks;
- canonical complete JSON encoding;
- memoized level traversal;
- exact-profile comparison;
- deterministic attack record and strict validation.

## Vertical-slice progress

- `VS-01` through `VS-08` — `COMPLETE / CHECKED`.
- `VS-09` — `PARTIAL / READY`: use `NAE-017` either to prove a restricted polynomial-state theorem or to define a stronger exact merge layer over PCRNF.
- `VS-10` through `VS-12` remain blocked until VS-09 produces a precise surviving candidate.

## Current obstruction

PCRNF exposes the core difficulty clearly:

```text
exact residual syntax != exact semantic equivalence
```

A stronger merge rule must identify semantically equal but syntactically different residuals without invoking satisfiability, exact completion enumeration, or another intractable semantic oracle. Alternatively, a direct theorem may bound the number of reachable PCRNFs despite incomplete merging.

Either route must bound the complete generated state graph, not only each individual state.

## Continuation conditions

Continue from `NAE-017` through one of two precise routes:

1. prove polynomial reachable-state and total-encoding bounds on the largest identifiable structural class, then test whether the proof extends;
2. define a polynomial-time exact merge criterion strictly stronger than byte equality and attack it on the five-vertex witness, fan family, Fano, linear four-regular instances, and canonical reduction outputs.

A disproof of `NAE-016` requires an every-ordering superpolynomial family or another complete contradiction to its quantified statement.

Evidence: [VS-08 completion and status-correction audit](VS-08-AUDIT.md) and the deterministic PCRNF attack record.
