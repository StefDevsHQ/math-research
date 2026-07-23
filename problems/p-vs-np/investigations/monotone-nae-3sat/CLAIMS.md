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
| `NAE-016` | Every encoded Monotone NAE-3SAT instance has a polynomial-time constructible ordering for which memoized traversal by propagation-closed signed residual normal forms has polynomially many distinct states of polynomial maximum and total encoded size, with polynomial-time exact transition, equality, and acceptance. | `DISPROVED` | `CHECKED` | [`NAE-020` all-ordering expander lower bound](routes/exact-state-representations/pcrnf/proofs/NAE-016-expander-disproof.md) | 2026-07-23 |
| `NAE-017` | Direct substitution, deterministic propagation closure, and component-complement canonicalization with an explicit orientation bit per residual component preserve the exact labelled completion set and give exact next-variable transitions. | `PROVED` | `CHECKED` | [VS-08 exactness audit](VS-08-AUDIT.md#nae-017--exact-oriented-residualization) | 2026-07-23 |
| `NAE-018` | Byte equality of oriented PCRNF coincides with exact completion equivalence for every instance, ordering, level, and prefix. | `DISPROVED` | `CHECKED` | [VS-08 five-vertex counterexample](VS-08-AUDIT.md#nae-018--pcrnf-equality-is-not-semantic-equality) | 2026-07-23 |
| `NAE-019` | At every level of every fixed ordering, the number of oriented PCRNF states is at least the number of distinct exact labelled completion functions induced by prefixes at that level. | `PROVED` | `CHECKED` | [Semantic projection lemma](routes/exact-state-representations/pcrnf/proofs/NAE-016-expander-disproof.md#4-semantic-projection-lemma--nae-019) | 2026-07-23 |
| `NAE-020` | There is an infinite family of central lifts of constant-degree expanders such that every variable ordering has a level with `2^{Omega(n)}` pairwise distinct live exact completion functions, and hence `2^{Omega(n)}` distinct oriented PCRNF states. | `PROVED` | `CHECKED` | [Expander central-lift theorem](routes/exact-state-representations/pcrnf/proofs/NAE-016-expander-disproof.md#10-conclusion--nae-020) | 2026-07-23 |
| `NAE-021` | There is an infinite family of central lifts of constant-degree expanders whose exact satisfying-assignment functions require DNNF size `2^{Omega(n)}=2^{Omega(L/log L)}`. | `PROVED` | `CHECKED` | [DNNF expander lower bound](routes/exact-state-representations/decomposable-circuits/proofs/NAE-021-dnnf-expander-lower-bound.md) | 2026-07-23 |

## Current accepted state

PCRNF remains exact with exact transitions (`NAE-017`), but byte equality is not complete semantic equality (`NAE-018`) and every ordering has exponentially many exact residual functions on the central-lift expander family (`NAE-020`). By `NAE-019`, this forces exponentially many PCRNF states.

Conditioning the same family at its centre yields bounded-degree monotone two-CNFs of linear treewidth. The established DNNF lower bound for constant-arity, constant-degree monotone CNFs then gives `NAE-021`: exponential DNNF size for the unconditioned central lifts as well.

Thus universal ordered PCRNF, one-state-per-residual semantic quotients, reduced ordered decision diagrams, and DNNF representations are closed on this family. `NAE-006` remains unresolved because these are model-specific lower bounds; operationally it is dormant pending a materially new representation model.

## Claim boundaries

- Polynomial time means polynomial in complete binary encoding length.
- Restricted subclasses do not establish `NAE-002`'s premise.
- Polynomial recursion depth or local branching does not bound the complete computation graph.
- A compact syntax is insufficient unless construction, transition, equality, acceptance, and total generated representation are polynomially bounded.
- A lower bound for one representation model is model-specific unless a polynomial-overhead subsumption theorem is proved.
- Finite exact measurements do not imply universal asymptotic bounds.
- `NAE-020` does not prove `P!=NP` and does not disprove `NAE-006`.
- `NAE-021` lower-bounds DNNF and its subclasses, not unrestricted Boolean circuits or arbitrary algorithms.

## Identifier policy

Use stable identifiers of the form `NAE-###`. Never reuse an identifier after retraction or replacement.