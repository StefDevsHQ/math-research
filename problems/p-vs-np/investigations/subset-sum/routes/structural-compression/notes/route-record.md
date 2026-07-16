# Structural Compression — Route Record

**Recorded:** 2026-07-16  
**Route state:** Closed in its original form; local result retained; final audit pending

## Objective

The route asked whether the exact reachable-sum state of Subset Sum could be represented and updated in size polynomial in the binary input length.

For a multiset \(A\), write

\[
\Sigma(A)=\left\{\sum_{a\in B}a:B\subseteq A\right\}.
\]

The standard recurrence

\[
\Sigma(A_i)=\Sigma(A_{i-1})\cup\bigl(\Sigma(A_{i-1})+a_i\bigr)
\]

is exact but normally indexed by the target magnitude, making it pseudo-polynomial rather than polynomial in the binary encoding.

## Original route

The proposed decomposition had two easy regimes:

1. **Dense:** reachable sums contain intervals or long arithmetic progressions that admit compact representation.
2. **Separated:** an item or component lies beyond the total range of smaller items, making its inclusion target-forced.

The missing step was a bundle composition principle: partition an arbitrary instance into polynomially many locally dense or separated bundles, then combine those summaries without losing exactness.

## Why the original route was closed

The bundle composition principle did not control the information required across bundles:

- residue restrictions can survive apparent density;
- exact gaps can remain inside coarse interval summaries;
- compatibility between choices in different bundles can carry the hard combinatorial state;
- local separation need not remain useful after other components are introduced.

The original bundle lemma is therefore withdrawn as a usable theorem. The exact numerical counterexample from the exploratory session was not preserved, so the repository records the claim as `RETRACTED`, not `DISPROVED`, until a complete counterexample is reconstructed.

## Surviving result

A valid local result remains: a complete arithmetic progression of reachable sums becomes a full central interval when a disjoint component supplies bounded representatives of every residue modulo the progression step.

See [Residue-completion lemma](../proofs/residue-completion-lemma.md).

## Refined framework

The corrected structural language is:

1. **Forced separation** — target-relative choices are determined.
2. **Progression plus residue completion** — modular coverage certifies an exact interval.
3. **Persistent lattice structure** — unresolved states remain organized by nontrivial residue classes and require further analysis.

This is a framework for analysis, not a proved universal trichotomy or polynomial-time algorithm.

## Remaining barriers

Two barriers prevent the current framework from establishing polynomial time:

- A relevant modulus \(q\) may be exponentially large relative to its bit length, so work polynomial in \(q\) can still be exponential in the input size.
- Recursive residue decomposition may preserve the logical choices encoded by a SAT-to-Subset-Sum reduction instead of simplifying them.

No strictly decreasing, polynomially bounded complexity measure has been proved for the recursive branch.

## Decision

The route is retained for tractable subclasses and as a source of exact local lemmas. Before any further universal algorithm construction, it must be audited against a canonical SAT-to-Subset-Sum reduction.

If the audit shows that modular states merely track the original truth assignments, the main program pivots from universal structural compression to exact-state compression barriers.
