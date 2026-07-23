# Claims — R1 Exact-State Representations

This ledger maps investigation claims to the route and its subroutes. Investigation-wide status remains authoritative in [`../../CLAIMS.md`](../../CLAIMS.md).

| Claim | Subroute | Status | Role |
|---|---|---|---|
| `NAE-004` | Route foundation | `PROVED / CHECKED` | Exact extension equivalence admits exact one-variable transitions. |
| `NAE-006` | `R1` universal target | `CONJECTURE / DRAFT` | A universal polynomial exact-completion representation exists; dormant pending a fixed surviving model. |
| `NAE-016` | `R1.1` | `DISPROVED / CHECKED` | No ordering yields polynomial total PCRNF state on every instance. |
| `NAE-017` | `R1.1` | `PROVED / CHECKED` | Oriented PCRNF residualization and transitions are exact. |
| `NAE-018` | `R1.1` | `DISPROVED / CHECKED` | PCRNF byte equality is not complete semantic equality. |
| `NAE-019` | `R1.1`, `R6` | `PROVED / CHECKED` | PCRNF state count is at least exact residual-function count. |
| `NAE-020` | `R1.1`, `R6` | `PROVED / CHECKED` | Central lifts of constant-degree expanders force exponentially many exact residual functions under every ordering. |
| `NAE-021` | `R1.4`, `R6` | `PROVED / CHECKED` | Central lifts of constant-degree expanders require exponential DNNF size. |

## Final status of R1.1

The universal ordered PCRNF route is closed. The disproof is not based on missed syntactic merging: the hard family already has exponentially many pairwise semantically distinct live residual functions at one level for every ordering.

## Final status of R1.4

The universal DNNF route is closed. Conditioning the centre of the expander lift produces a constant-degree monotone two-CNF of linear treewidth, and the established monotone-CNF DNNF theorem gives exponential size. This lower bound applies before imposing determinism or structuredness.

## Consequence for R1.2

A state-per-semantic-class quotient cannot defeat `NAE-020`. DNNF cannot serve as the required collective polynomial representation by `NAE-021`. `R1.2` is dormant until a different fixed representation language is proposed.

## Reopening obligations

A new candidate must specify:

- the exact representation language and semantics;
- construction, equality, restriction, transition, or composition operations;
- maximum and total representation size;
- whether it enumerates residual functions individually;
- why `NAE-020` and `NAE-021` do not apply;
- hard controls and stop conditions.

## Status discipline

- `NAE-020` and `NAE-021` do not refute `NAE-006`.
- Neither result lower-bounds unrestricted Boolean circuits, arbitrary non-DNNF structures, algebraic global methods, or arbitrary algorithms.
- Every transfer to another model requires an explicit subsumption theorem.
