# VS-08 Completion Audit — Oriented PCRNF

**Slice:** `VS-08`  
**Status:** `COMPLETE / CHECKED`  
**Route decision:** close the universal PCRNF route; retain exact oriented residualization  
**Updated:** 2026-07-23

## Exact determination

VS-08 implemented and attacked propagation-closed signed residual normal forms.

The final result has four parts.

1. Unoriented component-complement normalization is unsound for labelled completion semantics.
2. Adding one orientation bit per residual component repairs soundness.
3. Oriented PCRNF byte equality is not complete for exact completion equivalence.
4. No polynomial bound on the complete reachable PCRNF state graph was proved or supported strongly enough to retain `NAE-016`.

Accordingly:

- `NAE-016` is `RETRACTED`, not `DISPROVED`;
- exact oriented PCRNF residualization is retained as `NAE-017 — PROVED / CHECKED`;
- semantic completeness of PCRNF byte equality is `NAE-018 — DISPROVED / CHECKED`.

## NAE-017 — exact oriented residualization

For a fixed labelled instance, ordering and prefix, direct substitution produces unary, signed-binary and ternary residual constraints.

Each transformation is exact:

- an unprocessed NAE edge remains ternary;
- one fixed colour `c` yields `not(x_u=x_v=c)`;
- two equal fixed colours `c` force the third variable to `1-c`;
- two different fixed colours satisfy the edge;
- a fully fixed monochromatic edge yields contradiction;
- a fully fixed nonmonochromatic edge is deleted.

Propagation repeatedly applies the same exact substitutions. Every nontrivial rewrite removes a constraint, lowers its arity, or adds a previously absent unary force. There are finitely many vertices and residual constraints, so the specified deterministic work-list process terminates.

Residual incidence components may be complemented independently, but exact labelled semantics require recording whether the stored canonical component is complemented relative to the original colour coordinates. With one flip bit per component, decoding restores the exact labelled residual relation.

Therefore, for every assignment `q` to the remaining labelled vertices,

```text
prefix + q satisfies the original instance
iff
q satisfies the decoded oriented PCRNF.
```

Restriction of the next variable followed by closure is an exact transition.

## Unoriented normalization counterexample

Use the single edge `{0,1,2}`, ordering `(0,1,2)`, and level two.

- prefix `00` leaves `x_2=1`, completion mask `2`;
- prefix `11` leaves `x_2=0`, completion mask `1`.

The two one-vertex components become identical if the complement orientation is discarded. Thus the claim that component-complement normalization can forget orientation while preserving labelled completion sets is `DISPROVED`.

The implementation repairs this with an explicit component flip bit.

## NAE-018 — PCRNF equality is not semantic equality

The five-vertex instance

```text
edges = {
  012, 013, 023, 034, 123, 124
}
ordering = (0,4,1,2,3)
level = 2
```

has prefixes `00` and `01` with the same exact completion mask

```text
40
```

but different oriented PCRNFs.

For prefix `00`, the residual separates into:

- both signed binary constraints on pair `{1,2}`;
- a forced value on vertex `3`.

For prefix `01`, the residual is one connected component containing:

- both signed constraints on `{1,2}`;
- signed constraints on `{1,3}` and `{2,3}`;
- ternary NAE constraint `{1,2,3}`.

The residual formulas define the same set of eight-bit-indexed completions but are not byte-identical. Hence PCRNF byte equality is strictly finer than exact extension equivalence.

This is a complete counterexample to semantic completeness of the selected equality relation.

## Finite exhaustive audit

Every labelled simple three-uniform instance and every ordering through four vertices was checked.

At `n=4`:

```text
profiles                 384
levels                   1920
prefixes                 11904
PCRNF states             4248
exact completion classes 4248
live PCRNF states        3696
dead PCRNF states        552
incompleteness excess    0
complete encoded bytes   731712
```

Thus oriented PCRNF equality happens to coincide with exact completion equivalence throughout this finite domain. The five-vertex witness shows that this pattern does not continue universally.

## Fan-family attack

For the bad fan ordering, the PCRNF peak is exactly

```text
2^(k+1)-1.
```

The states encode the different labelled unary-force patterns already identified by VS-07.

For the interleaved ordering, the peak is at most five, including a possible dead state.

Therefore PCRNF preserves the established ordering separation. It supplies no ordering-independent lower bound and no new global polynomial-state theorem.

## Complexity audit

One explicit PCRNF has polynomial encoded size: it contains at most the remaining vertices, unary records, signed binary records derived from original edges, ternary residual edges, component framing and orientation bits.

This is insufficient for polynomial time. The complete memoized computation graph may contain exponentially many distinct PCRNFs, as the bad fan ordering demonstrates.

No theorem was found that constructs, for every input, an ordering with polynomially many reachable PCRNFs and polynomial total encoded state. No exact merge rule beyond byte equality survived the requirement of polynomial-time construction without a semantic oracle.

## Route decision

`NAE-016` is retracted because the proposed universal polynomial-state claim lacks a surviving theorem or mechanism.

It is not marked `DISPROVED`: the five-vertex witness refutes semantic completeness of byte equality, but does not prove that every ordering of some family has exponentially many PCRNFs.

Retained results:

- exact oriented residual construction;
- exact transition and acceptance;
- deterministic canonical encoding;
- explicit unsoundness of orientation-free normalization;
- explicit incompleteness of byte equality;
- reproducible state-growth measurements.

## Scope

Nothing here proves `P=NP`, `P!=NP`, or a lower bound for arbitrary representations. The route should not be reopened without a new exact merge mechanism and a globally polynomial bound on the complete generated state graph.
