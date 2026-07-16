# Unevaluated Minkowski-DAG Boundary

**Claim:** `SS-ECB-013`  
**Status:** `PROVED / CHECKED`  
**Proof type:** Constructive upper bound  
**Updated:** 2026-07-16

## Claim

Any set-expression language that permits:

1. a leaf denoting the two-point set \(\{0,a\}\) for a binary-encoded item \(a\); and
2. an unevaluated binary Minkowski-sum node \(E_0\oplus E_1\) denoting
   \[
   \llbracket E_0\rrbracket+\llbracket E_1\rrbracket,
   \]

has a linear-size exact expression for the reachable set of every Subset Sum instance.

Consequently, no superpolynomial lower bound on final expression-DAG size is possible in such a language unless the cost measure also restricts or counts normalization, membership evaluation, or the complete generated computation graph.

## Proof

Let

\[
A=(a_1,\ldots,a_n).
\]

For each item create a leaf

\[
E_i=\{0,a_i\}.
\]

Combine the leaves by any binary tree of Minkowski-sum nodes. Let the root expression be

\[
E_A=E_1\oplus E_2\oplus\cdots\oplus E_n.
\]

By repeated application of exact item-block composition,

\[
\llbracket E_A\rrbracket
=
\{0,a_1\}+\cdots+\{0,a_n\}
=
\Sigma(A).
\]

The expression has \(n\) leaves and \(n-1\) internal nodes. Its constants are exactly the input items, so its encoded size is \(O(|A|)\) up to tree pointers and delimiters.

Thus every instance has a linear-size exact expression in this unevaluated language. \(\square\)

## Why this does not give a polynomial-time algorithm

Given a target \(t\), deciding

\[
t\in\llbracket E_A\rrbracket
\]

is exactly the original Subset Sum problem. The expression has merely retained the input's nondeterministic additive structure instead of compressing or resolving it.

A recursive evaluation that branches on both children can generate the full subset-choice graph. Polynomial expression depth and polynomial local syntax do not bound the total evaluation graph.

## Boundary cases

- For the empty item list, the expression is the singleton \(\{0\}\).
- Repeated items are handled because item leaves are occurrences, not distinct values.
- Sharing identical leaves can make the syntax smaller but does not remove multiplicity unless occurrence counts are separately encoded and correctly interpreted.
- Target truncation does not repair the issue: replacing every node by its denotation intersected with \([0,t]\) still requires exact normalization or membership evaluation.

## Consequence

The next language cannot treat arbitrary Minkowski-sum syntax as an already compressed state. It must require one or more of:

- a normalized representation with polynomial-time membership;
- an explicit bound on every merge result;
- a counted apply or normalization computation;
- a restricted transition system whose complete evaluation graph is part of the size measure.

This is the additive analogue of `SS-ECB-001`: storing the input as a small exact object is not the same as resolving its exact membership structure.