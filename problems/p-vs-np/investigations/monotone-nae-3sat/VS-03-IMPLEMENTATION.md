# VS-03 Implementation Specification — Exact Extension-Profile Engine

**Slice:** `VS-03`  
**Status:** `READY` — reviewed implementation contract; executable engine and profile corpus remain  
**Depends on:** `VS-01 — COMPLETE / CHECKED`, `VS-02 — COMPLETE / CHECKED`  
**Updated:** 2026-07-22

## Purpose

Build the exact semantic-state engine against which every later compression proposal is judged.

For a fixed labelled instance and vertex ordering, the engine must compute the complete set of satisfying futures for every prefix assignment, merge two prefixes if and only if those future sets are identical, construct both next-colour transitions, and verify final acceptance against the checked VS-02 oracle.

The engine is intentionally exponential. It measures exact state; it is not itself a polynomial-time algorithm.

## Mathematical contract

Fix a canonical instance `H=(V,E)` with `V={0,...,n-1}` and an ordering

\[
\pi=(v_1,\ldots,v_n).
\]

At level `i`, let

\[
P_i=(v_1,\ldots,v_i),\qquad R_i=(v_{i+1},\ldots,v_n).
\]

A prefix assignment is a bit tuple `a` of length `i` in `P_i` order. A completion is a bit tuple `c` of length `n-i` in `R_i` order. Define

\[
\operatorname{Ext}_{H,\pi,i}(a)
=
\{c\in\{0,1\}^{n-i}:a\cup c\models H\}.
\]

Two prefixes are equivalent exactly when these sets are equal.

## Canonical completion-mask encoding

Completions are ordered lexicographically, equivalently by binary numeric index with the first remaining bit most significant. The exact completion set is encoded as a nonnegative integer mask:

- bit `j` is `1` exactly when completion index `j` satisfies;
- the semantic width is exactly `2^(n-i)` bits, including leading zeros;
- mask `0` is the unique dead profile;
- at level `n`, mask `1` is accepting and mask `0` is dead.

If `M` is a level-`i` mask and

\[
h=2^{n-i-1},
\]

then extending the next vertex by `0` and `1` gives

\[
M_0=M\bmod 2^h,
\qquad
M_1=\left\lfloor M/2^h\right\rfloor.
\]

Thus transitions are literal lower/upper slices of the exact completion mask.

## Required API

```python
@dataclass(frozen=True, slots=True)
class ProfileLevel:
    index: int
    prefix_vertices: tuple[int, ...]
    remainder_vertices: tuple[int, ...]
    boundary_vertices: tuple[int, ...]
    assignment_class_ids: tuple[int, ...]
    class_masks: tuple[int, ...]
    transitions: tuple[tuple[int, int], ...] | None
    processed_valid_boundary_states: int

    @property
    def raw_assignment_count(self) -> int: ...

    @property
    def class_count(self) -> int: ...

    @property
    def live_class_count(self) -> int: ...

    @property
    def dead_class_id(self) -> int | None: ...


@dataclass(frozen=True, slots=True)
class ExactProfile:
    instance: Hypergraph3
    ordering: tuple[int, ...]
    levels: tuple[ProfileLevel, ...]

    @property
    def satisfiable(self) -> bool: ...


def validate_ordering(instance: Hypergraph3, ordering: Sequence[int]) -> tuple[int, ...]: ...


def build_exact_profile(instance: Hypergraph3, ordering: Sequence[int]) -> ExactProfile: ...


def extension_mask(
    instance: Hypergraph3,
    ordering: Sequence[int],
    prefix_bits: Sequence[int],
) -> int: ...


def profile_record(profile: ExactProfile) -> dict[str, object]: ...


def profile_bytes(profile: ExactProfile) -> bytes: ...
```

All public instance arguments reject non-`Hypergraph3` values. Ordering and bit containers are finite non-string sequences. Booleans, duplicate ordering vertices, missing vertices, extra vertices, floating-point values, and nonbinary bits are rejected.

## Deterministic indexing

At level `i`, prefix assignments are ordered lexicographically. Their numeric indices run from `0` to `2^i-1`.

`assignment_class_ids[j]` is the exact class of prefix index `j`.

Class identifiers are assigned by first occurrence while scanning prefix assignments in lexicographic order. Therefore:

- class `0` contains the lexicographically first prefix;
- identifiers are deterministic;
- `class_masks[class_id]` is the exact completion mask of every member;
- class identifiers have meaning only within their level.

`transitions[q]=(q_0,q_1)` records the classes reached by appending colours `0` and `1`. Final-level transitions are `None`.

## Construction algorithm

### Full assignments

Evaluate all `2^n` complete assignments once with an internal direct edge predicate cross-checked against VS-01 in tests. At level `n`, each full assignment has mask `1` if satisfying and `0` otherwise.

### Bottom-up masks

For `i=n-1,...,0`, the two children of prefix index `j` are indices `2j` and `2j+1`. If their masks are `M_0` and `M_1`, the parent mask is

\[
M=M_0+(M_1\ll 2^{n-i-1}).
\]

This reconstructs the exact lexicographically ordered completion bitset without reevaluating complete assignments.

### Quotient

At each level, scan assignment masks in lexicographic prefix order and intern equal integer masks. Equal masks receive the same class identifier and unequal masks receive different identifiers.

### Transitions

For every class mask, split it into lower and upper halves and look those masks up in the next level. Missing successor masks are an internal consistency failure.

## Correctness obligations

### Exact-mask theorem

For every level and prefix, the constructed mask equals the characteristic bit vector of its exact completion set.

**Proof method:** reverse induction on the level. At level `n`, the sole completion is the empty tuple and the mask is exactly the satisfaction bit. At level `i`, every completion begins uniquely with `0` or `1`; concatenating the lower and upper child masks gives precisely the parent completion set.

### Quotient exactness

Two prefixes receive the same class identifier if and only if their exact completion sets are equal, because classing is equality of their canonical masks.

### Transition well-definedness

Equal parent masks have equal lower and upper slices, so both next-colour transitions are independent of representative. This is the executable realization of `NAE-004`.

### Acceptance

The unique level-zero prefix is satisfiable exactly when its completion mask is nonzero. At level `n`, accepting full assignments form the mask-`1` class. Profile acceptance must equal VS-02 `solve_exact` for every checked instance and ordering.

## Boundary comparison

For each level, compute the processed boundary

\[
B_i=\{u\in P_i:\exists e\in E,\ u\in e,\ e\cap R_i\ne\varnothing\}.
\]

`processed_valid_boundary_states` is the number of distinct colourings of `B_i` induced by prefixes that satisfy every edge contained wholly in `P_i`.

Boundary cases:

- at level `0`, the count is `1`;
- at level `n`, it is `1` exactly when the instance is satisfiable, otherwise `0`;
- the count is at most `2^|B_i|`;
- it is a syntactic dynamic-programming comparison, not an exact semantic quotient.

## Size accounting

For a level with `q_i` exact classes and completion width `r_i=2^(n-i)`, record:

- raw prefixes: `2^i`;
- exact classes: `q_i`;
- live classes: masks other than zero;
- dense unique completion bits: `q_i r_i`;
- assignment-map bits:
  \[
  2^i\lceil\log_2 q_i\rceil,
  \]
  interpreted as zero when `q_i<=1`;
- transition bits for `i<n`:
  \[
  2q_i\lceil\log_2 q_{i+1}\rceil;
  \]
- canonical JSON byte length.

These are representation measurements, not claims of optimal encoding.

## Canonical profile record

`profile_record` must contain:

- format `nae3-vs03-profile-v1`;
- VS-01 instance identifier;
- ordering;
- satisfiable flag;
- one level record per `i`;
- class masks as fixed-width lowercase hexadecimal strings, padded to the semantic completion width;
- assignment class identifiers and transitions;
- all boundary and size metrics.

`profile_bytes` is compact UTF-8 JSON with fixed key order and no terminal newline. It is canonical for the fixed labelled instance and ordering, not up to isomorphism or ordering equivalence.

## Command-line interface

Extend the CLI with:

```bash
python3 -m nae3sat.cli profile path/to/instance.json
python3 -m nae3sat.cli profile path/to/instance.json --ordering 2,0,1
python3 -m nae3sat.cli profile-census --max-vertices 5 --output path/to/profile-corpus.json
```

`profile` emits a compact summary, not the full masks:

```json
{"format":"nae3-vs03-summary-v1","id":"...","ordering":[0,1,2],"satisfiable":true,"max_classes":2,"total_classes":7,"profile_bytes":...}
```

`profile-census` writes atomically and uses all orderings of all labelled instances through the requested bound.

## First exhaustive profile domain

The first authoritative profile census is

\[
\mathcal P_{\le5}
=
\{(H,\pi):H\in\mathcal H_{\le5},\ \pi\text{ a permutation of }V(H)\}.
\]

Its exact size is

\[
\sum_{n=0}^{5}2^{\binom n3}n!
=1+1+2+12+384+122880
=123280.
\]

The census must record by `n` and level:

- number of instance-ordering profiles;
- total raw prefixes;
- total exact classes and live classes;
- distributions of class counts;
- maximum class count;
- total processed-valid boundary states;
- dense unique completion bits;
- assignment-map bits;
- transition bits;
- exact profiles whose root is satisfiable or unsatisfiable.

The semantic payload has a non-self-referential SHA-256 digest defined exactly as in VS-02: hash compact canonical JSON with the digest field omitted. Interpreter patch versions and timestamps belong in the audit, not the semantic corpus.

## Independent reference implementation

Tests must include a logically separate reference engine that:

- uses `itertools.product` and tuple/frozenset completion sets rather than integer masks;
- checks edges directly;
- groups prefixes by exact completion tuples;
- derives transitions from all members, not from production mask splitting;
- does not call production profile construction;
- compares final acceptance to VS-02.

Production and reference outputs must agree on the complete declared finite domain used by the quality gate.

## Required controls

At minimum:

1. empty graph and empty ordering;
2. isolated vertices only;
3. one edge under every ordering;
4. two disconnected edges under representative interleavings;
5. overlap-chain fixture under every ordering;
6. complete five-vertex hypergraph under every ordering;
7. Fano plane under canonical, reversed, and adversarial interleaved orderings;
8. at least one instance with a dead class before the final level;
9. at least one instance with nontrivial live semantic merging;
10. final acceptance equal to VS-02 in every case.

A control called “nontrivial live merging” must exhibit two distinct live prefix assignments with equal nonzero exact completion masks. Merely merging dead prefixes does not qualify.

## Exhaustive tests

### Complete `n<=5` profile gate

For all `123280` instance-ordering pairs:

- every level has `2^i` assignment-class entries;
- production masks equal independent completion sets;
- class partitions agree exactly;
- both transitions agree for every class;
- all members of a class have the same successors;
- root acceptance equals VS-02;
- final masks are only `0` and `1`;
- boundary metrics match an independent computation;
- canonical bytes are deterministic.

If the full reference comparison is too slow for each CI runtime, the complete production gate must run on all runtimes and the full independent reference gate must run on at least one pinned runtime. Any reduced matrix must be explicit in the workflow and audit.

### Additional tests

- strict ordering and prefix validation;
- direct `extension_mask` agreement for every prefix of fixed controls;
- class identifier first-occurrence determinism;
- mask split/transition identity;
- wrong-instance rejection;
- profile record round-trip semantics;
- cross-process hash-seed determinism;
- corpus byte reproduction;
- CLI success, malformed ordering, and output-path failure behavior.

## Complexity accounting

For fixed `H`, ordering `pi`, `n` vertices, and `m` edges:

- complete-assignment truth table: `O(2^n m)` time;
- bottom-up mask construction: `O(n2^n)` stored semantic bits and corresponding bit-operation cost;
- quotient interning: expected time proportional to the total hashed mask length, `O(n2^n)` semantic bits, plus Python object overhead;
- assignment-class map size: `sum_i 2^i = 2^(n+1)-1` identifiers;
- transition count: `2 sum_{i=0}^{n-1} q_i`;
- dense unique mask bits: `sum_i q_i 2^(n-i)`, at most `(n+1)2^n` times class duplication only bounded by `q_i<=2^i`, giving the coarse bound `(n+1)2^n` for assignment masks but potentially the same order for unique-mask storage;
- processed-boundary enumeration: `O(n2^n m)` under the direct specified implementation;
- canonical full-profile output is exponential and output-sensitive.

The implementation audit must distinguish semantic bit counts from Python object memory and must not call any exponential quantity polynomial.

## Quality gate

`VS-03` becomes `COMPLETE / CHECKED` only when:

1. VS-01 and VS-02 remain green;
2. all required profile APIs and CLI commands exist;
3. exact-mask, quotient, transition, acceptance, and generator/domain proofs are recorded;
4. the independent tuple-set reference engine is committed;
5. the declared exhaustive instance-ordering domain passes production/reference agreement;
6. controls include dead merging and genuine live semantic merging;
7. deterministic profile and census records are committed and reproducible;
8. complete state, transition, bit-length, runtime, and memory accounting is audited;
9. supported-runtime automation is green under the documented matrix;
10. an independent break pass leaves no unresolved substantive defect;
11. `STATUS.md`, `VERTICAL-SLICES.md`, README, workflow, and completion audit are synchronized.

Until this gate passes, VS-04 through VS-08 may not cite profile outputs as trusted evidence.

## Explicit non-goals

VS-03 does not:

- claim the exact quotient is polynomially small;
- claim exact classes are efficiently computable on unrestricted inputs;
- select a symbolic compression language;
- prove `NAE-006`;
- infer hardness from observed class growth;
- quotient graph isomorphism or ordering equivalence;
- replace VS-02 as independent ground truth.

## Implementation sequence

1. freeze ordering, mask, class, transition, boundary, and size semantics;
2. implement the independent tuple-set reference engine in tests;
3. implement bottom-up exact masks and deterministic quotient classes;
4. implement transitions and profile records;
5. cross-check named controls and find a genuine live merge;
6. exhaust all `123280` profiles through five vertices;
7. add CLI and deterministic profile corpus;
8. reproduce the automated runtime matrix;
9. perform the independent attack and complete complexity audit;
10. promote and merge only after the full building-block gate passes.
