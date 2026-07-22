# Route Programme Status — Monotone NAE-3SAT

**Updated:** 2026-07-23

## Active programme

The Monotone NAE-3SAT investigation remains open.

The current recommended continuation is `R1.2 — Exact semantic quotient over PCRNF`, with `R1.1-B — Restricted PCRNF classes` available as a parallel theorem track.

## Route dashboard

| Route | Status | Current subroute | Next decision |
|---|---|---|---|
| `R1` Exact-state representations | `ACTIVE` | `R1.2 READY`; `R1.1 retained` | Select one exact semantic quotient candidate or a direct state-count theorem. |
| `R2` Decomposition and ordering | `RESTRICTED / OPEN` | `R2.1`, `R2.2` proved; `R2.3` ready | Prove the largest PCRNF restricted class or define a beyond-width decomposition. |
| `R3` Algebraic encodings | `CANDIDATE` | none active | Select one exact algebraic language before experimentation. |
| `R4` Obstruction and gluing | `CANDIDATE / EVIDENCE` | locality and obstruction baselines retained | Define a complete gluing invariant or obstruction family. |
| `R5` Propagation and branching | `PARTIAL / OPEN` | exact PCRNF propagation retained | Supply a polynomial global branching or memoization bound. |
| `R6` Representation barriers | `ONGOING SUPPORT` | summary, locality and byte-equality barriers retained | Attach a precise barrier model to each activated constructive subroute. |

## Claim dashboard

| Claim | Route | Status |
|---|---|---|
| `NAE-006` | `R1` | `CONJECTURE / DRAFT` |
| `NAE-016` | `R1.1` | `CONJECTURE / CHECKED` |
| `NAE-017` | `R1.1`, `R5.1` | `PROVED / CHECKED` |
| `NAE-018` | `R1.1`, `R6.3` | `DISPROVED / CHECKED` |
| `NAE-005` | `R2.1` | `PROVED / CHECKED` |
| `NAE-008` | `R2.2` | `PROVED / CHECKED` |
| `NAE-012` | `R4.2`, `R6.2` | `PROVED / CHECKED` |

## Route-state semantics

- `ACTIVE`: currently selected universal or mechanism-level route.
- `READY`: precise enough to begin after one candidate is selected.
- `RESTRICTED`: valid only under explicit hypotheses.
- `CANDIDATE`: registered direction without an activated atomic claim.
- `BARRIER`: model-specific lower-bound or failure programme.
- `CLOSED`: exact route claim or mechanism has reached a justified stop condition.

A top-level route remains open when one child closes unless the route thesis itself is disproved or exhausted.