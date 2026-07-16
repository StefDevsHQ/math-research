# Explicit Tree-State Systems and Tree Decision Diagrams

**Claim:** `SS-ECB-009`  
**Status:** `PROVED / CHECKED`  
**Proof type:** Constructive representation equivalence  
**Updated:** 2026-07-16

## 1. Motivation

The ordered query-state model processes assignment variables along one path. A broader context-independent Boolean model processes disjoint variable blocks along a binary decomposition tree.

The explicit version is a deterministic bottom-up tree-state system. Its state sets and transition tables are counted in full; transition programs are not treated as free.

## 2. Definition

Let \(X\) be a finite Boolean variable set and let \(T\) be a rooted full binary tree whose leaves are in one-to-one correspondence with \(X\). For a node \(v\), write \(X_v\) for the variables below \(v\).

An **explicit deterministic tree-state system** \(M\) respecting \(T\) consists of:

1. a finite state set \(Q_v\) for every node \(v\);
2. for every leaf \(v\) labelled by \(x\), a map
   \[
   \delta_v:\{0,1\}\to Q_v;
   \]
3. for every internal node \(v\) with children \(v_0,v_1\), a total transition table
   \[
   \delta_v:Q_{v_0}\times Q_{v_1}\to Q_v;
   \]
4. an accepting set \(F\subseteq Q_r\) at the root \(r\).

For an assignment \(\alpha\), states are computed bottom-up. The system accepts exactly when the root state lies in \(F\).

The explicit size is

\[
\|M\|=
\sum_{v\in T}|Q_v|
+
\sum_{v\text{ internal}}|Q_{v_0}|\,|Q_{v_1}|
+
|F|.
\]

The product term counts every transition-table entry. Binary encoding adds only logarithmic overhead for state identifiers and destinations.

## 3. Tree Decision Diagram syntax used

A deterministic Tree Decision Diagram respecting \(T\) has a set \(N_v\) of nodes at each tree node \(v\). Leaf nodes represent pairwise disjoint functions of one variable. At an internal node, each pair of child nodes belongs to the input relation of at most one parent node. One distinguished root node represents the accepted Boolean function.

Undefined cases are represented by explicit rejecting sinks.

## 4. Tree-state system to TDD

### Theorem 1

Every explicit deterministic tree-state system \(M\) can be converted into a deterministic Tree Decision Diagram computing the same Boolean function with size polynomial in \(\|M\|\).

### Proof

For each state \(q\in Q_v\), define

\[
f_{v,q}(\beta)=1
\quad\Longleftrightarrow\quad
q_v(\beta)=q.
\]

For fixed \(v\), these functions have pairwise disjoint model sets.

At a leaf labelled \(x\), create one node for every nonempty state preimage. Its function is \(x\), \(\neg x\), or the constant-one function when both bits map to the same state.

At an internal node \(v\), create one TDD node \(g_{v,q}\) for every state \(q\in Q_v\) with nonempty preimage. Its input relation contains exactly the child pairs

\[
(g_{v_0,q_0},g_{v_1,q_1})
\]

for which

\[
\delta_v(q_0,q_1)=q.
\]

Every child-state pair is assigned to exactly one parent state, so determinism holds. Induction on \(T\) shows that \(g_{v,q}\) computes exactly \(f_{v,q}\).

If \(F\) contains several accepting root states, first quotient them into a single accepting state \(q_\mathrm{acc}\): redirect every root transition whose destination lies in \(F\) to \(q_\mathrm{acc}\), leave all other destinations distinct, and set the accepting set to \(\{q_\mathrm{acc}\}\). Because acceptance depends only on membership in \(F\), this preserves the Boolean function and does not increase the transition-table size. The converted TDD then has one distinguished accepting root node.

The number of TDD nodes is at most \(\sum_v|Q_v|\), and the number of node-pair incidences is at most the number of explicit transition entries. The conversion therefore has polynomial, essentially linear, overhead. \(\square\)

## 5. TDD to tree-state system

### Theorem 2

Every deterministic Tree Decision Diagram \(C\) respecting \(T\) can be converted into an explicit deterministic tree-state system computing the same Boolean function with size polynomial in the fully explicit TDD size.

### Proof

For every tree node \(v\), take one state for each TDD node in \(N_v\), together with a rejecting sink \(\bot_v\).

At a leaf labelled \(x\), map each bit to the unique leaf node satisfied by that bit, if one exists, and otherwise to \(\bot_v\). Determinism guarantees uniqueness.

At an internal node \(v\), for child states \(q_0,q_1\):

- if the corresponding child-node pair occurs in the input relation of a parent node \(g\in N_v\), set \(\delta_v(q_0,q_1)=g\);
- otherwise set \(\delta_v(q_0,q_1)=\bot_v\).

Pairs involving a sink map to the parent sink. TDD determinism guarantees that no pair is assigned to two parent nodes. The accepting set contains exactly the distinguished TDD root node.

Induction on the tree proves that a non-sink state is reached exactly when the assignment restriction selects the corresponding TDD node. Hence the root accepts exactly the models of the TDD.

If the TDD width is \(w\), every transition table has at most \((w+1)^2\) entries and the tree has fewer than \(2|X|\) nodes. Thus the explicit system size is polynomial in the fully explicit TDD representation. \(\square\)

## 6. Consequence and limitation

Explicit deterministic tree-state systems and deterministic Tree Decision Diagrams are polynomially equivalent as representations of Boolean query functions respecting the same variable tree.

This does not establish a tree decomposition of Subset Sum item blocks or a polynomial-overhead compilation of binary-encoded interval, progression, residue, exception, or recursive arithmetic summaries. The route later failed to find a natural succinct extension that both retained those operations and excluded polynomial Boolean simulation.

## 7. Boundary cases

- A one-variable tree is handled entirely by the leaf map and accepting set.
- An empty variable set can be represented by one root state and one acceptance bit.
- Unreachable states may be deleted.
- Partial TDD relations become total only through rejecting sinks.
- The equivalence counts the complete transition structure and does not treat a transition oracle as free.