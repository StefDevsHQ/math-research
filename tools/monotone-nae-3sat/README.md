# Monotone NAE-3SAT Research Tool

Standard-library Python laboratory for canonical labelled 3-uniform hypergraphs, exact finite satisfiability, exact extension profiles, and checked tractability controls.

## Completed slices

### VS-01 — canonical instance model

Strict versioned parsing, canonical normalization, stable labelled identifiers, incidence components, deterministic relabelling, and strict witness verification.

### VS-02 — exact small-instance oracle

Exact decision, true least witnesses, complete assignment listing, exact direct and component-factorized counting, minimal-unsatisfiability checks, labelled generation, and deterministic census output.

### VS-03 — exact extension profiles

Exact completion masks, deterministic semantic classes, representative-independent transitions, boundary comparisons, canonical records, and exhaustive profile census.

### VS-04 — control calibration

- graph bipartiteness by parity propagation;
- XOR consistency, rank, counts, and least witnesses by Gaussian elimination;
- constructive incidence-forest NAE colouring;
- linearity, occurrence, and boundary utilities;
- deterministic control census and named-control report.

The exact oracle and profile procedures are exponential laboratory tools. The graph, XOR, incidence-forest, bounded-boundary, and component controls are restricted tractable mechanisms, not a universal algorithm.

## Runtime

- Python 3.11, 3.12, and 3.13;
- Python standard library only;
- automated compile, test, CLI, VS-02 corpus, VS-03 corpus, VS-04 calibration, and independent-reference gates.

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
python3 -m nae3sat.cli profile tests/fixtures/single-edge.json --ordering 2,0,1
python3 -m nae3sat.cli census --max-vertices 5 --output /tmp/vs02-corpus.json
python3 -m nae3sat.cli profile-census --max-vertices 5 --output /tmp/vs03-corpus.json
python3 -m nae3sat.cli calibrate --output /tmp/vs04-calibration.json
cmp /tmp/vs02-corpus.json corpus/all-labelled-n-le-5.json
cmp /tmp/vs03-corpus.json profile-corpus/all-labelled-orderings-n-le-5.json
cmp /tmp/vs04-calibration.json calibration/vs04-calibration.json
```

All census and calibration commands write deterministic compact JSON atomically.

## Checked finite records

### VS-02

- `1045` labelled instances through five vertices;
- `1044` satisfiable and `1` unsatisfiable;
- `33047` complete reference colourings evaluated.

### VS-03

- `123280` instance-ordering profiles;
- `7753542` raw prefixes;
- `2153049` exact classes;
- `1818651` live classes;
- maximum quotient size `8`.

### VS-04

- `1100` labelled graphs: `428` bipartite, `672` non-bipartite;
- `16453` canonical XOR systems: `890` consistent, `15563` inconsistent;
- `36` incidence-forest NAE instances, all constructively colourable;
- `344` maximum-occurrence-at-most-three NAE instances in the small domain, all satisfiable.

These are finite exhaustive measurements on their declared domains. They do not establish unrestricted asymptotic tractability.

## Public API

The package exports the canonical model, serialization, exact oracle, profile engine, and corpus APIs together with:

- `Graph2`, `Graph2Result`, `normalize_graph2`, `solve_graph2`, and `labelled_graphs`;
- `XorSystem`, `XorResult`, `normalize_xor_system`, `solve_xor`, and `labelled_xor_systems`;
- `is_incidence_forest`, `color_incidence_forest`, `is_linear`, and `vertex_occurrences`;
- `processed_boundary`, `boundary_width`, and guarded `minimum_boundary_width`;
- `calibration_payload`, `calibration_record`, `calibration_bytes`, and `verify_calibration_record`.

## Complexity

- exact NAE decision/counting: exponential in vertex count;
- exact profile construction/output: exponential and output-sensitive;
- graph parity solver: `O(n+m)`;
- direct XOR elimination: polynomial in rows and variable count;
- incidence-forest recognition and colouring: linear incidence work;
- one-ordering boundary width: `O(n(n+m))` in the direct implementation;
- exhaustive minimum ordering width: factorial and explicitly guarded.

No result here implies `P=NP` or `P!=NP`.
