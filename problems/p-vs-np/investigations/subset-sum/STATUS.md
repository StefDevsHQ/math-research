# Status — Subset Sum Investigation

**Phase:** Route selection after exact-state compression closeout  
**Updated:** 2026-07-16

## Current position

Two universal routes are closed:

1. **Structural compression:** local residue completion and the polynomially bounded exact-decomposition theorem survive, but the universal framework preserved SAT compatibility.
2. **Exact-state compression barriers:** correct model-specific boundaries were established, but no broad arithmetic model both subsumed the retained structural mechanisms and excluded polynomial Boolean simulation.

## Accepted results

- residue-completion lemma;
- polynomial-time solvability on classes with an efficiently constructible exact decomposition whose complete computation graph and total encoded state are polynomially bounded in binary input length;
- exact assignment-target embeddings of CNF evaluation into fixed-item Subset Sum query families;
- a superpolynomial ordered-binary-decision-diagram lower bound for the square-grid assignment-query family;
- exact item-block Minkowski composition identities;
- multiple representation-model boundary theorems recorded in the closed exact-state route.

These do not imply a lower bound for arbitrary Subset Sum algorithms or `P != NP`.

## Final exact-state obstruction

The attempted arithmetic proof-graph bridge failed:

- unevaluated additive syntax is universally small but leaves membership unresolved;
- normalized progression unions can be exponentially large on easy instances;
- compact bounded residue-range tests plus unrestricted repeated branching recover polynomial width-three CNF evaluation.

The candidate therefore crossed its circuit-simulation stop condition. Pure residue-equality branching alone is not classified.

## Next decision

No active route is selected.

Recommended choices:

1. open a positive tractable-subclass route with a concrete structural parameter and a globally polynomial algorithm target; or
2. move to a different P-versus-NP investigation rather than continuing universal exact-state compression.

Do not reopen either closed route without satisfying its recorded reopening conditions.