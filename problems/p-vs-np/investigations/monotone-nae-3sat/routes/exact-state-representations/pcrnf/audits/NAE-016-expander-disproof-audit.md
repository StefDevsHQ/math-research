# Audit — NAE-016 Expander Disproof

**Claim:** `NAE-016`  
**Determination:** `DISPROVED / CHECKED`  
**Primary proof:** [central-lift expander disproof](../proofs/NAE-016-expander-disproof.md)  
**Audit date:** 2026-07-23

## 1. Quantifier audit

The conjecture asserts:

```text
for every instance H
there exists a polynomial-time constructible ordering pi
such that the complete reachable PCRNF state graph is polynomially bounded.
```

The refutation constructs an infinite family `H_n` satisfying:

```text
for every ordering pi
there exists a level i
with 2^{Omega(n)} reachable PCRNF states.
```

This reverses the existential ordering quantifier correctly. A single bad ordering would not suffice; the proof handles every ordering.

## 2. Imported assumption audit

The only imported existence theorem is an infinite family of finite simple constant-degree edge expanders:

```text
|delta(U)| >= h |U|
```

for every `|U| <= |V|/2`, with constants `d` and `h` independent of the family member.

The project proof uses no stronger expander property. Ramanujan graph families are one standard source.

## 3. Central-lift audit

For each graph edge `{u,v}`, the lift contains `{c,u,v}`.

- with `c=0`, NAE forbids only `u=v=0`, so the residual clause is `u or v`;
- with `c=1`, NAE forbids only `u=v=1`, giving the dual clause;
- the construction is a simple three-uniform hypergraph when the graph is simple;
- duplicate graph edges are normalized away.

No satisfiability direction is lost.

## 4. Centre-position audit

The centre may occur first, last, or between graph vertices.

For an arbitrary ordering, the proof stops immediately after the first `floor(n/2)` graph vertices have appeared.

- if `c` is already processed, every constructed prefix assigns `c=0`;
- if `c` is unprocessed, every distinguishing suffix assigns `c=0`.

The processed graph set and unprocessed graph set are therefore the same balanced cut in all centre positions. No step assumes that the centre is first.

## 5. Induced-matching audit

The greedy process selects a crossing edge `uv` and removes every crossing edge with an endpoint in `N[u] union N[v]`.

Consequences:

- selected edges are vertex-disjoint;
- no endpoint of one selected edge is adjacent to an endpoint of another;
- hence the selected edges form an induced matching in the whole graph, not merely in the crossing bipartite subgraph.

For maximum degree `d`, one selection removes at most

```text
|N[u] union N[v]| d <= (2d+2)d = 2d(d+1)
```

crossing edges. This deliberately uses a loose valid constant. Thus a cut with `F` crossing edges yields at least `F/(2d(d+1))` selected edges.

Expansion of the balanced cut yields a matching of size `Omega(n)`.

## 6. Prefix liveness audit

For a subset `S` of matching indices, the only zero graph vertices in the proposed full extension are the processed left endpoints `u_j` with `j in S`.

Because the matching is induced, these vertices are pairwise nonadjacent. Every graph edge therefore has a `1` endpoint. With `c=0`, every lifted edge is nonmonochromatic.

Thus all `2^k` constructed prefixes are live. The lower bound is not produced by dead-state duplication.

## 7. Pairwise-separation audit

For distinct subsets `S` and `T`, choose `j in S\T` after swapping their names if needed.

The distinguishing suffix sets only `v_j=0` among suffix graph vertices.

- under `S`, `c=u_j=v_j=0`, so one lifted edge fails;
- under `T`, `u_j=1`;
- `v_j` is nonadjacent to every zero `u_t`, `t in T`, by inducedness;
- zero left endpoints in `T` are pairwise nonadjacent;
- all remaining graph vertices are `1`.

Therefore the same suffix is rejected under `S` and accepted under `T`. Every pair of prefixes has different exact labelled completion functions.

## 8. PCRNF transfer audit

`NAE-017` gives:

```text
same oriented PCRNF => same exact labelled completion function.
```

The contrapositive gives:

```text
different completion functions => different oriented PCRNFs.
```

The proof does not require the false converse disproved by `NAE-018`. PCRNF semantic incompleteness can only increase the state count.

## 9. Encoding audit

For constant degree `d`, the lifted instance has:

```text
n+1 vertices,
O(n) hyperedges,
O(n log n) binary encoding length L.
```

Therefore

```text
2^{Omega(n)} = 2^{Omega(L/log L)},
```

which is superpolynomial in `L`.

The argument does not confuse pseudo-polynomial and polynomial complexity.

## 10. Computational controls

The committed tests verify:

- central-lift truth tables for both centre colours;
- every ordering and every centre position for `K_4`;
- every ordering and every centre position for `K_{3,3}`;
- explicit centre-first, centre-middle, and centre-last matching controls;
- induced-matching verification;
- the greedy deletion bound;
- liveness and pairwise distinct completion masks for all generated certificate prefixes.

Reproducible command from the repository root:

```text
./scripts/check.sh fast
```

The finite tests support the proof but are not used as the universal argument.

## 11. Failed break attempts

The proof was attacked on:

- centre before, inside, and after the balanced graph prefix;
- odd graph sizes using `floor(n/2)`;
- internal edges within either side of the cut;
- extra crossing edges outside the selected matching;
- possible adjacency among zero left endpoints;
- possible adjacency from the distinguishing `v_j` to other zero left endpoints;
- PCRNF orientation canonicalization;
- dead prefixes;
- input encoding size;
- the distinction between state count and collective representation size.

No contradiction was found.

## 12. Final scope

The result proves an all-ordering exponential lower bound for:

- oriented PCRNF state enumeration;
- exact ordered state-per-residual-function quotients;
- reduced ordered binary decision diagrams through the standard residual-subfunction argument.

It does not prove a lower bound for:

- arbitrary circuits;
- arbitrary decomposable circuits;
- non-ordered branching programs;
- algebraic global methods;
- arbitrary algorithms.

No conclusion about `P=NP` or `P!=NP` follows.