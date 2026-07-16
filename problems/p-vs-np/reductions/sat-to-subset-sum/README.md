# 3-SAT to Subset Sum

This is the normalized no-carry reduction used by the Subset Sum audits.

## Construction

Let \(\varphi\) be a 3-CNF formula with variables \(x_1,\ldots,x_n\) and clauses \(C_1,\ldots,C_m\). Remove tautological clauses and repeated literals first.

Use base \(10\) with one digit column for each variable and each clause.

For every variable \(x_i\), create two numbers:

- \(T_i\): digit \(1\) in variable column \(i\), and digit \(1\) in clause column \(j\) when \(x_i\in C_j\);
- \(F_i\): digit \(1\) in variable column \(i\), and digit \(1\) in clause column \(j\) when \(\neg x_i\in C_j\).

For every clause \(C_j\), create two slack numbers with digits \(1\) and \(2\) respectively in clause column \(j\), and zero elsewhere.

The target has digit \(1\) in every variable column and digit \(4\) in every clause column.

## No-carry property

A variable column sums to at most \(2\). A clause column receives at most \(3\) from literal numbers and at most \(3\) from its two slack numbers. Every column sum is therefore below \(10\), so decimal addition acts as independent coordinate addition.

## Correctness

The target digit \(1\) in variable column \(i\) forces exactly one of \(T_i\) and \(F_i\) to be selected. The selected variable numbers therefore encode a truth assignment.

For clause \(C_j\), let \(k_j\in\{0,1,2,3\}\) be the number of selected literal numbers satisfying that clause. Its slack numbers can add exactly \(0,1,2\), or \(3\). The clause target \(4\) is reachable exactly when \(k_j\ge 1\):

- \(k_j=1\): add \(3\);
- \(k_j=2\): add \(2\);
- \(k_j=3\): add \(1\);
- \(k_j=0\): the maximum slack is \(3\), so the target cannot be reached.

Thus the Subset Sum instance reaches its target if and only if \(\varphi\) is satisfiable.

## Size

The construction produces \(2n+2m\) numbers, each with \(n+m\) decimal digits. Its binary description length and construction time are polynomial in the formula size.

## Related exact-query variant

The [assignment-target query embedding](assignment-target-query.md) fixes the item multiset and encodes a complete Boolean assignment in the target. It is used for exact-state and knowledge-compilation audits, not as a fixed-target NP-hardness reduction.

## Historical note

Subset Sum, under the closely related name Knapsack, is among Karp's original NP-complete problems. The digit-column construction above is recorded here with a complete proof so route audits do not depend on an informal reduction summary.

Richard M. Karp, “Reducibility Among Combinatorial Problems,” in *Complexity of Computer Computations*, 1972, pp. 85–103.
