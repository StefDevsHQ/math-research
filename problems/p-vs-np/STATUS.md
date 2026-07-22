# Status — P versus NP

**Phase:** Monotone NAE-3SAT VS-08 complete; PCRNF route closed  
**Updated:** 2026-07-23

## Current position

The active Monotone NAE-3SAT investigation has completed `VS-01` through `VS-08` as checked infrastructure, falsification, semantic measurement, and one fully implemented representation attack.

No proof route, universal polynomial-time mechanism, or general representation lower bound has been accepted.

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
- no polynomial bound on the complete reachable PCRNF state graph survived.

Claim status:

- `NAE-016` — `RETRACTED / CHECKED`;
- `NAE-017` — `PROVED / CHECKED`;
- `NAE-018` — `DISPROVED / CHECKED`.

The route is closed as a universal compression route, while exact oriented PCRNF remains a useful reference representation and restricted control.

## Current obstruction

The central unresolved gap is now sharper:

```text
polynomial explicit residual syntax
is not the same as
polynomially constructible exact semantic equivalence
```

A new route must identify semantically equal residuals beyond syntax without hiding NP-hard reasoning inside equality or normalization, and it must prove a polynomial bound on the complete generated state graph.

## Mandatory reopening conditions

Do not reopen PCRNF without:

1. a new exact merge criterion strictly stronger than byte equality;
2. polynomial-time construction and equality;
3. proof of exact transition and acceptance;
4. a global polynomial bound on state count and total encoded state;
5. successful attacks on the five-vertex PCRNF witness, fan family, Fano, linear four-regular samples, and verified reduction outputs.

## Retained project results

- Subset Sum residue-completion lemma and restricted exact-decomposition theorem;
- Monotone NAE-3SAT exact quotient and bounded-boundary theorems;
- incidence-forest constructive colouring;
- obstruction, locality-failure, summary-collision and semantic-merging evidence;
- exact oriented PCRNF residualization and its explicit model boundary.

No retained result proves `P=NP`, `P!=NP`, a general circuit lower bound, or a lower bound for arbitrary algorithms.

## Next decision

Select a sibling exact-representation route, choose another P-versus-NP investigation, or pause the Monotone NAE-3SAT programme. Do not activate VS-09 through VS-12 without a materially new mechanism.
