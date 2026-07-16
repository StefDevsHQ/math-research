# Claim Ledger — Subset Sum Investigation

This is the authoritative investigation-level ledger for Subset Sum claims.

## Claims

| ID | Statement | Status | Review | Evidence | Updated |
|---|---|---|---|---|---|
| `SS-001` | The original dense-or-separated bundle route yields a universal polynomial-time exact algorithm for Subset Sum. | `RETRACTED` | `CHECKED` | [Route retraction record](routes/structural-compression/counterexamples/bundle-lemma.md) | 2026-07-16 |
| `SS-002` | The residue-completion lemma gives an exact sufficient condition for a reachable arithmetic progression to expand into a complete central interval. | `PROVED` | `CHECKED` | [Proof](routes/structural-compression/proofs/residue-completion-lemma.md) | 2026-07-16 |
| `SS-003` | The forced/progression/lattice framework yields a universal polynomial-time exact algorithm for Subset Sum. | `RETRACTED` | `CHECKED` | [SAT audit](routes/structural-compression/audits/sat-to-subset-sum.md) | 2026-07-16 |
| `SS-004` | Subset Sum is polynomial-time decidable on classes admitting an efficiently constructible exact decomposition whose complete computation graph and total encoded state are polynomially bounded in the binary input length. | `PROVED` | `CHECKED` | [Proof](routes/structural-compression/proofs/polynomially-bounded-decomposition-class.md) | 2026-07-16 |
| `SS-005` | Canonical assignment-target Subset Sum query families induced by square-grid monotone two-CNF formulas require every ordered context-independent query-state graph to have size `2^{Omega(L^{1/4})}`, where `L` is binary query-instance length. | `PROVED` | `CHECKED` | [Grid-family barrier](routes/exact-state-compression-barriers/proofs/grid-family-state-barrier.md) | 2026-07-16 |

## Current accepted state

The structural-compression route is closed as a universal strategy. Its local coverage lemma and restricted-class theorem remain valid.

The exact-state barrier route has established a superpolynomial lower bound for one explicit ordered query-state model. This is a model-specific compilation result, not a lower bound for arbitrary fixed-target Subset Sum algorithms and not evidence sufficient for `P != NP`.

## Identifier policy

Use stable identifiers of the form `SS-###`. Never reuse an identifier after a claim is retracted or replaced; link the successor claim instead.

Route ledgers may contain finer-grained records, but every claim that changes the investigation's accepted state must be represented here.

See [Research Standards](../../../../RESEARCH_STANDARDS.md) for status definitions and promotion rules.
