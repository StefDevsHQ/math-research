# VS-01 Completion Audit — Canonical Instance Model

**Slice:** `VS-01`  
**Status:** `COMPLETE`  
**Classification:** Implementation and verification audit  
**Review maturity:** `CHECKED`  
**Updated:** 2026-07-22

## Scope

This audit closes only the canonical executable instance-model slice. It does not decide Monotone NAE-3SAT, establish Fano-plane unsatisfiability, create an exhaustive instance corpus, compute extension profiles, or establish a new complexity-class result.

## Implemented artifacts

Under `tools/monotone-nae-3sat/`:

- immutable canonical `Hypergraph3` and `RelabeledHypergraph3` values;
- strict public-constructor invariants;
- normalization of labelled simple 3-uniform hypergraphs;
- strict versioned JSON parsing;
- deterministic canonical serialization and SHA-256 identifiers;
- explicit encoded-byte measurement;
- incidence-component decomposition including isolated vertices;
- induced-subinstance and active-core relabelling maps;
- strict total binary-colouring validation;
- deterministic first-violated-edge reporting;
- a validation-only command-line interface;
- valid and malformed fixtures;
- standard-library unit, integration, and deterministic reference-cross-check tests.

## Correctness obligations checked

### Canonical construction

Direct construction rejects noncanonical edge order, duplicate edges, invalid labels, Boolean and floating-point labels, repeated edge vertices, and invalid vertex counts. `normalize_instance` accepts arbitrary edge order, sorts each edge, removes duplicate edges, and returns the unique canonical value for the fixed labelling.

### Serialization

The accepted format is `nae3-v1`. Parsing rejects unknown or missing fields, duplicate JSON keys, unsupported versions, invalid vertex sets, nonstandard numeric constants, invalid UTF-8, malformed edges, and noninteger labels.

The stable labelled identifier is:

```text
nae3-v1-sha256-<SHA-256 of canonical bytes>
```

It is not canonical up to hypergraph isomorphism.

### Components and relabelling

Component decomposition includes isolated singleton vertices and emits components in increasing least-vertex order. Induced subinstances and active cores relabel vertices increasingly and return an explicit new-to-old map.

The retained edge subsequence remains canonical under an increasing relabelling. The implementation therefore constructs it directly without a second normalization or sorting pass.

### Witness verification

A colouring is accepted only when it is a non-string finite `Sequence` of exactly `n` strict integer bits. Sets, mappings, generators, strings, byte strings, Booleans, floating-point values, nonbinary integers, and wrong-length sequences are rejected.

Verification checks every edge for non-monochromaticity. The empty instance accepts the empty colouring; one edge has exactly six satisfying colourings; global complementation preserves satisfaction; and the first violated edge is deterministic.

## Reproducible test evidence

From the tool directory:

```bash
cd tools/monotone-nae-3sat
python3 -m unittest discover -s tests -v
python3 -m nae3sat.cli validate tests/fixtures/fano-plane.json
```

The committed suite contains 25 test methods. One method performs a deterministic independent reference cross-check over exactly 1,350 generated labelled instances:

- seed: `20260722`;
- vertex counts: `0 <= n <= 8`;
- 150 generated instances for each `n`;
- independent component computation;
- independent NAE witness evaluation;
- canonical round-trip checks;
- active-core map and edge checks;
- every binary colouring checked for every generated instance.

This is finite computational verification of the implementation, not evidence for a universal satisfiability claim.

The Fano fixture summary is:

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
- parser schema and vertex-set validation: `O(L)` using a byte membership array rather than sorting;
- serialization, hashing, and byte measurement: `O(L)`;
- colouring validation and witness verification: `O(n + m)`;
- component decomposition: `O(n + m)`;
- selected-vertex validation and canonical ordering: `O(n + k)` for `k` supplied vertices;
- induced subinstance and active core: `O(n + m)` after the source instance is canonical;
- retained graph and traversal memory: `O(n + m)`.

Vertex labels use `O(log n)` bits. Because every vertex is explicitly serialized, all operations are polynomial in encoded input length. No pseudo-polynomial parameter is used.

## Full-review findings fixed

The final PR-wide review found and corrected:

1. unordered sets and mappings could be accepted as colourings despite the sequence contract;
2. selected-vertex and active-core paths sorted and re-normalized, exceeding the claimed linear bound;
3. parser vertex validation sorted the vertex list despite claiming linear schema validation;
4. serialization functions lacked explicit wrong-instance rejection;
5. the 1,350-instance break pass was described but not reproducible from committed code;
6. the vertical-slice ledger had been over-compressed and lost exact downstream exit gates;
7. the implementation specification still described a partial, differently laid-out package.

Earlier break-pass fixes retained here were removal of an unnecessary component sort and correction of the Fano canonical byte count to `113`.

## Final determination

`VS-01` is `COMPLETE / CHECKED` as an infrastructure slice. The next slice is `VS-02`: implement an exact exhaustive satisfiability oracle and record the first exhaustively justified labelled instance domain.
