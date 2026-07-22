# VS-03 Completion Audit — Exact Extension Profiles

**Slice:** `VS-03`  
**Status:** `COMPLETE / CHECKED` pending final PR automation and merge  
**Classification:** Proof, implementation, exhaustive computation, and complexity audit  
**Updated:** 2026-07-22

## Scope

VS-03 constructs exact completion behaviour for a fixed labelled Monotone NAE-3SAT instance and a fixed vertex ordering. It computes every prefix completion set, quotients prefixes only by equality of those sets, constructs both colour transitions, and compares acceptance with the checked VS-02 oracle.

The implementation is exponential. This audit does not claim that the exact quotient is polynomially bounded or efficiently constructible on unrestricted instances.

## Implemented artifacts

Under `tools/monotone-nae-3sat/`:

- `nae3sat/profile.py`: exact completion masks, quotient classes, transitions, boundary comparisons, and canonical profile records;
- `nae3sat/profile_census.py`: deterministic exhaustive aggregate profile census and per-profile sequence digests;
- `tests/test_vs03.py`: tuple-set reference engine, controls, finite exhaustive gates, CLI checks, and corpus reproduction;
- `tests/test_vs03_sequence_digest.py`: independent ordered digest of every exact finite profile;
- `profile-corpus/all-labelled-orderings-n-le-5.json`: canonical finite profile corpus;
- CLI commands `profile` and `profile-census`;
- Python 3.11, 3.12, and 3.13 automated gates.

## Exact-mask theorem

### Claim

For every canonical instance `H`, ordering `pi`, level `i`, and prefix assignment `a`, the integer mask constructed by `build_exact_profile` is the characteristic bit vector of

\[
\operatorname{Ext}_{H,\pi,i}(a).
\]

### Proof

Proceed by reverse induction on `i`.

At `i=n`, the remainder is empty. There is one possible completion, the empty tuple. The construction assigns mask `1` exactly when the full assignment satisfies every edge and mask `0` otherwise.

Assume the claim at level `i+1`. Every completion at level `i` begins uniquely with next colour `0` or `1`. Under lexicographic completion order, the `0` completions form the lower half and the `1` completions form the upper half. If the child masks are `M_0` and `M_1`, the construction forms

\[
M=M_0+(M_1\ll 2^{n-i-1}).
\]

By the induction hypothesis, the two halves are exactly the satisfying completions following each next colour. Their concatenation is exactly the parent completion set. ∎

**Status:** `PROVED / CHECKED`.

## Quotient and transition correctness

The implementation scans prefix masks in lexicographic prefix order and assigns a class identifier on first occurrence. Two prefixes receive the same class exactly when their canonical completion masks are equal, hence exactly when their completion sets are equal.

For a class mask `M`, the `0` and `1` successors are its lower and upper halves. Equal parent masks have equal halves, so transitions are independent of representative. Every successor half is looked up in the next level; absence is an internal consistency failure.

At level zero, the unique root mask is nonzero exactly when some satisfying assignment exists. At level `n`, masks are only `0` and `1`. Therefore profile acceptance equals satisfiability.

**Status:** `PROVED / CHECKED`.

## Boundary comparison semantics

At level `i`, the processed boundary contains precisely processed vertices occurring in an edge that also contains an unprocessed vertex.

`processed_valid_boundary_states` counts distinct boundary colourings induced by prefixes that have not violated any edge wholly contained in the processed prefix. It is a comparison with ordinary boundary dynamic programming, not the exact quotient.

## Exhaustive domain proof

For each `n`, edge masks enumerate all

\[
2^{\binom n3}
\]

labelled simple 3-uniform hypergraphs exactly once. `itertools.permutations(range(n))` enumerates all `n!` orderings exactly once. Thus the declared domain has

\[
\sum_{n=0}^{5}2^{\binom n3}n!=123280
\]

instance-ordering pairs.

## Independent reference evidence

The reference implementation does not use production integer-mask construction. It:

- enumerates complete assignments directly;
- stores each prefix completion set as a `frozenset` of completion tuples;
- assigns classes by equality of those sets;
- derives each transition from every class member;
- computes boundary states independently;
- aggregates the complete finite census separately.

Exact per-profile comparison is performed through four vertices, for all 120 orderings of the complete five-vertex obstruction, and for named disconnected, chain, single-edge, isolated, and Fano controls.

For the complete 123280-profile domain, both engines also compute an ordered profile-sequence SHA-256 for each `n`. Each profile signature contains its graph mask, ordering, every level's exact class masks, assignment partition, transitions, and boundary count. Therefore a disagreement in any individual profile changes the digest even if aggregate totals happen to cancel.

The six independently checked sequence digests are:

| `n` | Profile-sequence SHA-256 |
|---:|---|
| 0 | `383b6a55cb5c582dd98b505f0c0b7ab4ade288e4edf6e718524335f0cb1c44a9` |
| 1 | `28914bb8bb75644fabf9e97c1289735d68a1ee4ff707d8879e28cd7afc30f1f7` |
| 2 | `53d9dd4f1648414f7d05958cfd183518f245980f0db8197c10bee00143bf94e0` |
| 3 | `e4ff0bd86f840e4cdd516e7a6fa71158f2a5224f7ff0dc1a781d5728f0a5b1d2` |
| 4 | `26ffbfd05952ca42f3f64254cea3a58a704d0ef1b2914bb29d93e47368d6ad68` |
| 5 | `92c78b0455e3ce450ab6e511f66bfa903253a2a17de44610d6fb0db904b06d77` |

## Exact finite results

| Metric | Exact value |
|---|---:|
| Instance-ordering profiles | `123280` |
| Satisfiable-root profiles | `123160` |
| Unsatisfiable-root profiles | `120` |
| Raw prefixes | `7753542` |
| Exact classes | `2153049` |
| Live exact classes | `1818651` |
| Processed-valid boundary states | `2865585` |
| Dense unique completion bits | `15198660` |
| Assignment-map bits | `11673564` |
| Transition bits | `7146336` |
| Maximum classes at one level | `8` |

The `120` unsatisfiable profiles are the 120 orderings of the unique unsatisfiable five-vertex instance from VS-02.

These results are `COMPUTATIONAL / CHECKED` and exhaustive only for the declared finite domain.

## Pinned live semantic merge

For the single edge `((0,1,2),)` under ordering `(0,1,2)`, the distinct level-two prefixes `01` and `10` both have completion mask `3`, representing both remaining colours. This is a genuine nonzero exact merge, not dead-state collapse. The same profile contains a dead final class for monochromatic assignments.

## Canonical records

A profile record is canonical for a fixed labelled instance and ordering. Class masks are fixed-width hexadecimal strings whose width includes leading semantic zeros.

The profile corpus stores aggregate count rows separately from a top-level per-`n` sequence-digest map. Its payload digest is SHA-256 of compact canonical JSON with the digest field omitted. The strengthened committed corpus digest is:

```text
8b52eec88a16d6650b081cb197c4e955c0172e9f9558a1043fcca6ff997040cf
```

## Complexity audit

For `n` vertices and `m` edges:

- full-assignment truth evaluation uses `O(2^n(n+m))` time in the concrete implementation;
- the assignment-mask table contains exactly `(n+1)2^n` semantic bits before Python overhead;
- bottom-up construction and integer-mask hashing process `O(n2^n)` semantic bits;
- assignment-to-class maps contain `2^(n+1)-1` identifiers;
- the number of directed colour transitions is `2 sum_{i=0}^{n-1}q_i`;
- dense unique class-mask storage satisfies
  \[
  \sum_i q_i2^{n-i}\le(n+1)2^n;
  \]
- direct processed-boundary enumeration is `O(n2^n m)`;
- full canonical profile output is exponential and output-sensitive.

Python integers, tuples, dictionaries, and sets add implementation-dependent object overhead. Semantic bit counts are recorded separately from resident memory.

The profile census precomputes violation masks per ordering. This improves finite-domain constants without changing the exponential domain size.

## Break pass

The attack pass checked:

- leading-zero mask width;
- lexicographic completion orientation;
- first-occurrence class numbering;
- transition agreement for every member of a reference class;
- per-profile ordered sequence identity across the entire finite domain;
- dead versus live merging;
- ordering validation and malformed CLI input;
- root and final-level boundary cases;
- VS-02 acceptance agreement;
- deterministic corpus reproduction;
- cross-version execution.

A CI failure during the strengthened review was traced to a schema collision in the tests: the independent aggregate row was compared with a production row after the latter gained a `profile_sequence_sha256` field. The digest and aggregate values agreed; the metadata was moved to a dedicated top-level map so the independent aggregate schema remains exact and the sequence gate remains separate.

No unresolved substantive defect remains pending the final automated PR result.

## Final determination

After the automated matrix and pinned full reference gates pass, `VS-03` is `COMPLETE / CHECKED`.

The retained result is an exact exponential semantic-state laboratory. The next work is control calibration and obstruction analysis, not a claim that exact quotient construction is tractable in general.
