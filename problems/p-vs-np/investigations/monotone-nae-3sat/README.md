# Monotone NAE-3SAT Investigation

Monotone NAE-3SAT asks whether a 3-uniform hypergraph can be coloured with two colours so that no hyperedge is monochromatic:

\[
R_{\mathrm{NAE}}=\{0,1\}^{3}\setminus\{000,111\}.
\]

It is the symmetry-first Boolean CSP testbed: one ternary relation, no negations, no constants, no weights, and global complement symmetry.

## Current phase

`VS-01` through `VS-06` are `COMPLETE / CHECKED`:

- canonical executable instances;
- exact finite satisfiability;
- exact fixed-order completion profiles;
- tractable-control calibration;
- minimal-obstruction evidence;
- exact failures of explicitly defined naive summaries.

`VS-07` is ready. It will measure genuine live semantic merging separately from dead-state collapse, complement symmetry, boundary states, quotient count, representation size, and ordering effects.

No universal polynomial-time mechanism is claimed.

## Accepted baseline

- NP-completeness — `ESTABLISHED / CHECKED`;
- universal deterministic polynomial solution implies `P=NP` — `PROVED / CHECKED`;
- exact quotient transitions — `PROVED / CHECKED`;
- `2^{O(w)} poly(L)` bounded-boundary algorithm — `PROVED / CHECKED`;
- exact completion-mask construction — `PROVED / CHECKED`;
- incidence-forest constructive colouring — `PROVED / CHECKED`;
- single-deletion sufficiency — `PROVED / CHECKED`;
- globally unsatisfiable instances have one dead successful-completion class at every level — `PROVED / CHECKED`;
- every fixed locality radius admits equal-local-view/opposite-residual-satisfiability instances — `PROVED / CHECKED`;
- ten explicit naive summaries have checked collisions — `COMPUTATIONAL / CHECKED`.

## VS-06 result

The following summaries fail to determine exact semantics:

- degree sequence;
- edge-intersection multiset;
- pair-codegree multiset;
- parity data;
- second moments;
- incidence-Gram spectrum;
- root generalized arc consistency;
- satisfiability of every proper induced subinstance;
- boundary Hamming weight;
- boundary Hamming parity.

The exact boundary assignment remains correct but can expose exponentially many states. These failures are summary-specific and do not lower-bound arbitrary algorithms or representations.

## Mandatory controls

Graph 2-colouring, XOR-SAT, acyclic and bounded-width CSPs, planar and occurrence-at-most-three NAE instances, Positive 1-in-3 SAT, graph 3-colouring, linear 4-regular Monotone NAE-3SAT, and verified reduction-generated instances.

## Navigation

- [Current status](STATUS.md)
- [Vertical slices](VERTICAL-SLICES.md)
- [Phase I closeout](VS-01-05-PHASE-AUDIT.md)
- [VS-06 implementation](VS-06-IMPLEMENTATION.md)
- [VS-06 completion audit](VS-06-AUDIT.md)
- [Claim ledger](CLAIMS.md)
- [Object specification](OBJECT.md)
- [Attack plan](PLAN.md)
- [Primary sources](references/SOURCES.md)
- [P versus NP overview](../../README.md)

Investigation-wide claims use `NAE-###`. Route-local claims must link upward when they change accepted state.
