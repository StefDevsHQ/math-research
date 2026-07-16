# Assignment-Target Embedding and OBDD Transfer

**Claims:** `SS-ECB-003`, `SS-ECB-004`  
**Status:** `PROVED / CHECKED`  
**Proof type:** Constructive reduction and exact model transfer  
**Updated:** 2026-07-16

## 1. Source formula

Let \(\varphi\) be a CNF formula with variables \(x_1,\ldots,x_n\) and clauses \(C_1,\ldots,C_m\), each containing at most three distinct literals. Remove tautological clauses and repeated literals.

An assignment is a vector

\[
\alpha\in\{0,1\}^n,
\]

where \(\alpha_i=1\) means \(x_i\) is true.

## 2. Fixed item multiset

Use base \(10\) and the following digit columns:

- two selector columns \(P_i^T,P_i^F\) for every variable \(x_i\);
- one clause column \(D_j\) for every clause \(C_j\).

Construct the following positive integers.

### Assignment items

For each variable \(x_i\):

- \(T_i\) has digit \(1\) in selector column \(P_i^T\), digit \(1\) in clause column \(D_j\) whenever \(x_i\in C_j\), and zero elsewhere;
- \(F_i\) has digit \(1\) in selector column \(P_i^F\), digit \(1\) in clause column \(D_j\) whenever \(\neg x_i\in C_j\), and zero elsewhere.

### Clause slack items

For each clause \(C_j\), create two items:

- \(S_j^{(1)}\), with digit \(1\) in \(D_j\);
- \(S_j^{(2)}\), with digit \(2\) in \(D_j\).

All other digits are zero.

Let

\[
A_\varphi=\{T_i,F_i:1\le i\le n\}\cup
\{S_j^{(1)},S_j^{(2)}:1\le j\le m\}.
\]

This item multiset depends only on \(\varphi\), not on the queried assignment.

## 3. Assignment-to-target map

For \(\alpha\in\{0,1\}^n\), define \(\tau_\varphi(\alpha)\) by:

- selector digit \(P_i^T=1\) and \(P_i^F=0\) if \(\alpha_i=1\);
- selector digit \(P_i^T=0\) and \(P_i^F=1\) if \(\alpha_i=0\);
- every clause digit \(D_j=4\).

The selector columns make \(\alpha\mapsto\tau_\varphi(\alpha)\) injective.

## 4. No-carry verification

A selector column contains a nonzero digit in only one assignment item, so its sum is at most \(1\).

A clause column receives:

- at most \(3\) from assignment items, because the clause width is at most three;
- at most \(3\) from the two slack items.

Thus every column sum is at most \(6<10\). Decimal addition therefore acts coordinatewise with no carries.

## 5. Embedding theorem

### Theorem

For every assignment \(\alpha\),

\[
\tau_\varphi(\alpha)\in\Sigma(A_\varphi)
\quad\Longleftrightarrow\quad
\alpha\models\varphi.
\]

### Proof

In selector columns \(P_i^T,P_i^F\), exact equality to the target forces:

- inclusion of \(T_i\) and exclusion of \(F_i\) when \(\alpha_i=1\);
- exclusion of \(T_i\) and inclusion of \(F_i\) when \(\alpha_i=0\).

Therefore the assignment items in any target-reaching subset are uniquely fixed by \(\alpha\).

For clause \(C_j\), let \(k_j\in\{0,1,2,3\}\) be the number of literals of \(C_j\) satisfied by \(\alpha\). The forced assignment items contribute exactly \(k_j\) in digit \(D_j\). The two slack items can contribute exactly one of

\[
0,1,2,3.
\]

The target digit \(4\) is reachable precisely when:

- \(k_j=1\), by adding \(3\);
- \(k_j=2\), by adding \(2\);
- \(k_j=3\), by adding \(1\).

If \(k_j=0\), the maximum slack contribution is \(3\), so digit \(4\) is unreachable.

The target is therefore reachable in every clause column if and only if every clause has at least one satisfied literal. By the no-carry property, the coordinatewise argument is equivalent to equality of the encoded integers. \(\square\)

## 6. Size and construction time

The construction has:

- \(2n+2m\) items;
- \(2n+m\) base-ten columns.

Every item and target has \(O(n+m)\) bits up to the constant factor \(\log_2 10\), and the total explicit encoding length is \(O((n+m)^2)\). The construction and target map are computable in polynomial time.

## 7. Ordered query-state graphs

Fix a permutation \(\pi\) of the variables.

A **deterministic ordered assignment-target query graph** for \((A_\varphi,\tau_\varphi)\) is a directed acyclic graph with:

- one source;
- two terminal nodes labelled `0` and `1`;
- every nonterminal node labelled by a variable;
- exactly two outgoing edges, labelled \(0\) and \(1\);
- variables appearing along each source-to-terminal path in the order \(\pi\), with variables allowed to be skipped;
- output `1` on assignment \(\alpha\) exactly when \(\tau_\varphi(\alpha)\in\Sigma(A_\varphi)\).

The size is the total number of graph nodes. Nodes are the context-independent states that may be shared by different assignment prefixes.

## 8. Transfer theorem

### Theorem

A deterministic ordered assignment-target query graph for \((A_\varphi,\tau_\varphi)\) is an ordered binary decision diagram for \(\varphi\) under the same variable order, with exactly the same graph. Conversely, every ordered binary decision diagram for \(\varphi\) is such a query graph.

### Proof

The graph syntax is the syntax of an ordered binary decision diagram. For every assignment \(\alpha\), the embedding theorem gives

\[
\text{graph}(\alpha)=1
\iff
\tau_\varphi(\alpha)\in\Sigma(A_\varphi)
\iff
\alpha\models\varphi.
\]

Hence the graph computes the Boolean function represented by \(\varphi\). The converse uses the same equivalence in reverse. \(\square\)

## 9. Scope

This theorem lower-bounds only ordered context-independent query-state graphs. It does not lower-bound:

- a general algorithm that decodes \(\alpha\) from the target and evaluates \(\varphi\);
- a fixed-target Subset Sum solver;
- a free binary decision diagram with adaptive variable order;
- arithmetic circuits, modular programs, or unrestricted polynomial-time query procedures;
- tree-structured or non-compositional exact representations.
