# Phase I Closeout Audit — VS-01 through VS-05

**Scope:** `VS-01` through `VS-05`  
**Status:** `COMPLETE / CHECKED`, conditional only on the repository's final active-scope verification remaining green on the closing commit  
**Updated:** 2026-07-22

## Exact phase claim

The first five vertical slices form a compatible trusted laboratory for Monotone NAE-3SAT:

1. canonical labelled instance representation;
2. exact exponential satisfiability ground truth;
3. exact successful-completion profiles for fixed orderings;
4. calibrated tractable controls and restricted theorems;
5. exact minimal-obstruction evidence and a proved limitation of successful-completion semantics.

The phase does not solve Monotone NAE-3SAT in polynomial time, prove `P=NP`, prove `P!=NP`, establish an asymptotic compression bound, or lower-bound arbitrary representations.

## Dependency audit

### VS-01 to VS-02

VS-02 consumes only canonical instances, total-colouring validation, deterministic serialization, and witness verification exported by VS-01. It does not rely on isomorphism canonicalization or an unstated solver.

### VS-02 to VS-03

VS-03 uses exact completion enumeration as semantic ground truth. Its correctness theorem is independent of any polynomial-time claim; construction may be exponential and is recorded as such.

### VS-03 to VS-04

VS-04 uses the profile engine only as a comparison instrument. Graph parity, affine XOR, incidence-forest elimination, bounded-boundary dynamic programming, and component factorization remain distinct mechanisms rather than being conflated into one algorithm.

### VS-02 and VS-03 to VS-05

VS-05 uses VS-02 for exact satisfiability and deletion witnesses and VS-03 for all-ordering successful-completion profiles. Edge-minimality and induced-vertex-minimality are separate predicates. The Fano plane is a named control, not an exhaustive seven-vertex census.

## Quantifier and status audit

- `NAE-001` is external and established.
- `NAE-002` through `NAE-005`, `NAE-007` through `NAE-009`, and `NAE-011` are proved project claims.
- `NAE-010` remains finite exhaustive computation over the declared `n<=5` domain.
- `NAE-006` remains a draft conjecture without a selected representation language.
- No finite census is promoted to an asymptotic theorem.
- No restricted theorem is promoted to a universal algorithm.
- No representation-specific failure is promoted to a general lower bound.

## Boundary and degenerate cases

The retained audits cover empty instances, isolated vertices, disconnected components, malformed encodings, duplicate and noncanonical edges, maximal small instances, satisfiable and unsatisfiable cases, ordering dependence, complement symmetry, and deletion-certificate validation.

The phase explicitly preserves these boundaries:

- labels are canonical but not isomorphism-canonical;
- exact solving and profile construction are exponential in general;
- all-ordering enumeration is factorial;
- bounded-boundary tractability is parameterized and not universal;
- planar and bounded-occurrence tractability are imported, not re-proved;
- the Fano evidence is named-instance evidence;
- globally unsatisfiable instances collapse successful-completion semantics completely.

## Complexity audit

No phase artifact confuses finite feasibility with polynomial time.

- VS-01 operations are measured against encoded input size.
- VS-02 explicitly enumerates complete colourings.
- VS-03 may construct exponentially many prefixes and semantic objects.
- VS-04's bounded-boundary algorithm is exponential in boundary width and polynomial only for bounded width.
- VS-05 performs repeated exact solves and factorial all-ordering enumeration.

No claim relies only on polynomial recursion depth or local branching; complete generated-state and output sizes remain part of every future universal claim obligation.

## Cross-artifact synchronization

The following records are synchronized by this closeout:

- `README.md`;
- `STATUS.md`;
- `VERTICAL-SLICES.md`;
- `CLAIMS.md`;
- `BUILDING-BLOCK-GATE.md`;
- the VS-01 through VS-05 implementation and audit records;
- the active-scope verification lifecycle.

`NAE-011` is registered atomically: every unsatisfiable instance has one dead successful-completion class at every level under every ordering.

## Independent break pass

The phase was attacked for:

- hidden strengthening from labelled to unlabelled or isomorphism classes;
- conflation of edge and vertex minimality;
- inference from `n<=5` to larger orders;
- inference from named Fano evidence to a seven-vertex census;
- inference from exact quotient correctness to polynomial construction;
- inference from dead-state collapse to a general compression lower bound;
- conflation of distinct tractable mechanisms;
- stale documentation and contradictory slice status;
- CI requirements inconsistent with the repository's active-scope lifecycle.

The stale status and policy defects were corrected in the closeout change. No remaining mathematical contradiction was found in the exported phase contracts.

## Verification and reproducibility

Canonical entry points:

```bash
sh scripts/check.sh fast
sh scripts/check.sh full
```

The active scope remains `monotone-nae-3sat`, so the phase continues to participate in routine verification while the investigation is open. When the investigation is eventually `CLOSED` or `DEFERRED`, its final checked commit, records, fixtures, commands, and runtime requirements must be preserved before removing it from `.verification/active-paths`.

The phase status is valid only for the exact committed artifacts and their recorded verification environment. Future edits to a closed artifact require explicit reactivation or a new dependent scope.

## Export to VS-06

VS-06 may rely on:

- canonical instances and deterministic identifiers;
- exact satisfiability and least-witness ground truth;
- exact fixed-order successful-completion profiles;
- calibrated tractable controls;
- exact `K_5^(3)` and Fano obstruction records;
- `NAE-011` as a prohibition against using successful-completion sets alone to explain globally unsatisfiable structure.

VS-06 may not assume:

- a compact universal representation;
- asymptotically few quotient classes;
- that local structural similarity implies equal residual semantics;
- that dead-state collapse is informative about the cause of rejection;
- that a collision for one summary lower-bounds all algorithms.

## Final determination

`VS-01` through `VS-05` are retained as one `COMPLETE / CHECKED` laboratory phase. The next legitimate action is to formalize VS-06 collision claims. VS-07 remains blocked until VS-06 produces checked failure evidence.
