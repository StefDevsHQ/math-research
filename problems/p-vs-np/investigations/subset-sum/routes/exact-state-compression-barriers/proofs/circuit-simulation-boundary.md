# Circuit-Simulation Boundary

**Claim:** `SS-ECB-010`  
**Status:** `PROVED / CHECKED`  
**Proof type:** Constructive upper bound  
**Updated:** 2026-07-16

## Claim

Let \(\varphi\) be a CNF formula of clause width at most three, and let \((A_\varphi,\tau_\varphi)\) be the assignment-target Subset Sum embedding from `SS-ECB-003`.

Any representation model that may retain an arbitrary Boolean circuit of size polynomial in \(|\varphi|\), and may feed the assignment bits decoded from \(\tau_\varphi(\alpha)\) into that circuit, has a polynomial-size exact representation of the query function

\[
\alpha\longmapsto
\mathbf 1[\tau_\varphi(\alpha)\in\Sigma(A_\varphi)].
\]

Consequently, the assignment-target family cannot yield a superpolynomial lower bound against any model containing polynomial-size Boolean circuits with unrestricted access to the encoded assignment bits.

## Proof

By `SS-ECB-003`, for every assignment \(\alpha\),

\[
\tau_\varphi(\alpha)\in\Sigma(A_\varphi)
\quad\Longleftrightarrow\quad
\alpha\models\varphi.
\]

Construct the standard Boolean circuit \(C_\varphi\) for \(\varphi\):

1. use one input gate for each assignment bit;
2. use a negation gate where a literal is negative;
3. use one OR gate for each clause;
4. use an AND tree over the clause outputs.

For clause width at most three, this circuit has size \(O(n+m)\), where \(n\) is the number of variables and \(m\) the number of clauses. If the target encoding is presented instead of the bits directly, the designated variable columns of \(\tau_\varphi(\alpha)\) recover the bits by the fixed decoding map from the embedding; this adds only polynomial-size wiring or arithmetic decoding.

The representation consisting of the embedding metadata and \(C_\varphi\) therefore answers the exact membership query for every assignment target in polynomial time and polynomial size. Hence no superpolynomial lower bound for this family can hold in a model that contains such circuits. \(\square\)

## Boundary cases

- Empty CNF formulas compile to the constant-one circuit.
- A CNF containing an empty clause compiles to the constant-zero circuit.
- Tautological clauses may be removed before construction.
- The result concerns the assignment-target query family. It does not provide a circuit for arbitrary Subset Sum targets.

## Consequence for the route

The candidate succinct transition language must be strictly weaker than unrestricted polynomial-size circuits or unrestricted polynomial-time transition programs. At the same time, it must be strong enough to express binary-encoded interval, progression, residue, exception, and recursive-composition operations. This separation is now the central model-design problem.