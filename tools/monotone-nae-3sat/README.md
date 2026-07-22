# Monotone NAE-3SAT Research Tool

Standard-library Python implementation of the canonical labelled 3-uniform hypergraph model used by the Monotone NAE-3SAT investigation.

## Scope

This tool implements vertical slice `VS-01`:

- strict versioned JSON parsing;
- canonical graph normalization;
- deterministic serialization and SHA-256 identifiers;
- incidence components;
- induced subinstances and active-core relabelling;
- strict verification of proposed two-colourings;
- a validation and summary command.

It does **not** decide satisfiability, enumerate an exhaustive instance corpus, compute extension profiles, reduce graph isomorphism, or establish any new complexity result.

## Runtime

- Supported: Python 3.11 or later.
- Dependencies: Python standard library only.
- Full-review execution environment: Python 3.13.5.

## Canonical input format

```json
{"format":"nae3-v1","vertices":[0,1,2,3],"edges":[[0,1,2],[1,2,3]]}
```

The explicit vertex list must be exactly the set `0, ..., n-1`, though input order may vary. Edges may be unsorted and repeated; parsing normalizes them. Unknown fields, duplicate JSON keys, unsupported versions, nonstandard numeric constants, invalid UTF-8, repeated vertices inside an edge, and noninteger labels are rejected.

Canonical output is compact UTF-8 JSON with keys in the order `format`, `vertices`, `edges`. It is canonical for a fixed vertex labelling, not up to hypergraph isomorphism.

## Tests

From this directory:

```bash
python3 -m unittest discover -s tests -v
```

The suite contains 25 test methods. It includes a deterministic independent reference cross-check over 1,350 generated labelled instances with seed `20260722`, vertex counts `0` through `8`, and every binary colouring of each instance.

This verifies the implementation over a finite domain; it is not a universal mathematical proof about satisfiability.

## Validate an instance

```bash
python3 -m nae3sat.cli validate tests/fixtures/fano-plane.json
```

The command prints a compact summary containing the format, stable instance identifier, vertex and edge counts, component counts, and canonical encoded byte length. It intentionally does not report satisfiability.

```json
{"format":"nae3-v1-summary","id":"nae3-v1-sha256-...","n":7,"m":7,"components_total":1,"components_nontrivial":1,"encoded_bytes":113}
```

Errors are written to standard error and return exit status `2`.

## Public API

The package exports:

- `Hypergraph3` and `RelabeledHypergraph3`;
- `normalize_instance`;
- `parse_instance_json`, `to_canonical_json`, and `canonical_bytes`;
- `instance_id` and `encoded_size_bytes`;
- `incidence_components`, `induced_subinstance`, and `active_core`;
- `verify_coloring` and `first_violated_edge`;
- explicit parse, validation, and colouring error classes.

Colourings must be finite non-string sequences of strict integer bits. Sets, mappings, generators, strings, byte strings, Booleans, floating-point values, nonbinary integers, and wrong-length sequences are rejected.

## Complexity

After canonical normalization, component decomposition, induced subinstances, active-core extraction, and witness verification are linear in `n + m`. Initial edge normalization requires sorting and is `O(m log m)` in the comparison model. Serialization and hashing are linear in canonical encoded length.

## Limitations

The SHA-256 identifier changes if the labelled vertex set changes, including isolated vertices. Relabelled isomorphic graphs generally have different identifiers. Computational outputs from later vertical slices remain `COMPUTATIONAL` unless accompanied by an exhaustiveness argument or proof.
