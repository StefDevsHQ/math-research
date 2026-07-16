# Explicit Tree-State Systems and Tree Decision Diagrams

**Claim:** `SS-ECB-009`  
**Status:** `PROVED / CHECKED`  
**Proof type:** Constructive representation equivalence  
**Updated:** 2026-07-16

## 1. Motivation

The ordered query-state model processes assignment variables along one path. The natural broader context-independent model processes disjoint variable blocks along a binary decomposition tree.

The correct explicit version is a deterministic bottom-up tree-state system. Its state sets and transition tables must be counted in full; allowing an unrestricted program to compute transitions would collapse the model back into unrestricted polynomial-time query computation.

## 2. Definition

Let \(X\) be a finite Boolean variable set and let \(T\) be a rooted full binary tree whose leaves are in one-to-one correspondence with \(X\). For a node \(v\), write \(X_v\) for the variables in the leaves below \(v\).

An **explicit deterministic tree-state system** \(M\) respecting \(T\) consists of:

1. a finite state set \(Q_v\) for every node \(v\) of \(T\);
2. for every leaf \(v\) labelled by variable \(x\), a map

   \[
   \delta_v:\{0,1\}\to Q_v;
   \]

3. for every internal node \(v\) with children \(v_0,v_1\), a total transition table

   \[
   \delta_v:Q_{v_0}\times Q_{v_1}\to Q_v;
   \]

4. an accepting set \(F\subseteq Q_r\) at the root \(r\).

For an assignment \(\alpha\in\{0,1\}^X\), its state \(q_v(\alpha)\) is computed bottom-up:

- at a leaf \(x\), \(q_v(\alpha)=\delta_v(\alpha(x))\);
- internally,

  \[
  q_v(\alpha)=\delta_v(q_{v_0}(\alpha),q_{v_1}(\alpha)).
  \]

The system accepts \(\alpha\) exactly when \(q_r(\alpha)\in F\).

The explicit size is

\[
\|M\|=
\sum_{v\in T}|Q_v|
+
\sum_{v\text{ internal}}|Q_{v_0}|\,|Q_{v_1}|
+
|F|.
\]

The product term counts every transition-table entry. State names, accepting marks, and table destinations require logarithmic encoding overhead, so bit size differs by at most a logarithmic factor.

## 3. Tree Decision Diagram syntax used

A deterministic Tree Decision Diagram respecting \(T\) has a set \(N_v\) of nodes at every tree node \(v\). At a leaf, nodes represent pairwise disjoint functions of the leaf variable. At an internal node, each pair of child nodes belongs to the input relation of at most one parent node. A distinguished root node represents the accepted Boolean function.

This is the deterministic syntax introduced by Capelli, Choi, Mengel, Muñoz, and Van den Broeck in “A canonical generalization of OBDD,” 2026.

For the equivalence below, zero or undefined cases are handled by explicit rejecting sink states.

## 4. Tree-state system to TDD

### Theorem 1

Every explicit deterministic tree-state system \(M\) can be converted into a deterministic Tree Decision Diagram computing the same Boolean function with size polynomial in \(\|M\|\).

### Proof

For each state \(q\in Q_v\), define the local Boolean function

\[
f_{v,q}:\{0,1\}^{X_v}\to\{0,1\}
\]

by

\[
f_{v,q}(\beta)=1
\quad\Longleftrightarrow\quad
q_v(\beta)=q.
\]

Because the transition computation is deterministic, the functions \(f_{v,q}\), for fixed \(v\), have pairwise disjoint model sets.

At a leaf labelled \(x\), create one node for every nonempty state preimage under \(\delta_v\). Its function is one of \(x\), \(\neg x\), or the constant one function when both bits map to the same state.

At an internal node \(v\) with children \(v_0,v_1\), create one TDD node \(g_{v,q}\) for every state \(q\in Q_v\) with nonempty preimage. Give it all child-node pairs

\[
(g_{v_0,q_0},g_{v_1,q_1})
\]

such that

\[
\delta_v(q_0,q_1)=q.
\]

Every child-state pair is assigned to exactly one parent state, so the TDD determinism condition holds. By induction on \(T\), node \(g_{v,q}\) computes exactly \(f_{v,q}\).

If \(F\) has more than one accepting root state, add a new root above \(T\) with a dummy fixed variable, or equivalently create one output node whose input relation is the disjoint union of the accepting root-state relations. The accepted root-state functions are pairwise disjoint, so determinism is preserved. This adds only linear overhead. Alternatively, quotient all accepting root states into one state before conversion.

The number of node-pair incidences is at most the number of explicit transition entries of \(M\), and the number of TDD nodes is at most \(\sum_v|Q_v|\). Thus the conversion has polynomial, in fact essentially linear, overhead in the explicit system size. \(\square\)

## 5. TDD to tree-state system

### Theorem 2

Every deterministic Tree Decision Diagram \(C\) respecting \(T\) can be converted into an explicit deterministic tree-state system computing the same Boolean function with size polynomial in \(|C|+|T|\) and the square of its width.

### Proof

For every tree node \(v\), take one state for each TDD node in \(N_v\), together with a rejecting sink \(\bot_v\).

At a leaf labelled \(x\), map each bit to the unique leaf node satisfied by that bit, if one exists, and otherwise to \(\bot_v\). Determinism of the TDD guarantees uniqueness.

At an internal node \(v\), for child states \(q_0,q_1\):

- if the corresponding TDD node pair occurs in the input relation of a parent node \(g\in N_v\), set \(\delta_v(q_0,q_1)=g\);
- otherwise set \(\delta_v(q_0,q_1)=\bot_v\).

TDD determinism guarantees that no pair belongs to two parent nodes. Pairs involving a sink map to the parent sink. The accepting set contains exactly the distinguished TDD output node.

An induction on the tree shows that a non-sink state is reached exactly when the assignment restrictions select the corresponding TDD certificate node. Hence the root accepts exactly the models of the TDD.

If the TDD width is \(w\), every transition table has at most \((w+1)^2\) entries and \(T\) has fewer than \(2|X|\) nodes. Thus the explicit system size is polynomial in \(|X|\) and \(w\), and polynomial in the fully explicit TDD representation. \(\square\)

## 6. Consequence

Explicit deterministic tree-state systems and deterministic Tree Decision Diagrams are polynomially equivalent as representations of Boolean query functions.

Therefore any superpolynomial TDD lower bound transfers immediately to this explicit tree-compositional state model, including assignment-target Subset Sum query families through `SS-ECB-003`.

## 7. Attack: does this subsume structural compression?

Not yet.

The previous route allowed arithmetic atoms such as:

- membership in an interval;
- membership in a progression \(a+q\mathbb Z\) over a bounded range;
- residue predicates with \(q\) encoded in binary;
- exception lists;
- recursive arithmetic composition.

A binary-encoded modulus \(q\) may be exponentially larger than its bit length. An explicit tree-state transition table that stores all residues can therefore be exponentially large even when the arithmetic predicate has a short program.

Conversely, permitting an arbitrary polynomial-time program as a transition destroys the representation barrier: the root program may simply evaluate the source formula or solve the query by any available algorithm.

Thus the exact inclusion question is unresolved:

> Which restricted succinct transition language is strong enough to express the retained structural summaries but weak enough to support unconditional lower bounds?

This is the smallest remaining model-definition gap.

## 8. Boundary cases

- A one-variable tree is handled entirely by the leaf map and accepting set.
- Empty variable sets can be represented by one root state and one acceptance bit.
- Unreachable states may be deleted without changing the function.
- Partial TDD transitions are made total only by sink states; this does not alter asymptotic size.
- The equivalence counts the complete transition structure. It does not treat a transition oracle as free.
