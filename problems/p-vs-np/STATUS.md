# Status — P versus NP

**Phase:** Top-level route selection after Subset Sum closeout and landscape audits  
**Updated:** 2026-07-16

## Current position

The repository foundation is complete. The first concrete investigation, Subset Sum, closed two universal strategies:

1. **Structural compression** did not produce a universal polynomial-time algorithm. Canonical no-carry SAT-to-Subset-Sum instances preserve assignment and clause compatibility under the proposed modular decomposition.
2. **Exact-state compression barriers** produced correct model-specific lower bounds and representation boundaries, but no model simultaneously contained all retained structural mechanisms, excluded polynomial Boolean simulation, and admitted a superpolynomial hard-family lower bound.

The project has completed:

- a paradigm-level [Subset Sum algorithmic landscape](investigations/subset-sum/references/algorithmic-landscape.md);
- a cross-investigation [research-programme landscape](references/research-programme-landscape.md);
- a cross-investigation [problem-testbed landscape](references/problem-testbed-landscape.md);
- a supporting [top-level source map](references/top-level-landscape-sources.md).

No investigation or route is active.

## Accepted retained results

- the residue-completion lemma;
- polynomial-time solvability on classes with an efficiently constructible exact decomposition whose complete computation graph and total encoded state are polynomially bounded in binary input length;
- an exact assignment-target embedding of width-three CNF evaluation into fixed-item Subset Sum query families;
- a `2^{Omega(L^{1/4})}` lower bound for square-grid assignment-target queries in the explicitly defined ordered Boolean query model;
- exact item-block Minkowski composition identities;
- model-boundary theorems separating small syntax, expensive normalization, and excessive Boolean expressiveness.

These results do not prove `P=NP`, `P!=NP`, a fixed-target Subset Sum lower bound, a general Boolean circuit lower bound, or a lower bound for arbitrary Subset Sum algorithms.

## Completed

1. Established repository research standards and atomic record structure.
2. Normalized the no-carry 3-SAT-to-Subset-Sum reduction.
3. Audited and closed the structural-compression route.
4. Opened, attacked, audited, and closed the exact-state compression-barrier route.
5. Recorded final claim states, limitations, and reopening conditions for both routes.
6. Completed a sourced Subset Sum algorithmic landscape.
7. Completed a sourced top-level landscape of P-versus-NP research programmes, proof barriers, and candidate testbeds.

## Current methodological determination

The repository should distinguish two top-level tracks.

### Positive track

Choose a concrete NP-complete problem and a proposed universal polynomial-time mechanism. The current leading candidate is the **exact-incidence constraint cluster**:

- Positive 1-in-3 SAT as the primary row-sparse exact-one system;
- X3C as the column-sparse dual control;
- 3-Dimensional Matching as the tripartite exact-cover control;
- XOR-SAT, perfect matching, and bounded-width CSPs as tractable neighbours.

The first route must specify a mechanism before the investigation is opened. Candidate mechanisms include exact propagation closure, an incidence-width parameter, or a composition theorem that works across all three incidence orientations.

### Lower-bound track

The leading sibling candidate is **Circuit-SAT and restricted-circuit satisfiability**. A valid route must state:

- the exact circuit or proof model;
- the nontrivial algorithm or lower bound sought;
- the known transfer theorem to the claimed class separation;
- the relativization, natural-proof, algebrization, or model-transfer barrier that must be avoided.

## Next decision

Select one of the following before further route work:

1. open an exact-incidence investigation centred on Positive 1-in-3 SAT;
2. open a Circuit-SAT or restricted-circuit algorithms-to-lower-bounds investigation;
3. choose another testbed or programme from the top-level landscapes with an explicit reason it is superior;
4. remain within Subset Sum only by selecting a restricted positive subclass from its algorithmic landscape.

Do not reopen either closed Subset Sum route without satisfying its recorded reopening conditions.