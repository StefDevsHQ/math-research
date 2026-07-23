# R1.4 — Decomposable Circuit Representations

**Subroute:** `R1.4`  
**Status:** `CLOSED UNIVERSAL / RETAINED RESTRICTED`

## Original thesis

Represent exact completion behaviour by deterministic or structured decomposable circuits so that repeated semantic subproblems can be shared without enumerating one state per residual function.

## Determination

`NAE-021 — PROVED / CHECKED` closes DNNF as a universal polynomial exact-representation route.

For the central lifts of constant-degree expanders used in `NAE-020`, conditioning the centre to zero yields bounded-degree monotone two-CNFs whose clause graphs have linear treewidth. The established lower bound of Amarilli, Capelli, Monet, and Senellart then forces DNNF size `2^{Omega(n)}`. Conditioning cannot increase DNNF size, so the unconditioned central lifts also require exponential DNNF size.

Because the theorem applies to unrestricted DNNF, it also applies to every subclass, including:

- deterministic DNNF;
- structured DNNF;
- deterministic structured DNNF;
- decision DNNF.

## Retained scope

Decomposable compilation remains useful on explicitly restricted classes, including bounded-treewidth inputs and any class for which a separate polynomial-size compilation theorem is proved.

## Closed obligations

The route no longer needs attacks based only on canonicity, equality, or transition cost: representation size itself is already exponential on the hard family.

## Reopening rule

Do not reopen `R1.4` as a universal route unless the proposed language is not a DNNF subclass and no polynomial-overhead translation to DNNF is assumed. Any reopening must fix exact syntax, semantics, operations, size measure, and a survival argument against `NAE-021`.

## Evidence

- [NAE-021 DNNF lower bound](proofs/NAE-021-dnnf-expander-lower-bound.md)
- [NAE-020 ordered-state lower bound](../pcrnf/proofs/NAE-016-expander-disproof.md)