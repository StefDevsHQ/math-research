# Status — P versus NP

**Phase:** Route selection after two Subset Sum route closeouts and landscape audit  
**Updated:** 2026-07-16

## Current position

The repository foundation is complete and the first Subset Sum investigation has closed two universal strategies.

1. **Structural compression** did not produce a universal polynomial-time algorithm. Canonical no-carry SAT-to-Subset-Sum instances preserve assignment and clause compatibility under the proposed modular decomposition.
2. **Exact-state compression barriers** produced correct model-specific lower bounds and representation boundaries, but no model simultaneously contained all retained structural mechanisms, excluded polynomial Boolean simulation, and admitted a superpolynomial hard-family lower bound.

A paradigm-level audit of currently known Subset Sum directions is complete:

- [Algorithmic landscape](investigations/subset-sum/references/algorithmic-landscape.md)
- [Primary-source map](investigations/subset-sum/references/algorithmic-landscape-sources.md)

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
6. Completed and sourced a route-selection landscape covering general exact algorithms, pseudopolynomial algorithms, structured subclasses, compression mechanisms, lower-bound programmes, approximation, heuristics, and quantum methods.

## Current obstruction

Natural exact-state languages fall into three regimes:

1. unevaluated additive syntax is universally small but leaves membership unresolved;
2. normalized arithmetic representations can be exponentially large even on easy instances;
3. compact bounded residue-range tests plus unrestricted branching or intersection recover polynomial Boolean computation.

No broad natural model was found between these regimes that also subsumes every retained structural operation.

## Next decision

Select one new route before further mathematical work.

The strongest positive Subset Sum candidates identified by the landscape are:

1. bounded doubling or another constructive additive-structure subclass;
2. a dense additive-combinatorial regime with a genuinely uncovered parameter range;
3. a small-item or succinct-multiplicity subclass with a structural parameter not reducible to bounded magnitude;
4. a new decomposition-width parameter with complete global-state accounting.

The main barrier alternative is communication or interface complexity, but it should not be opened without first proving that the model naturally contains the retained arithmetic operations with polynomial overhead.

Otherwise, move to a different P-versus-NP investigation not centered on universal exact-state compression.

Do not reopen either closed route without satisfying its recorded reopening conditions.