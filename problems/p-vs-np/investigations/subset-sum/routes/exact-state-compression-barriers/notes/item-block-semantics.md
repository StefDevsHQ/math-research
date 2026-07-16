# Item-Block Semantics and Structural-Atom Audit

**Claims:** `SS-ECB-011`, `SS-ECB-012`  
**Classification:** Definition, lemma, and route audit  
**Status:** `PROVED / CHECKED` for the composition identities and layer-separation conclusion  
**Updated:** 2026-07-16

## 1. Item blocks and reachable sets

Let \(A\) be a finite multiset of nonnegative integers. An **item block** is a submultiset \(B\subseteq A\). Write

\[
\Sigma(B)=\left\{\sum_{b\in X}b:X\subseteq B\right\}.
\]

For a query target \(t\ge 0\), define the target-truncated reachable set

\[
\Sigma_t(B)=\Sigma(B)\cap[0,t].
\]

A context-independent exact summary of \(B\) denotes either \(\Sigma(B)\) or, when the target is globally fixed, \(\Sigma_t(B)\). The summary may use a compressed syntax, but its denotation must be exact.

## 2. Exact composition identity

### Lemma 1

For disjoint item blocks \(B_0,B_1\),

\[
\Sigma(B_0\uplus B_1)=\Sigma(B_0)+\Sigma(B_1),
\]

where

\[
X+Y=\{x+y:x\in X,\ y\in Y\}
\]

is the Minkowski sum.

### Proof

Every subset of \(B_0\uplus B_1\) splits uniquely into a subset of \(B_0\) and a subset of \(B_1\), so every reachable sum is a sum of one element from each child reachable set. Conversely, the disjoint union of subsets witnessing \(x\in\Sigma(B_0)\) and \(y\in\Sigma(B_1)\) witnesses \(x+y\in\Sigma(B_0\uplus B_1)\). \(\square\)

### Lemma 2

For nonnegative items and target \(t\ge0\),

\[
\Sigma_t(B_0\uplus B_1)
=
\bigl(\Sigma_t(B_0)+\Sigma_t(B_1)\bigr)\cap[0,t].
\]

### Proof

If \(x+y\le t\) and all items are nonnegative, then \(x\le t\) and \(y\le t\). Thus truncating each child before composition loses no pair capable of reaching a sum at most \(t\). Lemma 1 then gives the identity. \(\square\)

These identities are the mandatory semantics of any exact item-block composition model.

## 3. Three distinct kinds of structural information

The closed structural-compression route used three mathematically different mechanisms.

### A. Exact set summaries

Examples include an exact interval, a bounded arithmetic progression, an explicit residue table, a finite exception decomposition, or an exact recursively composed reachable set.

Such a summary denotes all of \(\Sigma(B)\) or \(\Sigma_t(B)\) and may be composed by the identities above.

### B. Coverage certificates

A coverage certificate proves only

\[
K\subseteq\Sigma(B)
\]

for a specified set \(K\). The residue-completion lemma is of this form: it proves that a central interval is reachable, but does not describe all reachable sums outside that interval.

A coverage certificate can terminate a query when \(t\in K\). It cannot replace an exact summary of \(\Sigma(B)\) in an arbitrary later composition unless the omitted reachable sums are separately retained.

### C. Target-relative residual transformations

A forced rule proves an equivalence

\[
t\in\Sigma(B)
\quad\Longleftrightarrow\quad
 t'\in\Sigma(B')
\]

for a smaller block or residual target. This transforms one decision instance; it does not necessarily produce a compact representation of the full reachable set.

For example, if \(a\in B\), \(R=\sum(B\setminus\{a\})\), and \(a>R\), then:

- if \(t\le R\), any solution excludes \(a\);
- if \(R<t<a\), the instance is impossible;
- if \(a\le t\le a+R\), any solution includes \(a\) and the residual target is \(t-a\);
- if \(t>a+R\), the instance is impossible.

This is the mechanism that solves superincreasing instances without constructing their full reachable sets.

## 4. Audit of the retained structural framework

The retained operations cannot be faithfully represented by one final exact-set syntax alone:

1. **forced separation** is a target-relative residual transformation;
2. **progression plus residue completion** is a coverage certificate;
3. **persistent lattice or recursive structure** requires exact subinstance composition and compatibility accounting;
4. **the polynomially bounded decomposition theorem** counts the complete graph containing all of these rule types.

Therefore a faithful successor model needs two semantic layers:

- a **summary layer** for exact or certified arithmetic sets;
- a **query/proof-graph layer** for target-relative transformations, acceptance certificates, branching, and compatibility merges.

This is not optional terminology. Collapsing the two layers causes one of two errors:

- treating a coverage subset as if it were the full reachable set;
- forcing a target-relative greedy rule to materialize an exponentially large full set.

## 5. Claims established

### `SS-ECB-011`

Every context-independent exact item-block model must respect exact Minkowski composition, with the truncated identity above available for nonnegative target-bounded queries.

### `SS-ECB-012`

The retained structural-compression framework is intrinsically heterogeneous: it uses exact summaries, one-sided coverage certificates, and target-relative residual transformations. A model that contains only final exact reachable-set representations does not, by that fact alone, subsume the framework.

## 6. Required accounting

Any successor model must count:

- every item-block and residual-target node;
- all exact summary atoms and binary-encoded constants;
- every coverage certificate and its verification data;
- every branch and compatibility interface;
- all intermediate representations, including discarded ones;
- construction and query time.

A polynomial final object is insufficient if producing or evaluating it requires a superpolynomial complete graph.