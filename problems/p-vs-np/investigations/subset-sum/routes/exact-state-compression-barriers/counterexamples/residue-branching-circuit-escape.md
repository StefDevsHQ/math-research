# Bounded-Residue Branching Escape

**Claim:** `SS-ECB-017`  
**Status:** `PROVED / CHECKED`  
**Classification:** Model attack and rejection theorem  
**Proof type:** Constructive polynomial-size simulation  
**Updated:** 2026-07-16

## 1. Exact claim

Let \(\varphi\) be a CNF formula over variables \(x_0,\ldots,x_{n-1}\), with every clause containing at most three literals, and let

\[
\widehat\tau_\varphi(\alpha)=MH+c(\alpha),
\qquad
M=2^n,
\qquad
c(\alpha)=\sum_{i=0}^{n-1}\alpha_i2^i
\]

be the binary-payload assignment-target map from `SS-ECB-014`.

Consider a target-relative proof-graph language that permits:

1. a binary-encoded target or residual target \(t\);
2. polynomial-size branch predicates of the form
   \[
   t\bmod q\in[a,b],
   \]
   where \(q,a,b\) are binary encoded and the predicate is evaluated exactly;
3. unrestricted repeated use of such branch predicates in a finite directed acyclic control-flow graph;
4. accepting and rejecting terminal nodes;
5. full accounting of every branch node and every encoded predicate parameter.

Then the assignment-target query function

\[
\alpha\longmapsto
\mathbf 1\!\left[
\widehat\tau_\varphi(\alpha)
\in
\Sigma(\widehat A_\varphi)
\right]
\]

has a proof graph of size polynomial in the binary encoding length of \(\varphi\) and its assignment-target query instances.

Consequently, this assignment-target family cannot support a superpolynomial lower bound against any model containing compact bounded residue-range tests together with unrestricted repeated branching.

## 2. Payload-bit extraction

### Lemma 1

For every assignment \(\alpha\), every \(i\in\{0,\ldots,n-1\}\), and

\[
t=\widehat\tau_\varphi(\alpha)=MH+c(\alpha),
\]

we have

\[
\alpha_i=1
\quad\Longleftrightarrow\quad
2^i\le t\bmod 2^{i+1}<2^{i+1}.
\]

Equivalently,

\[
\alpha_i=0
\quad\Longleftrightarrow\quad
0\le t\bmod 2^{i+1}<2^i.
\]

### Proof

Because \(M=2^n\) and \(i+1\le n\),

\[
2^{i+1}\mid M.
\]

Therefore

\[
t\bmod 2^{i+1}
=
(MH+c(\alpha))\bmod 2^{i+1}
=
c(\alpha)\bmod 2^{i+1}.
\]

The residue \(c(\alpha)\bmod 2^{i+1}\) consists exactly of the lowest \(i+1\) payload bits. Its \(i\)-th bit is one precisely when the residue lies in the upper half

\[
[2^i,2^{i+1}-1]
\]

of the residue range, and zero precisely when it lies in the lower half

\[
[0,2^i-1].
\]

This proves both equivalences. \(\square\)

## 3. Literal predicates

For a literal \(\ell\) on variable \(x_i\), define the exact target predicate

\[
P_\ell(t)=
\begin{cases}
1,&\ell=x_i\text{ and }2^i\le t\bmod 2^{i+1}<2^{i+1},\\
1,&\ell=\neg x_i\text{ and }0\le t\bmod 2^{i+1}<2^i,\\
0,&\text{otherwise}.
\end{cases}
\]

By Lemma 1,

\[
P_\ell(\widehat\tau_\varphi(\alpha))=1
\quad\Longleftrightarrow\quad
\ell\text{ is satisfied by }\alpha.
\]

Each predicate uses one modulus \(2^{i+1}\) and one bounded residue interval. All parameters have \(O(n)\) binary bits.

## 4. Clause-by-clause proof graph

Write

\[
\varphi=C_1\land\cdots\land C_m.
\]

Construct a directed acyclic graph as follows.

For every nonempty clause

\[
C_j=(\ell_{j,1}\lor\cdots\lor\ell_{j,k_j}),
\qquad
1\le k_j\le3,
\]

create a chain of at most \(k_j\) literal-test nodes:

1. test \(P_{\ell_{j,1}}(t)\);
2. if true, proceed immediately to the first node for clause \(C_{j+1}\), or to the accepting terminal when \(j=m\);
3. if false, test the next literal;
4. if every literal test in \(C_j\) is false, proceed to the rejecting terminal.

If \(\varphi\) has no clauses, use the accepting terminal. If \(\varphi\) contains an empty clause, use the rejecting terminal.

### Theorem 2 — Correctness

For every assignment \(\alpha\), the constructed graph accepts

\[
t=\widehat\tau_\varphi(\alpha)
\]

if and only if

\[
\widehat\tau_\varphi(\alpha)
\in
\Sigma(\widehat A_\varphi).
\]

### Proof

By the literal-predicate equivalence, the chain for clause \(C_j\) proceeds to the next clause exactly when at least one literal of \(C_j\) is satisfied by \(\alpha\). It reaches the rejecting terminal exactly when every literal of some clause is false.

Hence the graph reaches the accepting terminal exactly when every clause is satisfied:

\[
\operatorname{Graph}(\widehat\tau_\varphi(\alpha))=1
\quad\Longleftrightarrow\quad
\alpha\models\varphi.
\]

By the binary-payload embedding theorem `SS-ECB-014`,

\[
\alpha\models\varphi
\quad\Longleftrightarrow\quad
\widehat\tau_\varphi(\alpha)
\in
\Sigma(\widehat A_\varphi).
\]

Combining the two equivalences proves the claim. \(\square\)

## 5. Complete size accounting

The graph contains at most one branch node per literal occurrence. For width-three CNF, the number of branch nodes is at most

\[
3m.
\]

It also contains two terminals and only constant additional control edges per branch node.

A predicate for variable \(x_i\) stores:

- modulus \(2^{i+1}\);
- lower interval endpoint;
- upper interval endpoint;
- two successor identifiers.

The arithmetic parameters use \(O(n)\) bits, and node identifiers use logarithmic bits in the graph size. Thus the total encoded proof-graph size is

\[
O(mn+m\log m),
\]

which is polynomial in \(|\varphi|\). Construction time and evaluation time are also polynomial. On any query path, at most three tests are made per clause, so evaluation uses \(O(m)\) exact residue-range tests.

The binary-payload item multiset and every assignment target have polynomial encoding length by `SS-ECB-014`. Therefore the complete construction and query graph are polynomial in the relevant binary input lengths.

## 6. Attack on the restricted arithmetic proof-graph candidate

The candidate `SS-ECB-016` was intended to permit compact large-modulus arithmetic branching while excluding polynomial Boolean simulation. The theorem above defeats its natural bounded-residue completion:

1. the payload target exposes every assignment bit through one compact bounded residue-range test;
2. repeated branching evaluates each clause;
3. the full conjunction is implemented by sequential control flow;
4. the complete graph remains polynomially bounded.

No arbitrary Boolean-circuit node is required. The arithmetic predicates and reusable branch graph already recover polynomial CNF evaluation on the assignment-target slice.

Therefore `SS-ECB-016` fails its non-universality requirement under this natural completion and remains `RETRACTED`.

## 7. Boundary cases and limitations

- The proof applies to targets in the binary-payload assignment slice. It does not classify arbitrary targets.
- It proves a polynomial upper bound for the query function, not a polynomial-time algorithm for unrestricted Subset Sum.
- The proof uses bounded residue-range predicates. It does not prove that residue-equality predicates alone suffice to recover payload bits with polynomial complete graph size.
- Restricting branch order, branch reuse, modulus size, or target access may produce a weaker model, but that model must be fully specified and separately shown to contain all retained structural operations.
- A model that charges superpolynomial cost for evaluating one binary-encoded residue-range predicate is outside the stated assumptions.
- The construction is deterministic and exact; it uses no probabilistic or computationally sampled step.

## 8. Final disposition

`SS-ECB-017` is proved for compact bounded residue-range tests plus unrestricted repeated branching. It supplies the precise escape theorem needed to reject the natural completion of `SS-ECB-016`.

Pure residue-equality branching remains unclassified.