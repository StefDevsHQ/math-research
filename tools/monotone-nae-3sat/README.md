# Monotone NAE-3SAT Research Tool

Standard-library Python laboratory for canonical labelled 3-uniform hypergraphs, exact finite satisfiability, exact extension profiles, tractable controls, minimal obstructions, and naive-summary collision analysis.

## Completed slices

- `VS-01`: canonical model, strict parser, serialization, components, relabelling, and witness verification;
- `VS-02`: exact solver, least witnesses, listing, direct and factorized counting, generation, and finite census;
- `VS-03`: exact completion masks, semantic quotient classes, transitions, boundary metrics, and profile census;
- `VS-04`: graph parity, affine XOR, incidence forests, bounded boundaries, disconnected products, and calibration;
- `VS-05`: edge/vertex minimality, deletion certificates, `K_5^(3)` and Fano controls, obstruction census, and all-ordering aggregates;
- `VS-06`: degree, intersection, pair-codegree, parity, moment, spectral, local-consistency, induced-subinstance, and boundary-summary collisions plus a fixed-radius locality-failure family.

The exact oracle, profiles, censuses, atlases, and collision searches are finite exponential or factorial laboratory tools. They are not a universal polynomial algorithm.

## Runtime

- Python 3.11, 3.12, and 3.13;
- Python standard library only;
- active-scope compile, tests, CLI, record-envelope, byte-reproduction, and independent-reference gates.

## Input format

```json
{"format":"nae3-v1","vertices":[0,1,2,3],"edges":[[0,1,2],[1,2,3]]}
```

Canonical output is deterministic for a fixed labelling, not up to hypergraph isomorphism.

## Verification

From the repository root:

```bash
sh scripts/check.sh fast
sh scripts/check.sh full
```

Reproducibility commands:

```bash
python3 -m nae3sat.cli census --max-vertices 5 --output /tmp/vs02.json
python3 -m nae3sat.cli profile-census --max-vertices 5 --output /tmp/vs03.json
python3 -m nae3sat.cli calibrate --output /tmp/vs04.json
python3 -m nae3sat.cli obstruction-atlas --output /tmp/vs05.json
python3 -m nae3sat.cli summary-collisions --output /tmp/vs06.json
cmp /tmp/vs02.json corpus/all-labelled-n-le-5.json
cmp /tmp/vs03.json profile-corpus/all-labelled-orderings-n-le-5.json
cmp /tmp/vs04.json calibration/vs04-calibration.json
cmp /tmp/vs05.json obstruction-atlas/vs05-obstruction-atlas.json
cmp /tmp/vs06.json summary-collisions/vs06-summary-collisions.json
```

All record commands write deterministic compact JSON atomically. Public `verify_*_record` functions validate the strict versioned envelope and digest. Semantic verification remains regeneration plus byte comparison and independent tests.

## VS-06 APIs

The package exports:

- degree, intersection, pair-codegree, parity, second-moment, and incidence-Gram-spectrum summaries;
- root generalized arc consistency and proper-induced-satisfiability summaries;
- exact, weight, and parity boundary summaries;
- exact completion masks;
- graph cycle-union, bipartiteness, rooted bounded-radius, and anchored-NAE helpers;
- named collision constructors;
- deterministic summary-collision payload, record, bytes, and strict verifier.

## Checked records

- VS-02: `1045` labelled instances through five vertices;
- VS-03: `123280` instance-ordering profiles and `2153049` exact classes;
- VS-04: exhaustive graph, XOR, incidence-forest, and bounded-occurrence controls on declared domains;
- VS-05: unique `n<=5` obstruction, complete named deletion certificates, and all-ordering aggregates;
- VS-06: ten explicit same-summary/different-semantics collisions and checked radius-one/radius-two samples of a proved all-fixed-radius family.

## Complexity boundaries

- exact NAE decision and counting: exponential;
- exact profiles: exponential and output-sensitive;
- all-ordering aggregation: factorial;
- generic rooted-radius canonicalization: factorial in the ball size;
- exact boundary dynamic programming: exponential in boundary width;
- graph parity, affine XOR, and incidence-forest controls: polynomial on their stated domains.

No result here implies `P=NP` or `P!=NP`.
