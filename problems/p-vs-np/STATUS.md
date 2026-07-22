# Status — P versus NP

**Phase:** Monotone NAE-3SAT `NAE-016` disproved; collective exact representations under review  
**Updated:** 2026-07-23

## Current position

The active Monotone NAE-3SAT investigation has completed its first universal ordered-state lower-bound attack.

Central lifts of constant-degree expanders force exponentially many pairwise distinct live exact completion functions under every variable ordering. This disproves the universal polynomial-state PCRNF conjecture `NAE-016`.

No universal polynomial-time algorithm or general representation lower bound is claimed.

The Subset Sum investigation remains closed after its universal structural-compression strategies failed within their stated models.

## Route organization

Monotone NAE-3SAT has an explicit [route registry](investigations/monotone-nae-3sat/routes/README.md) and [route dashboard](investigations/monotone-nae-3sat/routes/STATUS.md).

Current hierarchy:

- `R1 — Exact-state representations` remains open but narrowed;
  - `R1.1 — PCRNF` is closed as a universal ordered state-enumeration route;
  - exact PCRNF residualization and restricted-class analysis are retained;
  - `R1.2` must be reformulated as a collective representation route;
  - reduced ordered decision diagrams inherit the same residual-subfunction obstruction;
  - decomposable circuits and other collective structures remain candidate routes.
- `R2` retains bounded-width and incidence-forest theorems.
- `R6` now includes an explicit all-ordering barrier for state-per-residual-function models.

## Accepted determination

- `NAE-016 — DISPROVED / CHECKED`.
- `NAE-017 — PROVED / CHECKED`.
- `NAE-018 — DISPROVED / CHECKED`.
- `NAE-019 — PROVED / CHECKED`.
- `NAE-020 — PROVED / CHECKED`.
- `NAE-006 — CONJECTURE / DRAFT` remains unresolved.

## Mathematical content

For the central lift of a bounded-degree expander, every ordering admits a balanced prefix cut with a linear crossing induced matching. Subsets of the processed matching endpoints produce `2^{Omega(n)}` live prefixes with pairwise different exact suffix-completion functions.

Exact PCRNF states cannot merge different completion functions, so every ordering has exponentially many PCRNF states at one level.

## Scope boundary

The result applies to ordered computations that materialize one exact state per residual completion function. It does not lower-bound:

- collective circuit representations;
- non-ordered decompositions;
- algebraic global methods;
- arbitrary polynomial-time algorithms.

It therefore proves neither `P=NP` nor `P!=NP`.

## Retained project results

- Subset Sum residue-completion lemma and restricted exact-decomposition theorem;
- Monotone NAE-3SAT exact quotient and bounded-boundary theorems;
- incidence-forest constructive colouring;
- obstruction, locality-failure, summary-collision and semantic-merging evidence;
- exact oriented PCRNF residualization;
- all-ordering expander lower bound for PCRNF and ordered residual-state enumeration.

## Next decision

Select one collective exact-representation route, with deterministic decomposable circuits as the clearest current candidate, or pursue the parallel restricted PCRNF classification programme.

Proof record: [NAE-016 expander disproof](investigations/monotone-nae-3sat/routes/exact-state-representations/pcrnf/proofs/NAE-016-expander-disproof.md).