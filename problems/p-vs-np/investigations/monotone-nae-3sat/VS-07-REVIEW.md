# VS-07 Post-Merge Review — Semantic Merging

**Slice:** `VS-07`  
**Review status:** `CHECKED`  
**Updated:** 2026-07-22

## Determination

The mathematical conclusions of VS-07 survive full review.

- `NAE-014` remains `PROVED / CHECKED`.
- `NAE-015` remains `COMPUTATIONAL / CHECKED`.
- No ordering-independent lower bound, representation lower bound, polynomial-time algorithm, or conclusion about `P` versus `NP` follows.

The review found one documentation/artifact mismatch and two verification/engineering gaps. They do not refute either claim, but they required correction and explicit recording.

## Rechecked mathematics

### Fan bad ordering

For `F_k` with edges `{c,a_i,b_i}` and order

```text
c,a_1,...,a_k,b_1,...,b_k,
```

stop after `c,a_1,...,a_k`. Let

```text
E = {i : a_i=c}.
```

Every prefix is live. For `i in E`, `b_i` is forced to `1-c`; for `i not in E`, `b_i` is free. The completion set is therefore determined by `(c,E)`.

- For `E != empty`, distinct pairs `(c,E)` give distinct exact completion sets.
- For `E = empty`, both values of `c` give the full completion set.

Hence

```text
2(2^k-1)+1 = 2^(k+1)-1
```

live exact classes occur at level `k+1`.

The incidence graph is connected, so global complement gives `2^k` prefix orbits and `2^k` semantic-mask orbits. Exact equality merges no two distinct prefix complement orbits at this level.

All `k+1` processed variables remain on the boundary, giving `2^(k+1)` live boundary assignments.

### Fan interleaved ordering

For

```text
c,a_1,b_1,...,a_k,b_k,
```

the boundary is contained in `{c}` except between `a_i` and `b_i`, when it is contained in `{c,a_i}`. Thus width is at most two.

Exact boundary completeness gives at most

```text
2^2 = 4
```

live exact classes at every level. A fifth class is possible only when counting one dead class as well.

The boundary cases `k=1`, the final level, and levels before the first completed edge are consistent with the proof.

### First all-live genuine merge

For edges `{012,013}`, order `(0,2,3,1)`, and level three, independent enumeration gives

```text
(2,2,2,3,3,1,1,1).
```

All eight prefixes are live. The four global-complement prefix orbits map into two semantic complement orbits, while exact equality has three classes. Two exact classes contain members from multiple prefix-complement orbits. The merge is therefore not dead-state collapse and not direct complement identification.

## Findings

### Finding 1 — conservative record bound

The authoritative proof and claim ledger state the sharp live bound `4`, but the committed version-one record stores

```text
"maximum_live_exact_classes": 5
```

for the good fan ordering.

This is not a false upper bound: `5` remains valid, but it is conservative and its field name does not explain that one extra class is only the possible dead class. The record samples themselves peak at four live classes.

**Resolution:**

- the executable family assertion now enforces the sharp bound `4`;
- the independent test now enforces the sharp bound `4`;
- the version-one record is retained byte-for-byte as historical reproducibility evidence and is explicitly documented as conservative;
- any future record format must store `4` as the live bound and, if desired, `5` separately as the total-class bound.

### Finding 2 — missing unsatisfiable controls

The exhaustive `n<=4` census contains no unsatisfiable three-uniform instance. It therefore did not directly exercise the all-dead profile case inside VS-07.

**Resolution:** exact tests now run both `K_5^(3)` and the Fano plane and verify at every level:

- zero live prefixes;
- one dead exact class;
- zero live semantic orbits;
- zero live boundary states;
- every processed-valid boundary state is dead.

This independently reconnects VS-07 to `NAE-011`.

### Finding 3 — repeated exact-profile reconstruction

`measure_semantic_merging_profile` constructed one exact profile and then reconstructed the same profile once per level.

**Resolution:** the implementation now constructs the exact profile once and passes it to an internal fixed-level measurement routine. This changes no metric or committed record byte.

### Finding 4 — byte-accounting terminology

The per-level dense-mask, packed-map, and explicit-boundary byte fields count raw fixed-width payload only. They exclude framing, field names, cardinality metadata, and decoder conventions. Only `exact_profile_json_bytes` is a complete serialized record size.

**Resolution:** implementation documentation and helper docstrings now state this explicitly. These fields remain reference payload measures, not optimal or self-delimiting representation sizes.

## Independent attack retained

The review again checked for:

- dead-state collapse reported as useful compression;
- direct component complement reported as a new merge;
- inconsistent prefix and suffix symmetry actions;
- comparisons across different levels;
- processed-valid states confused with live states;
- a raw payload count presented as a complete encoding;
- fixed-order growth presented as intrinsic hardness;
- exact class count presented as a symbolic-representation lower bound;
- a compact residual syntax presented as polynomial-time semantic equivalence.

No mathematical contradiction was found.

## Final status

`VS-07` remains `COMPLETE / CHECKED`.

The review sharpens the handoff to VS-08:

> A useful representation must explain genuine live merging, preserve exact labelled completion behaviour, expose exact transitions, and avoid hiding residual satisfiability or semantic equivalence inside an intractable operation.
