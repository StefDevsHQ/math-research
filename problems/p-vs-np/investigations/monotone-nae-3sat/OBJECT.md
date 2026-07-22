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
- the 3-uniform hypergraph \(H=(V,E)\) has Property B.

## Encoding

Use an indexed variable list and a list of ordered triples with pairwise distinct indices. Duplicate hyperedges may be removed in polynomial time. Let

\[
L=\Theta(n\log n+|E|\log n)
\]

under a conventional binary index encoding.

All runtime and state-size claims must be polynomial in \(L\), not merely in a numerical parameter or in the number of generated branches.

## Symmetries

If \(\sigma\) satisfies the instance, then \(1-\sigma\) also satisfies it. No instance can force an absolute colour without adding an external convention. Algorithms may quotient by this global complement symmetry, but must not confuse it with all local symmetries.

## Relation to controls

### Graph 2-colouring

For rank-two edges, the condition that every edge contain both colours is ordinary graph bipartiteness, decidable by breadth-first or depth-first search. The jump from edge size two to three is therefore a mandatory boundary test.

### XOR-SAT

For three variables, NAE is not equivalent to parity. XOR constraints are affine and solvable by Gaussian elimination; NAE constraints admit six local assignments and are not closed under the same affine operations.

### Positive 1-in-3 SAT

Positive 1-in-3 SAT permits only the assignments \(100,010,001\). Monotone NAE-3SAT additionally permits \(110,101,011\). The former breaks complement symmetry and imposes exact cardinality; the latter preserves complement symmetry and asks only for non-monochromaticity.

## Arity minimality

### Claim `NAE-003`

Every fixed-template Boolean CSP using only unary and binary relations reduces to 2-SAT.

### Proof

For a binary relation \(R\subseteq\{0,1\}^2\), the constraint \(R(x,y)\) is equivalent to

\[
\bigwedge_{(a,b)\notin R}((x\ne a)\lor(y\ne b)).
\]

Each conjunct is a clause of width at most two. Unary relations give unit clauses. Replacing every constraint in this way yields a 2-CNF formula of size at most four times the number of binary constraints, plus unary clauses. The transformation and 2-SAT decision procedure are polynomial.

Therefore an NP-complete fixed-template Boolean CSP must use a relation of arity at least three unless `P=NP`. Monotone NAE-3SAT attains arity three with one relation and no negations.

## Exact local-solution system

For \(S\subseteq V\), define

\[
\mathcal F_I(S)=\{a:S\to\{0,1\}:a\text{ satisfies every hyperedge contained in }S\}.
\]

For \(T\subseteq S\), restriction gives

\[
\rho_T^S(a)=a|_T.
\]

The instance is satisfiable exactly when \(\mathcal F_I(V)\ne\varnothing\).

## Future equivalence

For \(a,b\in\mathcal F_I(S)\), define

\[
a\equiv_{I,S}b
\]

if for every assignment \(c:V\setminus S\to\{0,1\}\),

\[
a\cup c\models I\iff b\cup c\models I.
\]

The quotient

\[
\mathcal Q_I(S)=\mathcal F_I(S)/{\equiv_{I,S}}
\]

is the exact semantic information about \(S\) relevant to all future completions.

This definition is exact but not yet algorithmic. The central unresolved issue is whether useful separators or decompositions admit polynomially many efficiently computable equivalence classes on every instance.
