# Claim Ledger — Monotone NAE-3SAT Investigation

This is the authoritative investigation-level ledger for Monotone NAE-3SAT claims.

## Claims

| ID | Statement | Status | Review | Evidence | Updated |
|---|---|---|---|---|---|
| `NAE-001` | Monotone NAE-3SAT is NP-complete. | `ESTABLISHED` | `CHECKED` | Schaefer's Boolean CSP dichotomy and the canonical source map `[P03]` | 2026-07-22 |
| `NAE-002` | A deterministic polynomial-time algorithm deciding every Monotone NAE-3SAT instance would prove `P=NP`. | `PROVED` | `CHECKED` | Membership in `NP`, `NAE-001`, and closure under polynomial-time many-one reductions | 2026-07-22 |
| `NAE-003` | Every fixed-template Boolean CSP using only unary and binary relations is polynomial-time reducible to 2-SAT. | `PROVED` | `DRAFT` | [Object specification](OBJECT.md#arity-minimality) | 2026-07-22 |
| `NAE-004` | Exact future-equivalence classes of partial colourings admit a universally polynomial-size, polynomial-time constructible representation. | `CONJECTURE` | `DRAFT` | [Research plan](PLAN.md) | 2026-07-22 |

## Current accepted state

The investigation has one established hardness fact, one checked class-consequence theorem, and one elementary project proof concerning arity minimality.

`NAE-004` is deliberately strong. It is not supported by evidence and is expected to be the first object of attack. Failure of this representation would not prove `P!=NP`.

## Claim boundaries

- Polynomial time means polynomial in the complete binary encoding length.
- Restricted subclasses do not establish `NAE-002`'s premise.
- Randomized bounded-error algorithms do not establish deterministic `P=NP` without an explicit derandomization theorem.
- A compact syntax is insufficient unless construction, transition, evaluation, and total generated state are polynomially bounded.
- A lower bound for future-equivalence representations is model-specific unless a polynomial-overhead subsumption theorem is proved.

## Identifier policy

Use stable identifiers of the form `NAE-###`. Never reuse an identifier after retraction or replacement.
