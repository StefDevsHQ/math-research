# CNF Assignment Evaluation as Subset Sum Target Membership

**Recorded:** 2026-07-16  
**Status:** `PROVED / CHECKED`  
**Use:** Exact-state compression and knowledge-compilation audits

## Statement

For every CNF formula \(\varphi\) of clause width at most three, one can construct in polynomial time:

- a fixed multiset \(A_\varphi\) of positive integers;
- an injective polynomial-time map \(\tau_\varphi:\{0,1\}^n\to\mathbb N\);

such that for every assignment \(\alpha\),

\[
\tau_\varphi(\alpha)\in\Sigma(A_\varphi)
\quad\Longleftrightarrow\quad
\alpha\models\varphi.
\]

The item multiset is fixed while the target encodes the assignment.

## Construction

Use base ten with:

- selector columns \(P_i^T,P_i^F\) for each variable;
- clause columns \(D_j\) for each clause.

For each variable, create items \(T_i,F_i\):

- \(T_i\) has a one in \(P_i^T\) and in every clause column containing literal \(x_i\);
- \(F_i\) has a one in \(P_i^F\) and in every clause column containing literal \(\neg x_i\).

For each clause, create slack items with digits one and two in its clause column.

For assignment \(\alpha\), the target has:

- selector pair \((1,0)\) when \(\alpha_i=1\);
- selector pair \((0,1)\) when \(\alpha_i=0\);
- clause digit four in every clause column.

## Correctness

Selector columns force exactly the assignment item matching \(\alpha_i\). In a clause column, those forced items contribute the number \(k\in\{0,1,2,3\}\) of satisfied literals. The two slack items contribute exactly \(0,1,2,3\). Target digit four is reachable if and only if \(k\ge1\).

All column sums are at most six, so no base-ten carry occurs.

## Size

The construction uses \(2n+2m\) items and \(2n+m\) digit columns. Its explicit binary encoding length and construction time are polynomial in \(n+m\).

## Scope

This is not a fixed-target NP-hardness reduction. It embeds the assignment-evaluation function into a structured family of target-membership queries. A general query algorithm can decode the assignment and evaluate the formula directly.

The full proof and state-model transfer are recorded in:

- [Assignment-target embedding and OBDD transfer](../../investigations/subset-sum/routes/exact-state-compression-barriers/proofs/assignment-target-obdd-transfer.md)
