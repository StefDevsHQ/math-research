# VS-06 Implementation Specification — Destroy Naive Summaries

**Slice:** `VS-06`  
**Status:** `COMPLETE / CHECKED`  
**Updated:** 2026-07-22

## Objective

Define concrete candidate summaries that might be used to merge exact states, then either:

1. produce a complete same-summary/different-semantics collision; or
2. retain the exact unresolved scope.

No statement concerns an undefined class of all local, algebraic, or spectral summaries.

## Semantic targets

Two exact observables are used.

### Whole-instance target

For summaries of a complete hypergraph, the discriminator is exact satisfiability.

### Prefix-state target

For a fixed instance, ordering, processing level, and prefix assignment, the discriminator is the exact completion mask from `VS-03`.

Globally unsatisfiable instances are not compared through successful-completion profiles because `NAE-011` makes all such profiles identically dead.

## Candidate summaries

The executable module `nae3sat/summaries.py` defines:

1. sorted degree sequence;
2. multiset of pairwise hyperedge-intersection sizes;
3. multiset of pair codegrees;
4. parity of vertex count, edge count, degrees, and pair codegrees;
5. edge/degree/pair-codegree first and second moments;
6. characteristic polynomial of the vertex incidence-Gram matrix;
7. root generalized arc-consistency domains;
8. satisfiability of every proper induced vertex subinstance;
9. boundary width and Hamming weight of the boundary assignment;
10. boundary width and parity of that Hamming weight;
11. multiset of rooted radius-`r` graph neighbourhoods in a conditioned residual encoding.

The exact boundary assignment together with the processed-consistency flag is retained as the complete same-level control.

## Bounded-radius construction

For every integer `r>=1`, define two graphs:

- `G_r^- = C_(2r+3) disjoint-union C_(2r+3)`;
- `G_r^+ = C_(2r+2) disjoint-union C_(2r+4)`.

Both have `4r+6` vertices, all degree two, and every cycle has length greater than `2r+1`. Every rooted radius-`r` neighbourhood is therefore the same rooted path on `2r+1` vertices. The rooted-neighbourhood multisets are equal.

`G_r^-` is non-bipartite because both cycles are odd. `G_r^+` is bipartite because both cycles are even.

For a graph `G`, construct `H(G)` with anchors `a,b` and one vertex for each graph vertex. For every graph edge `uv`, add NAE constraints `{a,u,v}` and `{b,u,v}`. Under the prefix assignment `a=0,b=1`, the first constraint forbids `u=v=0` and the second forbids `u=v=1`. Together they enforce `u!=v`. Thus the conditioned residual is satisfiable exactly when `G` is bipartite.

This proves `NAE-012`.

## Deterministic record

The command

```bash
python3 -m nae3sat.cli summary-collisions --output /tmp/vs06.json
```

reproduces `tools/monotone-nae-3sat/summary-collisions/vs06-summary-collisions.json` byte-for-byte.

The record contains ten explicit collisions, the bounded-radius family theorem and checked samples for radii one and two, the retained exact-boundary control, limitations, and a strict versioned payload digest.

The initial post-merge record was stale and caused workflow run `29954395327` to fail on all supported runtimes. It was regenerated from the checked implementation. The corrected semantic payload retains digest:

```text
ee7f47f96beafcda088848d8d29312e66df033376e68ac793f5e398a04aa8df6
```

## Verification

The executable gate now checks:

- every named summary collision;
- independent complete assignment enumeration for each whole-instance witness;
- exact stored solution counts and least witnesses;
- exact characteristic-polynomial values on known matrices;
- the anchored inequality reduction in both directions on odd and even controls;
- exact-boundary completeness through four vertices;
- bounded-radius samples;
- strict record-envelope rejection of malformed or re-digested wrong-format records;
- byte-for-byte record regeneration in the full gate.

## Complexity

- named whole-instance witnesses contain at most seven vertices;
- their semantics are verified independently by exhaustive enumeration of at most `2^7` colourings;
- exact prefix masks use the existing exponential `VS-03` oracle;
- the exact-boundary control is exhaustively checked through four vertices;
- the generic rooted-radius canonicalizer is factorial in the radius-ball size and is a verification tool, not a proposed algorithm;
- the bounded-radius theorem itself is constructive and does not depend on the canonicalizer's runtime.

## Exit gate

Satisfied when every listed summary has an explicit collision or a proved retained scope, the record reproduces deterministically, inherited slices remain green, independent witness checks pass, and documentation and claims are synchronized.
