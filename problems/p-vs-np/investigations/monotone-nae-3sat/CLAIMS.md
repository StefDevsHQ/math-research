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
| `NAE-009` | For an unsatisfiable hypergraph, satisfiability of every single-edge deletion is equivalent to satisfiability of every proper edge-subhypergraph; satisfiability of every single-vertex induced deletion is equivalent to satisfiability of every proper induced vertex subhypergraph. | `PROVED` | `CHECKED` | [VS-05 proof and audit](VS-05-AUDIT.md#single-deletion-sufficiency--nae-009) | 2026-07-22 |
| `NAE-010` | In the complete labelled domain through five vertices, the unique unsatisfiable, edge-minimal-unsatisfiable, and vertex-minimal-unsatisfiable instance is `K_5^(3)`. | `COMPUTATIONAL` | `CHECKED` | [VS-05 exhaustive census](VS-05-AUDIT.md#exhaustive-small-domain--nae-010) | 2026-07-22 |
| `NAE-011` | For every unsatisfiable Monotone NAE-3SAT instance and every variable ordering, every prefix has the empty set of satisfying full completions; consequently the exact successful-completion quotient has exactly one dead equivalence class at every level. | `PROVED` | `CHECKED` | [VS-05 all-ordering profile theorem](VS-05-AUDIT.md#exact-all-ordering-profile-evidence) | 2026-07-22 |
| `NAE-012` | For every fixed radius `r>=1`, there are two conditioned Monotone NAE-3SAT residuals whose underlying binary inequality graphs have identical multisets of rooted radius-`r` neighbourhoods but whose residual satisfiability differs. | `PROVED` | `CHECKED` | [VS-06 bounded-radius construction](VS-06-AUDIT.md#bounded-radius-theorem--nae-012) | 2026-07-22 |
| `NAE-013` | The explicit degree, intersection, pair-codegree, parity, second-moment, incidence-Gram-spectrum, root-GAC, proper-induced-satisfiability, boundary-weight, and boundary-parity summaries in VS-06 each admit a checked same-summary/different-semantics collision. | `COMPUTATIONAL` | `CHECKED` | [VS-06 collision atlas](VS-06-AUDIT.md#explicit-collision-audit) | 2026-07-22 |
| `NAE-014` | For the fan hypergraph `F_k` with edges `{c,a_i,b_i}`, the ordering `c,a_1,...,a_k,b_1,...,b_k` has `2^(k+1)-1` live exact completion classes at level `k+1`, while the interleaved ordering `c,a_1,b_1,...,a_k,b_k` has processed boundary width at most two and therefore at most four live exact classes at every level. | `PROVED` | `CHECKED` | [VS-07 fan ordering-separation theorem](VS-07-AUDIT.md#claim-nae-014--fan-ordering-separation-theorem) | 2026-07-22 |
| `NAE-015` | In the exhaustive domain of all labelled instances and all orderings through four vertices, genuine all-live exact merging beyond component-complement prefix orbits occurs; the first recorded witness is the two-edge four-vertex instance at ordering `(0,2,3,1)` and level three. | `COMPUTATIONAL` | `CHECKED` | [VS-07 finite genuine-merging evidence](VS-07-AUDIT.md#claim-nae-015--finite-genuine-merging-evidence) | 2026-07-22 |

## Current accepted state

The investigation has:

- an established NP-complete target and checked consequence theorem;
- proved exact transition and bounded-interface results;
- a checked executable exact-profile laboratory;
- proved incidence-forest and deletion-monotonicity theorems;
- checked finite obstruction and summary-collision atlases;
- a proved dead-quotient limitation for unsatisfiable instances;
- a proved fixed-radius locality failure family for conditioned binary inequality residuals;
- an exact measurement framework separating dead collapse, complement symmetry, live semantic merging, boundary states, encoding size, and ordering effects;
- a proved family with exponential fixed-order live quotient growth but a constant-width alternative ordering;
- finite exact evidence that genuine all-live merging exists beyond component-complement prefix identification.

`NAE-006` remains unresolved. VS-06 eliminates only explicitly defined summaries and bounded locality. VS-07 shows that exact live quotients can be both smaller than raw boundary state and exponentially large under a poor order, but it does not select or lower-bound a general symbolic representation language.

`NAE-015` is finite exact computation. It is not an asymptotic lower bound. `NAE-014` is an ordering-separation theorem on an easy family, not an intrinsic hardness result.

## Claim boundaries

- Polynomial time means polynomial in complete binary encoding length.
- Restricted subclasses do not establish `NAE-002`'s premise.
- Randomized bounded-error algorithms do not establish deterministic `P=NP` without an explicit derandomization theorem.
- Polynomial recursion depth or local branching does not bound the complete computation graph.
- A compact syntax is insufficient unless construction, transition, equivalence, acceptance, and total generated representation are polynomially bounded.
- A lower bound for one representation model is model-specific unless a polynomial-overhead subsumption theorem is proved.
- Finite exact-profile, control, obstruction, collision, and semantic-merging measurements do not imply universal asymptotic quotient bounds.
- A large quotient under one ordering does not imply every ordering has a large quotient.
- Exact quotient count does not lower-bound an unspecified symbolic representation.
- Planarity and occurrence-at-most-three tractability remain imported results, not project-original proofs.
- Named Fano evidence is not an exhaustive seven-vertex census.
- Exact boundary-assignment completeness is a fixed-instance, fixed-ordering, fixed-processing-level statement.

## Identifier policy

Use stable identifiers of the form `NAE-###`. Never reuse an identifier after retraction or replacement.
