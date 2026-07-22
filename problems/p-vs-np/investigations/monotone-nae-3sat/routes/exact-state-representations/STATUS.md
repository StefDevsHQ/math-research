# Status — R1 Exact-State Representations

**Route:** `R1`  
**Status:** `ACTIVE`  
**Updated:** 2026-07-23

## Current position

The route remains open.

The first concrete subroute, oriented PCRNF, proved exact residual construction and transitions but did not provide complete semantic equality or a polynomial global state bound.

## Accepted results

- `NAE-004 — PROVED / CHECKED`: exact extension equivalence is transition-compatible.
- `NAE-017 — PROVED / CHECKED`: oriented PCRNF exactly represents labelled residual semantics and transitions.
- `NAE-018 — DISPROVED / CHECKED`: PCRNF byte equality is not exact semantic equivalence.
- `NAE-016 — CONJECTURE / CHECKED`: the existential polynomial-state PCRNF claim remains open.

## Active subroute

`R1.2 — Semantic quotient over PCRNF` is the recommended next subroute.

It must identify semantically equal PCRNFs more strongly than byte equality without invoking exact completion enumeration, satisfiability, or another hidden hard oracle.

## Parallel restricted track

Use `NAE-017` to prove polynomial reachable-state and total-encoding bounds on explicit structural classes. This supports VS-09 but does not establish the universal conjecture.

## Blocker

No polynomial-time exact equivalence or canonical representation has yet been shown to produce a polynomial complete state graph on all inputs.

## Next decisive test

Define one exact semantic quotient candidate and test it on:

1. the five-vertex PCRNF incompleteness witness;
2. both fan orderings;
3. Fano and `K_5^(3)`;
4. linear four-regular samples;
5. verified reduction outputs.

## Stop conditions

Close only a specific subroute when its exactness fails, its equality hides hard semantic work, or an explicit family forces superpolynomial state in its stated model.

Do not close `R1` merely because one representation language fails.