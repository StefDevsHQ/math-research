# Claim Ledger — Monotone NAE-3SAT Investigation

This is the authoritative investigation-level ledger for Monotone NAE-3SAT claims.

## Claims

| ID | Statement | Status | Review | Evidence | Updated |
|---|---|---|---|---|---|
| `NAE-001` | Monotone NAE-3SAT is NP-complete. | `ESTABLISHED` | `CHECKED` | [Schaefer and restricted-hardness sources](references/SOURCES.md) | 2026-07-22 |
| `NAE-002` | A deterministic polynomial-time algorithm deciding every Monotone NAE-3SAT instance would prove `P=NP`. | `PROVED` | `CHECKED` | Membership in `NP`, `NAE-001`, and polynomial-time many-one completeness | 2026-07-22 |
| `NAE-003` | Every fixed-template Boolean CSP using only unary and binary relations is polynomial-time reducible to 2-SAT. | `PROVED` | `CHECKED` | [Arity-minimality proof](OBJECT.md#arity-minimality) | 2026-07-22 |
| `NAE-004` | For a fixed variable ordering, exact extension equivalence is a congruence under appending the next colour; explicit polynomial construction of all quotient states and transitions would decide Monotone NAE-3SAT in polynomial time. | `PROVED` | `CHECKED` | [Exact quotient transition theorem](OBJECT.md#claim-nae-004--exact-quotient-transition-theorem) | 2026-07-22 |
| `NAE-005` | Given a variable ordering of maximum processed boundary width `w`, Monotone NAE-3SAT is decidable in `2^{O(w)} poly(L)` time and space. | `PROVED` | `CHECKED` | [Bounded-boundary dynamic programme](OBJECT.md#claim-nae-005--bounded-boundary-algorithm) | 2026-07-22 |
| `NAE-006` | Every Monotone NAE-3SAT instance admits a polynomial-size, polynomial-time constructible symbolic representation of exact completion behaviour with polynomial-time exact transitions and acceptance. | `CONJECTURE` | `DRAFT` | [Attack plan](PLAN.md) | 2026-07-22 |
| `NAE-007` | For every fixed labelled instance and ordering, the bottom-up completion-mask construction computes the exact completion set of every prefix; equality of masks is exact extension equivalence, mask slicing gives well-defined colour transitions, and root acceptance equals satisfiability. | `PROVED` | `CHECKED` | [VS-03 proof and implementation audit](VS-03-AUDIT.md) | 2026-07-22 |
| `NAE-008` | Every finite 3-uniform hypergraph whose incidence graph is a forest is two-colourable, and a valid colouring is constructible in linear incidence-graph time. | `PROVED` | `CHECKED` | [VS-04 incidence-forest proof and audit](VS-04-AUDIT.md#incidence-forest-theorem) | 2026-07-22 |
| `NAE-009` | For an unsatisfiable hypergraph, satisfiability of every single-edge deletion is equivalent to satisfiability of every proper edge-subhypergraph; satisfiability of every single-vertex induced deletion is equivalent to satisfiability of every proper induced vertex subhypergraph. | `PROVED` | `DRAFT` | [VS-05 specification](VS-05-IMPLEMENTATION.md#single-deletion-sufficiency) | 2026-07-22 |
| `NAE-010` | In the complete labelled domain through five vertices, the unique unsatisfiable, edge-minimal-unsatisfiable, and vertex-minimal-unsatisfiable instance is `K_5^(3)`. | `COMPUTATIONAL` | `DRAFT` | VS-05 exhaustive census and independent reference gate | 2026-07-22 |

## Current accepted state

The investigation has:

- an established NP-complete target;
- a checked consequence theorem linking a universal deterministic polynomial algorithm to `P=NP`;
- a proved arity-minimality lemma;
- a proved exact semantic transition theorem;
- a proved bounded-interface dynamic programme;
- a checked executable exact-profile construction for fixed instances and orderings;
- a proved linear-time constructive theorem for incidence-forest instances;
- checked graph-parity, affine-XOR, bounded-boundary, and component-factorization controls;
- an active exact atlas separating dense and sparse minimal obstructions.

`NAE-006` is the unresolved universal proposal. It is deliberately stronger than a claim that raw quotient classes are few: a compact symbolic representation may encode many semantic classes, as linear algebra does for XOR-SAT. It must therefore state its representation language and operations before it can become a route-level conjecture.

`NAE-007` establishes correctness of the explicit exponential laboratory. It does not establish a polynomial bound on the quotient, construction, representation, or complete computation graph.

`NAE-008` is a restricted acyclic theorem. Its proof relies on the absence of a second compatibility path in the incidence graph and does not extend to cyclic instances merely because they are sparse, planar, linear, or low occurrence.

`NAE-009` is a monotonicity lemma. It justifies complete single-deletion certificates but does not make finding or recognizing obstructions efficient.

`NAE-010` is finite computation over an exhaustive declared domain. It does not classify six-vertex or larger critical hypergraphs.

## Claim boundaries

- Polynomial time means polynomial in complete binary encoding length.
- Restricted subclasses do not establish `NAE-002`'s premise.
- Randomized bounded-error algorithms do not establish deterministic `P=NP` without an explicit derandomization theorem.
- Polynomial recursion depth or local branching does not bound the complete computation graph.
- A compact syntax is insufficient unless construction, transition, equivalence, acceptance, and total generated representation are polynomially bounded.
- A lower bound for one representation model is model-specific unless a polynomial-overhead subsumption theorem is proved.
- Finite exact-profile, control, and obstruction measurements do not imply asymptotic quotient bounds.
- Planarity and occurrence-at-most-three tractability remain imported results, not project-original proofs.
- Named Fano evidence is not an exhaustive seven-vertex census.

## Identifier policy

Use stable identifiers of the form `NAE-###`. Never reuse an identifier after retraction or replacement.
