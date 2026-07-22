# VS-07 Implementation Specification — Measure Genuine Semantic Merging

**Slice:** `VS-07`  
**Status:** `COMPLETE / CHECKED`  
**Updated:** 2026-07-22

## Objective

Measure exact completion-state merging without confusing it with:

- globally dead prefixes;
- componentwise colour-complement symmetry;
- exact boundary-state merging;
- a compact-looking but large or expensive encoding;
- a poor variable ordering.

The semantic observable remains the exact completion mask from `VS-03`.

## Fixed-level definitions

For a fixed instance, ordering, and processing level:

- a **live prefix** has at least one satisfying completion;
- a **dead prefix** has completion mask zero;
- an **exact semantic class** is an equality class of completion masks;
- a **component-complement prefix orbit** is an orbit under independently complementing incidence components;
- a **semantic component-complement orbit** identifies completion masks under the induced suffix flips;
- a **genuine exact merge** occurs when one exact live class contains prefixes from more than one component-complement prefix orbit;
- a **live boundary state** is an exact processed-boundary assignment attained by a live prefix.

The implementation records raw counts, live/dead counts, exact classes, symmetry quotients, boundary counts, dense-mask bytes, assignment-map bytes, explicit-boundary bytes, and full canonical profile JSON bytes.

## Executable implementation

The module `nae3sat/semantic_merging.py` provides:

- `measure_semantic_merging_level`;
- `measure_semantic_merging_profile`;
- strict immutable metric records;
- exact component-complement actions on prefixes and completion masks;
- independent processed-boundary reconstruction;
- fan-family constructors and good/bad orderings.

The deterministic research record is produced by:

```bash
python3 -m nae3sat.semantic_merging_cli \
  --output /tmp/vs07-semantic-merging.json
```

The committed output is:

```text
tools/monotone-nae-3sat/semantic-merging/vs07-semantic-merging.json
```

The full gate regenerates this record and requires exact byte equality.

## First all-live genuine merge

Let

```text
H = ({0,1,2,3}, {{0,1,2},{0,1,3}})
ordering = (0,2,3,1)
level = 3
```

The exact completion masks, in lexicographic prefix order, are

```text
(2,2,2,3,3,1,1,1).
```

Therefore:

- all eight prefixes are live;
- there are three exact live classes;
- there are four prefix complement orbits;
- there are two semantic complement orbits;
- two exact classes contain multiple prefix complement orbits.

This is finite exact evidence that useful semantic merging exists beyond dead-state collapse and beyond direct identification of complement-related prefixes.

## Fan family

For `k>=1`, define `F_k` on vertices

```text
c,a_1,...,a_k,b_1,...,b_k
```

with edges

```text
{c,a_i,b_i}, 1<=i<=k.
```

### Bad ordering

For

```text
c,a_1,...,a_k,b_1,...,b_k
```

at level `k+1`:

- all `2^(k+1)` prefixes are live;
- exact live class count is `2^(k+1)-1`;
- prefix complement-orbit count is `2^k`;
- semantic complement-orbit count is `2^k`;
- live boundary-state count is `2^(k+1)`;
- no exact class merges distinct complement prefix orbits.

Thus the bad ordering has exponential live exact-state growth, and its only meaningful prefix reduction at this level is global complement symmetry.

### Interleaved ordering

For

```text
c,a_1,b_1,...,a_k,b_k
```

the processed boundary has size at most two. Exact boundary completeness therefore gives at most four live exact classes at every level. The executable record retains the conservative checked bound of five total classes, allowing one dead class.

This proves strong ordering dependence. It is not an intrinsic lower bound for `F_k`, because the good ordering yields a constant-width dynamic programme.

## Exhaustive finite domain

The census covers every labelled simple three-uniform hypergraph and every ordering through four vertices:

```text
profiles by n = 1, 1, 2, 12, 384.
```

At `n=4`, across 384 profiles and 1,920 levels, the record contains:

- 11,904 raw prefixes;
- 9,264 live prefixes;
- 2,640 dead prefixes;
- 4,248 exact classes;
- 3,696 live exact classes;
- 4,080 live prefix complement orbits;
- 2,520 live semantic complement orbits;
- 4,824 live boundary states;
- 648 levels with cross-orbit exact merging;
- 96 all-live levels with cross-orbit exact merging.

These are finite computational facts only.

## Verification

The gate checks:

- independent brute-force completion masks for the first witness;
- live/dead partition invariants;
- exact-boundary dominance of live semantic classes;
- fan bad-order formulas through six edges;
- fan good-order width and class bounds through eight edges;
- strict record-envelope rejection;
- deterministic record byte reproduction;
- inherited `VS-01` through `VS-06` gates.

## Complexity and scope

The measurement engine is an exponential reference instrument. It constructs exact completion masks and explicitly enumerates finite prefix and symmetry actions. The census through four vertices and named fan samples are not proposed algorithms for general instances.

A large exact quotient for one ordering does not prove every ordering is large. A large explicit quotient also does not prove every exact symbolic language is large. Conversely, a small number of semantic classes does not imply that those classes can be constructed, compared, transitioned, or encoded in polynomial total size.
