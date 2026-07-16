# Residue-Completion Lemma

**Claim:** `SS-SC-002`  
**Mathematical status:** `PROVED`  
**Review maturity:** `CHECKED`  
**Recorded:** 2026-07-16

## Statement

Let \(C\) and \(E\) be disjoint collections of nonnegative integers.

Assume that

\[
\{L,L+q,L+2q,\ldots,U\}\subseteq\Sigma(C),
\]

where \(q\ge 1\) and \(U=L+mq\) for some integer \(m\ge 0\).

For every residue \(r\in\{0,1,\ldots,q-1\}\), assume there is a subset sum \(e_r\in\Sigma(E)\) such that

\[
e_r\equiv r\pmod q.
\]

Let

\[
B=\max_{0\le r<q} e_r.
\]

Then

\[
[L+B,U]\subseteq\Sigma(C\cup E).
\]

If \(L+B>U\), the conclusion is vacuous.

## Proof

Take any integer \(x\in[L+B,U]\).

Choose \(e_r\in\Sigma(E)\) satisfying

\[
e_r\equiv x-L\pmod q.
\]

Then

\[
x-e_r\equiv L\pmod q.
\]

Since \(e_r\le B\),

\[
x-e_r\ge L+B-B=L.
\]

Since \(e_r\ge 0\),

\[
x-e_r\le x\le U.
\]

Therefore \(x-e_r\) lies in the complete progression from \(L\) to \(U\), so \(x-e_r\in\Sigma(C)\).

Because \(C\) and \(E\) are disjoint, the subsets producing \(x-e_r\) and \(e_r\) can be combined. Their sum is \(x\), hence \(x\in\Sigma(C\cup E)\).

Thus every integer in \([L+B,U]\) is reachable. ∎

## Scope

The lemma is an exact coverage certificate. It does not establish that the progression, residue representatives, or modulus can be found in polynomial time. It also does not control the size of \(q\) relative to the binary input length.
