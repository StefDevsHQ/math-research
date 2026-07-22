# Complete Attack Plan — Monotone NAE-3SAT

## 1. Objective and success criterion

**Universal target:** construct a deterministic algorithm that decides every encoded Monotone NAE-3SAT instance in time and space polynomial in its binary input length \(L\).

By `NAE-002`, a complete proof would establish `P=NP`.

No weaker outcome is to be confused with that target. In particular, a heuristic, bounded-width algorithm, planar algorithm, bounded-occurrence algorithm, randomized method without derandomization, or compact representation with expensive operations is insufficient.

## 2. Current mathematical baseline

The following are already separated:

- `NAE-001`: NP-completeness — `ESTABLISHED / CHECKED`;
- `NAE-002`: universal deterministic polynomial-time solution implies `P=NP` — `PROVED / CHECKED`;
- `NAE-003`: unary/binary fixed-template Boolean CSPs reduce to 2-SAT — `PROVED / CHECKED`;
- `NAE-004`: exact extension profiles have well-defined one-variable transitions — `PROVED / CHECKED`;
- `NAE-005`: boundary width \(w\) gives a \(2^{O(w)}\operatorname{poly}(L)\) algorithm — `PROVED / CHECKED`;
- `NAE-006`: a universal polynomial symbolic representation of exact completion behaviour — `CONJECTURE / DRAFT`.

The baseline means that ordinary separator dynamic programming is understood. The research problem begins when every useful ordering has large boundary.

## 3. Primary research question

Can exact future compatibility be represented symbolically, updated exactly, and tested for acceptance in polynomial total size and time even when the raw interface contains linearly many variables?

The route must distinguish:

1. the number of semantic completion classes;
2. the size of the chosen symbolic representation;
3. the cost of constructing it;
4. the cost of equality, transition, merge, and acceptance operations;
5. the total number and encoded size of all generated representations.

A small formula that hides an NP-hard operation is not progress.

## 4. Phase A — normalize and verify the object

### A1. Canonical input model

Prove and record preprocessing for duplicate edges, isolated vertices, disconnected components, malformed triples, and componentwise complement fixing.

### A2. Hardness and tractability map

Maintain verified reductions or primary citations for:

- unrestricted Monotone NAE-3SAT hardness;
- linear 4-regular hardness;
- occurrence-at-most-three tractability;
- planar tractability;
- bounded-width tractability;
- rank-two bipartiteness.

### A3. Reduction infrastructure

Implement or formalize at least one canonical polynomial reduction from a standard NP-complete problem into the selected simple-hypergraph input convention. Audit both directions and all size bounds.

**Exit condition:** no ambiguity remains about the exact problem, encoding, or adversarial hard family.

## 5. Phase B — small-instance structural attack

### B1. Exact enumeration

Enumerate nonisomorphic 3-uniform hypergraphs in bounded size, with separate tracks for:

- general instances;
- connected instances;
- linear instances;
- regular instances;
- planar-incidence instances;
- reduction-generated instances.

For every instance compute:

- satisfiability;
- number of colourings modulo componentwise complement;
- minimum boundary width over all orders for feasible sizes;
- exact extension-profile counts for every prefix and ordering;
- minimal unsatisfiable subhypergraphs;
- automorphism group size where practical.

### B2. First adversarial controls

Include explicitly:

- the Fano plane as the standard seven-vertex non-2-colourable example;
- odd cycles viewed at rank two as the easy obstruction control;
- satisfiable high-symmetry instances;
- linear 4-regular hard-family samples;
- canonical reduction outputs.

### B3. Hypothesis generation

Search only for invariants with a finite exact statement, such as:

- closure under forced bichromatic pairs;
- signed pair relations;
- componentwise parity or cut structure;
- obstruction minors or cores;
- bounded-rank algebraic signatures;
- exact decomposition rules with a globally bounded state representation.

**Exit condition:** produce one atomic conjecture with a specified representation and transition operation, or record a negative structural finding.

## 6. Phase C — attack candidate representation families

Each family must first be proved correct on its intended domain, then attacked on hard instances.

### C1. Propagation closure

Study rules triggered when two vertices of an edge receive the same colour, forcing the third to differ. Determine whether closure can be represented as a tractable signed graph, implication system, or matroid-like object.

Attack:

- instances where no propagation starts;
- branching interactions between alternative equal pairs;
- cycles of conditional rather than unconditional implications;
- reduction gadgets preserving unresolved choice.

### C2. Algebraic encodings

Compare NAE constraints with:

- XOR equations;
- low-degree polynomial equations over finite fields;
- integer inequalities \(1\le x+y+z\le2\);
- cut and signed-graph formulations.

Required proof obligation: any relaxation or transformed system must be exact in both directions. If rounding or case splitting is needed, account for the complete branching graph.

### C3. Symbolic extension profiles

Select a concrete representation language—such as reduced decision diagrams, decomposable circuits, constraint automata, polynomial ideals, or another exact object—and define:

- canonical form or equivalence test;
- restriction and extension operations;
- conjunction/merge;
- emptiness or acceptance;
- encoded size.

Attack with lower bounds and reduction-generated instances. A lower bound remains representation-specific.

### C4. Obstruction and gluing systems

Investigate whether unsatisfiability has a complete polynomially checkable obstruction family stronger than bounded local consistency.

Attack:

- locally consistent unsatisfiable instances;
- required obstruction degree or support size;
- exponential number of candidate obstructions;
- cost of deciding whether an obstruction exists.

### C5. Decomposition beyond ordinary width

A proposed decomposition parameter is useful universally only if every instance has an efficiently constructible decomposition of polynomial total state. Prove the global bound rather than merely defining a compact-looking parameter.

**Stop condition for each family:** close it when exactness fails, operations become NP-hard, representation size is superpolynomial on a polynomial-size family, or the method collapses to a known restricted-width algorithm.

## 7. Phase D — mandatory controls

Every surviving mechanism must be tested against:

| Control | Required lesson |
|---|---|
| Graph bipartiteness | Recover the rank-two polynomial algorithm without unnecessary complexity |
| XOR-SAT | Distinguish many explicit states from compact symbolic algebra |
| Acyclic/bounded-width CSP | Recover standard exact dynamic programming |
| Planar NAE-3SAT | Respect the known tractable planar boundary |
| Occurrence-at-most-three NAE | Respect the known bounded-occurrence boundary |
| Positive 1-in-3 SAT | Determine whether complement symmetry is essential |
| 3-colouring | Compare the alternative minimal hard corner \(q=3,k=2\) |
| Linear 4-regular NAE | Survive a structurally clean NP-complete restriction |
| Canonical reduction outputs | Prevent success caused by omitting encoded logical compatibility |

## 8. Phase E — complexity audit

For every claimed algorithm record:

- input encoding and length;
- preprocessing cost;
- recursion depth;
- branching factor;
- total distinct and repeated states;
- canonicalization cost;
- transition and merge cost;
- maximum and total intermediate representation size;
- runtime and space in \(L\);
- deterministic, randomized, existential, or computational nature.

Polynomial depth with polynomial branching is not a polynomial algorithm unless the entire computation graph is polynomially bounded or memoized into polynomially many polynomial-size states.

## 9. Computational programme

Experiments may discover counterexamples or formulate conjectures but do not prove universality without exhaustiveness.

Each experiment record must contain:

- exact claim tested;
- generation domain and isomorphism handling;
- solver and algorithm;
- reproducible command and environment;
- raw result and summarized finding;
- finite-domain limitation.

Initial implementation targets:

1. exact brute-force verifier;
2. hypergraph normalizer and component splitter;
3. boundary-width dynamic programme;
4. exact extension-profile calculator for small instances;
5. nonisomorphic small-instance generator;
6. reduction-generated benchmark set;
7. candidate-invariant falsification harness.

## 10. Decision gates

### Gate 1 — object readiness

Passed when definitions, sources, tractable boundaries, and hard controls are verified.

### Gate 2 — route activation

Requires one atomic conjecture specifying:

- representation language;
- decomposition or processing order;
- exact operations;
- proposed universal polynomial bound;
- correctness theorem target;
- first hard family;
- stop condition.

### Gate 3 — continuation

Continue only if the candidate survives small counterexamples, tractable controls, and reduction-generated instances without hidden exponential work.

### Gate 4 — promotion

A universal algorithm may be promoted only after a complete proof, independent break attempt, encoding audit, and verification that all generated state is polynomial.

## 11. Possible outcomes

1. **Universal deterministic polynomial algorithm:** after verification, proves `P=NP`.
2. **Restricted polynomial theorem:** retain with exact hypotheses and no universal claim.
3. **Counterexample:** mark the exact conjecture `DISPROVED` with a complete instance.
4. **Representation lower bound:** retain only for that model.
5. **Mechanism failure without complete counterexample:** mark `RETRACTED`, not `DISPROVED`.
6. **No materially new mechanism:** close the route and return to project-level route selection.

## 12. Immediate first attack

The first active task is not to assume `NAE-006`. It is to determine the smallest exact information needed beyond boundary assignments.

Proceed in this order:

1. build the small-instance extension-profile harness;
2. compute the first examples where raw boundary states merge semantically;
3. compute the first examples where every natural pairwise or affine summary merges states unsoundly;
4. isolate the minimal missing compatibility relation;
5. state the first route conjecture around that relation;
6. attack it immediately on the Fano plane, linear 4-regular samples, and reduction-generated instances.
