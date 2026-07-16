# Grid-Family Ordered Query-State Barrier

**Claims:** `SS-ECB-005`, `SS-ECB-006`  
**Status:** `ESTABLISHED / CHECKED` for the imported OBDD theorem; `PROVED / CHECKED` for the transfer and grid bound  
**Proof type:** External theorem plus project combinatorial proof  
**Updated:** 2026-07-16

## 1. Hard Boolean family

For an even integer \(r\ge 2\), let \(G_r\) be the \(r\times r\) square grid graph. Its vertices are

\[
V(G_r)=[r]\times[r],
\]

with edges between horizontally or vertically adjacent vertices.

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

Apply the assignment-target construction from [Assignment-target embedding and OBDD transfer](assignment-target-obdd-transfer.md), obtaining the fixed item multiset \(A_r\) and targets \(\tau_r(\alpha)\).

## 2. Imported OBDD lower bound

For a graph \(G\), let \(lu(G)\) denote its linear upper induced-matching width.

Razgon proves:

> For the monotone two-CNF \(\varphi(G)\), every ordered binary decision diagram has size at least \(2^{lu(G)}\).

Source: Igor Razgon, “Classification of OBDD size for monotone 2-CNFs,” arXiv:2103.09115v2, Theorem 2, 2021, pp. 7–8.

It remains to prove a linear lower bound on \(lu(G_r)\).

## 3. Grid cut lemma

### Lemma 1

For every subset \(U\subseteq V(G_r)\) with \(|U|=r^2/2\), the number of grid edges with one endpoint in \(U\) and the other outside \(U\) is at least \(r/2\).

### Proof

For row \(i\), let

\[
S_i=\{j:(i,j)\in U\},
\qquad
u_i=|S_i|.
\]

Call row \(i\) mixed when \(0<\nu_i<r\), and let \(q\) be the number of mixed rows.

Every mixed row contains at least one horizontal edge crossing between \(U\) and its complement because a row is a path containing both kinds of vertices.

Between consecutive rows \(i\) and \(i+1\), the number of crossing vertical edges is

\[
|S_i\triangle S_{i+1}|\ge |\nu_i-\nu_{i+1}|.
\]

Therefore the total crossing-edge count \(b(U)\) satisfies

\[
b(U)\ge q+\sum_{i=1}^{r-1}|\nu_i-\nu_{i+1}|.
\]

If \(q\ge r/2\), then \(b(U)\ge r/2\).

Assume \(q<r/2\). If no row has \(\nu_i=0\), then each nonmixed row has \(\nu_i=r\), so

\[
|U|=\sum_i\nu_i\ge (r-q)r>r^2/2,
\]

a contradiction.

If no row has \(\nu_i=r\), then only the \(q\) mixed rows contribute vertices, so

\[
|U|<qr<r^2/2,
\]

also a contradiction.

Hence some row has count \(0\) and another has count \(r\). By the triangle inequality along the row sequence,

\[
\sum_{i=1}^{r-1}|\nu_i-\nu_{i+1}|\ge r.
\]

Thus \(b(U)\ge r\), which is stronger than required. \(\square\)

## 4. Induced matching extraction

For \(U\subseteq V(G_r)\), let \(G_r^U\) be the upper subgraph used in the definition of \(lu\): remove edges whose two endpoints both lie outside \(U\), while retaining edges inside \(U\) and edges crossing the cut.

### Lemma 2

If the cut \((U,V(G_r)\setminus U)\) has \(b\) crossing edges, then \(G_r^U\) contains an induced crossing matching of size at least \(b/41\).

### Proof

Construct a conflict graph \(K\) whose vertices are the crossing edges. Two crossing edges conflict when their four endpoints do not induce exactly those two edges in \(G_r^U\); equivalently, they share an endpoint or an endpoint of one is adjacent in \(G_r^U\) to an endpoint of the other.

Fix a crossing edge \(e=xy\). Every edge conflicting with \(e\) is incident to a vertex in

\[
N_{G_r^U}[x]\cup N_{G_r^U}[y].
\]

The grid has maximum degree at most \(4\), so this union has at most \(10\) vertices, each incident to at most \(4\) crossing edges. Thus at most \(40\) crossing edges, including \(e\), lie in the closed conflict neighborhood of \(e\). The conflict graph has maximum degree at most \(39\), and certainly at most \(40\).

A greedy independent-set algorithm therefore selects at least \(b/41\) vertices of \(K\). Their corresponding crossing edges form an induced matching in \(G_r^U\). \(\square\)

## 5. Linear upper induced-matching width of the grid

### Lemma 3

For every even \(r\),

\[
lu(G_r)\ge \frac{r}{82}.
\]

### Proof

Take an arbitrary ordering of the \(r^2\) vertices and let \(U\) be its prefix of length \(r^2/2\).

By Lemma 1, the cut has at least \(r/2\) crossing edges. By Lemma 2, the upper subgraph \(G_r^U\) has an induced crossing matching of size at least

\[
\frac{r/2}{41}=\frac{r}{82}.
\]

This holds for every vertex ordering, so the maximum prefix width of every ordering is at least \(r/82\). Taking the minimum over orderings gives the claimed bound. \(\square\)

## 6. Ordered state lower bound

### Theorem

Every deterministic ordered assignment-target query graph for \((A_r,\tau_r)\), under every variable order, has size at least

\[
2^{r/82}.
\]

### Proof

By the transfer theorem, the query graph is an ordered binary decision diagram for \(\varphi_r\). Razgon's theorem and Lemma 3 give

\[
|Q|
\ge 2^{lu(G_r)}
\ge 2^{r/82}.
\]

\(\square\)

## 7. Binary input-length accounting

The assignment-target construction for \(\varphi_r\) has:

- \(2N+2M<6r^2\) items;
- \(2N+M<4r^2\) base-ten columns.

Every encoded integer is less than \(10^{4r^2}\), so each has \(O(r^2)\) binary digits. The total explicit binary length \(L_r\) of the item multiset and one target satisfies

\[
L_r=O(r^4).
\]

Therefore

\[
r=\Omega(L_r^{1/4}),
\]

and the state lower bound can be written as

\[
|Q|=2^{\Omega(L_r^{1/4})}.
\]

This is superpolynomial in the binary query-instance length.

## 8. Independent attack and limitations

The proof was checked against the following failure modes:

- **Ordering:** the half-prefix argument applies to every ordering.
- **Inducedness:** conflicts caused by edges inside \(U\) are included because the matching is extracted in the upper subgraph, not merely in the bipartite cut graph.
- **No-carry:** clause digits remain at most \(2+3=5\) for two-CNF, below base ten.
- **Encoding:** the bound is expressed in binary input length, not the numerical target magnitude.
- **Decision hardness:** \(\varphi_r\) is satisfiable by the all-true assignment. The theorem is not a lower bound for deciding whether one fixed target is reachable.

The remaining scope is exactly the ordered assignment-target query-state model.
