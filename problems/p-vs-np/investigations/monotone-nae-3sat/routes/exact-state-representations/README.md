# R1 — Exact-State Representations

**Operational status:** `ACTIVE / NARROWED`  
**Universal target:** `NAE-006`

## Thesis

Represent exact completion behaviour by a polynomially constructible symbolic object with exact operations and polynomial total generated representation.

`NAE-020` now forces a crucial distinction:

```text
polynomial number of residual functions
```

is impossible for ordered state enumeration on all inputs, but

```text
polynomial collective representation of many residual functions
```

remains open.

## Subroute registry

| ID | Subroute | Status | Established result | Remaining gap |
|---|---|---|---|---|
| `R1.1` | [PCRNF](pcrnf/README.md) | `CLOSED UNIVERSAL / RETAINED` | `NAE-017` exactness; `NAE-019/020` all-order state lower bound. | Restricted PCRNF classes only. |
| `R1.2` | [Collective representation over PCRNF](semantic-quotient/README.md) | `REFORMULATION REQUIRED` | State-per-semantic-class quotients are blocked by `NAE-020`. | Share many distinct residual functions in one exact structure. |
| `R1.3` | [Decision diagrams](decision-diagrams/README.md) | `ORDERED VARIANT BLOCKED` | Ordered residual-subfunction lower bound transfers from `NAE-020`. | Assess broader non-ordered models separately. |
| `R1.4` | [Decomposable circuits](decomposable-circuits/README.md) | `CANDIDATE — NEXT` | Decomposition may share structure across distinct residual functions. | Fix a precise circuit language and prove exact construction and size bounds. |

## Claim map

- `NAE-004` — exact extension equivalence has well-defined transitions — `PROVED / CHECKED`.
- `NAE-006` — universal collective exact-completion representation — `CONJECTURE / DRAFT`.
- `NAE-016` — polynomial-state PCRNF traversal under some ordering — `DISPROVED / CHECKED`.
- `NAE-017` — exact oriented PCRNF residualization and transition — `PROVED / CHECKED`.
- `NAE-018` — PCRNF byte equality equals exact semantic equivalence — `DISPROVED / CHECKED`.
- `NAE-019` — PCRNF states dominate exact residual-function count — `PROVED / CHECKED`.
- `NAE-020` — expander central lifts force exponential residual-function count under every ordering — `PROVED / CHECKED`.

## Current decision

The next universal candidate must be collective rather than state-per-residual-function.

Recommended order:

1. formalize one deterministic decomposable circuit model under `R1.4`;
2. prove exact representation and construction before claiming compression;
3. test whether the `NAE-020` family has polynomial or exponential circuit size;
4. audit all intermediate circuit operations and total generated size.

The parallel theorem track remains restricted PCRNF and decomposition classes.

## Promotion gate

A universal subroute survives only if it proves:

1. exactness;
2. polynomial construction and equality;
3. polynomial transition, restriction, or composition;
4. polynomial maximum representation size;
5. polynomial total generated representation;
6. no hidden enumeration of exponentially many residual functions;
7. survival on `NAE-020` and reduction-generated controls.

## Administration

- [Route status](STATUS.md)
- [Route claim ledger](CLAIMS.md)
- [NAE-016 expander disproof](pcrnf/proofs/NAE-016-expander-disproof.md)
- [Top-level route registry](../README.md)