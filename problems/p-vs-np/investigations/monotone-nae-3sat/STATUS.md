# Status — Monotone NAE-3SAT Investigation

**Phase:** `NAE-016` disproved; ordered state-enumeration route closed; collective representations next  
**Updated:** 2026-07-23

## Current position

`VS-01` through `VS-08` remain `COMPLETE / CHECKED`.

The subsequent direct attack on `NAE-016` is also complete. Central lifts of constant-degree expanders force exponentially many pairwise distinct live exact completion functions under every variable ordering. Since exact PCRNF states cannot identify distinct completion functions, every ordering has exponentially many PCRNF states.

The Monotone NAE-3SAT programme remains open. The universal ordered PCRNF route is closed.

## Accepted results

- `NAE-016 — DISPROVED / CHECKED`: no polynomial-state PCRNF ordering exists universally.
- `NAE-017 — PROVED / CHECKED`: oriented PCRNF residualization and transitions are exact.
- `NAE-018 — DISPROVED / CHECKED`: PCRNF byte equality is not complete semantic equality.
- `NAE-019 — PROVED / CHECKED`: PCRNF state count dominates exact residual-function count.
- `NAE-020 — PROVED / CHECKED`: central lifts of constant-degree expanders yield `2^{Omega(n)}` exact residual functions under every ordering.
- `NAE-006 — CONJECTURE / DRAFT`: a broader polynomial collective exact representation remains unresolved.

## Route position

- [`R1.1 — PCRNF`](routes/exact-state-representations/pcrnf/README.md): closed as a universal ordered state-enumeration route; exact and restricted results retained.
- [`R1.2 — Collective exact representation`](routes/exact-state-representations/semantic-quotient/README.md): reformulation required; state-per-semantic-class quotients are blocked by `NAE-020`.
- [`R1.3 — Decision diagrams`](routes/exact-state-representations/decision-diagrams/README.md): reduced ordered variants blocked; broader models unassessed.
- `R1.4 — Decomposable circuits`: remains a candidate collective representation route.
- `R2`: restricted decomposition and ordering results remain valid.
- `R6`: now contains an explicit all-ordering model-specific barrier.

## Exact determination

```text
PCRNF exactness                              RETAINED
PCRNF byte equality as semantic equality     DISPROVED
polynomial PCRNF state under some ordering    DISPROVED
ordered state per residual function           BLOCKED
collective exact representations              OPEN
restricted PCRNF classes                      OPEN
```

## Scope boundary

The lower bound does not prove `P!=NP`, does not disprove `NAE-006`, and does not lower-bound arbitrary circuits or algorithms. It applies to ordered computations that materialize one exact state for each residual completion function.

## Next decision

The strongest next constructive option is a collective representation route, most plausibly deterministic decomposable circuits or another non-ordered structure that can share information across exponentially many distinct residual functions.

The parallel small-win track is to classify the largest restricted graph or hypergraph classes on which PCRNF state remains polynomial.

Evidence: [NAE-016 expander disproof](routes/exact-state-representations/pcrnf/proofs/NAE-016-expander-disproof.md).