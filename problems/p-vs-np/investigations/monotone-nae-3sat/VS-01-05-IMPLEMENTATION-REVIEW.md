# VS-01 through VS-05 — Implementation Review

**Scope:** current executable implementation and verification boundary  
**Status:** `CHECKED`, subject to the active-scope gate on the merged commit  
**Updated:** 2026-07-22

## Review question

Does the current VS-01 through VS-05 implementation contain a meaningful remaining correctness, completeness, reproducibility, or downstream-safety defect that should be fixed before VS-06?

## Strongest supported determination

No solver, profile, control, certificate, or finite-census correctness defect was found in this pass.

The review did find three release-quality defects:

1. retained VS-04 source metadata named the wrong Randerath and used the wrong SAT 2003 DOI suffix;
2. the VS-04 audit still attributed planar tractability to the restricted-hardness paper rather than Moret's 1988 result;
3. the public committed-record verifiers accepted any re-digested payload, including a wrong format or additional top-level fields, because they checked only digest agreement.

The tool README also stopped at VS-04 despite VS-05 being complete. These defects are corrected by the implementation-hardening change.

## Layer-by-layer audit

### VS-01 — canonical model

Checked:

- strict integer and Boolean separation;
- canonical edge ordering and duplicate rejection in direct construction;
- normalization of arbitrary input edge order;
- empty instances, isolates, disconnected components, induced subinstances and active cores;
- deterministic UTF-8 JSON serialization and labelled identifiers;
- strict total-colouring validation and canonical first violation;
- exhaustive labelled-domain checks through five vertices;
- cross-process hash-seed determinism.

No meaningful remaining defect was found. The exported identity remains labelled, not isomorphism-canonical.

### VS-02 — exact oracle

Checked:

- baseline enumeration and component-complement reduction;
- proof that symmetry fixing preserves the true lexicographically least witness;
- complete solution listing and direct counts;
- component-factorized counts, including isolates;
- edge-minimal-unsatisfiability testing;
- exhaustive independent comparison on all `1045` labelled instances through five vertices;
- independent Fano decision and edge-deletion checks.

No meaningful remaining defect was found. Runtime remains exponential and is recorded as such.

### VS-03 — exact profiles

Checked:

- ordering and prefix validation;
- exact completion-mask construction;
- deterministic first-occurrence class numbering;
- representative-independent transitions;
- cross-level mask-slicing invariants;
- final-level agreement with direct satisfaction;
- processed-boundary agreement;
- independent tuple-set semantics on complete small domains and named controls;
- exhaustive aggregate and sequence-digest reproduction.

No meaningful remaining defect was found. Exact semantic correctness does not imply compact or polynomial construction.

### VS-04 — controls

Checked:

- graph parity solver against complete enumeration;
- XOR elimination, rank, count and least witness against complete enumeration;
- incidence-forest recognition and constructive colouring;
- high-degree incidence-tree regression after the earlier runtime correction;
- interval boundary computation against the direct definition;
- bounded exhaustive minimum-width guard;
- finite occurrence and forest filters;
- external-source boundaries and attribution.

The implementation is retained. Source metadata and the stale planar attribution were corrected.

### VS-05 — obstruction atlas

Checked:

- strict edge and vertex deletion operations;
- separate edge-minimal and induced-vertex-minimal predicates;
- independent direct enumeration for every unsatisfiable object in the `n<=5` domain;
- true least-witness deletion certificates for `K_5^(3)` and the Fano plane;
- independently recomputed degree and pair-codegree structure;
- exact all-ordering counts and deterministic sequence digests;
- explicit finite, exponential and factorial limitations.

No meaningful remaining defect was found. The Fano plane remains a named control, not an exhaustive seven-vertex census.

## Record-verification correction

The original `verify_*_record` functions checked only:

```text
SHA256(compact_json(payload)) == embedded_digest
```

That establishes internal digest agreement, but not that the record belongs to the claimed versioned format. An altered payload could change `format`, add an unexpected top-level field, recompute the digest, and still pass.

The public verifiers now require:

- an exact top-level key set;
- the exact versioned format identifier;
- fixed generator and computation identifiers where applicable;
- a lowercase 64-character hexadecimal digest;
- digest agreement over the payload.

Adversarial tests cover re-digested wrong formats, unknown fields, and malformed digests.

This remains an **envelope-integrity** check. It does not independently establish semantic truth. Full semantic verification remains:

1. regenerate from committed code and declared domain;
2. compare canonical bytes with the committed record;
3. run the logically separate reference tests.

## Complexity and maintenance conclusion

No additional broadening of the completed phase is justified before VS-06. In particular, the following would be new research rather than completion work:

- exhaustive six- or seven-vertex obstruction enumeration;
- isomorphism canonicalization;
- a faster exact solver;
- a new profile representation;
- additional tractable subclasses;
- classification of all minimal non-two-colourable triple systems.

Those tasks should be opened only when required by a precise downstream claim.

## Final determination

After the corrections above, VS-01 through VS-05 are complete at their declared scope. The meaningful next work is VS-06. Reopening a completed slice requires either a concrete defect, a violated downstream assumption, or a new explicit contract—not general polishing or larger finite experiments.
