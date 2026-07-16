# Unrestricted Representation Boundary

**Claims:** `SS-ECB-001`, `SS-ECB-002`  
**Status:** `PROVED / CHECKED`  
**Proof type:** Constructive equivalence  
**Updated:** 2026-07-16

## Setting

Let

\[
A=(a_1,\ldots,a_n)
\]

be a list of positive integers encoded in binary. Write \(|A|\) for the total binary input length, including delimiters, and

\[
\Sigma(A)=\left\{\sum_{i\in S}a_i:S\subseteq[n]\right\}.
\]

An exact target-membership representation consists of a finite string \(R(A)\) and a query procedure that, given \(R(A)\) and a binary target \(t\), returns whether \(t\in\Sigma(A)\).

## Theorem 1 — Representation size alone is vacuous

For every item list \(A\), there is an exact representation of size \(O(|A|)\).

### Proof

Set

\[
R(A)=\operatorname{enc}(A),
\]

the original binary encoding of the item list.

Given \(R(A)\) and \(t\), enumerate all subsets \(S\subseteq[n]\), compute each corresponding sum, and accept exactly when one equals \(t\). This query algorithm is exact. The representation length is precisely the original input length up to fixed encoding overhead.

Thus no superpolynomial lower bound on representation length can hold when query computation is unrestricted. \(\square\)

## Theorem 2 — Polynomial preprocessing and query equivalence

The following are equivalent:

1. There exist algorithms `Compile` and `Query` and a polynomial \(p\) such that, for every item list \(A\):
   - `Compile(A)` runs in time polynomial in \(|A|\) and produces a string \(R(A)\) of length at most \(p(|A|)\);
   - `Query(R(A),t)` runs in time polynomial in \(|A|+|t|\);
   - `Query(R(A),t)` accepts if and only if \(t\in\Sigma(A)\), for every target \(t\).
2. Subset Sum is decidable in polynomial time.
3. \(P=NP\).

### Proof

#### `1 implies 2`

Given a standard Subset Sum instance \((A,t)\), compute \(R(A)=\texttt{Compile}(A)\), then run \(\texttt{Query}(R(A),t)\). Both stages run in polynomial time and the answer is exact.

#### `2 implies 1`

Let `Compile(A)` return the original encoding of \(A\). Let `Query` run the assumed polynomial-time Subset Sum algorithm on \((A,t)\). The representation has linear size and both procedures are polynomial-time.

#### `2 equivalent to 3`

Subset Sum is in `NP` and is `NP`-complete under polynomial-time many-one reductions. Therefore Subset Sum is in polynomial time if and only if \(P=NP\). \(\square\)

## Boundary cases

- For \(A=\emptyset\), the reachable set is \(\{0\}\); both proofs remain valid.
- A target \(t<0\) is immediately rejected because all items are positive.
- The result does not depend on numerical magnitude except through binary encoding length.
- Allowing negative items changes the reachable-set definition but not the representation-size argument: storing the original instance remains linear.

## Consequence for this route

A meaningful exact-state barrier must lower-bound a restricted representation language, query model, merge model, or complete computation graph. It cannot lower-bound unrestricted representation bytes.
