# Vertical Slices — Monotone NAE-3SAT

**Purpose:** Authoritative execution order and progress ledger.  
**Updated:** 2026-07-22

Every slice is governed by the mandatory [building-block quality gate](BUILDING-BLOCK-GATE.md). A dependent slice may begin only when every prerequisite is `COMPLETE / CHECKED` or stronger.

## Progress summary

| Slice | Name | Status | Current result | Next action |
|---:|---|---|---|---|
| `VS-01` | Canonical instance model | `COMPLETE / CHECKED` | Canonical model, parser, serialization, components, relabelling, verifier, exhaustive tests, and cross-version verification are checked. | Preserve the exported contract. |
| `VS-02` | Exact small-instance oracle | `COMPLETE / CHECKED` | Exact decision, least witnesses, listing, counting, factorization, generator, Fano control, and deterministic 1045-instance census are checked. | Preserve as finite ground truth. |
| `VS-03` | Exact extension-profile engine | `COMPLETE / CHECKED` | Exact completion masks, quotient classes, transitions, boundary metrics, canonical records, and a 123280-profile exhaustive census are checked. | Preserve as the semantic reference layer. |
| `VS-04` | Control calibration | `COMPLETE / CHECKED` | Graph parity, affine XOR, incidence forests, bounded boundaries, and disconnected products are separately calibrated and checked. | Use as controls, not as a universal synthesis. |
| `VS-05` | Minimal obstruction atlas | `COMPLETE / CHECKED` | The complete `n<=5` obstruction census, named `K_5^(3)` and Fano certificates, all-ordering profiles, and representation limitation are checked. | Preserve as the first obstruction and failure-semantics baseline. |
| `VS-06` | Destroy naive summaries | `READY` | Candidate summaries and exact collision obligations are specified. | Formalize each summary and search for same-summary/different-semantics collisions. |
| `VS-07` | Measure semantic merging | `BLOCKED` | Exact equivalence and tractable controls are calibrated. | Proceed after checked VS-06 failure evidence. |
| `VS-08` | Extract first atomic invariant | `BLOCKED` | No representation language is selected. | Use checked VS-06 and VS-07 evidence. |
| `VS-09` | Prove restricted theorem | `PARTIAL` | Bounded-boundary and incidence-forest theorems are checked. | Prove a future invariant on a larger exact subclass. |
| `VS-10` | Attack with hard families | `BLOCKED` | Hard controls are registered. | Attack a checked VS-08 invariant. |
| `VS-11` | Global complexity audit | `BLOCKED` | Audit criteria exist. | Count the complete computation graph of a candidate mechanism. |
| `VS-12` | Route decision | `BLOCKED` | Claim discipline is prepared. | Classify the route after VS-08 through VS-11. |

## Phase I — trusted laboratory (`VS-01` through `VS-05`)

**Phase status:** `COMPLETE / CHECKED`.

The phase exports five compatible layers:

1. a canonical labelled 3-uniform-hypergraph representation;
2. an exact exponential satisfiability oracle and finite census;
3. an exact successful-completion semantic quotient for fixed orderings;
4. independently calibrated tractable mechanisms and restricted theorems;
5. an exact minimal-obstruction atlas and the proved dead-quotient limitation `NAE-011`.

The phase does **not** export a universal polynomial-time algorithm, an asymptotic compression bound, a general lower bound, or an accepted route conjecture.

Evidence: [phase closeout audit](VS-01-05-PHASE-AUDIT.md).

## VS-01 — Canonical instance model

**Exit gate:** satisfied.

Exports canonical construction, strict versioned parsing, deterministic serialization and identifiers, incidence components, induced relabelling, total-colouring validation, and witness verification.

Evidence: [specification](VS-01-IMPLEMENTATION.md), [audit](VS-01-AUDIT.md), executable package, exhaustive labelled-domain checks through five vertices, independent sampled checks, determinism checks, and supported-runtime verification.

## VS-02 — Exact small-instance oracle

**Exit gate:** satisfied.

Exports exact decision, true least witnesses, complete solution listing, exact direct and factorized counting, edge-minimal-unsatisfiability testing, canonical labelled generation, and deterministic finite census output.

Checked results:

- complete domain `H_{<=5}` has `1045` labelled instances;
- `1044` are satisfiable;
- the unique unsatisfiable five-vertex instance is `K_5^(3)`;
- `33047` complete colourings were evaluated by the reference census;
- the Fano plane is unsatisfiable and edge-minimal unsatisfiable.

Evidence: [specification](VS-02-IMPLEMENTATION.md), [audit](VS-02-AUDIT.md), committed corpus, exhaustive production/reference tests, and CLI reproduction.

## VS-03 — Exact extension-profile engine

**Exit gate:** satisfied.

Exports exact completion masks, deterministic exact quotient classes, representative-independent transitions, processed-boundary comparisons, canonical profile records, and deterministic profile-census output.

Checked finite results:

- `123280` instance-ordering profiles through five vertices;
- `7753542` raw prefixes;
- `2153049` exact classes;
- `1818651` live classes;
- `2865585` processed-valid boundary states;
- maximum quotient size `8`;
- `120` unsatisfiable-root profiles.

Evidence: [specification](VS-03-IMPLEMENTATION.md), [proof and completion audit](VS-03-AUDIT.md), committed profile corpus, and exact/reference tests.

## VS-04 — Control calibration

**Exit gate:** satisfied.

Checked mechanisms:

- graph bipartiteness through root-relative parity;
- XOR consistency through affine row reduction;
- incidence-forest NAE colouring through acyclic elimination;
- bounded-boundary dynamic programming through complete finite interfaces;
- disconnected factorization through exact component independence.

Checked finite results:

- all `1100` labelled graphs through five vertices: `428` bipartite and `672` non-bipartite;
- all `16453` canonical XOR systems through three variables: `890` consistent and `15563` inconsistent;
- all `36` incidence-forest NAE instances through five vertices are constructively colourable;
- all `344` maximum-occurrence-at-most-three instances in that finite domain are satisfiable.

Planar and occurrence-at-most-three tractability remain imported results rather than project re-proofs.

Evidence: [specification](VS-04-IMPLEMENTATION.md), [proof and completion audit](VS-04-AUDIT.md), deterministic calibration report, and exhaustive independent tests.

## VS-05 — Minimal obstruction atlas

**Exit gate:** satisfied.

The complete `n<=5` census contains one unsatisfiable object, `K_5^(3)`, which is edge- and vertex-minimal. Complete least-witness certificates are stored for every edge and vertex deletion of `K_5^(3)` and the Fano plane. All `120` orderings of `K_5^(3)` and all `5040` orderings of the Fano plane are profiled.

The universal representation-specific theorem `NAE-011` is retained: every prefix of an unsatisfiable instance has no satisfying completion, so successful-completion equivalence collapses to one dead class at every level. This does not lower-bound richer representations.

Evidence: [specification](VS-05-IMPLEMENTATION.md), [proof and completion audit](VS-05-AUDIT.md), committed obstruction atlas, deletion certificates, independent census, and all-ordering aggregate verification.

## VS-06 — Destroy naive summaries

For each proposed summary, produce a complete same-summary/different-semantics collision or retain its exact unresolved scope. Degree, intersection, pair co-occurrence, parity, local consistency, bounded-radius, spectral, boundary-only, and low-moment summaries are mandatory targets.

The semantic discriminator must be explicitly defined. Globally unsatisfiable instances cannot be distinguished by successful-completion sets alone because of `NAE-011`; VS-06 must therefore use residual satisfiability, failure certificates, residual constraint systems, or another exact observable.

## VS-07 — Measure genuine semantic merging

Separate raw assignments, boundary states, dead-state merging, complement symmetry, live semantic merging, quotient count, and representation size across orderings. Exit with reproducible first merges and first significant growth families.

## VS-08 — Extract first atomic invariant

State one falsifiable representation language with semantics, construction, transitions, correctness target, proposed total-state bound, controls, adversarial family, and stop condition. No undefined operation may hide satisfiability or equivalence.

## VS-09 — Prove a restricted theorem

Prove the invariant first on the largest supported exact subclass, including assumptions, boundaries, encoding, runtime, memory, and total-state bounds. Independently attack the proof.

## VS-10 — Attack with hard families

Test against minimal obstructions, linear 4-regular instances, verified reduction outputs, high-width families, and defined sibling transfers. Produce a counterexample, restricted surviving theorem, or genuinely surviving candidate.

## VS-11 — Global complexity audit

Count input and intermediate bit lengths, construction, equivalence, transitions, recursion and branching, complete generated-state graph, duplicate detection, memory, normalization, witness reconstruction, uniformity, and deterministic correctness.

## VS-12 — Route decision

Record a surviving universal candidate, restricted theorem, complete disproof, representation-specific barrier, or closure. Synchronize claims, evidence, limitations, and reopening conditions.

## Immediate queue

1. Preserve the checked `VS-01` through `VS-05` laboratory phase without expanding its default tests after the investigation is eventually closed or deferred.
2. Formalize `VS-06` summaries and semantic collision targets before implementation.
3. Use `VS-07` only after VS-06 produces checked failure evidence.

Computational results remain `COMPUTATIONAL` unless accompanied by a proof or a complete exhaustiveness argument.
