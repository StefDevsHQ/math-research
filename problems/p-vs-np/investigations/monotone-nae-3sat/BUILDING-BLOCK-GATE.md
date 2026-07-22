# Building-Block Quality Gate

**Applies to:** `VS-01` through `VS-12`  
**Policy:** A later slice may not begin until every prerequisite slice passes this gate.  
**Updated:** 2026-07-22

## Principle

Each vertical slice is a dependency. A downstream result is only as reliable as the strongest unverified assumption inherited from earlier slices.

A slice is promoted from `PARTIAL` to `COMPLETE` only after its outputs are concrete, reproducible, independently attacked, synchronized, and safe for downstream reuse.

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
- exhaustive finite testing where practical;
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

Evidence described only in prose is not accepted if it can reasonably be committed as a test, script, or canonical record.

### 4. Complexity and encoding

The audit must track:

- encoded input length;
- preprocessing cost;
- intermediate representation size;
- total generated states or objects;
- transition and equivalence costs;
- memory;
- deterministic versus expected bounds;
- assumptions about machine words, hashing, and numeric bit length.

A local bound, recursion-depth bound, or branching bound is not accepted as a global computation bound.

### 5. Independent attack

After the slice appears complete, perform a separate break pass covering:

- wrong types and malformed encodings;
- empty, isolated, disconnected, duplicate, and maximal-small cases;
- order and hash-seed dependence;
- cross-component compatibility;
- discrepancy between documentation and implementation;
- hidden sorting, normalization, enumeration, or exponential work;
- misuse by the next slice.

Every substantive finding must be fixed or the slice returned to `PARTIAL` or `COMPLETE / DRAFT`.

### 6. Verification

Where executable artifacts exist:

- staged syntax and whitespace checks must run locally before commit;
- the active scope's fast gate must pass on the final feature-branch commit;
- the active scope's full gate must pass before promotion of executable mathematics, generated records, claim status, or phase status;
- supported runtimes must be tested rather than merely declared;
- representative command-line or end-to-end paths must run;
- the exact locally checked commit SHA must be recorded for substantive pull requests;
- the `main` workflow must provide final integration verification for active scopes.

The repository deliberately does not run expensive CI automatically on every pull-request commit. Local hooks are bypassable and are evidence only when the checked SHA is recorded. The main-only workflow is a post-merge integration gate, not proof that every pull-request revision was checked.

When an investigation or route becomes `CLOSED` or `DEFERRED`, its final full gate must pass on the exact closing commit before the scope is removed from `.verification/active-paths`. Closed or deferred suites then leave routine local and CI execution while their evidence and reproduction instructions remain preserved.

### 7. Documentation synchronization

Before promotion, synchronize:

- implementation or proof artifact;
- completion audit;
- `VERTICAL-SLICES.md`;
- `STATUS.md`;
- investigation README;
- claim ledger when a mathematical claim changes;
- parent project status when the active phase or route changes.

Contradictory status records block promotion.

## Promotion states

- `PARTIAL` — implementation, proof, or evidence exists but one or more gate conditions remain open.
- `COMPLETE / DRAFT` — exit gate appears satisfied, but independent attack, synchronization, or verification remains incomplete.
- `COMPLETE / CHECKED` — gate satisfied, independent attack completed, records synchronized, and required active-scope checks passed.
- `COMPLETE / INDEPENDENTLY-CHECKED` — a logically independent reviewer or implementation has revalidated the slice.

Only `COMPLETE / CHECKED` or stronger may unlock a dependent slice.

## Regression rule

If a later review finds a substantive defect in a completed prerequisite:

1. immediately return that slice to `PARTIAL` or `COMPLETE / DRAFT`;
2. mark dependent work as provisionally blocked;
3. fix and rerun the full gate while the scope is active;
4. audit whether downstream results relied on the defect;
5. restore statuses only after the dependency chain is sound.

Fixing a defect does not by itself restore completion; the quality gate must be rerun.

## Phase closeout rule

A group of slices may be closed as one phase unit when:

1. every included slice is `COMPLETE / CHECKED` or stronger;
2. cross-slice contracts and assumptions are audited in both directions;
3. claim statuses and quantifiers are rechecked globally;
4. complexity and encoding statements remain compatible;
5. canonical records and reproduction commands are preserved;
6. status, slice, claim, README, and parent records are synchronized;
7. the next phase's permitted dependencies and prohibited assumptions are stated.

The phase closeout does not retire its tests while the investigation remains active. Test retirement occurs only when the corresponding investigation or route is `CLOSED` or `DEFERRED` under the active-scope lifecycle.

## Current application

`VS-01` through `VS-05` satisfy this gate as one trusted-laboratory phase, subject to the exact committed active-scope verification recorded by the closeout change. `VS-06` is ready for formalization. `VS-07` remains blocked until VS-06 has checked failure evidence.
