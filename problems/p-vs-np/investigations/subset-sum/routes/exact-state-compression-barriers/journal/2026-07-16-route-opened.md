# 2026-07-16 — Exact-State Compression Barriers Opened

## Decision

The structural-compression route remains closed. A sibling route, `exact-state-compression-barriers`, is opened to formalize and lower-bound specified exact-state computation models.

## Results established

1. Representation size without a restricted query model is vacuous: storing the original instance is an exact linear-size representation.
2. Polynomial-time preprocessing plus polynomial-time exact queries for all targets is equivalent to polynomial-time Subset Sum and therefore to `P=NP`.
3. CNF assignment evaluation admits a fixed-item, variable-target no-carry Subset Sum embedding.
4. Ordered context-independent query-state graphs for that embedding are exactly ordered binary decision diagrams.
5. Square-grid monotone two-CNF families require ordered query graphs of size

   \[
   2^{\Omega(L^{1/4})},
   \]

   where \(L\) is the binary query-instance length.

## Negative finding

The ordered lower bound is not a direct Subset Sum algorithmic lower bound. The target exposes the assignment, which an unrestricted algorithm can decode and check in polynomial time. The result blocks only the ordered decision-diagram state model.

## Current gap

Find a broader tree-structured exact composition model that contains the previous interval, progression, residue, exception, and recursive summaries and still admits a superpolynomial lower bound.

The leading literature candidates are Tree Decision Diagrams, structured decision decomposable negation normal form, and bounded-read branching programs.

## Next decisive test

Formalize the state syntax and merge semantics of a tree-structured model, then prove or refute that every structural-compression summary compiles into it with polynomial overhead. Without that inclusion theorem, lower bounds in the candidate model do not constrain the closed route.
