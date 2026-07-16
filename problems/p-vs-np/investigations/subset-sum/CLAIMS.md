# Claim Ledger — Subset Sum Investigation

This is the authoritative investigation-level ledger for Subset Sum claims.

## Claims

| ID | Statement | Status | Review | Evidence | Updated |
|---|---|---|---|---|---|
| `SS-001` | The original dense-or-separated bundle route yields a universal polynomial-time exact algorithm for Subset Sum. | `RETRACTED` | `CHECKED` | [Route retraction record](routes/structural-compression/counterexamples/bundle-lemma.md) | 2026-07-16 |
| `SS-002` | The residue-completion lemma gives an exact sufficient condition for a reachable arithmetic progression to expand into a complete central interval. | `PROVED` | `CHECKED` | [Proof](routes/structural-compression/proofs/residue-completion-lemma.md) | 2026-07-16 |
| `SS-003` | The forced/progression/lattice framework yields a universal polynomial-time exact algorithm for Subset Sum. | `RETRACTED` | `CHECKED` | [SAT audit](routes/structural-compression/audits/sat-to-subset-sum.md) | 2026-07-16 |
| `SS-004` | Subset Sum is polynomial-time decidable on classes admitting an efficiently constructible exact decomposition whose complete computation graph and total encoded state are polynomially bounded in binary input length. | `PROVED` | `CHECKED` | [Proof](routes/structural-compression/proofs/polynomially-bounded-decomposition-class.md) | 2026-07-16 |
| `SS-005` | Even square-grid assignment-target query functions require every ordered assignment-target query graph to have size `2^{Omega(L^{1/4})}` in binary query-instance length `L`. | `PROVED` | `CHECKED` | [Grid-family ordered barrier](routes/exact-state-compression-barriers/proofs/grid-family-state-barrier.md) | 2026-07-16 |

## Current accepted state

Two universal routes are closed:

- structural compression is closed as a universal algorithmic strategy;
- exact-state compression barriers is closed as a broad model-barrier strategy.

The residue-completion lemma and polynomially bounded exact-decomposition theorem remain valid. The ordered square-grid lower bound remains valid only for the explicitly defined ordered Boolean query-representation model.

No retained result proves a lower bound for arbitrary fixed-target Subset Sum algorithms or implies `P != NP`.

## Current phase

No active Subset Sum route is selected. See [Status](STATUS.md) and the [exact-state closeout](routes/exact-state-compression-barriers/CLOSEOUT.md).

## Identifier policy

Use stable identifiers of the form `SS-###`. Never reuse an identifier after a claim is retracted or replaced.

Route ledgers may contain finer-grained records, but every claim that changes the investigation's accepted state must be represented here.

See [Research Standards](../../../../RESEARCH_STANDARDS.md) for status definitions and promotion rules.