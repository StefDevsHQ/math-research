# SAT-to-Subset-Sum Audit

**Status:** Complete — route fails its pass condition  
**Primary claim:** `SS-SC-004`  
**Recorded:** 2026-07-16

## Question

When the forced/progression/lattice framework is applied to the canonical no-carry 3-SAT-to-Subset-Sum reduction, does it reduce the encoded logical state, or merely restate it as additive and modular structure?

## Reduction used

The shared construction is recorded at:

[`problems/p-vs-np/reductions/sat-to-subset-sum/README.md`](../../../../../../reductions/sat-to-subset-sum/README.md)

It uses one digit column per variable and clause. The target forces exactly one of \(T_i,F_i\) for each variable. Clause columns and slack values accept exactly the assignments satisfying every clause. No carries occur.

## Representative instance

Use

\[
(x_1\lor x_2\lor x_3)\land(\neg x_1\lor\neg x_2\lor x_3).
\]

With variable columns followed by the two clause columns, the constructed numbers are:

| Number | Decimal vector |
|---|---:|
| \(T_1\) | `10010` |
| \(F_1\) | `10001` |
| \(T_2\) | `01010` |
| \(F_2\) | `01001` |
| \(T_3\) | `00111` |
| \(F_3\) | `00100` |
| clause-1 slack | `00010`, `00020` |
| clause-2 slack | `00001`, `00002` |
| target | `11144` |

Direct enumeration gives six target-reaching subsets, corresponding exactly to the six satisfying assignments with the uniquely required slack choices.

## Structural analysis

### Forced separation

The variable target digits force **one of** \(T_i,F_i\), but do not determine which one. The framework therefore identifies the variable decision without eliminating it. There remain two compatible local choices per unresolved variable.

### Progression completion

Clause slack values provide the small progression \(\{0,1,2,3\}\) in each clause coordinate. This completes a clause target only after the selected variable numbers contribute at least one satisfying literal. The progression removes bookkeeping after an assignment choice; it does not select or compress the assignment choices themselves.

### Lattice structure

The no-carry base makes the digit columns an exact coordinate system. Quotienting or tracking residues preserves:

- one binary choice for each variable column;
- the incidence of each selected literal in the clause columns;
- the compatibility condition that every clause receives a positive literal contribution.

The modular state is therefore a restatement of the original truth assignment and clause-satisfaction state.

## Complexity measure

The audit tested the proposed measures:

- unresolved variables;
- unresolved clauses;
- necessary compatibility states;
- binary description length;
- modulus or coordinate width;
- recursive branching.

No route rule was established that decreases these measures independently of choosing truth values. Forced analysis exposes \(n\) binary choices. Clause progression completion applies only after those choices determine the clause contributions. Lattice analysis preserves the same compatibility information.

## Determination

**Fails.**

The route does not meet its pass condition on the canonical reduction family. It reveals the logical encoding but supplies no exact polynomial-size merge of the unresolved assignment states and no strictly decreasing polynomially bounded measure.

This is not a proof that every possible structural-compression algorithm fails, nor a lower bound for Subset Sum. It closes this specific forced/progression/lattice framework as a universal polynomial-time strategy.

## Consequence

- `SS-SC-004` is disproved as a claim about this framework.
- `SS-SC-003` is retracted as the route's universal algorithmic conjecture.
- The residue-completion lemma remains valid.
- The positive boundary is the polynomially bounded decomposition class in `proofs/polynomially-bounded-decomposition-class.md`.
- Further work should move to exact-state compression barriers or separately justified tractable subclasses.