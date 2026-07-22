# Claims — R1 Exact-State Representations

This ledger maps investigation claims to the route and its subroutes. Investigation-wide status remains authoritative in [`../../CLAIMS.md`](../../CLAIMS.md).

| Claim | Subroute | Status | Role |
|---|---|---|---|
| `NAE-004` | Route foundation | `PROVED / CHECKED` | Exact extension equivalence admits exact one-variable transitions. |
| `NAE-006` | `R1` universal target | `CONJECTURE / DRAFT` | A universal polynomial exact-completion representation exists. |
| `NAE-016` | `R1.1` | `DISPROVED / CHECKED` | No ordering yields polynomial total PCRNF state on every instance. |
| `NAE-017` | `R1.1` | `PROVED / CHECKED` | Oriented PCRNF residualization and transitions are exact. |
| `NAE-018` | `R1.1` | `DISPROVED / CHECKED` | PCRNF byte equality is not complete semantic equality. |
| `NAE-019` | `R1.1`, `R6` | `PROVED / CHECKED` | PCRNF state count is at least exact residual-function count. |
| `NAE-020` | `R1.1`, `R6` | `PROVED / CHECKED` | Central lifts of constant-degree expanders force exponentially many exact residual functions under every ordering. |

## Final status of R1.1

The universal ordered PCRNF route is closed. The disproof is not based on missed syntactic merging: the hard family already has exponentially many pairwise semantically distinct live residual functions at one level for every ordering.

## Consequence for R1.2

A state-per-semantic-class quotient cannot defeat `NAE-020`. `R1.2` survives only if it is reformulated as a collective representation that shares structure across many distinct residual functions without materializing each function as one state.

## Open obligations for surviving R1 candidates

A new candidate must specify:

- the collective representation language;
- exact semantics;
- construction and canonicalization;
- transition or composition operations;
- maximum and total representation size;
- whether it enumerates residual functions individually;
- hard controls and stop conditions.

## Status discipline

- `NAE-020` does not refute `NAE-006`.
- Failure of ordered PCRNF does not refute collective circuits, non-ordered decompositions, algebraic global methods, or arbitrary algorithms.
- The lower bound transfers only through an explicit subsumption theorem.