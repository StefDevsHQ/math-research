# Status — P versus NP

**Phase:** Monotone NAE-3SAT formalization and route selection after Subset Sum closeout  
**Updated:** 2026-07-22

## Current position

The repository foundation and canonical landscapes are complete. The Monotone NAE-3SAT investigation is open in formalization mode, but no proof route is active.

The first concrete investigation, Subset Sum, closed two universal strategies:

1. **Structural compression** did not produce a universal polynomial-time algorithm. Canonical no-carry SAT-to-Subset-Sum instances preserve assignment and clause compatibility under the proposed modular decomposition.
2. **Exact-state compression barriers** produced correct model-specific lower bounds and representation boundaries, but no model simultaneously contained all retained structural mechanisms, excluded polynomial Boolean simulation, and admitted a superpolynomial hard-family lower bound.

The programme maintains one canonical version of each top-level orientation artifact:

- [Research-programme landscape](references/research-programme-landscape.md);
- [Problem-testbed landscape](references/problem-testbed-landscape.md);
- [Canonical source map](references/top-level-landscape-sources.md).

## Active investigation

[Monotone NAE-3SAT](investigations/monotone-nae-3sat/README.md) is the symmetry-first testbed.

The object has been formalized as 2-colourability of a 3-uniform hypergraph. Its claim ledger records:

- NP-completeness as an established external result;
- the checked implication that a deterministic polynomial-time algorithm on all instances proves `P=NP`;
- the elementary arity-minimality reduction from all unary/binary Boolean CSPs to 2-SAT;
- a deliberately strong open conjecture concerning exact future-equivalence compression.

No algorithmic mechanism has been accepted.

## Current mathematical target

Find an exact, polynomially constructible global-compatibility invariant for Monotone NAE-3SAT, or disprove the first candidate cleanly.

The initial candidate family represents local satisfying colourings by their exact future completion behaviour. A successful route must bound the complete computation graph and total encoded state, not merely recursion depth or local branching.

## Mandatory controls

- graph 2-colouring;
- XOR-SAT;
- acyclic and bounded-width CSPs;
- Positive 1-in-3 SAT;
- canonical 3-SAT reductions;
- robust restricted Monotone NAE-3SAT hard families.

## Retained Subset Sum results

- the residue-completion lemma;
- polynomial-time solvability on classes with an efficiently constructible exact decomposition whose complete computation graph and total encoded state are polynomially bounded in binary input length;
- an exact assignment-target embedding of width-three CNF evaluation into fixed-item Subset Sum query families;
- a `2^{Omega(L^{1/4})}` lower bound for square-grid assignment-target queries in the explicitly defined ordered Boolean query model;
- exact item-block Minkowski composition identities;
- model-boundary theorems separating small syntax, expensive normalization, and excessive Boolean expressiveness.

These results do not prove `P=NP`, `P!=NP`, a fixed-target Subset Sum lower bound, a general Boolean circuit lower bound, or a lower bound for arbitrary Subset Sum algorithms.

## Next decision

State and attack the first atomic Monotone NAE-3SAT route conjecture. It must specify the decomposition, exact state representation, transition operation, proposed global polynomial bound, adversarial family, and stop condition before a route directory is activated.
