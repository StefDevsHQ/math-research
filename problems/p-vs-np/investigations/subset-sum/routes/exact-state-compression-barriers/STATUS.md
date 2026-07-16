# Status — Exact-State Compression Barriers

**State:** Active; arithmetic model bracket established, candidate proof graph open  
**Updated:** 2026-07-16

## Current position

The route now has two groups of results.

First, the earlier Boolean representation work remains valid but model-specific:

- assignment-target query graphs are ordered binary decision diagrams by definition and semantics;
- square-grid monotone two-CNF families require ordered graphs of size \(2^{\Omega(L^{1/4})}\);
- explicit Boolean tree-state systems are polynomially equivalent to deterministic Tree Decision Diagrams.

These results do not subsume the former structural-compression framework.

Second, the item-block semantics and arithmetic-language boundary have now been formalized.

## New arithmetic model bracket

### Exact composition

For disjoint nonnegative item blocks,

\[
\Sigma_t(B_0igma_t(B_0\uplus B_1)
=
(\Sigma_t(B_0)+\Sigma_t(B_1))\cap[0,t].
\]

Any exact item-block model must respect this identity.

### Heterogeneous semantics

The retained structural framework used three distinct mechanisms:

1. exact reachable-set summaries;
2. one-sided coverage certificates;
3. target-relative residual transformations.

A final exact-set language alone does not subsume all three.

### Lower and upper escape boundaries

- **Unevaluated Minkowski DAGs are too weak as a cost model:** every instance has a linear-size exact expression obtained by retaining the original item choices.
- **Normalized progression unions are too rigid:** for \(A_n=\{1,3,\ldots,3^{n-1}\}\), every exact progression-union representation needs at least \(2^{n-1}=2^{\Omega(\sqrt{L_n})}\) atoms, although the instances are easy by forced residual reasoning.
- **Unrestricted intersection is too expressive:** intervals, bounded progressions, union, translation, Minkowski sum, and arbitrary intersection compactly encode every width-three CNF assignment-target slice.

These three results isolate the viable region:

\[
	ext{more semantic power than normalized progression unions}
\]

but

\[
	ext{less unrestricted Boolean combination than intersection/circuits}.
\]

## Candidate model

A restricted arithmetic proof graph has been defined with separate node types for:

- exact summaries;
- coverage certificates;
- residual transformations;
- counted exact merges;
- locally restricted branches.

The candidate forbids free unevaluated Minkowski nodes, unrestricted intersection, arbitrary complement, general Boolean circuits, and uncounted transition programs.

This is currently `OPEN / DRAFT`. It is a model proposal, not a barrier theorem.

## Smallest remaining gap

The decisive next question is now sharper:

> Can the permitted local residual, residue, coverage, and sharing operations simulate arbitrary polynomial-size Boolean circuits with polynomial complete graph cost?

If yes, reject the model as too strong.

If no, the next requirement is a complete compilation theorem showing that every retained structural-compression rule fits the fixed local schemas with polynomial overhead.

Only after both tests survive should a hard-family lower bound be attempted.

## Immediate next actions

1. Fix a finite grammar of admissible local branch and certificate rules.
2. Audit hidden circuit simulation through repeated residue tests, branching, and shared residual nodes.
3. Prove or refute polynomial-overhead compilation of forced separation and residue completion into the candidate.
4. Keep exact-merge normalization and every discarded intermediate atom in the cost measure.
5. Do not search for a general lower bound until the escape audit is complete.

## Stop condition

Close the candidate if it either:

- simulates arbitrary polynomial-size Boolean circuits with polynomial complete cost; or
- fails to express a retained structural operation without an uncounted oracle.

Do not present the candidate definition, the ordered lower bound, or the progression-union lower bound as a general Subset Sum lower bound.