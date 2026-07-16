# Binary-Payload Embedding and Intersection Escape

**Claim:** `SS-ECB-014`  
**Status:** `PROVED / CHECKED`  
**Proof type:** Constructive embedding and representation upper bound  
**Updated:** 2026-07-16

## 1. Purpose

The first assignment-target embedding shows that general Boolean circuits defeat an assignment-query lower bound. This record proves a stronger and more specific boundary:

> Intervals, bounded arithmetic progressions, Minkowski sum, union, and unrestricted intersection already suffice to represent every width-three CNF assignment-query family in polynomial size.

Thus a proposed arithmetic transition language becomes too expressive if it allows unrestricted conjunction or intersection of compact target sets.

## 2. Binary-payload assignment-target embedding

Let \(\varphi\) be a CNF formula over variables \(x_0,\ldots,x_{n-1}\), with clauses of width at most three.

Construct a high-order no-carry decimal encoding with:

- one variable column \(V_i\) for each variable;
- one clause column \(D_j\) for each clause.

For each variable create high-order item vectors:

- \(T_i^H\): digit one in \(V_i\), and digit one in every clause column containing \(x_i\);
- \(F_i^H\): digit one in \(V_i\), and digit one in every clause column containing \(\neg x_i\).

For each clause create slack vectors with digits one and two in its clause column. Let \(H\) be the high-order target with digit one in every variable column and digit four in every clause column.

Set

\[
M=2^n.
\]

Define integer items

\[
\widehat T_i=M T_i^H+2^i,
\qquad
\widehat F_i=M F_i^H,
\]

and multiply every slack item by \(M\).

For an assignment \(\alpha\in\{0,1\}^n\), define its binary code

\[
c(\alpha)=\sum_{i=0}^{n-1}\alpha_i2^i
\]

and target

\[
\widehat\tau_\varphi(\alpha)=MH+c(\alpha).
\]

The fixed item multiset is denoted \(\widehat A_\varphi\).

## 3. Correctness

### Theorem 1

For every assignment \(\alpha\),

\[
\widehat\tau_\varphi(\alpha)\in\Sigma(\widehat A_\varphi)
\quad\Longleftrightarrow\quad
\alpha\models\varphi.
\]

### Proof

All slack items and all high-order parts of assignment items are multiples of \(M\). The total low-order contribution from all \(\widehat T_i\) is at most

\[
\sum_{i=0}^{n-1}2^i=M-1,
\]

so no low-order sum can carry into the high-order component.

Equality in each high-order variable column \(V_i\) to target digit one forces exactly one of \(\widehat T_i,\widehat F_i\) to be selected. The low-order component of the selected items is therefore the binary code of the variables for which \(\widehat T_i\) was selected. Equality to \(c(\alpha)\) forces that selected truth assignment to be exactly \(\alpha\).

The high-order clause-column argument is the canonical no-carry proof: selected assignment items contribute the number \(k_j\in\{0,1,2,3\}\) of satisfied literals in clause \(C_j\), and the two slack items contribute one of \(0,1,2,3\). Target digit four is reachable exactly when \(k_j\ge1\).

Hence the complete target is reachable exactly when \(\alpha\) satisfies every clause. \(\square\)

The construction uses polynomially many integers of polynomial bit length.

## 4. Compact arithmetic sets for individual bits

Work in the payload range

\[
C_n=[0,M-1].
\]

For bit position \(i\), define the bounded progression

\[
P_i=\{0,2^{i+1},2\cdot2^{i+1},\ldots,M-2^{i+1}\}.
\]

For \(i=n-1\), this is the singleton \(\{0\}\).

Define

\[
B_i^1=[2^i,2^{i+1}-1]+P_i
\]

and

\[
B_i^0=[0,2^i-1]+P_i.
\]

### Lemma 2

For every code \(c\in C_n\),

\[
c\in B_i^b
\quad\Longleftrightarrow\quad
\text{the }i\text{-th binary bit of }c\text{ equals }b.
\]

### Proof

Every \(c\in C_n\) has a unique decomposition

\[
c=q2^{i+1}+r,
\qquad
0\le r<2^{i+1}.
\]

Its \(i\)-th bit is zero exactly when \(0\le r<2^i\), and one exactly when \(2^i\le r<2^{i+1}\). The quotient contribution \(q2^{i+1}\) belongs to \(P_i\), giving the two stated Minkowski representations. \(\square\)

Each bit-value set is therefore represented by one interval, one bounded progression, and one Minkowski-sum operation, using binary constants of \(O(n)\) bits.

## 5. Polynomial representation of a CNF query family

For a literal \(\ell\) on variable \(x_i\), let

\[
L(\ell)=
\begin{cases}
B_i^1,&\ell=x_i,\\
B_i^0,&\ell=\neg x_i.
\end{cases}
\]

For a clause \(C_j\), define

\[
S_j=\bigcup_{\ell\in C_j}L(\ell).
\]

The satisfying assignment-code set is

\[
S_\varphi=\bigcap_{j=1}^m S_j.
\]

Finally translate by the fixed high-order target:

\[
T_\varphi=MH+S_\varphi.
\]

By Lemma 2 and Theorem 1,

\[
MH+c(\alpha)\in T_\varphi
\quad\Longleftrightarrow\quad
\alpha\models\varphi
\quad\Longleftrightarrow\quad
MH+c(\alpha)\in\Sigma(\widehat A_\varphi).
\]

The expression has \(O(n+m)\) arithmetic atoms and Boolean-operation gates for width-three CNF.

## 6. Consequence

Any target-set language that supports, with polynomial encoding:

- binary-bounded intervals;
- binary-bounded arithmetic progressions;
- Minkowski sum of an interval and a progression;
- finite union;
- unrestricted intersection;
- translation;

has polynomial-size representations for the assignment-target slice of every width-three CNF.

Therefore this assignment-target family cannot yield a superpolynomial representation lower bound against such a language.

The critical escape operation is unrestricted intersection: it supplies clause conjunction directly. No general Boolean-circuit gate is needed beyond the arithmetic bit sets and repeated union/intersection.

## 7. Scope

- This theorem represents the structured assignment-target slice, not the entire reachable set \(\Sigma(\widehat A_\varphi)\).
- It does not show that membership in arbitrary expressions of the language is polynomial-time.
- It does show that lower bounds based on this query family fail if the model permits these compact atoms and unrestricted intersection.
- Restricting intersection to clipping by one interval does not trigger this proof.
- A candidate language must specify exactly which intersections, guards, or target predicates are allowed.