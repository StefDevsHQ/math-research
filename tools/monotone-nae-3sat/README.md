# Monotone NAE-3SAT Research Tool

Standard-library Python laboratory for the canonical labelled 3-uniform hypergraph model and exact finite oracle.

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

These procedures are exponential laboratory tools. They are not candidate polynomial-time algorithms.

## Runtime

- Python 3.11, 3.12, and 3.13;
- Python standard library only;
- automated compile, test, CLI, and corpus-reproduction matrix.

## Input format

```json
{"format":"nae3-v1","vertices":[0,1,2,3],"edges":[[0,1,2],[1,2,3]]}
```

The vertex set must be exactly `0,...,n-1`. Input edges may be unsorted and repeated; parsing normalizes them. Malformed JSON, duplicate keys, unsupported versions, invalid UTF-8, malformed edges, Booleans, floating-point labels, and unknown fields are rejected.

Canonical output is deterministic for a fixed vertex labelling, not up to hypergraph isomorphism.

## Commands

From this directory:

```bash
python3 -m unittest discover -s tests -v
python3 -m nae3sat.cli validate tests/fixtures/fano-plane.json
python3 -m nae3sat.cli solve tests/fixtures/single-edge.json
python3 -m nae3sat.cli count tests/fixtures/single-edge.json
python3 -m nae3sat.cli census --max-vertices 5 --output /tmp/vs02-corpus.json
cmp /tmp/vs02-corpus.json corpus/all-labelled-n-le-5.json
```

`solve` reports the exact decision, least witness, candidate count, and symmetry policy. `count` reports the exact number of satisfying colourings. `census` writes deterministic compact JSON atomically.

## Exhaustive corpus

`corpus/all-labelled-n-le-5.json` contains the complete labelled domain through five vertices:

- `1045` instances;
- `1044` satisfiable;
- `1` unsatisfiable;
- `33047` complete reference colourings evaluated.

The unique unsatisfiable five-vertex instance contains all ten triples. The Fano-plane fixture is a separate exact control and is edge-minimal unsatisfiable.

## Public API

The package exports the canonical model and serialization APIs together with:

- `SolveResult`;
- `solve_exact`;
- `satisfying_assignments`;
- `count_satisfying_assignments`;
- `count_satisfying_assignments_factorized`;
- `is_edge_minimal_unsatisfiable`;
- `labelled_instances`;
- `corpus_payload`, `corpus_record`, `corpus_bytes`, and `verify_corpus_record`.

## Complexity

For `n` vertices and `m` edges:

- baseline exact decision and counting: `O(2^n m)` after validation;
- symmetry-reduced decision: `O(2^(n-c-z) m)` for `c` nontrivial components and `z` isolates;
- complete listing: output-sensitive `O(2^n m + Sn)`;
- fixed-`n` labelled generation: exactly `2^binom(n,3)` instances.

Finite corpus results remain `COMPUTATIONAL` unless accompanied by the recorded exhaustiveness argument. No result here implies `P=NP` or `P!=NP`.
