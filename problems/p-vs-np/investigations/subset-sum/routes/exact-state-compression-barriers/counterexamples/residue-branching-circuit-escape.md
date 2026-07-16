# Residue-Branching Circuit Escape

**Claim:** `SS-ECB-017`  
**Status:** `PROVED / CHECKED`  
**Classification:** Model attack and rejection theorem  
**Updated:** 2026-07-16

## 1. Claim

Consider a target-relative proof-graph language that permits:

1. a binary-encoded target or residual target \(t\);
2. branch nodes testing congruence predicates
   
   \[
   t\equiv r\pmod q
   \]
   
   for binary-encoded \(q,r\);
3. polynomially many branch nodes with unrestricted directed-acyclic control flow and repeated tests of the same target;
4. accepting and rejecting terminals.

Then the language can evaluate every polynomial-size CNF formula encoded in the binary payload of the target with polynomial complete graph size.

Consequently, the restricted arithmetic proof-graph candidate `SS-ECB-016`, as currently written, does not exclude polynomial-size Boolean computation: its local residue tests plus unrestricted branching already recover a polynomial-size branching program for CNF evaluation.

## 2. Binary payload

Let an assignment \(\alpha\in\{0,1\}^n\) be encoded by

\[
c(\alpha)=\sum_{i=0}^{n-1}\alpha_i2^i.
\]

The binary-payload Subset Sum embedding in `SS-ECB-014` uses targets

\[
\widehat\tau_\varphi(\alpha)=MH+c(\alpha),
\qquad M=2^n,
\]

where \(MH\) is divisible by \(2^n\). Therefore for every \(i<n\), the \(i\)-th assignment bit is recoverable from the target residue modulo \(2^{i+1}\):

\[
\alpha_i=1
\quad\Longleftrightarrow\quad
\widehat\tau_\varphi(\alpha)\bmod 2^{i+1}\in[2^i,2^{i+1}-1].
\]

The interval condition is a disjunction of \(2^i\) residues if only equality predicates are available, which may be exponential. However the candidate model explicitly intends local interval, progression, and congruence predicates. Equivalently, the bit can be tested by the bounded residue predicate

\[
2^i\le t\bmod 2^{i+1}<2^{i+1}.
\]

Call this local predicate `Bit(i,1)`; its negation within the residue range is `Bit(i,0)`.

## 3. Polynomial branching graph for CNF evaluation

Let

\[
\varphi=C_1\land\cdots\land C_m
\]

be a CNF formula of width at most three.

Construct a directed acyclic branch graph as follows.

For each clause

\[
C_j=\ell_{j,1}\lor\cdots\lor\ell_{j,k_j},
\qquad k_j\le3,
\]

create a chain of at most \(k_j\) literal-test nodes.

At the node for literal \(\ell\) on variable \(x_i\):

- if \(\ell=x_i\), test `Bit(i,1)`;
- if \(\ell=\neg x_i\), test `Bit(i,0)`.

If the literal test succeeds, jump to the first node for clause \(C_{j+1}\), or to the accepting terminal when \(j=m\). If it fails, test the next literal in the same clause. If every literal in the clause fails, go to the rejecting terminal.

The graph accepts exactly when every clause has a satisfied literal, hence exactly when

\[
\alpha\models\varphi.
\]

The graph has at most the number of literal occurrences plus two terminals, therefore size \(O(|\varphi|)\). Repeated variables may be tested in different clauses; unrestricted residual branching permits this.

## 4. Transfer to the assignment-target Subset Sum slice

By `SS-ECB-014`,

\[
\widehat\tau_\varphi(\alpha)\in\Sigma(\widehat A_\varphi)
\quad\Longleftrightarrow\quad
\alpha\models\varphi.
\]

Therefore the branch graph above decides exact membership on every target in the assignment-target slice using polynomial complete cost.

No unrestricted intersection gate or stored Boolean circuit is required. The graph topology supplies conjunction across clauses, while local residue tests supply literal evaluation.

## 5. Verification of candidate assumptions

The attack uses only capabilities contemplated by `SS-ECB-016`:

- binary-encoded residue or modular predicates;
- target-relative branch nodes;
- a directed acyclic proof graph;
- repeated use of local predicates;
- shared accepting and rejecting continuations.

The attack does not use:

- unevaluated Minkowski-sum syntax;
- arbitrary set intersection;
- complement gates;
- an oracle transition;
- an uncounted general-purpose program.

All branch nodes and constants are explicitly counted, and their total encoding is polynomial.

## 6. Determination

The current candidate fails its non-universality requirement.

The phrase “fixed list of local arithmetic predicates” does not prevent circuit simulation when the list contains bit-recovering congruence predicates and the control graph may test them repeatedly in unrestricted order.

To block this escape, a successor model must restrict at least one of:

1. the number of times target information may be inspected;
2. the order in which target coordinates or residues may be tested;
3. control-flow reuse and arbitrary clause-like sequencing;
4. the dependence of branch predicates on binary target digits;
5. target-dependent branching itself.

Each such restriction must then be checked against the retained structural-compression operations. Restricting the model merely by declaring predicates “local” is insufficient. \(\square\)

## 7. Scope

This theorem rejects the current candidate model, not every possible arithmetic proof graph.

It does not show that all restricted residue-based systems simulate circuits. A read-once, ordered, bounded-read, or decomposition-local restriction may prevent the construction, but no such restriction has yet been shown to subsume the retained structural framework.