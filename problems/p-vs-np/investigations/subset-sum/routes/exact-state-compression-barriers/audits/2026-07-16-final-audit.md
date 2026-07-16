# Final Audit — Exact-State Compression Barriers

**Route:** `SS-ECB`  
**Mode:** VERIFY / CLOSE  
**Verdict:** Closed with retained model-specific results  
**Date:** 2026-07-16

## Audit scope

This audit rechecked:

- claim statements and statuses;
- quantifiers and boundary cases;
- binary input-length accounting;
- complete-state versus per-state complexity;
- the assignment-target reduction;
- the grid lower-bound proof;
- the tree-state/TDD equivalence;
- the arithmetic candidate and its escape attack;
- parent investigation navigation and route status.

## Corrections made

1. Corrected the grid-cut notation so the row counts use one symbol consistently.
2. Replaced the questionable dummy-variable root construction in the tree-state/TDD proof with an explicit quotient of accepting root states.
3. Corrected `SS-ECB-017`: the proved escape assumes compact bounded residue-range predicates, not residue-equality tests alone.
4. Marked the arithmetic proof-graph note `RETRACTED / CHECKED` and recorded that its branch grammar was under-specified.
5. Removed stale references describing the route as active.
6. Preserved the unresolved broad model question as inactive and subject to explicit reopening conditions.

## Claims surviving review

The following survive with their recorded scope:

- unrestricted representation size is vacuous;
- polynomial compilation plus polynomial exact arbitrary-target query is equivalent to `P=NP`;
- the assignment-target embedding is exact;
- the ordered query model is an OBDD model by definition;
- the square-grid family has a `2^{Omega(L^{1/4})}` lower bound in that ordered model;
- explicit tree-state systems and deterministic TDDs are polynomially equivalent when their full transition structures are counted;
- exact item-block summaries compose by Minkowski sum;
- structural compression used distinct exact-summary, coverage, and residual-transformation semantics;
- unevaluated Minkowski DAG size is a vacuous measure;
- unrestricted intersection yields compact CNF assignment-slice representations;
- exact progression-union normalization can be exponentially large on easy ternary superincreasing instances;
- compact bounded residue-range tests plus unrestricted repeated branching evaluate width-three CNF assignment slices in polynomial graph size.

## Failed claim

`SS-ECB-016` is retracted. The candidate did not specify a branch grammar strong enough to contain the intended compact residue operations while weak enough to rule out Boolean simulation. Its natural bounded-residue completion is refuted by `SS-ECB-017`.

This does not disprove every conceivable arithmetic proof graph.

## Final scope

No retained result proves:

- a lower bound for arbitrary Subset Sum algorithms;
- hardness of the fixed-target grid-derived instances;
- a universal lower bound against structural compression;
- `P != NP`.

## Repository disposition

- route status: closed;
- parent investigation: route selection;
- active Subset Sum route: none;
- reopening: only under the conditions in `CLOSEOUT.md`;
- pull request: squash-merged as PR #1;
- route working branch: removed.
