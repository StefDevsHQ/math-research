# Restricted Arithmetic Proof Graph — Retracted Candidate

**Claim:** `SS-ECB-016`  
**Classification:** Definition and failed model candidate  
**Status:** `RETRACTED / CHECKED`  
**Updated:** 2026-07-16

## Purpose

This candidate attempted to contain the retained structural-compression mechanisms without treating arbitrary Boolean conjunction or arbitrary programs as free.

It separated:

- exact reachable-set summaries;
- one-sided coverage certificates;
- target-relative residual transformations;
- counted exact item-block merges;
- locally specified branch rules.

No lower bound was established for the candidate.

## Candidate syntax

A proof graph for a Subset Sum instance \((A,t)\) was a finite directed acyclic graph with the following node types.

### Exact-summary node

An exact-summary node attached to an item block \(B\subseteq A\) denoted exactly \(\Sigma_t(B)\) as a finite union of atoms

\[
\{x\in\mathbb Z:\ell\le x\le u,\ x\equiv r\pmod q\}
\]

plus an explicit finite exception set. All integers were binary encoded.

### Coverage-certificate node

A coverage node certified

\[
K\subseteq\Sigma_t(B)
\]

using polynomial-time-verifiable witness data. The residue-completion lemma was an intended certificate schema. A coverage node could not be substituted for an exact summary unless omitted reachable sums were separately retained.

### Residual-transformation node

A residual node recorded an exact target-relative equivalence

\[
(B,t)\equiv(B',t')
\]

under a polynomial-time-verifiable rule such as forced inclusion, forced exclusion, or immediate rejection.

### Exact-merge node

For disjoint blocks \(B_0,B_1\), an exact merge had to implement and fully count normalization of

\[
\Sigma_t(B_0\uplus B_1)
=
(\Sigma_t(B_0)+\Sigma_t(B_1))\cap[0,t].
\]

All output atoms, discarded intermediate atoms, and compatibility states were counted.

### Branch node

A branch node could split into finitely many sound and exhaustive residual subinstances using a declared local arithmetic predicate.

## Intended exclusions

The candidate did not allow as free unit-cost operations:

- unevaluated Minkowski-sum syntax;
- unrestricted set intersection;
- arbitrary complement;
- arbitrary Boolean circuits or general programs stored at nodes;
- uncounted transition oracles.

## Retraction reason

The branch grammar was not specified tightly enough to establish non-universality.

The natural completion needed to express compact binary-modulus target tests permits bounded residue-range predicates such as

\[
2^i\le t\bmod 2^{i+1}<2^{i+1}.
\]

With unrestricted repeated branching and directed-acyclic control flow, these predicates recover binary payload bits and evaluate a width-three CNF clause by clause using a polynomial-size graph. This is proved in `SS-ECB-017`.

Accordingly:

- the candidate did not satisfy its non-universality requirement;
- it met its explicit stop condition;
- it is retracted rather than retained as an open model.

Pure residue-equality tests alone were not proved sufficient for the same simulation; that narrower variant was never formalized as a complete model and is not an active route.

## Retained value

The record remains useful as an inventory of the semantic layers and cost terms any future model must specify. Reopening requires a materially new restriction that both subsumes the retained structural mechanisms and provably prevents polynomial Boolean simulation.