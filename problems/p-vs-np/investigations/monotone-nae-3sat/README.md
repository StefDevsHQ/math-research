# Monotone NAE-3SAT Investigation

Monotone NAE-3SAT asks whether a 3-uniform hypergraph can be coloured with two colours so that no hyperedge is monochromatic:

\[
R_{\mathrm{NAE}}=\{0,1\}^{3}\setminus\{000,111\}.
\]

It is the symmetry-first Boolean CSP testbed: one ternary relation, no negations, no constants, no weights, and global complement symmetry.

## Current phase

`VS-01` through `VS-08` are `COMPLETE / CHECKED`.

The investigation now has:

- canonical executable instances;
- exact finite satisfiability and exact extension profiles;
- tractable controls and bounded-boundary algorithms;
- obstruction, locality-failure and summary-collision records;
- exact measurements of live semantic merging and ordering effects;
- an exact oriented PCRNF residual language and transition system;
- a checked counterexample to PCRNF byte equality as complete semantic equality.

The Monotone NAE-3SAT programme remains open.

`NAE-016` is `CONJECTURE / CHECKED`. VS-08 disproved one proposed merge mechanism but did not refute the existential polynomial-state claim.

`VS-09` is `PARTIAL / READY` and must proceed through a clearly selected route or subroute.

No universal polynomial-time mechanism or general representation lower bound is claimed.

## Current route selection

The active top-level family is:

- [`R1 — Exact-state representations`](routes/exact-state-representations/README.md).

Its current branches are:

- [`R1.1 — PCRNF`](routes/exact-state-representations/pcrnf/README.md): exact substrate retained; byte equality incomplete; `NAE-016` open;
- [`R1.2 — Semantic quotient over PCRNF`](routes/exact-state-representations/semantic-quotient/README.md): recommended next subroute;
- [`R1.3 — Decision diagrams`](routes/exact-state-representations/decision-diagrams/README.md): registered candidate;
- [`R1.4 — Decomposable circuits`](routes/exact-state-representations/decomposable-circuits/README.md): registered candidate.

Other top-level route families remain registered separately rather than being mixed into R1:

- decomposition and ordering;
- algebraic encodings;
- obstruction and gluing;
- propagation and exact branching;
- representation-specific barriers.

See the [route registry](routes/README.md) and [route dashboard](routes/STATUS.md).

## Accepted baseline

- NP-completeness — `ESTABLISHED / CHECKED`;
- universal deterministic polynomial solution implies `P=NP` — `PROVED / CHECKED`;
- exact quotient transitions — `PROVED / CHECKED`;
- `2^{O(w)} poly(L)` bounded-boundary algorithm — `PROVED / CHECKED`;
- exact completion-mask construction — `PROVED / CHECKED`;
- incidence-forest constructive colouring — `PROVED / CHECKED`;
- globally unsatisfiable instances have one dead successful-completion class at every level — `PROVED / CHECKED`;
- every fixed locality radius can miss conditioned residual satisfiability — `PROVED / CHECKED`;
- ten explicit naive summaries have checked collisions — `COMPUTATIONAL / CHECKED`;
- the fan family has exponential live exact-state growth under one order and a constant-width alternative — `PROVED / CHECKED`;
- genuine all-live exact merging occurs beyond component-complement prefix orbits — `COMPUTATIONAL / CHECKED`;
- oriented PCRNF residualization and transitions are exact — `NAE-017, PROVED / CHECKED`;
- PCRNF byte equality is not exact semantic equivalence — `NAE-018, DISPROVED / CHECKED`.

## Mandatory controls

Graph 2-colouring, XOR-SAT, acyclic and bounded-width CSPs, planar and occurrence-at-most-three NAE instances, Positive 1-in-3 SAT, graph 3-colouring, linear four-regular Monotone NAE-3SAT, Fano, `K_5^(3)`, both fan orderings, the VS-06 collision atlas, the VS-08 five-vertex witness, and verified reduction-generated instances.

## Navigation

### Operational

- [Current investigation status](STATUS.md)
- [Route registry](routes/README.md)
- [Route dashboard](routes/STATUS.md)
- [Vertical slices](VERTICAL-SLICES.md)
- [Claim ledger](CLAIMS.md)
- [Attack plan](PLAN.md)

### Completed slices

- [Phase I closeout](VS-01-05-PHASE-AUDIT.md)
- [VS-06 implementation](VS-06-IMPLEMENTATION.md)
- [VS-06 audit](VS-06-AUDIT.md)
- [VS-07 implementation](VS-07-IMPLEMENTATION.md)
- [VS-07 audit](VS-07-AUDIT.md)
- [VS-08 preparation](VS-08-PREPARATION.md)
- [VS-08 implementation](VS-08-IMPLEMENTATION.md)
- [VS-08 completion and status-correction audit](VS-08-AUDIT.md)

### Foundations

- [Object specification](OBJECT.md)
- [Primary sources](references/SOURCES.md)
- [P versus NP overview](../../README.md)

Investigation-wide claims use `NAE-###`. Route-local claims must link upward when they change accepted state.