# Claim Ledger — Structural Compression

This ledger records the detailed claims for the structural-compression route.

## Claims

| ID | Statement | Status | Review | Evidence | Promotes to | Updated |
|---|---|---|---|---|---|---|
| `SS-SC-001` | Every Subset Sum instance admits a polynomial bundle decomposition whose local density or separation composes into a polynomial-size exact representation. | `RETRACTED` | `CHECKED` | [Bundle lemma retraction](counterexamples/bundle-lemma.md) | `SS-001` | 2026-07-16 |
| `SS-SC-002` | A complete reachable \(q\)-step progression plus bounded representatives of every residue modulo \(q\) from a disjoint component yields a complete central interval. | `PROVED` | `CHECKED` | [Residue-completion lemma](proofs/residue-completion-lemma.md) | `SS-002` | 2026-07-16 |
| `SS-SC-003` | Every Subset Sum instance can be solved in polynomial time by repeated forced separation, progression completion, or recursive lattice reduction. | `OPEN` | `DRAFT` | [Route record](notes/route-record.md) | — | 2026-07-16 |
| `SS-SC-004` | On canonical SAT-to-Subset-Sum instances, recursive lattice analysis strictly reduces a polynomially bounded complexity measure rather than preserving assignment choices. | `OPEN` | `DRAFT` | [Planned audit](audits/sat-to-subset-sum.md) | — | 2026-07-16 |

## Identifier policy

Route identifiers use `SS-SC-###`. Claims that change the accepted Subset Sum state are mirrored in the investigation ledger.
