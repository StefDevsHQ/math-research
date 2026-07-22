# Vertical Slices — Monotone NAE-3SAT

**Purpose:** Authoritative execution order and progress ledger.  
**Updated:** 2026-07-22

Every slice is governed by the [building-block quality gate](BUILDING-BLOCK-GATE.md). A dependent slice may begin only when every prerequisite is `COMPLETE / CHECKED` or stronger.

## Progress summary

| Slice | Name | Status | Current result | Next action |
|---:|---|---|---|---|
| `VS-01` | Canonical instance model | `COMPLETE / CHECKED` | Canonical labelled model, strict parsing, serialization, components, relabelling, and witness verification. | Preserve. |
| `VS-02` | Exact small-instance oracle | `COMPLETE / CHECKED` | Exact decision, least witnesses, listing, counting, factorization, generator, and finite census. | Preserve as ground truth. |
| `VS-03` | Exact extension-profile engine | `COMPLETE / CHECKED` | Exact completion masks, semantic classes, transitions, boundary metrics, and profile census. | Preserve as semantic reference. |
| `VS-04` | Control calibration | `COMPLETE / CHECKED` | Graph parity, affine XOR, incidence forests, bounded boundaries, and disconnected products. | Use as controls only. |
| `VS-05` | Minimal obstruction atlas | `COMPLETE / CHECKED` | `K_5^(3)`, Fano certificates, all-ordering profiles, and dead-quotient theorem. | Preserve as obstruction baseline. |
| `VS-06` | Destroy naive summaries | `COMPLETE / CHECKED` | Ten explicit collisions and a proved fixed-radius locality-failure family; exact boundary assignment retained. | Proceed to VS-07. |
| `VS-07` | Measure semantic merging | `READY` | Exact profiles and collision controls are available. | Separate live merging, symmetry, dead collapse, width, quotient count, and representation size. |
| `VS-08` | Extract first atomic invariant | `BLOCKED` | No representation language selected. | Use checked VS-07 evidence. |
| `VS-09` | Prove restricted theorem | `PARTIAL` | Bounded-boundary and incidence-forest theorems are checked. | Extend only after VS-08. |
| `VS-10` | Attack with hard families | `BLOCKED` | Hard controls are registered. | Attack a checked VS-08 invariant. |
| `VS-11` | Global complexity audit | `BLOCKED` | Audit criteria exist. | Count the complete computation graph of a candidate. |
| `VS-12` | Route decision | `BLOCKED` | Claim discipline is prepared. | Decide after VS-08 through VS-11. |

## Phase I — trusted laboratory (`VS-01` through `VS-05`)

**Status:** `COMPLETE / CHECKED`.

Exports canonical instances, exact finite solving, exact fixed-order completion semantics, tractable controls, and a minimal-obstruction atlas. It exports no universal polynomial algorithm or general lower bound.

Evidence: [phase closeout audit](VS-01-05-PHASE-AUDIT.md).

## VS-06 — Destroy naive summaries

**Exit gate:** satisfied.

### Exact semantic targets

- whole-instance summaries are judged by exact satisfiability;
- prefix summaries are judged by exact completion masks;
- bounded-radius summaries are judged by conditioned residual satisfiability under an explicit anchored encoding.

### Disproved summaries

The committed atlas gives complete same-summary/different-semantics witnesses for:

1. sorted degree sequence;
2. hyperedge-intersection multiset;
3. pair-codegree multiset;
4. parity data;
5. second moments;
6. incidence-Gram characteristic polynomial;
7. root generalized arc consistency;
8. satisfiability of every proper induced vertex subinstance;
9. boundary Hamming weight;
10. boundary Hamming parity.

These are summary-specific disproofs, not a lower bound against arbitrary representations.

### Fixed-radius theorem

For every `r>=1`, the graph unions

- `C_(2r+3) disjoint-union C_(2r+3)`, and
- `C_(2r+2) disjoint-union C_(2r+4)`

have identical multisets of rooted radius-`r` neighbourhoods and opposite bipartiteness. The anchored NAE encoding converts this into opposite conditioned residual satisfiability. This is `NAE-012 — PROVED / CHECKED`.

### Retained control

Processed consistency plus the exact processed-boundary assignment determines the remaining completion set. This recovers the known `2^w` boundary dynamic programme and may still be exponential when the boundary is large.

Evidence: [implementation specification](VS-06-IMPLEMENTATION.md), [completion audit](VS-06-AUDIT.md), executable summary module, deterministic collision atlas, and exact tests.

## VS-07 — Measure genuine semantic merging

Separate and measure:

- raw prefix assignments;
- processed-valid assignments;
- exact boundary assignments;
- complement-symmetry identifications;
- dead-state merging;
- live exact semantic merging;
- quotient count;
- representation bytes;
- ordering dependence.

Exit with reproducible first live merges, first significant growth families, and a precise statement of what is semantic compression versus merely compact syntax.

## VS-08 — Extract first atomic invariant

State one falsifiable representation language with exact semantics, construction, transitions, equality, acceptance, encoded size, proposed total-state bound, controls, adversarial family, and stop condition.

## VS-09 — Prove a restricted theorem

Prove the invariant first on the largest supported exact subclass, including assumptions, boundaries, encoding, runtime, memory, and total generated-state bounds.

## VS-10 — Attack with hard families

Test minimal obstructions, linear 4-regular instances, verified reduction outputs, high-width families, and defined sibling transfers.

## VS-11 — Global complexity audit

Count input and intermediate bit lengths, construction, equality, transitions, branching, complete generated-state graph, duplicate detection, memory, normalization, witness reconstruction, and deterministic correctness.

## VS-12 — Route decision

Record a surviving universal candidate, restricted theorem, complete disproof, representation-specific barrier, or closure. Synchronize claims, evidence, limitations, and reopening conditions.

## Immediate queue

1. Preserve `VS-01` through `VS-06` without expanding completed-slice scope.
2. Execute `VS-07` semantic-merging measurements.
3. Do not activate a representation route before VS-07 identifies an exact mechanism worth formalizing.

Computational results remain `COMPUTATIONAL` unless accompanied by a proof or complete exhaustiveness argument.
