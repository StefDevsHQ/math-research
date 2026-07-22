# VS-01 Completion and Quality Audit — Canonical Instance Model

**Slice:** `VS-01`  
**Status:** `COMPLETE / CHECKED`  
**Classification:** Implementation and verification audit  
**Updated:** 2026-07-22

## Scope

This audit closes only the canonical executable instance-model slice. It does not decide Monotone NAE-3SAT, establish Fano-plane unsatisfiability, create an exhaustive satisfiability corpus, compute extension profiles, or establish a new complexity-class result.

The mandatory promotion policy is [BUILDING-BLOCK-GATE.md](BUILDING-BLOCK-GATE.md). `VS-02` may depend on this slice only while the complete quality gate remains green.

## Exported contract

`VS-01` exports:

- immutable canonical `Hypergraph3` and `RelabeledHypergraph3` values;
- normalization of labelled simple 3-uniform hypergraphs;
- strict versioned `nae3-v1` parsing;
- deterministic canonical serialization and SHA-256 identifiers;
- explicit encoded-byte measurement;
- incidence components including isolated vertices;
- induced-subinstance and active-core relabelling maps;
- strict total binary-colouring validation;
- deterministic exact witness checking and first-violated-edge reporting;
- a validation-only command-line interface.

It exports no satisfiability solver, isomorphism canonicalizer, exhaustive corpus, or extension-profile mechanism.

## Correctness obligations checked

### Canonical construction

Direct construction rejects noncanonical edge order, duplicate edges, invalid labels, Boolean and floating-point labels, repeated edge vertices, and invalid vertex counts. `normalize_instance` accepts arbitrary edge order, sorts each edge, removes duplicate edges, and returns the unique canonical value for the fixed labelling.

### Serialization

Parsing rejects unknown or missing fields, duplicate JSON keys, unsupported versions, invalid vertex sets, nonstandard numeric constants, invalid UTF-8, malformed edges, and noninteger labels.

The stable labelled identifier is:

```text
nae3-v1-sha256-<SHA-256 of canonical bytes>
```

It is canonical for a fixed labelling, not up to hypergraph isomorphism.

### Components and relabelling

Component decomposition includes isolated singleton vertices and emits components in increasing least-vertex order. Induced subinstances and active cores relabel increasingly and retain explicit new-to-old maps.

An increasing relabelling preserves the canonical order of the retained edge subsequence, so the implementation constructs it directly without a second normalization or sorting pass.

### Witness verification

A colouring is accepted only when it is a non-string finite `Sequence` of exactly `n` strict integer bits. Sets, mappings, generators, strings, byte strings, Booleans, floating-point values, nonbinary integers, and wrong-length sequences are rejected.

Verification checks every edge for non-monochromaticity. The empty instance accepts the empty colouring; one edge has exactly six satisfying colourings; complementation preserves satisfaction; and the first violated edge is deterministic.

## Reproducible verification

From `tools/monotone-nae-3sat/`:

```bash
python3 -m compileall -q nae3sat tests
python3 -m unittest discover -s tests -v
python3 -m nae3sat.cli validate tests/fixtures/fano-plane.json
```

### Deterministic sampled cross-check

The committed suite contains a separate reference checker over exactly 1,350 generated labelled instances:

- seed `20260722`;
- vertex counts `0 <= n <= 8`;
- 150 generated instances per vertex count;
- independent component and NAE-verifier logic;
- canonical round trips and active-core checks;
- every binary colouring checked for every generated instance.

### Exhaustive small-domain gate

A separate committed test exhausts every labelled 3-uniform hypergraph with at most five vertices:

- 1,045 complete hypergraphs instances across `0 <= n <= 5`;
- 33,047 total instance-colouring checks;
- 33,047 induced-subinstance checks;
- canonical round trips;
- independent component decomposition;
- active-core reconstruction;
- verifier and first-violation agreement;
- cross-process determinism under four `PYTHONHASHSEED` values.

This exhaustiveness concerns the VS-01 implementation contract on that finite domain. It is not evidence for a universal satisfiability claim.

### Runtime matrix

GitHub Actions run `29930706766` completed successfully on:

- Python 3.11;
- Python 3.12;
- Python 3.13.

Each job compiled the package and tests, ran the complete suite, and exercised the CLI fixture path.

The Fano fixture summary remains:

```json
{"format":"nae3-v1-summary","id":"nae3-v1-sha256-3b78789e10d0828f0051c7a0cea558bf988e067433a230a5c62af86db9d45de8","n":7,"m":7,"components_total":1,"components_nontrivial":1,"encoded_bytes":113}
```

The command intentionally does not decide satisfiability.

## Pinned fixture identifiers

| Fixture | Identifier |
|---|---|
| empty | `nae3-v1-sha256-95e95c77352dcd2d94e832f3bc4964beb13da79439f89f79632bee4f420f368f` |
| isolated three | `nae3-v1-sha256-3c53e92c81bc5276993163f9cccb0b0934c00e1c0b696d0b7ebfae92d48c6443` |
| single edge | `nae3-v1-sha256-794c043ed817d84d30d57d79bb3dd40bad9cd0f8ebe594100b93e0abf97bebf7` |
| two disconnected edges | `nae3-v1-sha256-1be9a1eaf7f773add7754fd24c926e13f6cea32bb18b7f0074156ccc7fbb1af9` |
| overlap chain | `nae3-v1-sha256-69636ad41f919734caf63189a5880399cb1062bdf772b85809bfc87f64caef07` |
| Fano plane | `nae3-v1-sha256-3b78789e10d0828f0051c7a0cea558bf988e067433a230a5c62af86db9d45de8` |

## Complexity audit

Let `n` be the explicitly listed vertex count, `m` the supplied edge count, and `L` the canonical byte length.

- normalization: expected `O(m)` hash insertion plus `O(m log m)` constant-arity tuple comparisons;
- direct canonical validation: `O(m)` after the immutable tuple exists;
- parser schema and vertex-set validation: `O(L)`;
- serialization, hashing, and byte measurement: `O(L)`;
- colouring validation and witness verification: `O(n + m)`;
- component decomposition: `O(n + m)`;
- selected-vertex validation and canonical ordering: `O(n + k)` for `k` supplied vertices;
- induced subinstance and active core: `O(n + m)` after the source instance is canonical;
- retained graph and traversal memory: `O(n + m)`.

Vertex labels use `O(log n)` bits. Every vertex is explicitly serialized, so all operations are polynomial in encoded input length. No pseudo-polynomial parameter is used.

## Defects found and corrected

The review sequence found and fixed:

1. unordered sets and mappings accepted as colourings;
2. selected-vertex and active-core sorting and re-normalization beyond the claimed bound;
3. parser vertex sorting despite a linear validation claim;
4. missing wrong-instance rejection in serialization functions;
5. a non-reproducible prose-only random break pass;
6. loss of downstream exit gates through tracker over-compression;
7. an obsolete implementation specification;
8. an unnecessary component sort;
9. an incorrect documented Fano byte count;
10. an untested Python 3.11+ support claim.

Every defect was corrected and the complete quality gate was rerun.

## Final determination

`VS-01` is `COMPLETE / CHECKED` as a concrete infrastructure building block. No open prerequisite defect is known. `VS-02` is unlocked, subject to the same building-block quality gate before it may be promoted or used by `VS-03` and later slices.
