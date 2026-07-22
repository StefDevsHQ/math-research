# R1.1 — Propagation-Closed Signed Residual Normal Form

**Subroute:** `R1.1`  
**Status:** `CLOSED AS UNIVERSAL / RETAINED AS EXACT AND RESTRICTED`  
**Primary claim:** `NAE-016 — DISPROVED / CHECKED`  
**Completed slices:** `VS-08`, `VS-09A`

## Thesis

Process variables in an ordering and represent every residual instance by a propagation-closed signed residual normal form containing:

- labelled remaining vertices;
- unary colour requirements;
- signed binary constraints;
- residual ternary NAE constraints;
- residual incidence components;
- explicit component orientation bits.

Memoize identical residual states and attempt to bound the complete generated state graph polynomially.

## Retained theorem — NAE-017

`NAE-017 — PROVED / CHECKED`:

- direct residualization is exact;
- deterministic closure terminates;
- component complement is exact when orientation is recorded;
- next-variable restriction and re-closure are exact transitions.

PCRNF remains a valid exact residual substrate.

## Earlier model boundary — NAE-018

`NAE-018 — DISPROVED / CHECKED`:

> Byte equality of oriented PCRNF is exact completion equivalence.

The five-vertex witness has two different PCRNFs with the same exact completion mask. Orientation-free normalization was also disproved independently on a single edge.

## Universal lower bound — NAE-019 and NAE-020

`NAE-019 — PROVED / CHECKED` shows that PCRNF state count dominates exact residual-function count.

`NAE-020 — PROVED / CHECKED` constructs central lifts of constant-degree expanders for which every variable ordering has one level containing `2^{Omega(n)}` pairwise distinct live exact completion functions. Therefore every ordering has `2^{Omega(n)}` oriented PCRNF states.

This attacks the existential ordering quantifier directly and yields:

```text
NAE-016 — DISPROVED / CHECKED.
```

## Final determination

The universal state-enumeration route is closed:

```text
some efficient ordering gives polynomial total PCRNF state
```

is false.

The route retains:

1. exact oriented residualization and transitions;
2. restricted PCRNF algorithms on explicitly bounded classes;
3. the all-ordering expander lower bound;
4. executable lower-bound certificate helpers;
5. a transfer principle from exact residual functions to PCRNF states.

## Remaining restricted track

Polynomial PCRNF behaviour may still be proved under explicit hypotheses such as:

- bounded boundary width;
- bounded incidence treewidth;
- bounded residual component size;
- other exact structural parameters.

Such results are restricted theorems and do not reopen `NAE-016`.

## Handoff

The all-ordering lower bound also blocks any ordered method that materializes one exact state per residual completion function. It does not rule out a collective representation sharing many residual functions inside one circuit or global object.

Continue through:

- [decomposable circuits](../decomposable-circuits/README.md);
- non-ordered or collective exact representations;
- algebraic or global methods;
- restricted PCRNF classes.

A simple semantic quotient that merely merges equal residual functions cannot defeat `NAE-020`, because the hard family already contains exponentially many semantically distinct functions.

## Evidence

- [NAE-016 expander disproof](proofs/NAE-016-expander-disproof.md)
- [VS-08 preparation](../../../VS-08-PREPARATION.md)
- [VS-08 implementation](../../../VS-08-IMPLEMENTATION.md)
- [VS-08 completion audit](../../../VS-08-AUDIT.md)
- executable module `tools/monotone-nae-3sat/nae3sat/pcrnf_lower_bound.py`
- tests `tools/monotone-nae-3sat/tests/test_nae016_lower_bound.py`

## Reopening rule

Do not reopen universal ordered PCRNF enumeration. A reopening would require changing the computation model materially, such as representing many residual functions collectively rather than enumerating one state per function.