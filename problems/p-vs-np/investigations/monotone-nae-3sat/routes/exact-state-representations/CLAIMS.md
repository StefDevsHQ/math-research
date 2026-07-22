# Claims — R1 Exact-State Representations

This ledger maps investigation claims to the route and its subroutes. Investigation-wide status remains authoritative in [`../../../CLAIMS.md`](../../../CLAIMS.md).

| Claim | Subroute | Status | Role |
|---|---|---|---|
| `NAE-004` | Route foundation | `PROVED / CHECKED` | Exact extension equivalence admits exact one-variable transitions. |
| `NAE-006` | `R1` universal target | `CONJECTURE / DRAFT` | A universal polynomial exact-completion representation exists. |
| `NAE-016` | `R1.1` / continuation | `CONJECTURE / CHECKED` | Some efficiently constructible ordering yields polynomial total PCRNF state. |
| `NAE-017` | `R1.1` | `PROVED / CHECKED` | Oriented PCRNF residualization and transitions are exact. |
| `NAE-018` | `R1.1` | `DISPROVED / CHECKED` | PCRNF byte equality is not complete semantic equality. |

## Open obligations

### For `NAE-016`

Prove all of:

1. a polynomial-time ordering algorithm;
2. polynomial maximum PCRNF or quotient-state size;
3. polynomial reachable-state count;
4. polynomial total encoded state;
5. polynomial transition, equality, memoization, and acceptance.

A complete disproof requires an every-ordering superpolynomial family or another contradiction to the full quantified claim.

### For a stronger semantic quotient

State a new claim identifier only after fixing:

- the representation language;
- exact semantics;
- equality or canonicalization;
- transition and merge;
- total-state conjecture;
- hard controls and stop condition.

## Status discipline

- Failure of a subroute does not refute `NAE-006` or `R1`.
- Failure of byte equality does not refute `NAE-016`.
- A model-specific exponential lower bound does not lower-bound arbitrary exact representations.