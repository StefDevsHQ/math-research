# Audit — Ordered Query-State Barrier Scope

**Target:** `SS-ECB-006`  
**Verdict:** Survives as a model-specific barrier; fails as a direct algorithmic lower bound  
**Updated:** 2026-07-16

## Audit question

Does the square-grid ordered-state lower bound establish that the corresponding Subset Sum instances, or Subset Sum in general, require superpolynomial time or space?

## Adversarial family

The family is produced from the monotone two-CNF

\[
\varphi_r=\bigwedge_{\{u,v\}\in E(G_r)}(x_u\vee x_v)
\]

using the assignment-target embedding. The item multiset \(A_r\) is fixed for each formula and the target \(\tau_r(\alpha)\) encodes a full Boolean assignment.

## Pass condition

A direct algorithmic lower bound would require showing that every exact algorithm for the relevant Subset Sum decision task must realize a superpolynomial computation graph or use superpolynomial resources.

## Attack 1 — Fixed-target satisfiability

The monotone formula \(\varphi_r\) is satisfied by the all-true assignment. Therefore the ordinary SAT question for each fixed formula is trivial, and the associated canonical fixed-target Subset Sum instance is a yes-instance.

A lower bound for representing the full assignment function cannot be converted into a lower bound for deciding that one bit.

**Result:** direct fixed-target inference fails.

## Attack 2 — Decode the structured target

For a target in the image of \(\tau_r\), each selector pair \((P_i^T,P_i^F)\) is either \((1,0)\) or \((0,1)\). These digits reveal the assignment bit \(\alpha_i\).

An unrestricted query algorithm can:

1. decode all assignment bits from the target;
2. evaluate every clause of \(\varphi_r\) under that assignment;
3. accept exactly when all clauses are satisfied.

This runs in time polynomial in the formula and target length.

Thus the target slice has a polynomial-time membership algorithm even though every ordered binary decision diagram for the same function is superpolynomial.

**Result:** the lower bound is caused by the ordered decision-diagram restriction, not by computational intractability of the query function.

## Attack 3 — Arithmetic summaries

A compact arithmetic representation may test a large binary-encoded modulus, evaluate a formula, or invoke another polynomial-time subroutine without expanding the operation into an ordered decision diagram of comparable size.

Therefore an ordered-binary-decision-diagram lower bound does not automatically lower-bound:

- a residue table with succinct arithmetic evaluation;
- an arithmetic circuit;
- a Presburger formula;
- a general program stored as part of a state;
- the interval, progression, and large-modulus summaries used by the previous route.

**Result:** formal subsumption of structural compression is absent.

## Attack 4 — State count versus state encoding

The theorem proves that the complete ordered decision graph contains superpolynomially many nodes. It does not prove that any individual state needs superpolynomially many bits. A node identifier among \(S\) nodes requires only \(O(\log S)\) bits.

The valid obstruction is total graph size, not per-state encoding length.

**Result:** state-count interpretation survives only with complete-graph accounting.

## Verdict

`SS-ECB-006` survives exactly as stated:

> Ordered context-independent assignment-target query states cannot be globally merged into a polynomial complete graph on the grid family.

The following stronger statements are unsupported:

- arbitrary Subset Sum algorithms require superpolynomial resources;
- the grid-derived fixed-target instances are hard;
- every exact representation of the reachable set is large;
- the previous structural-compression language is contained in the ordered model;
- the result implies \(P\ne NP\).

## Required next theorem

The route needs a transfer theorem from a broader exact composition language to a model such as a Tree Decision Diagram, structured deterministic decomposable negation normal form, bounded-read branching program, or another representation with a proven lower bound.

The model must count all intermediate states and operations and must explicitly permit the arithmetic primitives required to contain the previous route.
