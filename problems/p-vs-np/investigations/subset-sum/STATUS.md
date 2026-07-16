# Status — Subset Sum Investigation

**Phase:** Exact-state compression barriers active  
**Updated:** 2026-07-16

## Current position

The structural-compression route is closed as a universal polynomial-time strategy. Its residue-completion lemma and polynomially bounded exact-decomposition theorem remain accepted.

The sibling [exact-state compression barriers](routes/exact-state-compression-barriers/README.md) route is now active.

## New established boundary

The first formal model is an ordered assignment-target query-state graph. A fixed-item, variable-target no-carry embedding transfers these state graphs exactly to ordered binary decision diagrams.

For query families induced by square-grid monotone two-CNF formulas, every such ordered state graph has size

\[
2^{\Omega(L^{1/4})},
\]

where \(L\) is the binary length of the item multiset and target.

This is a genuine model-specific compression barrier. It does not imply a lower bound for arbitrary Subset Sum algorithms or for one fixed target: the structured target exposes an assignment that can be decoded and checked directly in polynomial time.

## Accepted results

1. Residue-completion lemma.
2. Polynomial-time solvability for classes with an efficiently constructible exact decomposition whose complete computation graph and total encoded state are polynomially bounded in binary input length.
3. Unrestricted representation size alone cannot yield a barrier, because the original instance is already a linear-size exact representation.
4. Ordered context-independent assignment-target states require a superpolynomial complete graph on the square-grid family.

## Current blocker

The ordered model does not formally contain the interval, progression, residue, exception, and recursive summaries from the closed route. A broader tree-structured model is required before a lower bound can constrain that framework.

## Next action

Formalize a tree-compositional exact-state model and test transfer to Tree Decision Diagrams, structured decision decomposable negation normal form, or bounded-read branching programs. The decisive condition is a proved polynomial-overhead inclusion of the previous structural summaries.

Do not infer a general decision lower bound from a compilation or representation lower bound.
