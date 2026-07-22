# Research Plan — Monotone NAE-3SAT

## Objective

Determine whether Monotone NAE-3SAT admits a deterministic polynomial-time algorithm on every instance, or isolate a precise model-specific obstruction without overstating it as `P!=NP`.

## Strongest positive target

Construct an exact algorithm deciding every instance \(I\) in time polynomial in its binary encoding length \(L\).

By `NAE-002`, this would prove `P=NP`.

## Initial candidate mechanism

**Global-compatibility geometry:** represent local satisfying assignments, their restriction maps, and exact future-equivalence classes across a decomposition of the variable-hyperedge incidence structure.

The intended state at an interface \(S\) is not a raw partial colouring but its exact continuation behaviour:

\[
\mathcal Q_I(S)=\mathcal F_I(S)/{\equiv_{I,S}}.
\]

## What must be proved

A successful route must provide:

1. an efficiently constructible sequence or decomposition of interfaces;
2. a finite canonical representation of each relevant equivalence class;
3. exact transition rules preserving satisfiability in both directions;
4. a polynomial bound on the number and encoded size of all generated states;
5. polynomial runtime and memory in \(L\);
6. correct treatment of empty instances, isolated vertices, duplicate edges, disconnected components, and global complement symmetry.

## First attack programme

### A. Boundary controls

Prove the mechanism reduces to known polynomial algorithms on:

- rank-two hypergraphs, giving graph bipartiteness;
- acyclic incidence hypergraphs;
- bounded-treewidth or bounded-hypertree-width instances;
- affine/XOR controls where applicable.

### B. Small adversarial instances

Enumerate minimal unsatisfiable 3-uniform hypergraphs and test whether the proposed invariant detects incompatibility before full assignment enumeration.

Record the exact smallest failure when it does not.

### C. Reduction-generated instances

Use canonical reductions from 3-SAT or another verified NP-hard source. Measure:

- separator size;
- number of future-equivalence classes;
- state representation size;
- transition cost;
- whether complement symmetry provides genuine compression or only a factor of two.

### D. Cross-testbed transfer

Apply the same mechanism to Positive 1-in-3 SAT. A mechanism that works only because NAE admits complement symmetry is a restricted result, not a universal P-versus-NP route.

## Candidate claims to attack

### `NAE-004`

Exact future-equivalence classes admit a universally polynomial representation and construction.

Immediate attacks:

- construct families with many distinguishable continuations;
- compare quotient size under different variable orders and separators;
- test whether a compact symbolic representation merely postpones an NP-hard equivalence or transition query;
- test whether polynomial depth with polynomial local branching still produces an exponential global computation graph.

## Possible outcomes

1. **Universal polynomial algorithm:** proves `P=NP` after complete verification.
2. **Restricted polynomial theorem:** retain with exact structural hypotheses.
3. **Counterexample to the candidate invariant:** mark the exact claim `DISPROVED`; select a materially new mechanism or close the route.
4. **Representation-specific lower bound:** retain only for the named model; do not infer `P!=NP`.
5. **No concrete mechanism:** remain in route selection rather than accumulating speculative abstractions.

## First route-opening requirement

Before creating a route directory beyond the index, state one atomic conjecture specifying:

- the decomposition or interface family;
- the state representation;
- the exact merge/transition operation;
- the proposed global polynomial bound;
- the first adversarial family and stop condition.
