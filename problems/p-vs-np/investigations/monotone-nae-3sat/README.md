# Monotone NAE-3SAT Investigation

Monotone NAE-3SAT asks whether a 3-uniform hypergraph can be coloured with two colours so that no hyperedge is monochromatic.

The relation is

\[
R_{\mathrm{NAE}}=\{0,1\}^{3}\setminus\{000,111\}.
\]

It is the symmetry-first Boolean CSP testbed: one ternary relation, no negations, no constants, no weights, and global complement symmetry.

## Why this object

It sits on the minimal non-monochromatic frontier:

- graph bipartiteness: two colours, pairwise edges — polynomial time;
- Monotone NAE-3SAT: two colours, triple edges — NP-complete;
- graph 3-colouring: three colours, pairwise edges — NP-complete.

A deterministic polynomial-time algorithm correct on every encoded Monotone NAE-3SAT instance would prove `P=NP`. A heuristic, restricted-class result, bounded-width algorithm, or compact syntax with expensive operations would not.

## Current phase

`VS-01`, the canonical executable instance layer, is complete. It supplies strict versioned parsing, canonical serialization, stable labelled identifiers, component and relabelling operations, witness verification, fixtures, tests, and a command-line validator.

The next task is `VS-02`: build the exact small-instance oracle and record the first exhaustively justified labelled domain. No universal proof route is active.

## Accepted baseline

- NP-completeness — `ESTABLISHED / CHECKED`;
- universal deterministic polynomial solution implies `P=NP` — `PROVED / CHECKED`;
- Boolean unary/binary arity-minimality lemma — `PROVED / CHECKED`;
- exact quotient-transition theorem — `PROVED / CHECKED`;
- `2^{O(w)} poly(L)` bounded-boundary algorithm — `PROVED / CHECKED`;
- canonical executable instance model — `COMPLETE` infrastructure slice.

## Mandatory controls

Graph 2-colouring, XOR-SAT, acyclic and bounded-width CSPs, planar and occurrence-at-most-three NAE instances, Positive 1-in-3 SAT, graph 3-colouring, linear 4-regular Monotone NAE-3SAT, and verified reduction-generated instances.

## Navigation

- [Current status](STATUS.md)
- [Vertical slices and progress](VERTICAL-SLICES.md)
- [VS-01 implementation specification](VS-01-IMPLEMENTATION.md)
- [VS-01 completion audit](VS-01-AUDIT.md)
- [Claim ledger](CLAIMS.md)
- [Object specification and baseline proofs](OBJECT.md)
- [Complete attack plan](PLAN.md)
- [Primary sources](references/SOURCES.md)
- [Routes](routes/README.md)
- [P versus NP overview](../../README.md)
- [Problem-testbed landscape](../../references/problem-testbed-landscape.md)
- [Research standards](../../../../RESEARCH_STANDARDS.md)

Investigation-wide claims use `NAE-###`. Route-local claims must link to the claim ledger when they change accepted state.
