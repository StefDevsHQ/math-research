# Monotone NAE-3SAT Investigation

Monotone NAE-3SAT is the symmetry-first Boolean CSP testbed in the P versus NP programme.

An instance is a 3-uniform hypergraph. The question is whether its vertices can be coloured with two colours so that no hyperedge is monochromatic.

The allowed relation is

\[
R_{\mathrm{NAE}}=\{0,1\}^{3}\setminus\{000,111\}.
\]

## Why this object

Monotone NAE-3SAT has one Boolean domain, one ternary relation, no negations, no constants, no weights, and full complement symmetry. It removes exact-cardinality syntax while retaining NP-completeness.

It sits on the minimal non-monochromatic frontier:

- graph bipartiteness: two colours and pairwise edges — polynomial time;
- Monotone NAE-3SAT: two colours and triple edges — NP-complete;
- graph 3-colouring: three colours and pairwise edges — NP-complete.

Positive 1-in-3 SAT remains the exactness-first sibling; Monotone NAE-3SAT is the symmetry-first testbed.

## Current phase

Formalization is complete. No universal proof route is active.

The investigation has established the exact semantic extension-profile object and the standard bounded-boundary dynamic programme. The next work begins where ordinary interface width becomes large: finding or refuting a stronger polynomial symbolic representation of global compatibility.

## Consequence theorem

Because Monotone NAE-3SAT is NP-complete, a deterministic polynomial-time algorithm correct on every encoded instance would prove `P=NP`.

A heuristic, restricted-subclass result, bounded-width algorithm, randomized algorithm without derandomization, or compact syntax with expensive operations does not meet this condition.

## Accepted baseline

- NP-completeness — `ESTABLISHED / CHECKED`;
- universal deterministic polynomial solution implies `P=NP` — `PROVED / CHECKED`;
- unary/binary Boolean CSP arity-minimality lemma — `PROVED / CHECKED`;
- exact quotient transition theorem — `PROVED / CHECKED`;
- `2^{O(w)} poly(L)` bounded-boundary algorithm — `PROVED / CHECKED`.

## Mandatory controls

- graph 2-colouring;
- XOR-SAT;
- acyclic and bounded-width CSPs;
- planar and occurrence-at-most-three NAE instances;
- Positive 1-in-3 SAT;
- graph 3-colouring;
- linear 4-regular Monotone NAE-3SAT;
- canonical reduction-generated instances.

## Navigation

- [Current status](STATUS.md)
- [Claim ledger](CLAIMS.md)
- [Object specification and baseline proofs](OBJECT.md)
- [Complete attack plan](PLAN.md)
- [Primary sources](references/SOURCES.md)
- [Routes](routes/README.md)
- [P versus NP overview](../../README.md)
- [Problem-testbed landscape](../../references/problem-testbed-landscape.md)
- [Research standards](../../../../RESEARCH_STANDARDS.md)

## Identifier policy

Investigation-wide claims use `NAE-###`. Route-local claims must link to this ledger when they change accepted investigation state.
