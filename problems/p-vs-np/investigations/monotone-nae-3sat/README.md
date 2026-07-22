# Monotone NAE-3SAT Investigation

Monotone NAE-3SAT asks whether a 3-uniform hypergraph can be coloured with two colours so that no hyperedge is monochromatic:

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

Phase I, `VS-01` through `VS-05`, is `COMPLETE / CHECKED`:

- `VS-01`: canonical executable instance model;
- `VS-02`: exact finite satisfiability oracle;
- `VS-03`: exact extension-profile engine;
- `VS-04`: tractable-control calibration;
- `VS-05`: exact minimal-obstruction atlas.

The laboratory can represent instances unambiguously, determine exact finite ground truth, compute exact successful-completion equivalence, distinguish several known tractable mechanisms, and preserve dense and sparse minimal obstruction evidence.

The next work is `VS-06`: formalize and destroy naive summaries through exact same-summary/different-semantics collisions. No universal polynomial-time mechanism is currently claimed.

## Accepted baseline

- NP-completeness — `ESTABLISHED / CHECKED`;
- universal deterministic polynomial solution implies `P=NP` — `PROVED / CHECKED`;
- Boolean unary/binary arity-minimality lemma — `PROVED / CHECKED`;
- exact quotient-transition theorem — `PROVED / CHECKED`;
- `2^{O(w)} poly(L)` bounded-boundary algorithm — `PROVED / CHECKED`;
- exact bottom-up completion-mask construction — `PROVED / CHECKED`;
- incidence-forest constructive colouring theorem — `PROVED / CHECKED`;
- single-deletion sufficiency for edge and induced-vertex minimality — `PROVED / CHECKED`;
- globally unsatisfiable instances have one dead successful-completion class at every level — `PROVED / CHECKED`;
- canonical instance, exact oracle, exact profile, control-calibration, and obstruction-atlas layers — `COMPLETE / CHECKED`.

## Retained finite evidence

- all `1045` labelled 3-uniform hypergraphs through five vertices are classified exactly;
- exactly one is unsatisfiable, `K_5^(3)`;
- the Fano plane is independently verified unsatisfiable and edge-minimal unsatisfiable;
- all `123280` instance-ordering profiles through five vertices are measured exactly;
- the profile census contains `2153049` exact classes from `7753542` raw prefixes;
- all `1100` labelled graphs through five vertices are calibrated exactly;
- all `16453` canonical XOR systems through three variables are calibrated exactly;
- all `36` incidence-forest NAE instances through five vertices are constructively colourable;
- all `344` occurrence-at-most-three instances in that finite NAE domain are satisfiable;
- all `120` orderings of `K_5^(3)` and `5040` orderings of the Fano plane are represented in the obstruction atlas aggregates.

These are exhaustive finite results on declared domains, not asymptotic polynomial bounds.

## Mandatory controls

Graph 2-colouring, XOR-SAT, acyclic and bounded-width CSPs, planar and occurrence-at-most-three NAE instances, Positive 1-in-3 SAT, graph 3-colouring, linear 4-regular Monotone NAE-3SAT, and verified reduction-generated instances.

VS-04 calibrates the tractable mechanisms already implemented. Planar and bounded-occurrence tractability remain imported primary-source results. Hard-corner and reduction-generated controls remain for later slices.

## Navigation

- [Current status](STATUS.md)
- [Vertical slices and progress](VERTICAL-SLICES.md)
- [Phase I closeout audit](VS-01-05-PHASE-AUDIT.md)
- [Building-block quality gate](BUILDING-BLOCK-GATE.md)
- [VS-01 implementation specification](VS-01-IMPLEMENTATION.md)
- [VS-01 completion audit](VS-01-AUDIT.md)
- [VS-02 implementation specification](VS-02-IMPLEMENTATION.md)
- [VS-02 completion audit](VS-02-AUDIT.md)
- [VS-03 implementation specification](VS-03-IMPLEMENTATION.md)
- [VS-03 proof and completion audit](VS-03-AUDIT.md)
- [VS-04 implementation specification](VS-04-IMPLEMENTATION.md)
- [VS-04 proof and completion audit](VS-04-AUDIT.md)
- [VS-05 implementation specification](VS-05-IMPLEMENTATION.md)
- [VS-05 proof and completion audit](VS-05-AUDIT.md)
- [Claim ledger](CLAIMS.md)
- [Object specification and baseline proofs](OBJECT.md)
- [Complete attack plan](PLAN.md)
- [Primary sources](references/SOURCES.md)
- [Routes](routes/README.md)
- [P versus NP overview](../../README.md)
- [Problem-testbed landscape](../../references/problem-testbed-landscape.md)
- [Research standards](../../../../RESEARCH_STANDARDS.md)

Investigation-wide claims use `NAE-###`. Route-local claims must link to the claim ledger when they change accepted state.
