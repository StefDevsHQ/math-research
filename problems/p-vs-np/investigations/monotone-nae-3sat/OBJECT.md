# Object Specification — Monotone NAE-3SAT

## Decision problem

**Input:** A finite set of variables \(V=\{x_1,\ldots,x_n\}\) and a family \(E\) of 3-element subsets of \(V\).

**Question:** Does there exist \(\sigma:V\to\{0,1\}\) such that for every \(e=\{u,v,w\}\in E\),

\[
(\sigma(u),\sigma(v),\sigma(w))\notin\{(0,0,0),(1,1,1)\}?
\]

Equivalent forms:

- every hyperedge contains both colours;
- every constraint satisfies \(1\le x_u+x_v+x_w\le 2\);
- the 3-uniform hypergraph \(H=(V,E)\) has Property B;
- the vertex set can be split into two sets, each meeting every hyperedge.

Primary sources are listed in [references/SOURCES.md](references/SOURCES.md).

## Encoding and normalization

Use indexed variables and a list of triples with pairwise distinct indices. Under a conventional binary index encoding,

\[
L=O((n+|E|)\log(n+1)).
\]

If the input explicitly lists every variable, including isolated variables, the same expression is also a matching bound up to conventional delimiters.

Polynomial preprocessing may:

- sort every triple and remove duplicate hyperedges;
- remove isolated vertices, which never affect satisfiability;
- split the hypergraph into connected components of its incidence graph;
- reject malformed triples containing repeated indices under the selected simple-hypergraph canon.

The whole instance is satisfiable exactly when every connected component is satisfiable. Runtime, memory, and intermediate-state claims must be polynomial in the complete encoded length \(L\).

## Symmetry

If \(\sigma\) satisfies an instance, then \(1-\sigma\) also satisfies it. Each nonempty connected component may therefore fix one chosen vertex to colour zero without changing satisfiability.

This removes one global bit per component. It does not remove the remaining logical compatibility and cannot by itself change an exponential state space into a polynomial one.

## Minimal non-monochromatic frontier

For integers \(q,k\ge 2\), let \(\operatorname{NMC}(q,k)\) ask whether a \(k\)-uniform hypergraph has a \(q\)-colouring with no monochromatic edge.

The nearest easy and hard cases are:

| Object | Parameters | Complexity role |
|---|---:|---|
| graph bipartiteness | \(\operatorname{NMC}(2,2)\) | polynomial-time control |
| Monotone NAE-3SAT | \(\operatorname{NMC}(2,3)\) | NP-complete Boolean hard corner |
| graph 3-colouring | \(\operatorname{NMC}(3,2)\) | NP-complete binary-relation hard corner |

This is a project organizing canon, not a new complexity theorem. It isolates the first hard step obtained by increasing either edge size or domain size from two to three.

## Relation to controls

### Graph 2-colouring

For rank-two edges, requiring both colours on every edge is ordinary bipartiteness. The jump from edge size two to three is the primary local-complexity boundary.

### XOR-SAT

NAE is not parity. XOR constraints are affine and solvable by Gaussian elimination. NAE constraints admit six local assignments but lack the affine closure that makes XOR-SAT compact.

XOR-SAT is also a warning: an explicit set of continuation behaviours may be large even when a compact symbolic linear-algebra representation exists. State count and representation size must therefore be audited separately.

### Positive 1-in-3 SAT

Positive 1-in-3 SAT permits only \(100,010,001\). Monotone NAE-3SAT additionally permits \(110,101,011\). The former imposes exact cardinality and breaks complement symmetry; the latter asks only for non-monochromaticity.

### Known structural borders

The attack programme must preserve the distinctions between:

- rank two, which is bipartite checking;
- bounded incidence or primal width, which supports dynamic programming;
- monotone NAE-3SAT with variable occurrence at most three, which has known polynomial algorithms;
- planar NAE-3SAT, which is polynomial-time decidable;
- linear, 4-regular Monotone NAE-3SAT, which remains NP-complete.

## Arity minimality

### Claim `NAE-003`

Every fixed-template Boolean CSP using only unary and binary relations reduces to 2-SAT.

### Proof

For a binary relation \(R\subseteq\{0,1\}^2\), the constraint \(R(x,y)\) is equivalent to

\[
\bigwedge_{(a,b)\notin R}((x\ne a)\lor(y\ne b)).
\]

Each forbidden tuple contributes one clause of width at most two. Unary relations give unit clauses. This remains valid for the empty and universal relations and when the same variable occupies both argument positions, after ordinary clause simplification.

Replacing every constraint yields a 2-CNF formula with at most four clauses per binary constraint. Construction and 2-SAT decision are polynomial.

Therefore a fixed-template Boolean CSP cannot be NP-complete using only unary and binary relations unless `P=NP`. Monotone NAE-3SAT reaches the first possible arity, three, using one relation and no negations. ∎

## Exact extension profiles

Fix a variable ordering

\[
\pi=(v_1,\ldots,v_n).
\]

Let \(P_i=\{v_1,\ldots,v_i\}\) and \(R_i=V\setminus P_i\). For every assignment \(a:P_i\to\{0,1\}\), define its exact completion set

\[
\operatorname{Ext}_{I,i}(a)=
\{c:R_i\to\{0,1\}:a\cup c\models I\}.
\]

Define

\[
a\equiv_{I,i} b
\quad\Longleftrightarrow\quad
\operatorname{Ext}_{I,i}(a)=\operatorname{Ext}_{I,i}(b).
\]

Assignments with no completion form one dead equivalence class. The quotient is

\[
\mathcal Q_{I,i}=\{0,1\}^{P_i}/\!\equiv_{I,i}.
\]

### Claim `NAE-004` — exact quotient transition theorem

For every fixed ordering, appending the next colour induces a well-defined transition on exact extension classes. If all quotient states and transitions can be constructed explicitly with polynomial total encoded size and polynomial construction cost, satisfiability is decidable in polynomial time.

### Proof

Assume \(a\equiv_{I,i}b\). For \(d\in\{0,1\}\) and every assignment \(c:R_{i+1}\to\{0,1\}\),

\[
a\cup\{v_{i+1}=d\}\cup c\models I
\iff
b\cup\{v_{i+1}=d\}\cup c\models I,
\]

because \(\{v_{i+1}=d\}\cup c\) is an assignment of \(R_i\). Thus the successor class does not depend on the representative.

Starting from the unique class at \(P_0=\varnothing\), follow both colour transitions at each level. At \(P_n=V\), a class is accepting exactly when its assignments satisfy \(I\); the other class is dead. Explicit polynomial construction and polynomial total state therefore give a deterministic polynomial-time decision procedure. ∎

This theorem is conditional on explicit construction. It does not show that the quotient is small or efficiently computable.

## Bounded-boundary dynamic programming

For ordering \(\pi\), define the processed boundary

\[
B_i=\{u\in P_i:\exists e\in E\text{ with }u\in e\text{ and }e\cap R_i\ne\varnothing\}.
\]

Let

\[
w_\pi(I)=\max_i |B_i|.
\]

### Claim `NAE-005` — bounded-boundary algorithm

Given \(I\) and \(\pi\), Monotone NAE-3SAT is decidable in

\[
2^{O(w_\pi(I))}\operatorname{poly}(L)
\]

time and space.

### Proof

At level \(i\), retain each colouring of \(B_i\) that extends to a colouring of \(P_i\) satisfying every hyperedge contained in \(P_i\). When \(v_{i+1}\) is introduced, try both colours, check every newly completed hyperedge, and forget any processed vertex no longer incident to an unprocessed hyperedge.

A forgotten vertex cannot occur in a future constraint by definition of \(B_i\), so forgetting it loses no future information. Induction on \(i\) gives exact soundness and completeness. There are at most \(2^{|B_i|}\) states at a level and polynomial work per generated transition. At \(i=n\), the boundary is empty and the empty state exists exactly when the full hypergraph is 2-colourable. ∎

This is a restricted-width theorem. A universal P-versus-NP route requires a new mechanism when every useful ordering has large boundary.

## Central open question

The exact semantic quotient is well-defined, and bounded interfaces yield an exact algorithm. The unresolved problem is whether a more powerful symbolic representation can preserve all completion information on every instance while keeping construction, transitions, evaluation, and total encoded state polynomial.
