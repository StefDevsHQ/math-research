# Research Routes — Monotone NAE-3SAT

This directory is the authoritative route tree for the Monotone NAE-3SAT investigation.

A **top-level route** is a materially distinct mathematical strategy. A **subroute** is one concrete representation, algorithm, theorem programme, or lower-bound model inside that strategy.

## Current route tree

```text
routes/
├── R1 exact-state-representations/          ACTIVE
│   ├── R1.1 pcrnf/                          RETAINED / OPEN
│   ├── R1.2 semantic-quotient/              READY — NEXT
│   ├── R1.3 decision-diagrams/              CANDIDATE
│   └── R1.4 decomposable-circuits/          CANDIDATE
├── R2 decomposition-and-ordering/           PARTIAL
│   ├── R2.1 boundary-width/                  PROVED / RESTRICTED
│   ├── R2.2 incidence-forest/                PROVED / RESTRICTED
│   └── R2.3 beyond-width/                    OPEN
├── R3 algebraic-encodings/                  PROPOSED
├── R4 obstruction-and-gluing/               PROPOSED
├── R5 propagation-and-branching/            PROPOSED / PARTIAL
└── R6 representation-barriers/              SUPPORT / PROPOSED
```

## Top-level route registry

| ID | Route | Operational status | Mathematical objective | Immediate gate |
|---|---|---|---|---|
| `R1` | [Exact-state representations](exact-state-representations/README.md) | `ACTIVE` | Represent exact future completion behaviour with polynomial-time exact operations and polynomial total generated state. | Execute `R1.2` or prove a direct polynomial PCRNF state bound. |
| `R2` | [Decomposition and ordering](decomposition-and-ordering/README.md) | `PARTIAL` | Find efficiently constructible decompositions or orderings with polynomial complete state. | Extend beyond known bounded-width and incidence-forest classes. |
| `R3` | [Algebraic encodings](algebraic-encodings/README.md) | `PROPOSED` | Replace explicit logical compatibility by an exact polynomial algebraic object. | Select one exact field, ideal, cut, or inequality mechanism. |
| `R4` | [Obstruction and gluing](obstruction-and-gluing/README.md) | `PROPOSED` | Characterize global compatibility or unsatisfiability through exact gluing data or polynomial certificates. | State one complete obstruction or gluing theorem. |
| `R5` | [Propagation and branching](propagation-and-branching/README.md) | `PROPOSED / PARTIAL` | Turn forced implications and controlled branching into a globally polynomial computation. | Go beyond the exact propagation closure already retained in PCRNF. |
| `R6` | [Representation barriers](representation-barriers/README.md) | `SUPPORT / PROPOSED` | Prove model-specific state or size lower bounds without overstating them as general lower bounds. | Select a precise representation model and quantified family. |

## Current active branch

The active programme is `R1 — Exact-state representations`.

Within it:

- `R1.1 PCRNF` supplies the exact residual substrate proved by `NAE-017`;
- PCRNF byte equality as a complete semantic quotient is closed by `NAE-018`;
- `NAE-016` remains `CONJECTURE / CHECKED`;
- `R1.2 Semantic quotient over PCRNF` is the next unselected mechanism;
- decision diagrams and decomposable circuits are explicit sibling candidates, not assumed solutions.

## Status discipline

Mathematical status and route status are separate.

- `PROVED`, `DISPROVED`, `CONJECTURE`, and `OPEN` describe claims.
- `ACTIVE`, `READY`, `PARTIAL`, `PROPOSED`, `DEFERRED`, and `CLOSED` describe work programmes.

A failed subroute does not close its parent route unless every child mechanism is covered by a valid subsumption theorem.

## Directory requirements

Every activated top route must contain:

- `README.md` — thesis, scope, subroute registry, dependencies, and gates;
- `STATUS.md` — current operational state and next decisive test;
- `CLAIMS.md` — route-local claims linked to investigation-level `NAE-###` claims;
- subroute directories for each concrete mechanism.

Every activated subroute must state:

1. exact represented object or algorithm;
2. assumptions and quantifiers;
3. correctness theorem in both directions;
4. construction, equality, transition, merge, and acceptance costs;
5. maximum and total encoded state;
6. mandatory tractable and hard controls;
7. decisive stop, defer, and promotion conditions.

## Cross-cutting controls

Every universal candidate must face:

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
- [Complete attack plan](../PLAN.md)
- [VS-08 audit](../VS-08-AUDIT.md)

Failure of one route or subroute does not imply `P!=NP`, and success on one restricted class does not imply `P=NP`.