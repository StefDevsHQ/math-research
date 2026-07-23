# Research Routes — Monotone NAE-3SAT

This directory is the authoritative route tree for the Monotone NAE-3SAT investigation.

A **top-level route** is a materially distinct mathematical strategy. A **subroute** is one concrete representation, algorithm, theorem programme, or lower-bound model inside that strategy.

## Current route tree

```text
routes/
├── R1 exact-state-representations/          CLOSED UNIVERSAL / DORMANT
│   ├── R1.1 pcrnf/                          CLOSED UNIVERSAL / RETAINED
│   ├── R1.2 collective-representation/      DORMANT / UNSPECIFIED
│   ├── R1.3 decision-diagrams/              ORDERED VARIANT BLOCKED
│   └── R1.4 decomposable-circuits/           CLOSED UNIVERSAL / RETAINED RESTRICTED
├── R2 decomposition-and-ordering/           RESTRICTED RESULTS / OPEN SECONDARY
│   ├── R2.1 boundary-width/                  PROVED / RESTRICTED
│   ├── R2.2 incidence-forest/                PROVED / RESTRICTED
│   └── R2.3 beyond-width/                    OPEN SECONDARY
├── R3 algebraic-encodings/                  PROPOSED / INACTIVE
├── R4 obstruction-and-gluing/               PROPOSED / INACTIVE
├── R5 propagation-and-branching/            PROPOSED / PARTIAL / INACTIVE
└── R6 representation-barriers/              RETAINED SUPPORT
```

## Top-level route registry

| ID | Route | Operational status | Retained result | Reopening gate |
|---|---|---|---|---|
| `R1` | [Exact-state representations](exact-state-representations/README.md) | `CLOSED UNIVERSAL / DORMANT` | Exact PCRNF; ordered residual-function and DNNF lower bounds. | Fix a materially new representation language not subsumed by `NAE-020` or `NAE-021`. |
| `R2` | [Decomposition and ordering](decomposition-and-ordering/README.md) | `RESTRICTED RESULTS / OPEN SECONDARY` | Bounded-boundary dynamic programming and incidence-forest colouring. | State a structural class and prove a complete polynomial total-state bound. |
| `R3` | [Algebraic encodings](algebraic-encodings/README.md) | `PROPOSED / INACTIVE` | None universal. | Select one exact algebraic language and a falsifiable construction claim. |
| `R4` | [Obstruction and gluing](obstruction-and-gluing/README.md) | `PROPOSED / INACTIVE` | Locality and collision barriers retained. | State one complete obstruction or gluing theorem. |
| `R5` | [Propagation and branching](propagation-and-branching/README.md) | `PROPOSED / PARTIAL / INACTIVE` | Exact PCRNF propagation retained. | Supply a globally polynomial computation model not covered by current barriers. |
| `R6` | [Representation barriers](representation-barriers/README.md) | `RETAINED SUPPORT` | `NAE-020` and `NAE-021`. | Extend only through an explicit model-subsump­tion theorem. |

## Current determination

- `NAE-016 — DISPROVED / CHECKED`;
- `NAE-017 — PROVED / CHECKED`;
- `NAE-018 — DISPROVED / CHECKED`;
- `NAE-019 — PROVED / CHECKED`;
- `NAE-020 — PROVED / CHECKED`;
- `NAE-021 — PROVED / CHECKED`.

The central-lift expander family now yields two distinct barriers:

1. every variable ordering has exponentially many exact residual completion functions;
2. every DNNF for the exact satisfying-assignment function has exponential size.

Consequently, universal ordered PCRNF enumeration, one-state-per-residual-function quotients, reduced ordered decision diagrams, and DNNF are closed as polynomial exact-representation routes. This does not lower-bound unrestricted Boolean circuits, algebraic global methods, arbitrary data structures, or arbitrary algorithms.

## Status discipline

Mathematical status and route status are separate. A closed mechanism does not imply `P!=NP`, and a restricted theorem does not imply `P=NP`.

`NAE-006` remains a conjecture, but the generic route is dormant because no fixed surviving representation language is presently specified.

## Cross-cutting controls

Any reopened universal route must face:

- central-lift expanders from `NAE-020` and `NAE-021`;
- the four-vertex genuine semantic-merge witness;
- the five-vertex PCRNF incompleteness witness;
- both fan orderings;
- `K_5^(3)` and Fano;
- linear four-regular instances;
- bounded-width and incidence-forest controls;
- VS-06 collision pairs;
- verified reduction-generated instances.

## Navigation

- [Investigation status](../STATUS.md)
- [Vertical slices](../VERTICAL-SLICES.md)
- [Investigation claim ledger](../CLAIMS.md)
- [Route dashboard](STATUS.md)
- [NAE-016 expander disproof](exact-state-representations/pcrnf/proofs/NAE-016-expander-disproof.md)
- [NAE-021 DNNF lower bound](exact-state-representations/decomposable-circuits/proofs/NAE-021-dnnf-expander-lower-bound.md)
