# VS-02 Completion Audit — Exact Small-Instance Oracle

**Slice:** `VS-02`  
**Status:** `COMPLETE / CHECKED`  
**Classification:** Exact exponential oracle and finite computational census  
**Updated:** 2026-07-22

## Scope

VS-02 supplies trusted finite ground truth. It does not provide a polynomial-time algorithm and does not change any `P` versus `NP` claim.

## Established implementation facts

The package now exports exact decision, complete listing, exact counting, component-factorized counting, edge-minimal-unsatisfiability testing, and canonical labelled generation.

`solve_exact` returns the true lexicographically least satisfying colouring. Its baseline path enumerates all complete colourings. Its optimized path fixes the least vertex of each nontrivial incidence component and every isolated vertex to zero.

## Correctness proofs

### Component-wise complement fixing

Every hyperedge lies in one incidence component. Complementing all colours in one component therefore preserves non-monochromaticity of every edge. Given a satisfying colouring, complement each component whose least vertex is one. This yields a satisfying colouring with all selected representatives zero.

The lexicographically least satisfying colouring must already have every component representative zero: complementing a component whose least vertex is one changes no earlier vertex and changes that vertex to zero. Isolated vertices are unconstrained and hence zero in the least witness.

Thus lexicographic enumeration of only the unfixed vertices returns the true least full witness.

### Component factorization

A full colouring satisfies the instance exactly when each nontrivial component restriction satisfies its component. Isolated vertices are arbitrary. Hence

\[
\#\operatorname{Sat}(H)=2^z\prod_j\#\operatorname{Sat}(H_j).
\]

### Generator exhaustiveness

For fixed `n`, the lexicographically ordered triples form a list of length `binom(n,3)`. Each bit mask selects one subset of this list, and each edge subset has one mask. Therefore the generator enumerates every labelled simple 3-uniform hypergraph exactly once.

### Edge-minimality test

An unsatisfiable instance is edge-minimal exactly when every one-edge deletion is satisfiable. Any proper edge subset is contained in a one-edge deletion, and satisfiability is preserved under further edge deletion.

## Exhaustive first domain

The committed corpus covers

\[
\mathcal H_{\le5},\qquad
\sum_{n=0}^{5}2^{\binom n3}=1045
\]

labelled instances.

Totals:

- instances: `1045`;
- satisfiable: `1044`;
- unsatisfiable: `1`;
- connected under the declared convention: `971`;
- edge-minimal unsatisfiable: `1`;
- complete reference colourings evaluated: `33047`.

The unique unsatisfiable five-vertex labelled instance is the complete 3-uniform hypergraph on five vertices, containing all ten triples. Its stable identifier is `nae3-v1-sha256-45778a8830dc32395a6306cf9b2bea1f48f6770ea08bfe786cd0664a3040ee3d`.

The corpus payload digest is `6d621d42bbbc392d26096a7da61e1c35664e573f2c3949928f5c2f12fbe2abf5`.

## Separate Fano control

The seven-edge Fano-plane instance is exactly unsatisfiable. Every one-edge deletion is satisfiable, so it is edge-minimal unsatisfiable. This result is obtained by the committed exhaustive oracle and independently checked by direct enumeration in the test suite.

## Verification

The committed tests compare production logic with a direct `itertools.product` reference implementation on all 1045 first-domain instances. They verify decisions, complete solution lists, counts, least witnesses, optimized/baseline agreement, public witness verification, component-factorized counts, generator cardinality, corpus bytes, CLI behavior, and the Fano control.

The workflow compiles, tests, exercises `validate`, `solve`, and `count`, regenerates the corpus, and byte-compares it with the committed record on Python 3.11, 3.12, and 3.13.

## Complexity

For `n` vertices, `m` edges, `c` nontrivial components, `z` isolates, and `S` satisfying assignments:

- baseline decision: `O(2^n m)` after validation;
- optimized decision: `O(2^(n-c-z) m)`;
- exact counting: `O(2^n m)`;
- complete listing: `O(2^n m + Sn)` time and `Theta(Sn)` output space;
- labelled generation: exactly `2^binom(n,3)` instances;
- count values have at most `n+1` bits.

These are exponential laboratory procedures.

## Claim status

The census and Fano results are `COMPUTATIONAL / CHECKED`: finite exhaustive evidence with a complete domain argument. The component, symmetry, factorization, generator, and edge-minimality arguments are `PROVED / CHECKED` within the project.

## Final determination

`VS-02` is `COMPLETE / CHECKED`. Its exact outputs may now be used as ground truth by VS-03 and later finite experiments, subject to their own building-block gates.
