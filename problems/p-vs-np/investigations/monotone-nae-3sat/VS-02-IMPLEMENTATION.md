# VS-02 Implementation Specification — Exact Small-Instance Oracle

**Slice:** `VS-02`  
**Status:** `READY` — implementation contract prepared; executable oracle and corpus remain  
**Depends on:** `VS-01 — COMPLETE / CHECKED`  
**Updated:** 2026-07-22

## Purpose

Build a trusted exact satisfiability oracle for finite Monotone NAE-3SAT experiments.

The oracle is not intended to be polynomial-time on unrestricted inputs. Its role is to provide mathematically exact answers on explicitly bounded domains so that later slices can:

- validate extension-profile acceptance;
- enumerate minimal unsatisfiable instances;
- destroy insufficient summaries with complete counterexamples;
- measure semantic compression against ground truth.

Every universal claim remains outside the scope of this slice.

## Exact problem

For a canonical instance

\[
H=(V,E),\qquad V=\{0,\ldots,n-1\},
\]

decide whether there exists

\[
\sigma:V\to\{0,1\}
\]

such that every edge contains both colours.

The reference decision procedure is exhaustive enumeration of all binary colourings, checked by the `VS-01` verifier.

## Required outputs

```python
@dataclass(frozen=True, slots=True)
class SolveResult:
    satisfiable: bool
    witness: tuple[int, ...] | None
    assignments_tested: int
    symmetry_reduction: str


def solve_exact(instance: Hypergraph3, *, use_symmetry: bool = True) -> SolveResult:
    """Decide satisfiability exactly and return a verified witness when one exists."""


def satisfying_assignments(instance: Hypergraph3) -> tuple[tuple[int, ...], ...]:
    """Return every satisfying total colouring in lexicographic order."""


def count_satisfying_assignments(instance: Hypergraph3) -> int:
    """Return the exact number of satisfying total colourings."""


def is_edge_minimal_unsatisfiable(instance: Hypergraph3) -> bool:
    """Return whether the instance is unsatisfiable and every one-edge deletion is satisfiable."""
```

`SolveResult.witness` must be `None` exactly when `satisfiable` is false. Every non-`None` witness must be rechecked through `verify_coloring` before return.

## Baseline algorithm

The baseline implementation enumerates colourings in lexicographic order.

Without optimization:

\[
T(H)=O(2^n(n+m)),
\]

including strict colouring validation through the existing verifier.

A direct internal edge loop may later reduce constant factors, but its result must remain cross-checked against `verify_coloring`.

## Permitted symmetry reduction

Global complementation preserves satisfaction:

\[
\sigma\models H\iff (1-\sigma)\models H.
\]

Therefore, for every nonempty incidence component, one chosen representative vertex may be fixed to colour `0` when deciding satisfiability.

For an instance with `c` nonempty incidence components and `z` isolated vertices, the optimized decision search may enumerate only

\[
2^{n-c-z}
\]

assignments on active vertices after fixing one representative per nonempty component. Isolated vertices are assigned `0` in the returned canonical witness.

### Correctness obligation

The implementation must include a project proof that component-wise colour complementation maps any satisfying assignment to one satisfying the fixed representatives. No optimization may be enabled solely because it appears empirically valid.

### Important limitation

Symmetry reduction may be used for decision and one-witness search. It must not be used to count or list all satisfying assignments unless multiplicities and isolated-vertex factors are restored exactly.

## Component factorization

For incidence components `H_1, ..., H_k` and `z` isolated vertices:

\[
H\text{ is satisfiable}
\iff
H_j\text{ is satisfiable for every }j.
\]

Moreover,

\[
\#\mathrm{Sat}(H)=2^z\prod_{j=1}^k \#\mathrm{Sat}(H_j).
\]

The implementation may solve components independently, but this identity must be proved and exhaustively cross-checked before becoming the default path.

## Canonical witness policy

For deterministic output, `solve_exact` returns the lexicographically least satisfying colouring under the selected algorithm's full-instance semantics.

If component symmetry is used internally, the implementation must still reconstruct and compare candidates as necessary to return the true lexicographically least full colouring, or else explicitly define and expose a different witness policy. The preferred requirement is the true lexicographically least witness.

Isolated vertices are `0` in the least witness.

## First exhaustive domain

The first corpus must be the complete labelled domain

\[
\mathcal H_{\le5}
=
\bigcup_{n=0}^{5}
\left\{
(V,E):V=\{0,\ldots,n-1\},\ E\subseteq\binom{V}{3}
\right\}.
\]

Its size is

\[
\sum_{n=0}^{5}2^{\binom n3}
=1+1+1+2+16+1024
=1045.
\]

This domain is chosen because it is small enough for complete independent verification and already fixed by the VS-01 exhaustive model tests.

### Required corpus record

For each `n=0,...,5`, record:

- total labelled instances;
- satisfiable instances;
- unsatisfiable instances;
- connected instances;
- edge-minimal unsatisfiable instances;
- total satisfying-colouring count distribution;
- exact command and runtime environment.

No count may be entered into the authoritative record until reproduced by two independent implementations or one implementation plus a logically independent exhaustive checker.

## Controls

The oracle must pass at least:

1. empty graph: satisfiable with the empty witness;
2. edgeless graph on `n` vertices: `2^n` satisfying assignments;
3. one edge: six satisfying assignments;
4. two disconnected edges: 36 satisfying assignments;
5. overlap chain fixture: independently enumerated result;
6. Fano plane: unsatisfiable;
7. disconnected unions: decision conjunction and count product identities;
8. complement pairing: every satisfying assignment has a distinct complement for `n>0`;
9. optimized and unoptimized decision paths agree on every instance in the first exhaustive domain;
10. all returned witnesses pass the VS-01 verifier.

The Fano result must be established by the committed exact oracle and independently checked; it is not imported from fixture naming.

## Independent reference implementation

The test suite must contain a deliberately simple reference solver that:

- enumerates all `2^n` tuples through `itertools.product`;
- checks each edge directly without calling the production solver;
- does not use component factorization;
- does not use symmetry reduction;
- returns the lexicographically least satisfying colouring and exact count.

The production and reference implementations must agree on every instance in `\mathcal H_{\le5}`.

## Corpus format

Store the first corpus summary as deterministic JSON, for example:

```json
{
  "format":"nae3-vs02-corpus-v1",
  "domain":"all-labelled-3-uniform-hypergraphs-n-le-5",
  "counts":[
    {"n":0,"instances":1,"satisfiable":1,"unsatisfiable":0}
  ]
}
```

The final schema must include:

- format version;
- exact domain definition;
- generator version or commit;
- Python version;
- totals and structural counts;
- SHA-256 digest of the canonical record;
- statement that results are finite exhaustive computation.

Do not store all 1045 instances unless a later slice needs them. They can be regenerated canonically from edge masks.

## Command-line interface

Extend the existing CLI with:

```bash
python3 -m nae3sat.cli solve path/to/instance.json
python3 -m nae3sat.cli count path/to/instance.json
python3 -m nae3sat.cli census --max-vertices 5 --output path/to/corpus.json
```

### `solve` output

```json
{"format":"nae3-v1-solve","id":"...","satisfiable":true,"witness":[0,0,1],"assignments_tested":2,"symmetry_reduction":"component-complement-v1"}
```

### `count` output

```json
{"format":"nae3-v1-count","id":"...","satisfying_assignments":6}
```

### `census` requirements

- refuse `--max-vertices` above the explicitly supported laboratory bound unless a separate override is provided;
- produce deterministic output;
- use the canonical labelled generator;
- report progress only to standard error;
- never label a sampled domain exhaustive.

## Generator

For fixed `n`, enumerate the triples

```python
triples = tuple(itertools.combinations(range(n), 3))
```

in lexicographic order. For edge mask

\[
0\le M<2^{\binom n3},
\]

include triple `j` exactly when bit `j` of `M` is one.

This is a bijection between masks and labelled simple 3-uniform hypergraphs on `V`. The exhaustiveness proof must be recorded in the audit.

## Required tests

### Solver semantics

- satisfiable and unsatisfiable controls;
- witness/null consistency;
- lexicographically least witness;
- strict wrong-instance rejection;
- optimized/unoptimized agreement;
- witness re-verification;
- deterministic assignments-tested accounting.

### Counting and listing

- count equals list length;
- list is lexicographically sorted and duplicate-free;
- all listed assignments verify;
- complement closure;
- disconnected product law;
- isolated-vertex factor `2^z`.

### Minimal unsatisfiability

- satisfiable instances return false;
- unsatisfiable instance with unsatisfiable edge deletion returns false;
- Fano plane returns true only if every one-edge deletion is verified satisfiable;
- empty and one-edge boundary cases.

### Exhaustive agreement

For every one of the 1045 labelled instances with `n<=5`:

- production and reference decisions agree;
- production and reference counts agree;
- least witnesses agree;
- optimized and baseline production paths agree;
- every returned witness verifies;
- component product identities agree.

### Runtime matrix

Compile, test, CLI controls, and corpus reproduction must pass on Python 3.11, 3.12, and 3.13.

## Complexity accounting

For a graph with `n` vertices and `m` edges:

- baseline decision: `O(2^n(n+m))` using the public verifier;
- direct internal decision loop: `O(2^n m)` after input validation;
- complete listing: output-sensitive `O(2^n m + S n)`, where `S` is the number of satisfying assignments;
- exact counting: `O(2^n m)`;
- component-factorized counting: sum of component search costs plus multiplication of integers whose bit length is at most `n+1`;
- complete labelled generation for fixed `n`: exactly `2^{\binom n3}` instances;
- total first-domain census: 1045 instances, with total colouring workload explicitly recorded rather than hidden in big-O notation.

No runtime result from this slice is evidence of polynomial-time solvability.

## Quality gate

`VS-02` may become `COMPLETE / CHECKED` only when:

1. `VS-01` remains green on all supported runtimes;
2. production solver, counter, listing API, generator, and CLI exist;
3. component and symmetry optimizations have written correctness proofs;
4. the independent baseline solver is committed;
5. exhaustive agreement holds on all 1045 instances with `n<=5`;
6. Fano unsatisfiability and edge-minimality are independently verified;
7. the deterministic corpus record is committed and reproducible;
8. all complexity and encoded-output sizes are audited;
9. CI passes on Python 3.11, 3.12, and 3.13;
10. an independent break pass finds no unresolved substantive defect;
11. `STATUS.md`, `VERTICAL-SLICES.md`, and the audit are synchronized.

Until this gate is satisfied, no `VS-03` result may cite VS-02 output as trusted ground truth.

## Explicit non-goals

This slice does not:

- provide a polynomial-time algorithm;
- use SAT solvers or external decision engines as the ground truth;
- claim novelty;
- reduce instances up to isomorphism;
- enumerate all six-vertex hypergraphs;
- infer a universal theorem from the finite corpus;
- extract a compression invariant.

## Implementation sequence

1. prove component factorization and component-wise complement fixing;
2. define result and witness policies;
3. implement the simple reference solver;
4. implement production baseline decision, count, and listing paths;
5. add and verify component/symmetry optimizations;
6. implement the canonical labelled generator;
7. exhaustively cross-check `n<=5`;
8. add CLI commands and deterministic corpus schema;
9. reproduce the census on all supported Python versions;
10. perform the independent attack and complexity audit;
11. promote only after the complete building-block gate passes.
