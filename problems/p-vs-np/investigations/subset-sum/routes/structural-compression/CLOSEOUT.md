# Structural Compression Route — Closeout

**Closed:** 2026-07-16  
**Disposition:** Closed as a universal polynomial-time strategy; retained for local results and restricted classes

## Final result

The route did not produce a polynomial-time exact algorithm for general Subset Sum.

The original dense-or-separated bundle composition claim was withdrawn because local density or separation does not preserve enough global exact information. The refined forced/progression/lattice framework was then tested against the canonical no-carry 3-SAT-to-Subset-Sum reduction.

That audit failed the route's pass condition. The variable columns preserve one exact binary choice per variable, and the clause columns preserve assignment-to-clause compatibility. The modular structure exposes the encoded satisfiability instance but does not compress its unresolved logical choices or provide a strictly decreasing polynomially bounded measure.

## Retained results

1. The residue-completion lemma is an exact local coverage result.
2. The route gives a polynomial-time method on classes where the decomposition, branching, moduli, residue states, intermediate descriptions, and recursion depth are all polynomially bounded in the binary input length.
3. The audit isolates the main obstruction: additive structure may coexist with uncompressed logical compatibility.

## Final claim state

- `SS-SC-001`: `RETRACTED / CHECKED`
- `SS-SC-002`: `PROVED / CHECKED`
- `SS-SC-003`: `RETRACTED / CHECKED`
- `SS-SC-004`: `DISPROVED / CHECKED`
- `SS-SC-005`: `PROVED / CHECKED`

## Bundle claim

The exact original wording and numerical counterexample were not preserved. The bundle claim therefore remains retracted rather than formally disproved. Recovering a counterexample is not required to close the route and should not be treated as active work.

## Decision

No further work on universal dense/separated/progression/lattice decomposition is justified without a new theorem that:

- preserves cross-component compatibility exactly;
- is efficiently constructible;
- bounds all moduli and state descriptions polynomially in binary input length; and
- proves a strict polynomially bounded progress measure on reduction-generated hard instances.

The next research program is exact-state compression barriers: identify what information prevents exact dynamic-programming states from being merged.