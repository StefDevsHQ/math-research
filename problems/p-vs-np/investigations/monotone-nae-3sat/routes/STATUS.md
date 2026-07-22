# Route Programme Status — Monotone NAE-3SAT

**Updated:** 2026-07-23

## Active programme

The Monotone NAE-3SAT investigation remains open.

`R1.1 — PCRNF` is now closed as a universal ordered state-enumeration route by the all-ordering expander lower bound. Exact PCRNF machinery and restricted PCRNF theorems remain retained.

## Route dashboard

| Route | Status | Current subroute | Next decision |
|---|---|---|---|
| `R1` Exact-state representations | `ACTIVE / NARROWED` | `R1.1 universal closed`; collective representations remain | Select a representation that shares many distinct residual functions collectively rather than enumerating one state per function. |
| `R2` Decomposition and ordering | `RESTRICTED / OPEN` | `R2.1`, `R2.2` proved; `R2.3` ready | Prove restricted PCRNF classes or a materially non-ordered decomposition. |
| `R3` Algebraic encodings | `CANDIDATE` | none active | Select one exact algebraic language before experimentation. |
| `R4` Obstruction and gluing | `CANDIDATE / EVIDENCE` | locality and obstruction baselines retained | Define a complete gluing invariant or obstruction family. |
| `R5` Propagation and branching | `PARTIAL / OPEN` | exact PCRNF propagation retained | Supply a computation model not defeated by all-order residual-function growth. |
| `R6` Representation barriers | `ACTIVE SUPPORT` | expander central-lift lower bound added | Determine which ordered or state-per-function models are subsumed. |

## Claim dashboard

| Claim | Route | Status |
|---|---|---|
| `NAE-006` | `R1` | `CONJECTURE / DRAFT` |
| `NAE-016` | `R1.1` | `DISPROVED / CHECKED` |
| `NAE-017` | `R1.1`, `R5.1` | `PROVED / CHECKED` |
| `NAE-018` | `R1.1`, `R6.3` | `DISPROVED / CHECKED` |
| `NAE-019` | `R1.1`, `R6` | `PROVED / CHECKED` |
| `NAE-020` | `R1.1`, `R6` | `PROVED / CHECKED` |
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

The expander lower bound closes ordered state-per-residual enumeration, not the entire exact-representation programme.