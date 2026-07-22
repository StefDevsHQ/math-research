# VS-07 Completion Audit — Genuine Semantic Merging

**Slice:** `VS-07`  
**Status:** `COMPLETE / CHECKED`  
**Classification:** Exact theorem, finite exhaustive computation, explicit witness, and complexity audit  
**Updated:** 2026-07-22

## Exact determination

VS-07 establishes three separate facts.

1. **Genuine live merging exists.** A four-vertex satisfiable instance has an all-live level where exact completion equivalence merges prefixes from distinct component-complement orbits.
2. **A fixed ordering can have exponentially many live exact states.** The fan family has `2^(k+1)-1` live exact classes at one level of the bad ordering.
3. **That growth can be purely ordering-induced.** The same fan family has an interleaved ordering of boundary width at most two.

The results do not establish an ordering-independent lower bound or a lower bound for arbitrary symbolic representations.

## Claim NAE-014 — fan ordering-separation theorem

For every integer `k>=1`, let `F_k` have vertices

```text
c,a_1,...,a_k,b_1,...,b_k
```

and constraints `{c,a_i,b_i}`.

### Bad ordering proof

Use ordering

```text
c,a_1,...,a_k,b_1,...,b_k
```

and stop after assigning `c,a_1,...,a_k`.

For a prefix define

```text
E = {i : a_i = c}.
```

For each `i`:

- if `i in E`, the constraint forces `b_i=1-c`;
- if `i not in E`, the edge already contains both colours, so `b_i` is free.

Every prefix is therefore live.

The completion mask is determined by `(c,E)`. If `E` is nonempty, different pairs `(c,E)` give different forced-coordinate patterns. If `E` is empty, both values of `c` give the full completion mask. Hence the number of exact live masks is

```text
2(2^k-1)+1 = 2^(k+1)-1.
```

The incidence graph is connected. Global complement pairs the `2^(k+1)` prefixes into `2^k` prefix orbits. Complement also pairs the semantic masks, except for the full mask, giving `2^k` semantic orbits. Equality of masks does not identify two distinct prefix complement orbits.

Every processed vertex `c,a_1,...,a_k` occurs with an unprocessed `b_i`, so the boundary contains all `k+1` processed vertices. Thus there are `2^(k+1)` live boundary assignments.

### Good ordering proof

Use

```text
c,a_1,b_1,...,a_k,b_k.
```

After assigning `c`, the boundary is `{c}`. Between `a_i` and `b_i`, it is contained in `{c,a_i}`. After `b_i`, vertex `a_i` expires, leaving at most `{c}` while later edges remain. At the end the boundary is empty.

Therefore maximum processed boundary width is at most two. By exact-boundary completeness, there are at most four live exact classes at every level, and at most five total classes if a dead class is included.

**Status:** `PROVED / CHECKED`.

## Claim NAE-015 — finite genuine-merging evidence

The four-vertex instance

```text
edges = {012,013}
ordering = (0,2,3,1)
level = 3
```

has completion masks

```text
(2,2,2,3,3,1,1,1).
```

All prefixes are live. Exact enumeration verifies three live exact classes, four live prefix complement orbits, two semantic complement orbits, and exact merging across prefix-orbit boundaries.

The exhaustive census covers all labelled instances and all orderings through four vertices. In the `n=4` row, 96 levels are both all-live and exhibit cross-orbit exact merging.

**Status:** `COMPUTATIONAL / CHECKED`.

## Independent attack

The slice was attacked for:

- counting dead-state collapse as compression;
- counting a prefix and its global complement as a new merge;
- quotienting prefix states without quotienting completion masks consistently;
- comparing different processing levels;
- treating processed-valid boundary states as live states;
- inferring semantic compactness from JSON size;
- inferring representation lower bounds from explicit mask counts;
- inferring intrinsic hardness from one bad ordering;
- overlooking isolated-vertex and disconnected-component complement actions;
- silently using total classes where the claim concerns live classes.

The attack corrected the interleaved fan statement: width two implies at most four live exact classes; five is only a conservative bound on total classes including a possible dead class.

## Representation audit

The record distinguishes:

- dense exact-mask bytes;
- dense live-mask bytes;
- packed assignment-to-class bytes;
- explicit live-boundary bytes;
- complete canonical profile JSON bytes.

None is claimed optimal. They are reproducible reference encodings.

The central distinction is:

```text
number of semantic classes != size of a symbolic representation
```

and

```text
small symbolic syntax != polynomial-time exact operations.
```

No representation family has yet been selected for VS-08.

## Limitations

- Exhaustive computation stops at four vertices.
- The fan family is easy under a good order and is not an NP-hard control.
- The bad-order theorem is a fixed-order lower bound only.
- No lower bound is proved for reduced decision diagrams, circuits, automata, ideals, or arbitrary exact representations.
- No universal polynomial algorithm is obtained.
- No conclusion about `P=NP` or `P!=NP` follows.

## Final determination

`VS-07` is `COMPLETE / CHECKED`.

It isolates the next exact question:

> Which relation allows genuine all-live semantic merging, and can that relation be represented and transitioned exactly with polynomial total size on adversarial high-width instances?

`VS-08` is ready to extract one atomic candidate invariant. The recommended first target is a residual-constraint representation normalized by component complement, because VS-07 shows that exact future equivalence can merge distinct boundary assignments while the fan family shows that symmetry alone is insufficient under bad orders.
