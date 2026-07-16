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

and horizontal or vertical adjacency.

Let

\[
\varphi_r=\bigwedge_{\{u,v\}\in E(G_r)}(x_u\vee x_v).
\]

This is a monotone two-CNF with

\[
N=r^2
\]

variables and

\[
M=2r(r-1)<2r^2
\]

clauses.

Apply the assignment-target construction from [Assignment-target embedding and OBDD equivalence](assignment-target-obdd-transfer.md), obtaining a fixed item multiset \(A_r\) and targets \(\tau_r(\alpha)\).

## 2. Imported OBDD lower bound

For a graph \(G\), let \(lu(G)\) denote its linear upper induced-matching width.

Razgon proves that for the monotone two-CNF \(\varphi(G)\),

\[
\operatorname{obdd}(\varphi(G))\ge 2^{lu(G)}.
\]

Source: Igor Razgon, “Classification of OBDD size for monotone 2-CNFs,” arXiv:2103.09115v2, Theorem 2, 2021.

It remains to prove a linear lower bound on \(lu(G_r)\).

## 3. Balanced grid-cut lemma

### Lemma 1

For every subset \(U\subseteq V(G_r)\) with \(|U|=r^2/2\), at least \(r/2\) grid edges have one endpoint in \(U\) and the other in \(V(G_r)\setminus U\).

### Proof

For row \(i\), let

\[
S_i=\{j:(i,j)\in U\},
\qquad
u_i=|S_i|.
\]

Call row \(i\) mixed when \(0<\nu_i<r\), and let \(q\) be the number of mixed rows.

Every mixed row contains at least one horizontal crossing edge because the row is a path containing vertices on both sides of the cut. Between consecutive rows \(i\) and \(i+1\), the number of vertical crossing edges is

\[
|S_i\triangle S_{i+1}|\ge |\nu_i-\nu_{i+1}|.
\]

Hence the total number \(b(U)\) of crossing edges satisfies

\[
b(U)\ge q+\sum_{i=1}^{r-1}|\nu_i-\nu_{i+1}|.
\]

If \(q\ge r/2\), then \(b(U)\ge r/2\).

Assume \(q<r/2\). If no row has \(\nu_i=0\), then every nonmixed row is full, so

\[
|U|=\sum_i\nu_i\ge (r-q)r>r^2/2,
\]

a contradiction. If no row has \(\nu_i=r\), then only the \(q\) mixed rows contain vertices of \(U\), so

\[
|U|<qr<r^2/2,
\]

also a contradiction.

Therefore some row has count \(0\) and another has count \(r\). The total variation of the sequence \((\nu_i)\) is at least \(r\):

\[
\sum_{i=1}^{r-1}|\nu_i-\nu_{i+1}|\ge r.
\]

Thus \(b(U)\ge r\), which is stronger than required. \(\square\)

## 4. Induced matching extraction

For \(U\subseteq V(G_r)\), let \(G_r^U\) be the upper subgraph used in the definition of \(lu\): delete all edges whose two endpoints lie in \(V(G_r)\setminus U\), while retaining edges inside \(U\) and edges crossing the cut.

### Lemma 2

If the cut \((U,V(G_r)\setminus U)\) has \(b\) crossing edges, then \(G_r^U\) contains an induced crossing matching of size at least \(b/41\).

### Proof

Construct a conflict graph \(K\) whose vertices are the crossing edges. Two crossing edges conflict if they share an endpoint or if an endpoint of one is adjacent in \(G_r^U\) to an endpoint of the other. An independent set in \(K\) is therefore an induced crossing matching in \(G_r^U\).

Fix a crossing edge \(e=xy\). Every crossing edge that conflicts with \(e\) is incident to a vertex in

\[
N_{G_r^U}[x]\cup N_{G_r^U}[y].
\]

The grid has maximum degree at most four, so this union contains at most ten vertices. Each such vertex is incident to at most four crossing edges. Thus the closed conflict neighborhood of \(e\) contains at most forty crossing edges, and \(K\) has maximum degree at most thirty-nine, hence certainly at most forty.

A greedy independent-set algorithm selects at least \(b/41\) vertices of \(K\). Their corresponding grid edges form an induced crossing matching in \(G_r^U\). \(\square\)

## 5. Linear upper induced-matching width of the grid

### Lemma 3

For every even \(r\),

\[
lu(G_r)\ge \frac{r}{82}.
\]

### Proof

Take an arbitrary ordering of the \(r^2\) vertices and let \(U\) be its prefix of length \(r^2/2\).

By Lemma 1, the cut has at least \(r/2\) crossing edges. By Lemma 2, the upper subgraph \(G_r^U\) contains an induced crossing matching of size at least

\[
\frac{r/2}{41}=\frac{r}{82}.
\]

This holds for every vertex ordering. Therefore the maximum prefix width of every ordering is at least \(r/82\), and taking the minimum over orderings gives the claim. \(\square\)

## 6. Ordered graph-size lower bound

### Theorem

Every deterministic ordered assignment-target query graph for \((A_r,\tau_r)\), under every variable order, has size at least

\[
2^{r/82}.
\]

### Proof

By `SS-ECB-004`, the query graph is exactly an ordered binary decision diagram for \(\varphi_r\). Razgon's theorem and Lemma 3 give

\[
|Q|
\ge 2^{lu(G_r)}
\ge 2^{r/82}.
\]

\(\square\)

## 7. Binary input-length accounting

The assignment-target construction for \(\varphi_r\) has fewer than \(6r^2\) items and fewer than \(4r^2\) base-ten columns. Every encoded integer is less than \(10^{4r^2}\), so each has \(O(r^2)\) binary digits. The total explicit binary length \(L_r\) of the item multiset and one target therefore satisfies

\[
L_r=O(r^4).
\]

Consequently,

\[
r=\Omega(L_r^{1/4}),
\]

and

\[
|Q|=2^{\Omega(L_r^{1/4})}.
\]

This is superpolynomial in the binary query-instance length.

## 8. Scope and independent attack

The proof survives the following checks:

- the half-prefix argument applies to every variable order;
- inducedness is tested in the upper subgraph, including conflicts from edges inside the prefix;
- clause-column sums are at most \(2+3=5<10\), so no carry occurs;
- the bound is measured against binary encoding length;
- the source formula is easy to evaluate from a full assignment and is satisfied by the all-true assignment.

Therefore the conclusion is exactly an ordered Boolean query-representation lower bound. It is not a lower bound for deciding a fixed Subset Sum target, for arbitrary target-query algorithms, or for the structural-summary language from the closed route.
