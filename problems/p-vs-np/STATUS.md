# Status — P versus NP

**Phase:** Route selection after two Subset Sum route closeouts  
**Updated:** 2026-07-16

## Current position

The repository foundation is complete and the first Subset Sum investigation has closed two universal strategies.

1. **Structural compression** did not produce a universal polynomial-time algorithm. Canonical no-carry SAT-to-Subset-Sum instances preserve assignment and clause compatibility under the proposed modular decomposition.
2. **Exact-state compression barriers** produced correct model-specific lower bounds and representation boundaries, but no model simultaneously contained all retained structural mechanisms, excluded polynomial Boolean simulation, and admitted a superpolynomial hard-family lower bound.

No active Subset Sum route is selected.

## Accepted retained results

- the residue-completion lemma;
- polynomial-time solvability on classes with an efficiently constructible exact decomposition whose complete computation graph and total encoded state are polynomially bounded in binary input length;
- an exact assignment-target embedding of width-three CNF evaluation into fixed-item Subset Sum query families;
- a `2^{Omega(L^{1/4})}` lower bound for square-grid assignment-target queries in the explicitly defined ordered Boolean query model;
- exact item-block Minkowski composition identities;
- model-boundary theorems separating small syntax, expensive normalization, and excessive Boolean expressiveness.

These results do not prove `P=NP`, `P!=NP`, a fixed-target Subset Sum lower bound, or a lower bound for arbitrary Subset Sum algorithms.

## Completed

1. Established repository research standards and atomic record structure.
2. Normalized the no-carry 3-SAT-to-Subset-Sum reduction.
3. Audited and closed the structural-compression route.
4. Opened, attacked, audited, and closed the exact-state compression-barrier route.
5. Recorded final claim states, limitations, and reopening conditions for both routes.

## Current obstruction

Natural exact-state languages fall into three regimes:

1. unevaluated additive syntax is universally small but leaves membership unresolved;
2. normalized arithmetic representations can be exponentially large even on easy instances;
3. compact bounded residue-range tests plus unrestricted branching or intersection recover polynomial Boolean computation.

No broad natural model was found between these regimes that also subsumes every retained structural operation.

## Next decision

Select one new route before further mathematical work:

1. a positive tractable-subclass investigation with a concrete structural parameter and a globally polynomial exact algorithm target; or
2. a different P-versus-NP investigation not centered on universal exact-state compression.

Do not reopen either closed route without satisfying its recorded reopening conditions.