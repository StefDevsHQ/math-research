# Status — P versus NP

**Phase:** Monotone NAE-3SAT trusted laboratory complete; naive-summary attack next  
**Updated:** 2026-07-22

## Current position

The repository foundation and canonical landscapes are complete. The active Monotone NAE-3SAT investigation has completed its first five vertical slices as one `COMPLETE / CHECKED` laboratory phase. No proof route and no universal polynomial-time mechanism has been accepted.

The first concrete investigation, Subset Sum, closed two universal strategies:

1. **Structural compression** did not produce a universal polynomial-time algorithm. Canonical no-carry SAT-to-Subset-Sum instances preserve assignment and clause compatibility under the proposed modular decomposition.
2. **Exact-state compression barriers** produced correct model-specific lower bounds and representation boundaries, but no model simultaneously contained all retained structural mechanisms, excluded polynomial Boolean simulation, and admitted a superpolynomial hard-family lower bound.

## Active investigation

[Monotone NAE-3SAT](investigations/monotone-nae-3sat/README.md) is the symmetry-first testbed.

Phase I exports:

- a canonical labelled 3-uniform-hypergraph model;
- an exact exponential satisfiability oracle and exhaustive `n<=5` census;
- exact successful-completion profiles for fixed orderings;
- calibrated graph-parity, affine-XOR, incidence-forest, bounded-boundary, and component controls;
- exact `K_5^(3)` and Fano obstruction evidence;
- a proved limitation: globally unsatisfiable instances collapse successful-completion semantics to one dead class at every level.

No algorithmic mechanism has been accepted.

## Current mathematical target

Formalize and attack naive polynomial-time summaries for residual Monotone NAE-3SAT structure. For each summary, produce a complete same-summary/different-semantics collision or retain its exact unresolved scope.

The semantic target must be richer than successful-completion sets on globally unsatisfiable instances. Every proposed mechanism must specify its representation, construction, transition, equivalence, acceptance, encoded size, total computation graph, adversarial family, and stop condition before it becomes a route conjecture.

## Mandatory controls

- graph 2-colouring;
- XOR-SAT;
- acyclic and bounded-width CSPs;
- Positive 1-in-3 SAT;
- canonical 3-SAT reductions;
- robust restricted Monotone NAE-3SAT hard families;
- dense `K_5^(3)` and sparse linear Fano obstructions.

## Retained Subset Sum results

- the residue-completion lemma;
- polynomial-time solvability on classes with an efficiently constructible exact decomposition whose complete computation graph and total encoded state are polynomially bounded in binary input length;
- an exact assignment-target embedding of width-three CNF evaluation into fixed-item Subset Sum query families;
- a `2^{Omega(L^{1/4})}` lower bound for square-grid assignment-target queries in the explicitly defined ordered Boolean query model;
- exact item-block Minkowski composition identities;
- model-boundary theorems separating small syntax, expensive normalization, and excessive Boolean expressiveness.

These results do not prove `P=NP`, `P!=NP`, a fixed-target Subset Sum lower bound, a general Boolean circuit lower bound, or a lower bound for arbitrary Subset Sum algorithms.

## Next decision

Execute `VS-06` in formalization-and-attack mode. Do not activate a route directory until one atomic representation claim survives explicit collision tests and states a global polynomial bound.
