# VS-01 Completion Audit — Canonical Instance Model

**Slice:** `VS-01`  
**Status:** `COMPLETE`  
**Classification:** Implementation and verification audit  
**Updated:** 2026-07-22

## Scope

This audit closes only the canonical executable instance-model slice. It does not decide Monotone NAE-3SAT, create an exhaustive instance corpus, compute extension profiles, or establish any new complexity-class result.

## Implemented artifacts

Under `tools/monotone-nae-3sat/`:

- immutable canonical `Hypergraph3` and relabelled derived-object types;
- strict construction invariants;
- normalization of labelled simple 3-uniform hypergraphs;
- strict versioned JSON parsing;
- deterministic canonical serialization and SHA-256 identifiers;
- explicit encoded-byte measurement;
- incidence-component decomposition including isolated vertices;
- induced-subinstance and active-core relabelling maps;
- exact validation of proposed binary colourings;
- deterministic first-violated-edge reporting;
- command-line validation and summary output;
- fixed valid and malformed fixtures;
- standard-library unit and integration tests.

## Correctness obligations checked

### Canonical construction

Direct construction rejects noncanonical edges, duplicate edges, invalid labels, Boolean labels, floating-point labels, repeated edge vertices, and invalid vertex counts. `normalize_instance` accepts arbitrary edge order, sorts edge vertices, removes duplicate edges, and returns the unique canonical internal value for the fixed labelling.

### Serialization

The accepted format is `nae3-v1`. Parsing rejects unknown or missing keys, duplicate JSON object keys, unsupported versions, noncontiguous vertex sets, nonstandard numeric constants, invalid UTF-8, malformed edge shapes, and noninteger labels. Canonical output is compact, deterministic UTF-8 JSON.

The identifier is:

```text
nae3-v1-sha256-<SHA-256 of canonical bytes>
```

It is canonical for a fixed vertex labelling, not up to hypergraph isomorphism.

### Components and relabelling

Component decomposition includes isolated singleton vertices and emits components in increasing least-vertex order. Induced subinstances and active cores relabel vertices increasingly and preserve an explicit new-to-old map.

### Witness verification

A colouring is accepted as input only when it is a total sequence of strict integer bits. Verification checks every edge for non-monochromaticity. The empty instance accepts the empty colouring; a single edge has exactly six satisfying colourings; complement symmetry is preserved; and the first violated edge is deterministic.

## Test evidence

The standard command is:

```bash
cd tools/monotone-nae-3sat
python3 -m unittest discover -s tests -v
```

The implementation was additionally attacked with an independent reference checker over 1,350 seeded random labelled instances with `0 <= n <= 8`. For every tested instance:

- canonical serialization round-tripped exactly;
- component decomposition agreed with an independent implementation;
- every binary colouring agreed with an independent NAE verifier;
- active-core relabelling agreed with the set of vertices appearing in edges.

Seed: `20260722`.

The command-line Fano fixture produced:

```json
{"format":"nae3-v1-summary","id":"nae3-v1-sha256-3b78789e10d0828f0051c7a0cea558bf988e067433a230a5c62af86db9d45de8","n":7,"m":7,"components_total":1,"components_nontrivial":1,"encoded_bytes":113}
```

The command intentionally does not decide whether the fixture is satisfiable.

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

- normalization uses a set of constant-arity edge tuples followed by sorting: expected `O(m)` insertion plus `O(m log m)` tuple comparisons;
- canonical validation is `O(n + m)` relative to the already canonical tuple representation;
- serialization, hashing, and encoded-size calculation are `O(L)`;
- colouring validation and edge verification are `O(n + m)`;
- component construction and traversal are `O(n + m)`;
- induced-subinstance and active-core construction use dictionaries and sets and are expected `O(n + m)`, followed by ordinary normalization of retained edges;
- retained graph and traversal memory are `O(n + m)`.

Vertex labels occupy `O(log n)` bits. Because vertices are explicitly enumerated, all operations remain polynomial in the encoded input length. No pseudo-polynomial parameter is used.

## Independent break findings

Two defects were found during the break pass and corrected before closure:

1. a final component sort was unnecessary and conflicted with the claimed linear component bound; component identifiers are now assigned in increasing start-vertex order, making the output canonical without sorting;
2. the documented Fano canonical byte count was corrected to `113`.

## Final determination

`VS-01` is complete. The executable laboratory now has a trustworthy canonical input layer and witness verifier.

The next slice is `VS-02`: implement an exact exhaustive satisfiability oracle and record the first exhaustively justified labelled instance domain.
