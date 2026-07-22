# VS-02 Implementation Specification — Exact Small-Instance Oracle

**Slice:** `VS-02`  
**Status:** `READY` — reviewed implementation contract; executable oracle and corpus remain  
**Depends on:** `VS-01 — COMPLETE / CHECKED`  
**Updated:** 2026-07-22

## Purpose

Build a trusted exact satisfiability oracle for finite Monotone NAE-3SAT experiments.

The oracle is deliberately exponential. Its role is to provide exact finite ground truth for later slices: extension-profile validation, obstruction enumeration, summary counterexamples, and semantic-state measurements. Nothing in this slice is evidence for a polynomial-time algorithm.

## Exact problem

For a canonical instance

\[
H=(V,E),\qquad V=\{0,\ldots,n-1\},
\]

decide whether there is a colouring

\[
\sigma:V\to\{0,1\}
\]

such that every edge contains both colours.

The independent reference procedure enumerates all binary colourings in lexicographic order and checks each edge directly.

## Required API

```python
@dataclass(frozen=True, slots=True)
class SolveResult:
    satisfiable: bool
    witness: tuple[int, ...] | None
    assignments_tested: int
    symmetry_reduction: str


def solve_exact(instance: Hypergraph3, *, use_symmetry: bool = True) -> SolveResult:
    """Return the exact decision and lexicographically least witness."""


def satisfying_assignments(instance: Hypergraph3) -> tuple[tuple[int, ...], ...]:
    """Return every satisfying colouring in lexicographic order."""


def count_satisfying_assignments(instance: Hypergraph3) -> int:
    """Return the exact number of satisfying total colourings."""


def is_edge_minimal_unsatisfiable(instance: Hypergraph3) -> bool:
    """Return whether H is unsatisfiable and each one-edge deletion is satisfiable."""


def labelled_instances(n: int) -> Iterator[Hypergraph3]:
    """Yield every labelled simple 3-uniform hypergraph on 0..n-1 once."""
```

All public functions reject non-`Hypergraph3` instances with `ValidationError`.

`witness is None` exactly when `satisfiable` is false. Every returned witness must be rechecked through the VS-01 public verifier before return.

## Deterministic search accounting

`assignments_tested` has one exact meaning:

> the number of candidate assignments evaluated by the decision path's internal edge predicate, including the successful candidate when one is found.

For `use_symmetry=False`, candidates are complete length-`n` colourings in ordinary tuple lexicographic order.

For `use_symmetry=True`, candidates are assignments to the unfixed active vertices, in increasing vertex order and tuple lexicographic order. The fixed representative bits and isolated zero bits are inserted before edge evaluation. The empty active search space still has one candidate, the empty tuple.

The only permitted values of `symmetry_reduction` are:

- `"none-v1"`;
- `"component-complement-v1"`.

This makes accounting independently reproducible and prevents implementation-dependent counters.

## Baseline algorithm

The baseline decision procedure enumerates complete colourings in lexicographic order.

Using the public verifier directly gives

\[
O(2^n(n+m)).
\]

A validated internal edge predicate may reduce this to

\[
O(2^n m)
\]

after input validation. Its results must be exhaustively cross-checked against `verify_coloring`.

Counting and listing use the complete baseline domain. They do not silently quotient symmetry.

## Component-wise complement symmetry

For any incidence component, complementing every colour inside that component preserves every constraint: each edge lies wholly inside one component and remains non-monochromatic after complementation.

For each component containing an edge, choose its least-labelled vertex as representative and fix it to `0`. Isolated vertices are fixed to `0` for decision and witness search.

If there are `c` nontrivial components and `z` isolated vertices, the optimized path enumerates exactly

\[
2^{n-c-z}
\]

active candidates in the unsatisfiable case.

### Required proof

Given any satisfying colouring, independently complement every nontrivial component whose least vertex has colour `1`. The resulting colouring is satisfying and has every representative equal to `0`.

Moreover, the lexicographically least satisfying full colouring necessarily has each nontrivial component's least vertex equal to `0`: otherwise complementing that component changes no earlier vertex and changes that first component vertex from `1` to `0`, producing a smaller satisfying colouring. Isolated bits are also `0` in the least witness.

Therefore lexicographic enumeration of unfixed vertices with these bits fixed returns the true lexicographically least full witness.

This optimization is allowed only for decision and one-witness search. Counting and listing must enumerate or exactly restore every omitted multiplicity.

## Component factorization

Let `H_1,...,H_k` be the nontrivial incidence components and let `z` be the number of isolated vertices. Then

\[
H\text{ is satisfiable}\iff H_j\text{ is satisfiable for every }j,
\]

and

\[
\#\mathrm{Sat}(H)=2^z\prod_{j=1}^{k}\#\mathrm{Sat}(H_j).
\]

The proof is the direct bijection between a full satisfying colouring and independent satisfying colourings of the nontrivial components together with arbitrary isolated bits.

Component-factorized counting may be implemented, but the simple full-enumeration count remains the reference semantics. Both paths must agree exhaustively before factorization can become the default.

## Edge-minimal unsatisfiability

`is_edge_minimal_unsatisfiable(H)` means:

1. `H` is unsatisfiable; and
2. for every edge `e`, `H-e` is satisfiable.

Checking one-edge deletions is sufficient for edge-minimality: satisfiability is preserved when further constraints are deleted, so if every one-edge deletion is satisfiable, every proper edge subset is satisfiable.

This is distinct from vertex-minimality.

## Canonical labelled generator

For fixed `n`, let

```python
triples = tuple(itertools.combinations(range(n), 3))
```

in lexicographic order. For masks

\[
0\le M<2^{\binom n3},
\]

include triple `j` exactly when bit `j` of `M` is `1`.

This is a bijection between masks and labelled simple 3-uniform hypergraphs on `0,...,n-1`. `labelled_instances(n)` yields increasing masks.

Invalid `n`, including Booleans and negative values, is rejected.

## First exhaustive domain

The first authoritative census is

\[
\mathcal H_{\le5}
=
\bigcup_{n=0}^{5}
\{(V,E):V=\{0,\ldots,n-1\},\ E\subseteq\binom V3\}.
\]

Its exact size is

\[
\sum_{n=0}^{5}2^{\binom n3}
=1+1+1+2+16+1024
=1045.
\]

For each `n`, record:

- total labelled instances;
- satisfiable and unsatisfiable instances;
- connected instances;
- edge-minimal unsatisfiable instances;
- a distribution mapping exact satisfying-colouring counts to numbers of instances;
- total complete colourings evaluated by the reference census.

### Connectedness convention

A labelled instance is `connected` exactly when `n>0` and `incidence_components(H)` contains one component. Thus:

- the zero-vertex instance is not connected;
- the one-vertex edgeless instance is connected;
- an edgeless instance on at least two vertices is disconnected.

This convention includes isolated singleton components and removes ambiguity from corpus counts.

No census count enters the authoritative record until production and logically independent reference implementations agree.

## Required controls

1. zero-vertex graph: satisfiable, empty least witness, count `1`;
2. edgeless graph on `n` vertices: count `2^n`, least witness all zero;
3. one edge: count `6`, least witness `001`;
4. two disconnected edges: count `36`;
5. overlap-chain fixture: independently enumerated decision, count, and least witness;
6. Fano plane: unsatisfiable;
7. every Fano one-edge deletion: satisfiable, establishing edge-minimality;
8. disconnected decision conjunction and counting product;
9. complement closure, with distinct complements whenever `n>0`;
10. optimized and baseline decisions agree on all 1045 first-domain instances;
11. every returned witness passes the VS-01 verifier.

The Fano plane is outside `\mathcal H_{\le5}` and is a separate exact control, not part of the first corpus totals.

## Independent reference implementation

Tests must contain a deliberately simple reference solver that:

- enumerates `itertools.product((0,1), repeat=n)`;
- checks edges directly;
- does not call production decision, count, listing, component, or symmetry logic;
- returns the least witness, full satisfying list, and exact count.

Production and reference implementations must agree on every instance in `\mathcal H_{\le5}` and on all named controls.

## Corpus record

The committed corpus is compact deterministic JSON with a semantic payload and a non-self-referential digest:

```json
{
  "format":"nae3-vs02-corpus-v1",
  "domain":"all-labelled-3-uniform-hypergraphs-n-le-5",
  "generator":"edge-mask-v1",
  "computation":"finite-exhaustive",
  "counts":[],
  "totals":{},
  "payload_sha256":"..."
}
```

Define `payload_sha256` as SHA-256 of the compact canonical JSON encoding of the object with the `payload_sha256` field omitted. Keys have a fixed documented order; nested distribution keys are decimal strings sorted numerically before emission.

Exact interpreter patch versions and run timestamps belong in `VS-02-AUDIT.md`, not in the semantic corpus payload. The committed corpus bytes and digest must be identical on Python 3.11, 3.12, and 3.13.

The corpus must state that it is finite exhaustive computation. It must not imply a universal theorem. The 1045 instances need not be stored individually because the generator reproduces them exactly.

## Command-line interface

Extend the CLI with:

```bash
python3 -m nae3sat.cli solve path/to/instance.json
python3 -m nae3sat.cli count path/to/instance.json
python3 -m nae3sat.cli census --max-vertices 5 --output path/to/corpus.json
```

`solve` emits:

```json
{"format":"nae3-v1-solve","id":"...","satisfiable":true,"witness":[0,0,1],"assignments_tested":2,"symmetry_reduction":"component-complement-v1"}
```

`count` emits:

```json
{"format":"nae3-v1-count","id":"...","satisfying_assignments":6}
```

`census`:

- accepts `0 <= --max-vertices <= 5` by default;
- requires the explicit flag `--allow-large-domain` above `5`;
- writes deterministic compact JSON;
- uses the canonical labelled generator;
- reports optional progress only to standard error;
- never labels a sampled or interrupted domain exhaustive;
- writes atomically through a temporary file followed by replacement.

## Required tests

### Solver semantics

- satisfiable and unsatisfiable controls;
- witness/null consistency;
- true lexicographically least witness;
- strict wrong-instance rejection;
- optimized/unoptimized agreement;
- witness re-verification;
- exact `assignments_tested` values on fixed controls.

### Counting and listing

- count equals list length;
- list is sorted and duplicate-free;
- all listed assignments verify;
- complement closure;
- disconnected product law;
- isolated factor `2^z`;
- factorized and direct counts agree where both exist.

### Generator

- exact instance counts for `n=0,...,5`;
- increasing mask order;
- no duplicates;
- all generated graphs are canonical;
- invalid bounds rejected.

### Minimal unsatisfiability

- satisfiable inputs return false;
- an unsatisfiable graph with an unsatisfiable edge deletion returns false;
- Fano returns true only after every one-edge deletion is found satisfiable;
- empty and one-edge boundary cases.

### Exhaustive agreement

For every one of the 1045 labelled instances with `n<=5`:

- production/reference decisions agree;
- counts and complete lists agree;
- least witnesses agree;
- optimized/baseline decision paths agree;
- all witnesses verify;
- component product identities agree;
- corpus aggregation agrees with a separate reference aggregation.

### Reproducibility and runtime matrix

On Python 3.11, 3.12, and 3.13:

- compile all package modules;
- run the complete VS-01 and VS-02 suite;
- exercise `solve`, `count`, and `census`;
- regenerate the corpus;
- compare regenerated bytes with the committed record.

## Complexity accounting

For `n` vertices, `m` edges, and `S` satisfying assignments:

- baseline decision using public verification: `O(2^n(n+m))`;
- internal direct decision after validation: `O(2^n m)`;
- symmetry decision: `O(2^{n-c-z}m)` for `c` nontrivial components and `z` isolates;
- complete listing: `O(2^n m + Sn)` time and `Theta(Sn)` output space;
- direct counting: `O(2^n m)` time and `O(n)` candidate space apart from the input;
- factorized counting: sum of component enumeration costs plus multiplication of integers of at most `n+1` bits;
- fixed-`n` labelled generation: exactly `2^{\binom n3}` instances;
- first census: exactly 1045 instances, with exact tested-colouring totals recorded.

These are exponential laboratory procedures. They are not candidate polynomial algorithms.

## Quality gate

`VS-02` becomes `COMPLETE / CHECKED` only when:

1. VS-01 remains green on all supported runtimes;
2. all required production APIs, generator, corpus builder, and CLI commands exist;
3. component factorization, complement fixing, least-witness preservation, and generator exhaustiveness have written proofs;
4. the independent reference implementation is committed;
5. exhaustive production/reference agreement holds on all 1045 instances;
6. Fano unsatisfiability and edge-minimality are independently verified;
7. the deterministic corpus record is committed and byte-reproducible;
8. complexity, integer bit lengths, output size, and assignment counters are audited;
9. Python 3.11, 3.12, and 3.13 CI is green;
10. an independent break pass leaves no unresolved substantive defect;
11. `STATUS.md`, `VERTICAL-SLICES.md`, README, and the completion audit are synchronized.

Until then, no dependent slice may treat VS-02 output as trusted ground truth.

## Explicit non-goals

VS-02 does not:

- provide a polynomial-time algorithm;
- use an external SAT solver as ground truth;
- claim novelty;
- quotient graph isomorphism;
- enumerate all six-vertex hypergraphs;
- infer a universal statement from the finite corpus;
- extract a compression invariant.

## Implementation sequence

1. commit the correctness proofs and fixed semantics;
2. implement the independent reference logic in tests;
3. implement decision, listing, and counting;
4. add the proved symmetry decision path;
5. implement the canonical generator and corpus builder;
6. exhaustively cross-check `n<=5`;
7. add CLI commands and atomic corpus output;
8. verify Fano unsatisfiability and edge-minimality independently;
9. regenerate identical corpus bytes on all supported runtimes;
10. perform the break pass and full complexity audit;
11. promote only after the complete building-block gate passes.
