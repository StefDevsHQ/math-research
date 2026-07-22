# R1 — Exact-State Representations

**Operational status:** `ACTIVE`  
**Universal target:** `NAE-006` and the more concrete PCRNF conjecture `NAE-016`

## Thesis

Represent the exact future completion relation of each processed prefix by a polynomially constructible symbolic object with:

- exact labelled semantics;
- polynomial-time canonical equality or equivalence;
- exact restriction and transition;
- exact conjunction, merge, and acceptance;
- polynomial maximum encoded state;
- polynomial number and total encoded size of all generated states.

Individual polynomial-size residuals are insufficient. The complete memoized computation graph must be polynomially bounded.

## Subroute registry

| ID | Subroute | Status | Established result | Remaining gap |
|---|---|---|---|---|
| `R1.1` | [PCRNF](pcrnf/README.md) | `RETAINED / OPEN` | Exact oriented residualization and transitions are `NAE-017 — PROVED / CHECKED`. | Byte equality is incomplete; `NAE-016` remains open. |
| `R1.2` | [Semantic quotient over PCRNF](semantic-quotient/README.md) | `READY — NEXT` | Exact PCRNF provides a trusted substrate. | Find a polynomial-time exact equivalence stronger than byte equality and prove global state bounds. |
| `R1.3` | [Decision diagrams](decision-diagrams/README.md) | `CANDIDATE` | Canonical function representations can provide exact equality for fixed representation conventions. | General size may be exponential; ordering and total-node bounds must be attacked. |
| `R1.4` | [Decomposable circuits](decomposable-circuits/README.md) | `CANDIDATE` | Decomposition may share repeated residual structure. | Canonical equality, determinism, construction cost, and total circuit size remain unresolved. |

## Claim map

- `NAE-004` — exact extension equivalence has well-defined transitions — `PROVED / CHECKED`.
- `NAE-006` — universal symbolic exact-completion representation — `CONJECTURE / DRAFT`.
- `NAE-016` — polynomial-state PCRNF traversal under an efficiently constructible ordering — `CONJECTURE / CHECKED`.
- `NAE-017` — exact oriented PCRNF residualization and transition — `PROVED / CHECKED`.
- `NAE-018` — PCRNF byte equality equals exact semantic equivalence — `DISPROVED / CHECKED`.

## Current decision

Do not treat the failure of PCRNF byte equality as a failure of the entire route.

The next active choice is:

1. `R1.2`: define a stronger exact quotient over PCRNF; or
2. prove a direct polynomial reachable-state theorem for PCRNF on a substantial restricted class and determine whether it extends.

## Promotion gate

A universal subroute survives only if it proves all of:

1. exactness;
2. polynomial construction and equality;
3. polynomial transition and acceptance;
4. polynomial maximum state size;
5. polynomial reachable-state count;
6. polynomial total encoded state;
7. survival on reduction-generated hard controls.

## Administration

- [Route status](STATUS.md)
- [Route claim ledger](CLAIMS.md)
- [Top-level route registry](../README.md)