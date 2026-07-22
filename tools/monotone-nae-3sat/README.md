# Monotone NAE-3SAT Research Tool

Standard-library Python laboratory for canonical labelled 3-uniform hypergraphs, exact finite satisfiability, and exact extension profiles.

## Completed slices

### VS-01 — canonical instance model

- strict versioned JSON parsing;
- canonical normalization and stable labelled identifiers;
- incidence components and deterministic relabelling;
- strict total-colouring verification.

### VS-02 — exact small-instance oracle

- exact satisfiability decision;
- true lexicographically least witness;
- complete satisfying-assignment listing;
- exact direct and component-factorized counting;
- edge-minimal-unsatisfiability testing;
- canonical labelled instance generation;
- deterministic exhaustive census and CLI commands.

### VS-03 — exact extension profiles

- exact completion masks for every prefix of a fixed ordering;
- deterministic exact quotient classes;
- representative-independent zero/one transitions;
- processed-boundary comparison metrics;
- canonical profile records and summaries;
- deterministic exhaustive profile census.

All decision and profile procedures are exponential laboratory tools. They are not candidate polynomial-time algorithms.

## Runtime

- Python 3.11, 3.12, and 3.13;
- Python standard library only;
- automated compile, test, CLI, VS-02 corpus, VS-03 corpus, and independent-reference gates.

## Input format

```json
{"format":"nae3-v1","vertices":[0,1,2,3],"edges":[[0,1,2],[1,2,3]]}
```

The vertex set must be exactly `0,...,n-1`. Input edges may be unsorted and repeated; parsing normalizes them. Malformed JSON, duplicate keys, unsupported versions, invalid UTF-8, malformed edges, Booleans, floating-point labels, and unknown fields are rejected.

Canonical instance output is deterministic for a fixed vertex labelling, not up to hypergraph isomorphism.

## Commands

From this directory:

```bash
python3 -m unittest discover -s tests -v
python3 -m nae3sat.cli validate tests/fixtures/fano-plane.json
python3 -m nae3sat.cli solve tests/fixtures/single-edge.json
python3 -m nae3sat.cli count tests/fixtures/single-edge.json
python3 -m nae3sat.cli profile tests/fixtures/single-edge.json --ordering 2,0,1
python3 -m nae3sat.cli census --max-vertices 5 --output /tmp/vs02-corpus.json
python3 -m nae3sat.cli profile-census --max-vertices 5 --output /tmp/vs03-corpus.json
cmp /tmp/vs02-corpus.json corpus/all-labelled-n-le-5.json
cmp /tmp/vs03-corpus.json profile-corpus/all-labelled-orderings-n-le-5.json
```

`solve` reports the exact decision and least witness. `count` reports the exact number of satisfying colourings. `profile` reports exact-state summary metrics for one ordering. Both census commands write deterministic compact JSON atomically.

## Exhaustive corpora

### VS-02 instance census

`corpus/all-labelled-n-le-5.json` records:

- `1045` labelled instances;
- `1044` satisfiable;
- `1` unsatisfiable;
- `33047` complete reference colourings evaluated.

The unique unsatisfiable five-vertex instance contains all ten triples. The Fano-plane fixture is a separate exact control and is edge-minimal unsatisfiable.

### VS-03 profile census

`profile-corpus/all-labelled-orderings-n-le-5.json` records all orderings of all labelled instances through five vertices:

- `123280` instance-ordering profiles;
- `7753542` raw prefixes;
- `2153049` exact classes;
- `1818651` live classes;
- maximum exact quotient size `8`.

These are finite exhaustive measurements. They do not establish an asymptotic polynomial bound.

## Public API

The package exports the canonical model, serialization, oracle, and corpus APIs together with:

- `ProfileLevel` and `ExactProfile`;
- `validate_ordering`;
- `build_exact_profile`;
- `extension_mask`;
- `profile_record` and `profile_bytes`;
- `profile_corpus_payload`, `profile_corpus_record`, and `profile_corpus_bytes`;
- `verify_profile_corpus_record`.

## Complexity

For `n` vertices and `m` edges:

- baseline exact decision and counting: `O(2^n m)` after validation;
- symmetry-reduced decision: `O(2^(n-c-z) m)` for `c` nontrivial components and `z` isolates;
- complete listing: output-sensitive `O(2^n m + Sn)`;
- one exact profile: `O(2^n(n+m))` truth evaluation plus `O(n2^n)` semantic mask processing and direct `O(n2^n m)` boundary comparison;
- full profile output is exponential and output-sensitive;
- fixed-`n` labelled generation: exactly `2^binom(n,3)` instances.

Finite corpus results remain `COMPUTATIONAL` unless accompanied by their recorded exhaustiveness arguments. No result here implies `P=NP` or `P!=NP`.
