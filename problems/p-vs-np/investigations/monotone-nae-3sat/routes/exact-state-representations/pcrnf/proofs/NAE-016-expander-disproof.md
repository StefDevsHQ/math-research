# NAE-016 Disproof — Central Lifts of Constant-Degree Expanders

**Claim attacked:** `NAE-016`  
**Final status:** `DISPROVED / CHECKED`  
**Proof type:** explicit infinite-family lower bound with one imported expander-existence theorem  
**Scope:** fixed-order PCRNF traversal and any exact state-per-residual-function quotient

## 1. Claim

`NAE-016` asserted that every encoded Monotone NAE-3SAT instance has a polynomial-time constructible variable ordering for which memoized traversal by propagation-closed signed residual normal forms has only polynomially many distinct states, polynomial maximum and total encoded state, and polynomial-time exact operations.

It is enough to refute the existential ordering quantifier by constructing an infinite family `H_n` such that every ordering has superpolynomially many reachable PCRNF states at some level.

## 2. Imported graph theorem

Use the standard existence of constants `d >= 3` and `h > 0` and an infinite family of finite simple `d`-regular graphs `G_n=(V_n,E_n)` satisfying

```text
|delta(U)| >= h |U|
```

for every `U subseteq V_n` with `1 <= |U| <= |V_n|/2`.

This follows, for example, from explicit constant-degree Ramanujan graph families together with the discrete spectral isoperimetric inequality. The proof below uses only the displayed edge-expansion property and the constant degree bound.

## 3. Central lift

For a simple graph `G=(V,E)`, introduce one new centre vertex `c` and define the three-uniform hypergraph

```text
H(G) = (V union {c}, {{c,u,v} : {u,v} in E}).
```

This is a valid Monotone NAE-3SAT instance.

If `c=0`, then one lifted edge satisfies

```text
NAE(0,u,v) iff u or v.
```

Thus the conditioned instance is the monotone two-CNF

```text
phi_G = and_{{u,v} in E} (u or v).
```

If `c=1`, the conditioned instance is its colour-complemented dual. Only the `c=0` conditioning is needed below.

## 4. Semantic projection lemma — NAE-019

Fix an instance `H`, ordering `pi`, and level `i`. For a prefix `a in {0,1}^i`, let `F_a` be its exact labelled completion function on the common suffix variables, and let `P_a` be its oriented PCRNF.

By `NAE-017`, for every suffix assignment `q`,

```text
F_a(q)=1 iff q satisfies P_a.
```

Therefore

```text
P_a = P_b  implies  F_a = F_b.
```

Equivalently, distinct completion functions require distinct PCRNF states. Hence at every level

```text
number of PCRNF states >= number of exact completion classes.
```

This uses soundness only. Semantic incompleteness of PCRNF byte equality can increase the PCRNF count but cannot invalidate the lower bound.

## 5. Balanced cut for an arbitrary ordering

Let `G=(V,E)` have `n` vertices and maximum degree at most `d`, and let `pi` be any ordering of `V union {c}`.

Delete `c` from `pi` and let `U` be the first `m=floor(n/2)` graph vertices in the resulting graph-vertex order. Let `W=V\U`.

In the original ordering, stop immediately after the `m`-th graph vertex. The processed variables are exactly `U`, together with `c` if the centre happened to appear earlier. Thus this defines one legitimate common prefix level for all assignments used below.

For an expander graph,

```text
|E(U,W)| >= h m.
```

The position of `c` is irrelevant: if already processed it will be assigned zero in every constructed prefix; otherwise it will be assigned zero in every distinguishing completion.

## 6. Crossing induced-matching lemma

### Lemma

If `G` has maximum degree at most `d`, then every cut `(U,W)` contains an induced matching of crossing edges of size at least

```text
|E(U,W)| / (2 d(d+1)).
```

### Proof

Start with all crossing edges. Repeatedly select one crossing edge `uv`, with `u in U` and `v in W`, and delete every remaining crossing edge having an endpoint in `N[u] union N[v]`.

Any later selected edge has neither endpoint equal or adjacent to an endpoint of an earlier selected edge. Hence the selected edges form an induced matching in the whole graph.

The set `N[u] union N[v]` has at most `2d+2` vertices. Each such vertex is incident with at most `d` crossing edges. Therefore one selection deletes at most `(2d+2)d=2d(d+1)` crossing edges. The stated lower bound follows. `QED`

For the balanced cut of an expander, this gives an induced matching

```text
M = {(u_1,v_1),...,(u_k,v_k)}
```

with `u_j in U`, `v_j in W`, and

```text
k >= h floor(n/2) / (2d(d+1)) = Omega(n).
```

## 7. Exponentially many live prefixes

For every subset `S subseteq {1,...,k}`, define one assignment `a_S` to the processed variables:

```text
u_j = 0  if j in S,
u_j = 1  if j not in S,
all other graph vertices in U = 1,
c = 0 if c is already processed.
```

### Liveness

Complete `a_S` by assigning every graph vertex in `W` the value `1`, and assign `c=0` if it is still unprocessed.

The only zero graph vertices are selected vertices `u_j` with `j in S`. Since `M` is induced, these left endpoints are pairwise nonadjacent. Therefore every graph edge has at least one endpoint coloured `1`. With `c=0`, every lifted NAE edge is nonmonochromatic.

Thus every one of the `2^k` prefixes is live.

## 8. Pairwise semantic separation

Take distinct subsets `S` and `T`. After exchanging their names if needed, choose `j in S \ T`.

Define a suffix assignment `q_j` by

```text
v_j = 0,
all other graph vertices in W = 1,
c = 0 if c is unprocessed.
```

Under prefix `a_S`, the lifted edge `{c,u_j,v_j}` receives `000`, so `q_j` is rejected.

Under prefix `a_T`, the graph vertices coloured zero are `v_j` together with the vertices `u_t` for `t in T`.

- `u_j=1` because `j notin T`;
- distinct left endpoints of an induced matching are nonadjacent;
- `v_j` is not adjacent to `u_t` for any `t != j`;
- every other suffix graph vertex is `1`.

Hence no graph edge has two zero endpoints. With `c=0`, every lifted NAE edge is satisfied, so `q_j` is accepted.

Therefore the exact completion functions of `a_S` and `a_T` differ.

The selected level consequently has at least

```text
2^k = 2^{Omega(n)}
```

exact completion classes. By `NAE-019`, it has at least that many oriented PCRNF states.

## 9. Encoding audit

The central lift has `n+1` vertices and `|E(G)| <= dn/2 = O(n)` hyperedges. Under the canonical binary encoding, each vertex label uses `O(log n)` bits, so the complete input length satisfies

```text
L = O(n log n).
```

The state lower bound is therefore

```text
2^{Omega(n)} = 2^{Omega(L/log L)},
```

which exceeds every polynomial in `L`.

The lower bound holds for every variable ordering, so it also holds for every polynomial-time constructible ordering algorithm.

## 10. Conclusion — NAE-020

There exists an infinite family of Monotone NAE-3SAT instances such that, for every variable ordering, one prefix level has `2^{Omega(n)}` pairwise distinct live exact completion functions and therefore `2^{Omega(n)}` distinct oriented PCRNF states.

Consequently, no ordering can make the complete PCRNF state graph polynomially bounded on all instances.

```text
NAE-016 — DISPROVED / CHECKED.
```

## 11. Boundary of the result

This theorem does not refute:

- exactness of PCRNF (`NAE-017`);
- polynomial PCRNF behaviour on restricted classes;
- a representation that stores many residual functions collectively rather than as separate ordered states;
- decomposable or non-ordered circuits not subject to this state-enumeration model;
- algebraic or global algorithms;
- `NAE-006` in its broad representation-independent form;
- `P=NP` or `P!=NP`.

It also yields the same all-ordering residual-subfunction obstruction for reduced ordered binary decision diagrams of the lifted instances. That is an ordered-representation corollary, not a lower bound for arbitrary decision diagrams or circuits.