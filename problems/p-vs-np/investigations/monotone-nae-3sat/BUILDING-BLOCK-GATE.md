# Building-Block Quality Gate

**Applies to:** `VS-01` through `VS-12`  
**Policy:** A later slice may not begin until every prerequisite slice passes this gate.  
**Updated:** 2026-07-22

## Principle

Each vertical slice is a dependency, not a disposable experiment. A downstream result is only as reliable as the strongest unverified assumption inherited from earlier slices.

A slice is therefore promoted from `PARTIAL` to `COMPLETE` only after its outputs are concrete, reproducible, independently attacked, and safe for downstream reuse.

## Mandatory gate

### 1. Exact contract

The slice must state:

- its mathematical object or executable interface;
- all assumptions and quantifiers;
- accepted and rejected inputs;
- outputs and semantics;
- boundary and degenerate cases;
- explicit non-goals;
- the exact downstream guarantees being exported.

No downstream slice may depend on an unstated convention.

### 2. Correctness evidence

The slice must provide the strongest applicable evidence:

- complete proof for mathematical claims;
- exact verifier or independent oracle for executable claims;
- exhaustive finite testing where the domain is small enough;
- adversarial and malformed-input testing;
- independent reference implementation or logically separate cross-check;
- named counterexamples for rejected alternatives.

Random testing alone is not sufficient when exhaustive testing is practical.

### 3. Reproducibility

Every computational result must record:

- committed code and fixtures;
- exact command;
- runtime and dependency requirements;
- deterministic seeds where sampling is used;
- domain generation and counts;
- expected output or pinned identifiers;
- limitations and whether the run is exhaustive or sampled.

Evidence described only in prose is not accepted if it can reasonably be committed as a test or script.

### 4. Complexity and encoding

The audit must track:

- encoded input length;
- preprocessing cost;
- intermediate representation size;
- total generated states or objects;
- transition and equivalence costs;
- memory;
- deterministic versus expected bounds;
- any assumptions about machine words, hashing, or numeric bit length.

A local bound is not accepted as a global bound.

### 5. Independent attack

After the slice appears complete, perform a separate break pass covering:

- wrong types and malformed encodings;
- empty, isolated, disconnected, duplicate, and maximal-small cases;
- order and hash-seed dependence;
- cross-component compatibility;
- discrepancy between documentation and implementation;
- hidden sorting, normalization, enumeration, or exponential work;
- misuse by the next slice.

Every substantive finding must be fixed or the slice returned to `PARTIAL`.

### 6. Automation

Where executable artifacts exist:

- the full test suite must run automatically on each relevant pull request;
- the supported runtime matrix must be tested rather than merely declared;
- compilation or syntax checks must run;
- a representative command-line or end-to-end path must run;
- required checks must be green before merge.

### 7. Documentation synchronization

Before promotion, synchronize:

- implementation or proof artifact;
- completion audit;
- `VERTICAL-SLICES.md`;
- `STATUS.md`;
- investigation README;
- claim ledger when a mathematical claim changes.

Contradictory status records block promotion.

## Promotion states

- `PARTIAL` — implementation, proof, or evidence exists but one or more gate conditions remain open.
- `COMPLETE / DRAFT` — exit gate appears satisfied, but independent attack or automation remains incomplete.
- `COMPLETE / CHECKED` — gate satisfied, independent attack completed, and all required automated checks pass.
- `COMPLETE / INDEPENDENTLY-CHECKED` — a logically independent reviewer or implementation has revalidated the slice.

Only `COMPLETE / CHECKED` or stronger may unlock a dependent slice.

## Regression rule

If a later review finds a substantive defect in a completed prerequisite:

1. immediately return that slice to `PARTIAL` or `COMPLETE / DRAFT`;
2. mark dependent work as provisionally blocked;
3. fix and re-run the full gate;
4. audit whether downstream results relied on the defect;
5. restore statuses only after the dependency chain is sound.

Fixing a defect does not by itself restore completion; the quality gate must be rerun.

## VS-01 application

`VS-01` exports only:

- canonical labelled instance construction;
- strict versioned parsing and serialization;
- stable labelled identifiers;
- deterministic components and relabelling;
- strict total-colouring validation;
- exact witness verification.

Its quality gate includes:

- unit, integration, malformed-input, and deterministic random reference tests;
- exhaustive checks over all 1,045 labelled 3-uniform hypergraphs with at most five vertices;
- all 33,047 associated binary-colouring checks;
- all 33,047 induced-subinstance checks;
- cross-process determinism under four hash seeds;
- Python 3.11, 3.12, and 3.13 automation;
- complexity and encoding audit.

`VS-02` remains blocked until this full gate is green.
