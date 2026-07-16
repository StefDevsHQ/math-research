# SAT-to-Subset-Sum Audit

**Status:** Planned  
**Primary open claim:** `SS-SC-004`  
**Recorded:** 2026-07-16

## Question

When the refined forced/progression/lattice framework is applied to a canonical SAT-to-Subset-Sum reduction, does it reduce the encoded logical state, or merely restate it as modular structure?

## Method

1. Construct a small symbolic SAT-to-Subset-Sum instance using assignment, clause, slack, and no-carry digit columns.
2. Identify every forced-separation step.
3. Identify reachable arithmetic progressions and the residue information needed to complete them.
4. Identify the natural lattice moduli and quotient states.
5. Map each surviving state back to its logical meaning in the SAT instance.
6. Track whether any polynomially bounded measure strictly decreases, including:
   - unresolved variables or clauses;
   - necessary compatibility states;
   - binary description length;
   - modulus bit length;
   - number of recursive branches.

## Pass condition

The route remains a candidate universal algorithm only if the decomposition yields an exact polynomial-size representation and a provable strict decrease independent of the satisfying assignment.

## Failure condition

The route is closed as a universal algorithmic strategy if the surviving modular states track the original assignment or clause-compatibility choices without polynomial compression.

## Output

The completed audit must contain:

- the exact reduction instance;
- a state-by-state structural analysis;
- the complexity measure used;
- the final pass or failure determination;
- corresponding updates to `CLAIMS.md` and `STATUS.md`.
