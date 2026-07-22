# Status — Monotone NAE-3SAT Investigation

**Phase:** `VS-08` complete; PCRNF route closed  
**Updated:** 2026-07-23

## Current position

`VS-01` through `VS-08` are `COMPLETE / CHECKED`.

VS-08 implemented propagation-closed signed residual normal forms, repaired an orientation defect, proved exact oriented residualization, found the first strict semantic-incompleteness witness, and closed the universal PCRNF compression conjecture.

No universal polynomial-time mechanism or general representation lower bound is claimed.

## Accepted VS-08 results

1. Orientation-free component-complement normalization is unsound for exact labelled completion semantics — `DISPROVED / CHECKED`.
2. Direct substitution, propagation closure, and component normalization with an explicit orientation bit preserve exact labelled completion sets and exact transitions — `NAE-017, PROVED / CHECKED`.
3. PCRNF byte equality is strictly finer than exact completion equivalence — `NAE-018, DISPROVED / CHECKED`.
4. PCRNF equality coincides with exact completion classes throughout the exhaustive domain through four vertices — `COMPUTATIONAL / CHECKED`.
5. The first strict gap occurs on a five-vertex six-edge instance at ordering `(0,4,1,2,3)` and level two.
6. The fan family retains exponential bad-order PCRNF growth and bounded good-order growth.

## Claim status

- `NAE-016` — `RETRACTED / CHECKED`.
- `NAE-017` — `PROVED / CHECKED`.
- `NAE-018` — `DISPROVED / CHECKED`.
- `NAE-006` remains `CONJECTURE / DRAFT` and unresolved.

`NAE-016` is retracted rather than disproved because the five-vertex witness refutes semantic completeness of byte equality, not the existence of some polynomial-state ordering for every instance.

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
- `VS-09` remains `PARTIAL` only through the previously proved bounded-boundary and incidence-forest results.
- `VS-10` through `VS-12` remain blocked pending a materially new exact representation mechanism.

## Current obstruction

PCRNF exposes the core difficulty clearly:

```text
exact residual syntax != exact semantic equivalence
```

A stronger merge rule must identify semantically equal but syntactically different residuals without invoking satisfiability, exact completion enumeration, or another intractable semantic oracle. It must also bound the complete generated state graph, not only each individual state.

## Reopening condition

Do not reopen PCRNF as a universal route without:

1. a new polynomial-time exact merge criterion strictly stronger than byte equality;
2. proof that the criterion preserves labelled completion semantics;
3. a globally polynomial bound on reachable state count and total encoded state;
4. successful tests on the five-vertex incompleteness witness, fan family, Fano, linear four-regular instances, and canonical reduction outputs.

Evidence: [VS-08 completion audit](VS-08-AUDIT.md) and the deterministic PCRNF attack record.
