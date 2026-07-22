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

The first three building blocks are complete and checked:

- `VS-01`: canonical executable instance model;
- `VS-02`: exact finite satisfiability oracle;
- `VS-03`: exact extension-profile engine.

The laboratory can now represent instances unambiguously, determine exact finite ground truth, and compute exact semantic future-equivalence for every prefix of a fixed ordering.

The next work is `VS-04` control calibration and `VS-05` minimal obstruction atlas construction. No universal polynomial-time mechanism is currently claimed.

## Accepted baseline

- NP-completeness — `ESTABLISHED / CHECKED`;
- universal deterministic polynomial solution implies `P=NP` — `PROVED / CHECKED`;
- Boolean unary/binary arity-minimality lemma — `PROVED / CHECKED`;
- exact quotient-transition theorem — `PROVED / CHECKED`;
- `2^{O(w)} poly(L)` bounded-boundary algorithm — `PROVED / CHECKED`;
- exact bottom-up completion-mask construction — `PROVED / CHECKED`;
- canonical instance, exact oracle, and exact profile layers — `COMPLETE / CHECKED`.

## Retained finite evidence

- all `1045` labelled 3-uniform hypergraphs through five vertices are classified exactly;
- exactly one is unsatisfiable, the complete 3-uniform hypergraph on five vertices;
- the Fano plane is independently verified unsatisfiable and edge-minimal unsatisfiable;
- all `123280` instance-ordering profiles through five vertices are measured exactly;
- the finite profile census contains `2153049` exact classes from `7753542` raw prefixes;
- the largest quotient observed in that domain has `8` classes.

These are exhaustive finite results, not asymptotic polynomial bounds.

## Mandatory controls

Graph 2-colouring, XOR-SAT, acyclic and bounded-width CSPs, planar and occurrence-at-most-three NAE instances, Positive 1-in-3 SAT, graph 3-colouring, linear 4-regular Monotone NAE-3SAT, and verified reduction-generated instances.

## Navigation

- [Current status](STATUS.md)
- [Vertical slices and progress](VERTICAL-SLICES.md)
- [Building-block quality gate](BUILDING-BLOCK-GATE.md)
- [VS-01 implementation specification](VS-01-IMPLEMENTATION.md)
- [VS-01 completion audit](VS-01-AUDIT.md)
- [VS-02 implementation specification](VS-02-IMPLEMENTATION.md)
- [VS-02 completion audit](VS-02-AUDIT.md)
- [VS-03 implementation specification](VS-03-IMPLEMENTATION.md)
- [VS-03 proof and completion audit](VS-03-AUDIT.md)
- [Claim ledger](CLAIMS.md)
- [Object specification and baseline proofs](OBJECT.md)
- [Complete attack plan](PLAN.md)
- [Primary sources](references/SOURCES.md)
- [Routes](routes/README.md)
- [P versus NP overview](../../README.md)
- [Problem-testbed landscape](../../references/problem-testbed-landscape.md)
- [Research standards](../../../../RESEARCH_STANDARDS.md)

Investigation-wide claims use `NAE-###`. Route-local claims must link to the claim ledger when they change accepted state.
