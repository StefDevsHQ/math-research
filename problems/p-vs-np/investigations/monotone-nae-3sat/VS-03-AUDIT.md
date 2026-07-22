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
- `nae3sat/profile_census.py`: deterministic exhaustive aggregate profile census;
- `tests/test_vs03.py`: independent tuple-set reference engine, named controls, finite exhaustive gates, CLI checks, and corpus reproduction;
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

At `i=n`, the remainder is empty. There is one possible completion, the empty tuple. The construction assigns mask `1` exactly when the full assignment satisfies every edge and mask `0` otherwise. This is the required characteristic vector.

Assume the claim at level `i+1`. Every completion at level `i` begins uniquely with next colour `0` or `1`. Under lexicographic completion order, the `0` completions form the lower half and the `1` completions form the upper half. If the child masks are `M_0` and `M_1`, the construction forms

\[
M=M_0+(M_1\ll 2^{n-i-1}).
\]

By the induction hypothesis, the two halves are exactly the satisfying completions following each next colour. Their concatenation is exactly the parent completion set. ∎

**Status:** `PROVED / CHECKED`.

## Quotient and transition correctness

The implementation scans prefix masks in lexicographic prefix order and assigns a class identifier on first occurrence. Therefore two prefixes receive the same class exactly when their canonical completion masks are equal, which is exactly equality of completion sets by the theorem above.

For a class mask `M`, the `0` and `1` successors are the lower and upper mask halves. Equal parent masks have equal halves, so the transitions are independent of the chosen representative. Every successor half is looked up in the next level; absence is treated as an internal consistency failure.

At level zero, the unique root mask is nonzero exactly when some full satisfying assignment exists. At level `n`, masks are only `0` and `1`. Thus profile acceptance equals satisfiability.

These implications are independently checked against VS-02 and against a tuple/frozenset reference engine.

**Status:** `PROVED / CHECKED`.

## Boundary comparison semantics

For each level, the processed boundary contains precisely the processed vertices occurring in an edge that also contains an unprocessed vertex.

The recorded `processed_valid_boundary_states` count is the number of distinct boundary colourings induced by prefixes that have not already violated an edge wholly contained in the processed prefix.

This quantity is a comparison with ordinary boundary dynamic programming. It is not the exact quotient and may be larger or smaller than the number of live exact classes for different reasons.

## Exhaustive domain proof

For each `n`, edge masks enumerate all

\[
2^{\binom n3}
\]

labelled simple 3-uniform hypergraphs exactly once. `itertools.permutations(range(n))` enumerates all `n!` orderings exactly once. Therefore the declared domain contains exactly

\[
\sum_{n=0}^{5}2^{\binom n3}n!
=123280
\]

instance-ordering pairs.

## Independent reference engine

The reference implementation does not use integer completion masks. It:

- enumerates complete assignments directly;
- stores each prefix completion set as a `frozenset` of completion tuples;
- assigns classes by equality of those sets;
- derives each transition from all class members;
- computes boundary states independently;
- aggregates the complete finite census separately.

The production and reference aggregate records agree on all `123280` declared profiles. Exact per-profile comparison is additionally performed for every profile through four vertices, all 120 orderings of the complete five-vertex obstruction, and named disconnected, chain, single-edge, isolated, and Fano controls.

## Exact finite results

The committed corpus records:

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

These results are `COMPUTATIONAL / CHECKED`. They are exhaustive only for the declared finite domain.

## Pinned live semantic merge

For the single edge `((0,1,2),)` under ordering `(0,1,2)`, the distinct level-two prefixes `01` and `10` both have completion mask `3`, representing both remaining colours. This is a genuine nonzero exact merge, not dead-state collapse.

The same profile also contains a dead final class for monochromatic full assignments.

## Canonical records

A profile record is canonical for a fixed labelled instance and ordering. Class masks are fixed-width hexadecimal strings whose width includes leading semantic zeros. The profile census digest is SHA-256 of the compact semantic payload with the digest field omitted.

The committed corpus digest is:

```text
a765b6164a0bd2bbc176c039e842de4cbf10793918798875f103f83ec099a9f8
```

## Complexity audit

For `n` vertices and `m` edges:

- full-assignment truth evaluation uses `O(2^n(n+m))` time in the concrete implementation;
- the assignment-mask table contains exactly `(n+1)2^n` semantic bits before Python object overhead;
- bottom-up construction and integer-mask hashing process `O(n2^n)` semantic bits;
- the assignment-to-class maps contain `2^(n+1)-1` identifiers;
- the number of directed colour transitions is `2 sum_{i=0}^{n-1} q_i`;
- dense unique class-mask storage is
  \[
  \sum_i q_i2^{n-i}\le(n+1)2^n;
  \]
- direct processed-boundary enumeration is `O(n2^n m)`;
- full canonical profile output is exponential and output-sensitive.

Python integers, tuples, dictionaries, and sets add implementation-dependent object overhead. The audit records semantic bit counts separately and makes no claim that Python resident memory equals those bit counts.

The profile census has an optimized finite-domain implementation that precomputes violation masks for each ordering. This improves constants and avoids repeated edge interpretation; it does not change the exponential domain size.

## Break pass

The attack pass checked:

- leading-zero mask width;
- lexicographic completion orientation;
- first-occurrence class numbering;
- transition agreement for every member of a reference class;
- dead versus live merging;
- ordering validation and malformed CLI input;
- root and final-level boundary cases;
- VS-02 acceptance agreement;
- deterministic corpus reproduction;
- cross-version execution.

No unresolved substantive defect remains pending the final automated PR result.

## Final determination

After the automated matrix and pinned full reference gate pass, `VS-03` is `COMPLETE / CHECKED`.

The retained result is an exact exponential semantic-state laboratory. The next work is empirical control calibration and obstruction analysis, not a claim that exact quotient construction is tractable in general.
