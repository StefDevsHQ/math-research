# Monotone NAE-3SAT Investigation

Monotone NAE-3SAT asks whether a 3-uniform hypergraph can be coloured with two colours so that no hyperedge is monochromatic:

\[
R_{\mathrm{NAE}}=\{0,1\}^{3}\setminus\{000,111\}.
\]

It is the symmetry-first Boolean CSP testbed: one ternary relation, no negations, no constants, no weights, and global complement symmetry.

## Current phase

`VS-01` through `VS-07` are `COMPLETE / CHECKED`:

- canonical executable instances;
- exact finite satisfiability;
- exact fixed-order completion profiles;
- tractable-control calibration;
- minimal-obstruction evidence;
- exact failures of explicitly defined naive summaries;
- exact measurement of live semantic merging, symmetry, boundary state, encoding size, and ordering effects.

`VS-08` is ready. It must select one concrete residual representation language and specify exact construction, equality, transitions, merge, acceptance, encoded size, proposed global bound, controls, and stop condition.

No universal polynomial-time mechanism or representation lower bound is claimed.

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
- ten explicit naive summaries have checked collisions — `COMPUTATIONAL / CHECKED`;
- the fan family has exponential live exact-state growth under one order and a constant-width alternative order — `PROVED / CHECKED`;
- genuine all-live exact merging beyond component-complement prefix orbits occurs through four vertices — `COMPUTATIONAL / CHECKED`.

## VS-07 result

VS-07 separates raw prefixes, dead collapse, complement symmetry, exact live classes, semantic symmetry orbits, boundary states, reference encoding sizes, and ordering effects.

The first recorded all-live genuine merge is the four-vertex instance with edges `{012,013}`, ordering `(0,2,3,1)`, and level three. Its eight prefixes form three exact live classes even though they occupy four prefix complement orbits.

For the fan family `F_k` with edges `{c,a_i,b_i}`:

- order `c,a_1,...,a_k,b_1,...,b_k` has `2^(k+1)-1` live exact classes at level `k+1`;
- the reduction from raw prefixes is essentially only global complement symmetry;
- order `c,a_1,b_1,...,a_k,b_k` has boundary width at most two and at most four live exact classes.

Thus exact future equivalence can merge distinct boundary assignments, but a large quotient under one ordering can disappear under another. Exact class count is not the same as symbolic representation size.

## Mandatory controls

Graph 2-colouring, XOR-SAT, acyclic and bounded-width CSPs, planar and occurrence-at-most-three NAE instances, Positive 1-in-3 SAT, graph 3-colouring, linear 4-regular Monotone NAE-3SAT, and verified reduction-generated instances.

## Navigation

- [Current status](STATUS.md)
- [Vertical slices](VERTICAL-SLICES.md)
- [Phase I closeout](VS-01-05-PHASE-AUDIT.md)
- [VS-06 implementation](VS-06-IMPLEMENTATION.md)
- [VS-06 completion audit](VS-06-AUDIT.md)
- [VS-07 implementation](VS-07-IMPLEMENTATION.md)
- [VS-07 completion audit](VS-07-AUDIT.md)
- [Claim ledger](CLAIMS.md)
- [Object specification](OBJECT.md)
- [Attack plan](PLAN.md)
- [Primary sources](references/SOURCES.md)
- [P versus NP overview](../../README.md)

Investigation-wide claims use `NAE-###`. Route-local claims must link upward when they change accepted state.
