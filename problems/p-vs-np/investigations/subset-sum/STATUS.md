# Status — Subset Sum Investigation

**Phase:** Route selection after two route closeouts and full landscape audit  
**Updated:** 2026-07-16

## Current position

Two universal routes are closed:

1. **Structural compression:** local residue completion and the polynomially bounded exact-decomposition theorem survive, but the universal framework preserved SAT compatibility.
2. **Exact-state compression barriers:** correct model-specific boundaries were established, but no broad arithmetic model both subsumed the retained structural mechanisms and excluded polynomial Boolean simulation.

A paradigm-level review of currently known Subset Sum directions is complete:

- [Algorithmic landscape](references/algorithmic-landscape.md)
- [Primary-source map](references/algorithmic-landscape-sources.md)

The review separates general exact algorithms, pseudopolynomial algorithms, structured polynomial regimes, candidate compression mechanisms, model barriers, approximation, heuristics, and quantum methods. It records no new investigation-level mathematical claim.

## Accepted results

- residue-completion lemma;
- polynomial-time solvability on classes with an efficiently constructible exact decomposition whose complete computation graph and total encoded state are polynomially bounded in binary input length;
- exact assignment-target embeddings of CNF evaluation into fixed-item Subset Sum query families;
- a superpolynomial ordered-binary-decision-diagram lower bound for the square-grid assignment-query family;
- exact item-block Minkowski composition identities;
- multiple representation-model boundary theorems recorded in the closed exact-state route.

These do not imply a lower bound for arbitrary Subset Sum algorithms or `P != NP`.

## Current external frontiers

As of 2026-07-16:

1. the pseudopolynomial frontier reaches deterministic near-linear dependence on the numeric target range, but remains polynomial in \(T\), not \(\log T\);
2. the worst-case exact-exponential frontier improves \(2^{n/2}\) only by polynomial factors, with no known \(O^*(2^{(1/2-c)n})\) algorithm for constant \(c>0\);
3. genuine polynomial algorithms are known on explicit subclasses such as bounded numerical range, dense additive regimes, small maximum item, low-density average-case instances, and bounded doubling;
4. no known favourable structural parameter is proved polynomially bounded on every binary-encoded instance.

## Final exact-state obstruction

The attempted arithmetic proof-graph bridge failed:

- unevaluated additive syntax is universally small but leaves membership unresolved;
- normalized progression unions can be exponentially large on easy instances;
- compact bounded residue-range tests plus unrestricted repeated branching recover polynomial width-three CNF evaluation.

The candidate therefore crossed its circuit-simulation stop condition. Pure residue-equality branching alone is not classified.

## Next decision

No active route is selected.

The landscape identifies the strongest positive Subset Sum candidates as:

1. a small-doubling or constructive additive-structure subclass;
2. a dense-regime subclass with an explicit uncovered parameter range;
3. a small-item or few-distinct-values subclass with a structural parameter not reducible to bounded magnitude;
4. a new decomposition-width parameter with a complete global state bound.

The main barrier alternative is a communication or interface model, but it should not be opened until a natural polynomial-overhead subsumption theorem is stated first.

Otherwise, move to a different P-versus-NP investigation rather than continuing universal exact-state compression.

Do not reopen either closed route without satisfying its recorded reopening conditions.