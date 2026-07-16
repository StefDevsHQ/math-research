# Progression-Union Lower Bound on Ternary Superincreasing Instances

**Claim:** `SS-ECB-015`  
**Status:** `PROVED / CHECKED`  
**Proof type:** Explicit family and combinatorial lower bound  
**Updated:** 2026-07-16

## 1. Claim

Let

\[
A_n=\{1,3,3^2,\ldots,3^{n-1}\}.
\]

Then

\[
\Sigma(A_n)=\left\{\sum_{i=0}^{n-1}\varepsilon_i3^i:\varepsilon_i\in\{0,1\}\right\}
\]

contains no nonconstant arithmetic progression of length three.

Consequently, every exact representation of \(\Sigma(A_n)\) as a union of bounded arithmetic progressions requires at least \(2^{n-1}\) progression atoms.

The binary input length of \(A_n\) is \(L_n=\Theta(n^2)\), so this atom lower bound is

\[
2^{\Omega(\sqrt{L_n})}.
\]

## 2. Three-term-progression freeness

### Lemma

There are no distinct \(x,y,z\in\Sigma(A_n)\) satisfying

\[
x+z=2y.
\]

### Proof

Proceed by induction on \(n\).

For \(n=1\), the set is \(\{0,1\}\), so the claim is immediate.

Assume the claim for \(n-1\). Every element of \(\Sigma(A_n)\) has a unique form

\[
u+\varepsilon 3^{n-1},
\]

where \(u\in\Sigma(A_{n-1})\) and \(\varepsilon\in\{0,1\}\).

Suppose

\[
x+z=2y.
\]

Reduce modulo \(3^{n-1}\). Writing

\[
x=u_x+\varepsilon_x3^{n-1},\quad
y=u_y+\varepsilon_y3^{n-1},\quad z=u_z+\varepsilon_z3^{n-1},
\]

we obtain

\[
u_x+u_z\equiv 2u_y\pmod{3^{n-1}}.
\]

Because every \(u\in\Sigma(A_{n-1})\) lies in

\[
0\le u\le \frac{3^{n-1}-1}{2},
\]

both sides differ in absolute value by less than \(3^{n-1}\). Therefore the congruence is equality:

\[
u_x+u_z=2u_y.
\]

By the induction hypothesis, \(u_x=u_y=u_z\).

Substituting back gives

\[
\varepsilon_x+\varepsilon_z=2\varepsilon_y.
\]

For \(\varepsilon_x,\varepsilon_y,\varepsilon_z\in\{0,1\}\), this forces

\[
\varepsilon_x=\varepsilon_y=\varepsilon_z.
\]

Hence \(x=y=z\). Thus no nonconstant three-term arithmetic progression exists. \(\square\)

## 3. Atom lower bound

A bounded arithmetic progression containing at least three distinct points contains a nonconstant three-term arithmetic progression, namely any three consecutive terms.

Since \(\Sigma(A_n)\) is three-term-progression-free, every bounded progression contained in it has at most two points.

The reachable set has exactly \(2^n\) elements by uniqueness of ternary expansions with digits in \(\{0,1\}\). Therefore any exact union of bounded arithmetic progressions equal to \(\Sigma(A_n)\) requires at least

\[
\frac{2^n}{2}=2^{n-1}
\]

atoms. Overlaps can only increase the required count because the union must still cover all \(2^n\) points and every atom covers at most two of them. \(\square\)

## 4. Encoding length

The item \(3^i\) has \(\Theta(i+1)\) binary bits. Hence

\[
L_n=\Theta\left(\sum_{i=0}^{n-1}(i+1)\right)=\Theta(n^2).
\]

Thus \(n=\Theta(\sqrt{L_n})\), and the atom lower bound is

\[
2^{\Omega(\sqrt{L_n})}.
\]

## 5. Interpretation

This is not a hardness result for the instances. They are superincreasing and are decidable by forced largest-item reasoning.

The result proves a representation mismatch:

- normalized unions of arithmetic progressions can be exponentially large even on easy instances;
- target-relative residual transformations solve the same family without materializing the full reachable set.

Therefore a successor to structural compression cannot require every state to be a normalized exact union of interval or progression atoms. It needs a separate target-relative proof-graph layer.