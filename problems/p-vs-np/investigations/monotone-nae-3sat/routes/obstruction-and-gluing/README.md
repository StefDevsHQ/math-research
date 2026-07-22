# R4 — Obstruction and Gluing Systems

**Operational status:** `CANDIDATE / EVIDENCE AVAILABLE`

## Thesis

Characterize exact global compatibility through local solution systems, restriction maps, gluing rules, and explicit certificates when local pieces cannot be combined.

## Subroute registry

| ID | Subroute | Status | Result or objective |
|---|---|---|---|
| `R4.1` | Minimal unsatisfiable obstructions | `EVIDENCE / RESTRICTED` | VS-05 records `K_5^(3)`, Fano and deletion certificates. |
| `R4.2` | Local-consistency hierarchies | `NEGATIVE BASELINE` | `NAE-012` shows every fixed radius can miss residual satisfiability. |
| `R4.3` | Exact gluing interfaces | `CANDIDATE` | Encode which local satisfying assignments are mutually extendable. |
| `R4.4` | Obstruction certificates for failed gluing | `CANDIDATE` | Seek polynomially checkable complete certificates. |
| `R4.5` | Cohomological or sheaf-style compatibility | `CANDIDATE / UNFORMALIZED` | Formalize only with exact finite objects, operations and bounds. |

## Central obstruction

Local satisfiability does not imply global compatibility. The route must preserve correlated choices across overlaps rather than count or summarize pieces independently.

## Mandatory attacks

- fixed-radius locality-failure family;
- VS-06 summary collisions;
- locally consistent unsatisfiable instances;
- Fano and dense `K_5^(3)` controls;
- reduction gadgets whose clauses remain individually satisfiable while assignments conflict globally;
- exponential numbers or supports of candidate obstructions.

## Success condition

A universal result requires a complete polynomially constructible gluing invariant or obstruction family with polynomial-time verification and polynomial total encoded size.

## Stop conditions

Close or restrict a subroute when completeness requires unbounded support, exponentially many obstructions, NP-hard obstruction detection, or exact interface data equivalent to the full exponential completion table.