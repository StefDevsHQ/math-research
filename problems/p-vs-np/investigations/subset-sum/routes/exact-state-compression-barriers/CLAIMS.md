# Claim Ledger — Exact-State Compression Barriers

This ledger is authoritative for route-local claims.

## Claims

| ID | Statement | Status | Review | Evidence | Dependencies | Known gap | Updated |
|---|---|---|---|---|---|---|---|
| `SS-ECB-001` | Without restrictions on construction or query computation, every Subset Sum item multiset has an exact representation of size linear in its binary encoding: store the item multiset itself. | `PROVED` | `CHECKED` | [Boundary proof](proofs/unrestricted-representation-boundary.md) | None | No algorithmic consequence; query time may be exponential. | 2026-07-16 |
| `SS-ECB-002` | A polynomial-time preprocessing scheme producing a polynomial-size representation that supports polynomial-time exact membership queries for every target exists for all Subset Sum item multisets if and only if `P=NP`. | `PROVED` | `CHECKED` | [Equivalence proof](proofs/unrestricted-representation-boundary.md) | NP-completeness of Subset Sum | This equivalence does not identify a route to either direction. | 2026-07-16 |
| `SS-ECB-003` | Every CNF formula of clause width at most three admits a polynomial-size no-carry assignment-target embedding: a fixed Subset Sum item multiset and an injective assignment-to-target map whose membership predicate equals formula satisfaction. | `PROVED` | `CHECKED` | [Embedding proof](proofs/assignment-target-obdd-transfer.md) | No-carry digit construction | This is a query-family reduction, not a fixed-target hardness result. | 2026-07-16 |
| `SS-ECB-004` | Every deterministic ordered assignment-target query graph for the embedding induces an ordered binary decision diagram for the source formula with the same nonterminal state graph; conversely an ordered binary decision diagram induces such a graph with at most a linear layering factor. | `PROVED` | `CHECKED` | [Transfer proof](proofs/assignment-target-obdd-transfer.md) | `SS-ECB-003` | Does not cover free variable order, arithmetic query programs, or tree-structured composition. | 2026-07-16 |
| `SS-ECB-005` | For a graph `G`, the smallest ordered binary decision diagram for the monotone two-CNF `phi(G)` has size at least `2^{lu(G)}`, where `lu(G)` is linear upper induced-matching width. | `ESTABLISHED` | `CHECKED` | [Literature map](notes/literature-map.md) | Razgon 2021, Theorem 2 | External theorem is model-specific. | 2026-07-16 |
| `SS-ECB-006` | For the assignment-target Subset Sum query families induced by even square grids, every ordered query-state graph has size `2^{Omega(r)}`; with binary query-instance length `L=O(r^4)`, the lower bound is `2^{Omega(L^{1/4})}`. | `PROVED` | `CHECKED` | [Grid barrier proof](proofs/grid-family-state-barrier.md) | `SS-ECB-003`, `SS-ECB-004`, `SS-ECB-005` | Does not imply hardness of deciding one fixed target. | 2026-07-16 |
| `SS-ECB-007` | The ordered grid barrier does not extend automatically to unrestricted exact query algorithms: the assignment encoded by the target can be decoded and the source CNF evaluated in polynomial time. | `PROVED` | `CHECKED` | [Scope audit](audits/ordered-model-scope.md) | `SS-ECB-003` | A broader transfer theorem is still required. | 2026-07-16 |
| `SS-ECB-008` | There is a tree-structured exact composition model that contains the previous interval, progression, residue, exception, and recursive summaries while retaining a superpolynomial lower bound on reduction-generated families. | `OPEN` | `DRAFT` | [Literature map](notes/literature-map.md) | Precise model definition | Central unresolved route question. | 2026-07-16 |

## Route disposition

A valid ordered-state barrier is established. The route remains active only to seek a broader model that subsumes the closed structural-compression framework. Route identifiers use `SS-ECB-###`.
