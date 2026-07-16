# Grid-Family Ordered Query-Representation Barrier

**Claims:** `SS-ECB-005`, `SS-ECB-006`  
**Status:** `ESTABLISHED / CHECKED` for the imported OBDD theorem; `PROVED / CHECKED` for the project grid bound and transfer  
**Proof type:** External theorem plus project combinatorial proof  
**Updated:** 2026-07-16

## 1. Hard Boolean family

For an even integer \(r\ge 2\), let \(G_r\) be the \(r\times r\) square grid graph with vertex set

\[
V(G_r)=[r]\times[r]
\]

and horizontal or vertical adjacency. Let

\[
\varphi_r=\bigwedge_{\{u,v\}\in E(G_r)}(x_u\vee x_v).
\]

This monotone two-CNF has \(N=r^2\) variables and \(M=2r(r-1)<2r^2\) clauses. Apply the assignment-target construction, obtaining a fixed item multiset \(A_r\) and targets \(\tau_r(\alpha)\).

## 2. Imported OBDD lower bound

For a graph \(G\), let \(lu(G)\) denote its linear upper induced-matching width. Razgon proves

\[
\operatorname{obdd}(\varphi(G))\ge 2^{lu(G)}.
\]

Source: Igor Razgon, “Classification of OBDD size for monotone 2-CNFs,” arXiv:2103.09115v2, Theorem 2, 2021.

## 3. Balanced grid-cut lemma

### Lemma 1

For every subset \(U\subseteq V(G_r)\) with \(|U|=r^2/2\), at least \(r/2\) grid edges cross from \(U\) to its complement.

### Proof

For row \(i\), let

\[
S_i=\{j:(i,j)\in U\},\qquad u_i=|S_i|.
\]

Call row \(i\) mixed when \(0<u_i<r\), and let \(q\) be the number of mixed rows. Every mixed row has at least one horizontal crossing edge. Between rows \(i\) and \(i+1\), the number of vertical crossing edges is

\[
|S_i\triangle S_{i+1}|\ge |u_i-u_{i+1}|.
\]

Thus

\[
b(U)\ge q+\sum_{i=1}^{r-1}|u_i-u_{i+1}|.
\]

If \(q\ge r/2\), the result follows. Assume \(q<r/2\). If no row is empty, every nonmixed row is full, yielding

\[
|U|=\sum_i u_i\ge (r-q)r>r^2/2,
\]

a contradiction. If no row is full, only the \(q\) mixed rows contain vertices of \(U\), yielding

\[
|U|<qr<r^2/2,
\]

also a contradiction. Hence some row has count zero and another count \(r\), so

\[
\sum_{i=1}^{r-1}|u_i-u_{i+1}|\ge r.
\]

Therefore \(b(U)\ge r\). \(\square\)

## 4. Induced matching extraction

For \(U\subseteq V(G_r)\), let \(G_r^U\) be the upper subgraph used in the definition of \(lu\): delete edges whose two endpoints both lie outside \(U\).

### Lemma 2

If the cut has \(b\) crossing edges, then \(G_r^U\) contains an induced crossing matching of size at least \(b/41\).

### Proof

Construct a conflict graph on the crossing edges. Two crossing edges conflict if they share an endpoint or if an endpoint of one is adjacent in \(G_r^U\) to an endpoint of the other. An independent set is an induced crossing matching.

For a crossing edge \(e=xy\), every conflicting crossing edge is incident to a vertex in

\[
N_{G_r^U}[x]\cup N_{G_r^U}[y].
\]

This union has at most ten vertices, each incident to at most four crossing edges. The closed conflict neighborhood therefore has size at most forty. A greedy independent-set algorithm selects at least \(b/41\) edges. \(\square\)

## 5. Grid width

For any vertex ordering, take the prefix \(U\) of length \(r^2/2\). Lemma 1 gives at least \(r/2\) crossing edges, and Lemma 2 gives an induced crossing matching of size at least

\[
\frac{r/2}{41}=\frac r{82}.
\]

Thus

\[
lu(G_r)\ge \frac r{82}.
\]

## 6. Ordered graph-size lower bound

By the OBDD equivalence and Razgon's theorem, every ordered assignment-target query graph for \((A_r,\tau_r)\), under every variable order, has size at least

\[
2^{lu(G_r)}\ge 2^{r/82}.
\]

## 7. Binary input-length accounting

The construction has fewer than \(6r^2\) items and fewer than \(4r^2\) base-ten columns. Every encoded integer has \(O(r^2)\) binary digits, so the total binary length \(L_r\) of the item multiset and one target satisfies

\[
L_r=O(r^4).
\]

Therefore

\[
|Q|=2^{\Omega(L_r^{1/4})}.
\]

## 8. Scope

This is an ordered Boolean query-representation lower bound. It is not a lower bound for a fixed Subset Sum target, arbitrary target-query algorithms, or the structural-summary language from the closed route.