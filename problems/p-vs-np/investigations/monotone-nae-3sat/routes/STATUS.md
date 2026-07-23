# Route Programme Status — Monotone NAE-3SAT

**Updated:** 2026-07-23

## Programme determination

The universal exact-representation programme is closed at the current model boundary.

`NAE-020` blocks ordered state-per-residual-function models. `NAE-021` blocks DNNF and every DNNF subclass on the same central-lift expander family.

## Route dashboard

| Route | Status | Current determination | Next decision |
|---|---|---|---|
| `R1` Exact-state representations | `CLOSED UNIVERSAL / DORMANT` | PCRNF, semantic-class enumeration, reduced ordered decision diagrams, and DNNF blocked universally within their models. | Reopen only for a precisely defined representation escaping both barriers. |
| `R2` Decomposition and ordering | `RESTRICTED / OPEN` | Bounded-width and incidence-forest results retained. | Continue only as a restricted theorem programme. |
| `R3` Algebraic encodings | `CANDIDATE` | No atomic mechanism selected. | Do not activate without a fixed exact algebraic language and stop condition. |
| `R4` Obstruction and gluing | `CANDIDATE / EVIDENCE` | Locality and obstruction baselines retained. | Require one complete gluing invariant or obstruction theorem. |
| `R5` Propagation and branching | `PARTIAL / DORMANT` | Exact PCRNF propagation retained; universal ordered traversal blocked. | Require a computation model not subsumed by current barriers. |
| `R6` Representation barriers | `COMPLETE SUPPORT / RETAINED` | Ordered residual-state and DNNF expander lower bounds established. | Map only explicit additional subsumption consequences. |

## Claim dashboard

| Claim | Route | Status |
|---|---|---|
| `NAE-006` | `R1` | `CONJECTURE / DRAFT — DORMANT` |
| `NAE-016` | `R1.1` | `DISPROVED / CHECKED` |
| `NAE-017` | `R1.1`, `R5.1` | `PROVED / CHECKED` |
| `NAE-018` | `R1.1`, `R6.3` | `DISPROVED / CHECKED` |
| `NAE-019` | `R1.1`, `R6` | `PROVED / CHECKED` |
| `NAE-020` | `R1.1`, `R6` | `PROVED / CHECKED` |
| `NAE-021` | `R1.4`, `R6` | `PROVED / CHECKED` |
| `NAE-005` | `R2.1` | `PROVED / CHECKED` |
| `NAE-008` | `R2.2` | `PROVED / CHECKED` |
| `NAE-012` | `R4.2`, `R6.2` | `PROVED / CHECKED` |

## Scope

The route closures are model-specific. They do not imply a lower bound for unrestricted Boolean circuits or arbitrary algorithms, and they do not resolve `P` versus `NP`.