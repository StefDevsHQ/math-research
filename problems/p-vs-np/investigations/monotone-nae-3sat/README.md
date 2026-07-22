# Monotone NAE-3SAT Investigation

Monotone NAE-3SAT is the symmetry-first Boolean CSP testbed in the P versus NP programme.

An instance consists of a finite variable set \(V\) and a family \(E\subseteq \binom{V}{3}\) of triples. The question is whether there exists an assignment

\[
\sigma:V\to\{0,1\}
\]

such that every triple contains both values. Equivalently, the associated 3-uniform hypergraph must admit a 2-colouring with no monochromatic hyperedge.

The allowed relation is

\[
R_{\mathrm{NAE}}=\{0,1\}^{3}\setminus\{000,111\}.
\]

## Why this object

Monotone NAE-3SAT has one Boolean domain, one ternary relation, no negations, no constants, no weights, and full complement symmetry. It removes exact-cardinality syntax while retaining NP-completeness. It is therefore a clean test of whether the central obstruction is global compatibility rather than arithmetic exactness.

It is paired with Positive 1-in-3 SAT:

- Positive 1-in-3 SAT is the exactness-first testbed;
- Monotone NAE-3SAT is the symmetry-first testbed.

## Current phase

The investigation is active in **formalization and route selection**.

No polynomial-time mechanism is claimed. The immediate task is to identify and attack one exact global-compatibility invariant that:

1. is computable without enumerating exponentially many partial colourings;
2. is complete for satisfiability, not merely a local obstruction;
3. survives reduction-generated hard instances;
4. has a complete polynomial bound on time, memory, and encoded intermediate state.

## Consequence theorem

Because Monotone NAE-3SAT is NP-complete, a deterministic polynomial-time algorithm correct on every encoded instance would prove `P=NP`.

This implication does not follow from a heuristic, restricted subclass, bounded-width algorithm, randomized algorithm without derandomization, or compact description whose construction or evaluation is exponential.

## Mandatory controls

- graph 2-colouring — rank-two tractable neighbour;
- XOR-SAT — affine tractable neighbour;
- bounded-width and acyclic CSPs — structural tractable neighbours;
- Positive 1-in-3 SAT — exactness-first hard control;
- 3-SAT — reduction-central adversarial control;
- restricted hard Monotone NAE-3SAT families — robustness controls.

## Navigation

- [Current status](STATUS.md)
- [Claim ledger](CLAIMS.md)
- [Object specification](OBJECT.md)
- [Research plan](PLAN.md)
- [Routes](routes/README.md)
- [P versus NP overview](../../README.md)
- [Problem-testbed landscape](../../references/problem-testbed-landscape.md)
- [Research standards](../../../../RESEARCH_STANDARDS.md)

## Identifier policy

Investigation-wide claims use `NAE-###`. Route-local claims must link to this ledger when they change accepted investigation state.
