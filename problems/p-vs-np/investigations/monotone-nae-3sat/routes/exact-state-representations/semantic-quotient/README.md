# R1.2 — Exact Semantic Quotient over PCRNF

**Subroute:** `R1.2`  
**Status:** `READY — RECOMMENDED NEXT`  
**Dependency:** `NAE-017 — PROVED / CHECKED`

## Objective

Construct a polynomial-time exact equivalence or canonicalization over oriented PCRNF residuals that identifies at least some semantically equal but byte-distinct states.

For residuals `R` and `S`, the target relation is

```text
R equivalent S
iff
R and S accept exactly the same assignments to the same remaining labelled vertices.
```

The relation must be computable without enumerating all completions or invoking a hidden satisfiability oracle.

## Why this is a distinct subroute

PCRNF supplies exact residual syntax and exact transitions. It does not supply complete semantic equality.

This subroute changes the merge mechanism while retaining PCRNF as the trusted transition language.

## Candidate mechanisms

Each candidate must receive its own child directory before activation.

1. canonical decision diagrams;
2. deterministic decomposable circuits;
3. prime residual or minimal-forbidden-assignment closures;
4. exact component-interface summaries;
5. algebraic canonical forms with proved exactness.

## First mandatory witness

Any candidate must merge the two residuals from the five-vertex `NAE-018` counterexample while keeping residuals with different exact completion masks separate.

Passing this witness is necessary, not sufficient.

## Exact obligations

A candidate must specify:

- represented semantics;
- canonical equality or exact equivalence;
- restriction and transition;
- conjunction and decomposition;
- acceptance;
- complete binary encoding;
- maximum and total representation size;
- cost of all intermediate operations.

## Hard controls

- VS-07 four-vertex genuine merge;
- VS-08 five-vertex byte-equality failure;
- both fan orderings;
- `K_5^(3)` and Fano;
- VS-06 collision pairs;
- linear four-regular instances;
- verified canonical reduction outputs.

## Stop conditions

Close a candidate when:

1. equal canonical objects can have different completion sets;
2. equality or minimization requires an NP-hard semantic primitive;
3. intermediate or final representation size is superpolynomial on an explicit family;
4. the complete generated state graph remains unbounded by any proved polynomial;
5. it reduces only to an already known restricted-width method.

## Success condition

Promote only after proving both exactness and a polynomial complete-state bound. Finite merging evidence alone is insufficient.