# NAE-021 — DNNF Lower Bound for Central-Lift Expanders

**Claim:** `NAE-021`  
**Status:** `PROVED / CHECKED`  
**Proof type:** project reduction to an established knowledge-compilation lower bound  
**Scope:** DNNF representations of the exact satisfying-assignment function

## 1. Exact claim

There are constants `d >= 3`, `h > 0`, and `alpha > 0`, and an infinite family of finite simple `d`-regular graphs `G_n=(V_n,E_n)` with `|V_n|=n`, such that their central lifts

```text
H(G_n) = (V_n union {c}, {{c,u,v} : {u,v} in E_n})
```

have the following property:

> Every decomposable negation normal form circuit computing the exact satisfying-assignment function of `H(G_n)` has size at least `2^(alpha n)`.

Under the canonical binary encoding of the lifted Monotone NAE-3SAT instance, whose length is `L=O(n log n)`, this is

```text
2^{Omega(n)} = 2^{Omega(L/log L)}.
```

The same lower bound therefore holds for every subclass of DNNF, including deterministic DNNF, structured DNNF, deterministic structured DNNF, and decision DNNF.

## 2. Imported results

### 2.1 Constant-degree expanders

As in `NAE-020`, use an infinite family of finite simple `d`-regular graphs satisfying

```text
|delta(U)| >= h |U|
```

for every nonempty `U subseteq V_n` with `|U| <= n/2`, where `d` and `h` are constants independent of `n`.

One standard source is the explicit constant-degree Ramanujan graph construction of Lubotzky, Phillips, and Sarnak together with the spectral isoperimetric inequality.

### 2.2 DNNF lower bound for monotone CNFs

Amarilli, Capelli, Monet, and Senellart, *Connecting Knowledge Compilation Classes and Width Parameters*, Theory of Computing Systems 64:861–914 (2020), Corollary 8.5, prove:

> For monotone CNF formulas of constant arity and constant degree, the size of the smallest DNNF is `2^{Omega(tw(phi))}`, where `tw(phi)` is the treewidth of the clause hypergraph.

The constants hidden by `Omega` may depend on the fixed arity and degree bounds. The theorem applies to unstructured, nondeterministic DNNFs; no structuredness or determinism assumption is required.

Primary sources:

- DOI: `10.1007/s00224-019-09930-2`
- Extended version: `arXiv:1811.02944`

## 3. Conditioning the central lift

Let `F_n(c,V_n)` denote the exact Boolean satisfying-assignment function of `H(G_n)`.

For one lifted edge,

```text
NAE(0,u,v) iff u or v.
```

Therefore conditioning the centre to zero gives

```text
F_n|_{c=0} = phi_{G_n}
```

where

```text
phi_{G_n} = and_{{u,v} in E_n} (u or v).
```

This is a monotone two-CNF.

## 4. Conditioning preserves DNNF without size increase

Let `D_n` be any DNNF computing `F_n`.

Replace every literal involving `c` by its value under `c=0`, and propagate constants through the circuit. For every AND gate, its children still mention pairwise disjoint variable sets after variables are removed, so decomposability is preserved. No new gate or wire is required.

Hence the conditioned circuit `D_n|_{c=0}` is a DNNF computing `phi_{G_n}` and

```text
|D_n| >= |D_n|_{c=0}|.
```

It is therefore enough to lower-bound DNNFs for `phi_{G_n}`.

## 5. Formula arity and degree

The clause hypergraph of `phi_{G_n}` has:

- one vertex for every graph vertex in `V_n`;
- one hyperedge `{u,v}` for every edge of `G_n`.

It is exactly the graph `G_n` viewed as a rank-two hypergraph. Consequently:

```text
arity(phi_{G_n}) = 2,
degree(phi_{G_n}) = d,
tw(phi_{G_n}) = tw(G_n).
```

The arity and degree bounds are constants, as required by the imported DNNF theorem.

## 6. Expander treewidth lemma

### Lemma

For the fixed constants `d` and `h`, every graph `G_n` in the family satisfies

```text
tw(G_n) >= h n/(4d) - 1.
```

### Proof

Let `k=tw(G_n)` and fix a tree decomposition of width `k`.

A graph of treewidth `k` has a vertex separator `S` with

```text
|S| <= k+1
```

such that every connected component of `G_n-S` has at most `n/2` vertices. For completeness, this follows directly from the tree decomposition: assign every graph vertex to one bag containing it, choose a weighted centroid bag of the decomposition tree, and remove the vertices of that bag. Each remaining graph component is contained in one component of the decomposition tree after deleting the centroid bag, hence has at most half of the assigned weight.

Because `G_n` is `d`-regular, `|delta(U)| <= d|U|` for every `U`, so the expansion constant satisfies `h <= d`.

If `|S| >= n/4`, then

```text
|S| >= n/4 >= h n/(4d),
```

and the desired conclusion follows immediately from `|S| <= k+1`.

Assume therefore that `|S| < n/4`. More than `3n/4` vertices remain in the components of `G_n-S`. Choose a union `U` of these components with

```text
n/4 <= |U| <= n/2.
```

Such a union now exists. If some component has size between `n/4` and `n/2`, use it. Otherwise every component has size below `n/4`; greedily add components until the union first reaches `n/4`. The previous partial union had size below `n/4`, and the last added component also has size below `n/4`, so the resulting union has size below `n/2`.

There are no edges from `U` to `V_n \ (U union S)`. Thus every edge of `delta(U)` has an endpoint in `S`. Since the maximum degree is `d`,

```text
|delta(U)| <= d |S|.
```

Expansion gives

```text
h |U| <= |delta(U)| <= d |S|.
```

Using `|U| >= n/4`,

```text
|S| >= h n/(4d).
```

Since `|S| <= k+1`,

```text
k >= h n/(4d) - 1.
```

This proves `tw(G_n)=Omega(n)`. `QED`

## 7. DNNF lower bound

Apply the imported theorem to `phi_{G_n}`. It is a monotone CNF of constant arity two, constant degree `d`, and treewidth `Omega(n)`. Therefore every DNNF computing it has size

```text
2^{Omega(tw(phi_{G_n}))} = 2^{Omega(n)}.
```

By the conditioning argument, every DNNF computing the original central-lift function `F_n` has at least this size.

## 8. Encoding audit

The central lift has:

```text
n+1 variables,
|E_n| = dn/2 = O(n) constraints.
```

With binary vertex labels, its complete input length is

```text
L = O(n log n).
```

Hence

```text
2^{Omega(n)} = 2^{Omega(L/log L)},
```

which exceeds every polynomial in `L`.

## 9. Conclusion

```text
NAE-021 — PROVED / CHECKED.
```

The central-lift expander family has exponential DNNF size. Thus `R1.4` fails as a universal polynomial exact-representation route, even before imposing determinism, structuredness, canonicity, or efficient construction.

## 10. Scope boundary

This result does not prove a lower bound for:

- unrestricted Boolean circuits;
- algebraic representations not polynomially translatable to DNNF;
- non-DNNF collective data structures;
- arbitrary algorithms.

It does not prove `P!=NP`, and it does not formally disprove the representation-independent conjecture `NAE-006`.

Restricted DNNF compilation remains valid on bounded-treewidth and other explicitly tractable classes.
