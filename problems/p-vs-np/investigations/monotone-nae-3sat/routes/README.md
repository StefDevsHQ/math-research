# Research Routes — Monotone NAE-3SAT

This directory is the authoritative route tree for the Monotone NAE-3SAT investigation.

A **top-level route** is a materially distinct mathematical strategy. A **subroute** is one concrete representation, algorithm, theorem programme, or lower-bound model inside that strategy.

## Current route tree

```text
routes/
├── R1 exact-state-representations/          ACTIVE / NARROWED
│   ├── R1.1 pcrnf/                          CLOSED UNIVERSAL / RETAINED
│   ├── R1.2 collective-representation/      REFORMULATION REQUIRED
│   ├── R1.3 decision-diagrams/              ORDERED VARIANT BLOCKED
│   └── R1.4 decomposable-circuits/           CANDIDATE — NEXT
├── R2 decomposition-and-ordering/           PARTIAL
│   ├── R2.1 boundary-width/                  PROVED / RESTRICTED
│   ├── R2.2 incidence-forest/                PROVED / RESTRICTED
│   └── R2.3 beyond-width/                    OPEN
├── R3 algebraic-encodings/                  PROPOSED
├── R4 obstruction-and-gluing/               PROPOSED
├── R5 propagation-and-branching/            PROPOSED / PARTIAL
└── R6 representation-barriers/              ACTIVE SUPPORT
```

## Top-level route registry

| ID | Route | Operational status | Mathematical objective | Immediate gate |
|---|---|---|---|---|
| `R1` | [Exact-state representations](exact-state-representations/README.md) | `ACTIVE / NARROWED` | Represent exact future completion behaviour without enumerating one state per residual function. | Select a collective representation, preferably `R1.4`, and attack it on `NAE-020`. |
| `R2` | [Decomposition and ordering](decomposition-and-ordering/README.md) | `PARTIAL` | Find efficiently constructible decompositions with polynomial complete collective state. | Extend beyond known bounded-width and incidence-forest classes. |
| `R3` | [Algebraic encodings](algebraic-encodings/README.md) | `PROPOSED` | Replace explicit logical compatibility by an exact polynomial algebraic object. | Select one exact field, ideal, cut, or inequality mechanism. |
| `R4` | [Obstruction and gluing](obstruction-and-gluing/README.md) | `PROPOSED` | Characterize global compatibility or unsatisfiability through exact gluing data or polynomial certificates. | State one complete obstruction or gluing theorem. |
| `R5` | [Propagation and branching](propagation-and-branching/README.md) | `PROPOSED / PARTIAL` | Turn forced implications and controlled branching into a globally polynomial computation. | Use a computation model not defeated by ordered residual-function growth. |
| `R6` | [Representation barriers](representation-barriers/README.md) | `ACTIVE SUPPORT` | Prove model-specific state or size lower bounds without overstating them as general lower bounds. | Determine exactly which ordered models are subsumed by `NAE-020`. |

## Current determination

- `NAE-016 — DISPROVED / CHECKED`;
- `NAE-017 — PROVED / CHECKED`;
- `NAE-018 — DISPROVED / CHECKED`;
- `NAE-019 — PROVED / CHECKED`;
- `NAE-020 — PROVED / CHECKED`.

The expander central-lift family forces exponentially many pairwise distinct exact residual functions under every variable ordering. Therefore:

- universal ordered PCRNF state enumeration is closed;
- a semantic quotient with one state per residual function is also blocked;
- reduced ordered decision diagrams inherit the same obstruction;
- collective circuit or non-ordered representations remain open.

## Status discipline

Mathematical status and route status are separate.

- `PROVED`, `DISPROVED`, `CONJECTURE`, and `OPEN` describe claims.
- `ACTIVE`, `READY`, `PARTIAL`, `PROPOSED`, `DEFERRED`, and `CLOSED` describe work programmes.

A failed subroute does not close its parent route unless every child mechanism is covered by a valid subsumption theorem.

## Cross-cutting controls

Every universal candidate must face:

- central lifts of constant-degree expanders from `NAE-020`;
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

Failure of one route or subroute does not imply `P!=NP`, and success on one restricted class does not imply `P=NP`.