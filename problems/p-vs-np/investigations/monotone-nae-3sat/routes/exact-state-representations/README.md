# R1 — Exact-State Representations

**Operational status:** `CLOSED UNIVERSAL / DORMANT`  
**Universal target:** `NAE-006 — CONJECTURE / DRAFT`

## Thesis

Represent exact completion behaviour by a polynomially constructible symbolic object with exact operations and polynomial total generated representation.

The investigation has now established two barriers on the same central-lift expander family:

- `NAE-020`: ordered computations that materialize one state per exact residual function require exponentially many states under every ordering;
- `NAE-021`: every DNNF representing the exact satisfying-assignment function has exponential size.

These results do not disprove the representation-independent conjecture `NAE-006`, but no fixed surviving universal representation language is presently specified. The generic route is therefore dormant rather than active.

## Subroute registry

| ID | Subroute | Status | Established result | Remaining scope |
|---|---|---|---|---|
| `R1.1` | [PCRNF](pcrnf/README.md) | `CLOSED UNIVERSAL / RETAINED` | `NAE-017` exactness; `NAE-019/020` all-order state lower bound. | Restricted PCRNF classes only. |
| `R1.2` | [Collective representation over PCRNF](semantic-quotient/README.md) | `DORMANT / UNSPECIFIED` | State-per-semantic-class quotients are blocked by `NAE-020`. | Reopen only with a fixed collective language not covered by current barriers. |
| `R1.3` | [Decision diagrams](decision-diagrams/README.md) | `ORDERED VARIANT BLOCKED` | Reduced ordered variants inherit `NAE-020`. | Broader non-ordered models require separate exact definitions and analysis. |
| `R1.4` | [Decomposable circuits](decomposable-circuits/README.md) | `CLOSED UNIVERSAL / RETAINED RESTRICTED` | `NAE-021` gives exponential DNNF size on central-lift expanders. | Bounded-treewidth and other restricted compilation classes only. |

## Claim map

- `NAE-004` — exact extension equivalence has well-defined transitions — `PROVED / CHECKED`.
- `NAE-006` — universal polynomial exact-completion representation — `CONJECTURE / DRAFT`, dormant.
- `NAE-016` — polynomial-state PCRNF traversal under some ordering — `DISPROVED / CHECKED`.
- `NAE-017` — exact oriented PCRNF residualization and transition — `PROVED / CHECKED`.
- `NAE-018` — PCRNF byte equality equals exact semantic equivalence — `DISPROVED / CHECKED`.
- `NAE-019` — PCRNF states dominate exact residual-function count — `PROVED / CHECKED`.
- `NAE-020` — expander central lifts force exponential residual-function count under every ordering — `PROVED / CHECKED`.
- `NAE-021` — expander central lifts require exponential DNNF size — `PROVED / CHECKED`.

## Route determination

Universal exact-state representation work stops here. A new candidate must not merely rename an unspecified symbolic object.

Reopening requires all of the following:

1. a fixed representation syntax and exact semantics;
2. polynomial-time construction and required operations;
3. polynomial maximum and total generated representation size;
4. no hidden enumeration of exact residual functions;
5. an explicit reason `NAE-020` and `NAE-021` do not apply;
6. survival on reduction-generated hard controls.

Restricted PCRNF, bounded-width compilation, and decomposition classification remain valid secondary theorem programmes.

## Scope boundary

The closeout does not lower-bound unrestricted Boolean circuits, arbitrary non-DNNF structures, algebraic global methods, or arbitrary algorithms. It proves neither `P=NP` nor `P!=NP`.

## Administration

- [Route status](STATUS.md)
- [Route claim ledger](CLAIMS.md)
- [NAE-016 expander disproof](pcrnf/proofs/NAE-016-expander-disproof.md)
- [NAE-021 DNNF lower bound](decomposable-circuits/proofs/NAE-021-dnnf-expander-lower-bound.md)
- [Top-level route registry](../README.md)
