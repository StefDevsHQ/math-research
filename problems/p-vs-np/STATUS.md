# Status — P versus NP

**Phase:** Monotone NAE-3SAT VS-08 complete; `NAE-016` open; VS-09 route selection next  
**Updated:** 2026-07-23

## Current position

The active Monotone NAE-3SAT investigation has completed `VS-01` through `VS-08` as checked infrastructure, falsification, semantic measurement and one fully implemented representation attack.

No proof route, universal polynomial-time mechanism or general representation lower bound has been accepted.

The Subset Sum investigation remains closed after its universal structural-compression strategies failed within their stated models.

## VS-08 determination

Propagation-closed signed residual normal form was implemented in full.

Retained:

- exact direct residualization into unary, signed-binary and ternary constraints;
- deterministic propagation closure;
- exact next-variable transitions;
- canonical component normalization with explicit orientation bits;
- complete encoded-size and reachable-state measurements.

Negative results:

- dropping component orientation is unsound even on one NAE edge;
- oriented PCRNF byte equality is not exact semantic equivalence;
- the first strict incompleteness witness occurs on five vertices;
- no polynomial bound on the complete reachable PCRNF state graph was proved.

Claim status:

- `NAE-016` — `CONJECTURE / CHECKED`;
- `NAE-017` — `PROVED / CHECKED`;
- `NAE-018` — `DISPROVED / CHECKED`.

The earlier `RETRACTED` classification of `NAE-016` was corrected. Failure of byte equality as a complete semantic quotient does not refute the existential claim that some efficiently constructible ordering has polynomial total PCRNF state.

## Current obstruction

The central unresolved gap is:

```text
polynomial explicit residual syntax
is not the same as
polynomially constructible exact semantic equivalence
```

A continuation must either:

1. prove a polynomial bound on the complete PCRNF state graph despite incomplete semantic merging; or
2. identify semantically equal residuals beyond byte equality without hiding NP-hard reasoning inside equality or normalization.

## Next vertical slice

`VS-09` is `PARTIAL / READY` and has two possible tracks.

### Track A — restricted PCRNF theorem

Prove polynomial reachable-state and total-encoding bounds on the largest identifiable structural class, starting from the exact substrate supplied by `NAE-017`.

### Track B — stronger exact quotient

Define and attack a polynomial-time exact merge mechanism over PCRNF that passes the five-vertex witness and has a complete global state bound.

`VS-10` through `VS-12` remain blocked only until one of these tracks yields a precise candidate.

## Retained project results

- Subset Sum residue-completion lemma and restricted exact-decomposition theorem;
- Monotone NAE-3SAT exact quotient and bounded-boundary theorems;
- incidence-forest constructive colouring;
- obstruction, locality-failure, summary-collision and semantic-merging evidence;
- exact oriented PCRNF residualization and its explicit byte-equality boundary.

No retained result proves `P=NP`, `P!=NP`, a general circuit lower bound or a lower bound for arbitrary algorithms.

## Next decision

Select VS-09 Track A or Track B. Do not close the Monotone NAE-3SAT programme and do not treat `NAE-018` as a disproof of `NAE-016`.
