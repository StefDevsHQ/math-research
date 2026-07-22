# Vertical Slices — Monotone NAE-3SAT

**Purpose:** Authoritative execution order and progress ledger.  
**Updated:** 2026-07-23

Every slice is governed by the [building-block quality gate](BUILDING-BLOCK-GATE.md).

## Progress summary

| Slice | Name | Status | Current result | Next action |
|---:|---|---|---|---|
| `VS-01` | Canonical instance model | `COMPLETE / CHECKED` | Canonical labelled representation and strict verification. | Preserve. |
| `VS-02` | Exact small-instance oracle | `COMPLETE / CHECKED` | Exact decision, counting, witnesses and finite census. | Preserve as ground truth. |
| `VS-03` | Exact extension-profile engine | `COMPLETE / CHECKED` | Exact completion masks, quotient classes and transitions. | Preserve as semantic reference. |
| `VS-04` | Control calibration | `COMPLETE / CHECKED` | Graph parity, XOR, incidence forests and bounded boundaries. | Preserve as controls. |
| `VS-05` | Minimal obstruction atlas | `COMPLETE / CHECKED` | `K_5^(3)`, Fano and dead-quotient results. | Preserve. |
| `VS-06` | Destroy naive summaries | `COMPLETE / CHECKED` | Ten explicit collisions and fixed-radius locality failure. | Preserve as falsification baseline. |
| `VS-07` | Measure semantic merging | `COMPLETE / CHECKED` | Genuine all-live merging and fan ordering separation. | Preserve. |
| `VS-08` | Extract first atomic invariant | `COMPLETE / CHECKED` | Oriented PCRNF is exact, but byte equality is semantically incomplete; universal route retracted. | Close unless a stronger exact merge rule appears. |
| `VS-09` | Prove restricted theorem | `PARTIAL` | Bounded-boundary and incidence-forest theorems remain checked. | No extension selected. |
| `VS-10` | Attack with hard families | `BLOCKED` | No surviving universal representation candidate. | Await a materially new mechanism. |
| `VS-11` | Global complexity audit | `BLOCKED` | No surviving candidate computation graph. | Await a new route. |
| `VS-12` | Route decision | `BLOCKED` | PCRNF route already closed locally. | Select or design a sibling route. |

## Trusted laboratory — VS-01 through VS-08

**Status:** `COMPLETE / CHECKED`.

The laboratory now includes exact residual syntax and attack records in addition to canonical instances, exact profiles, controls, obstruction evidence, summary collisions and semantic-merging measurements. It exports no universal polynomial algorithm or general lower bound.

## VS-08 result

### Exact retained mechanism

Direct substitution of processed colours yields unary, signed-binary and ternary residual constraints. Deterministic propagation closure preserves exact labelled completion semantics.

Component complement requires an explicit orientation bit. Without it, prefixes `00` and `11` on one NAE edge collapse syntactically while retaining different exact completion masks.

With orientation recorded, restriction and re-closure give exact transitions. This is `NAE-017 — PROVED / CHECKED`.

### Semantic-completeness failure

A five-vertex instance with edges

```text
012,013,023,034,123,124
```

under ordering `(0,4,1,2,3)` has prefixes `00` and `01` with equal exact completion mask `40` but different oriented PCRNFs.

Therefore byte equality of oriented PCRNF is not exact completion equivalence. This is `NAE-018 — DISPROVED / CHECKED`.

### State-growth audit

PCRNF equality agrees with exact completion classes for every labelled instance and ordering through four vertices, but the five-vertex witness ends that pattern.

The fan family has peak PCRNF state count `2^(k+1)-1` under the bad ordering and at most five under the interleaved ordering. This preserves ordering dependence and yields no global polynomial bound.

### Route decision

`NAE-016` is `RETRACTED / CHECKED`.

It is not disproved: the attacks do not show exponential PCRNF growth for every ordering of a family. The candidate is closed because no stronger polynomial-time exact merge rule or polynomial total-state theorem survived.

Evidence: [VS-08 preparation](VS-08-PREPARATION.md), [VS-08 completion audit](VS-08-AUDIT.md), executable PCRNF modules, deterministic attack record and independent tests.

## Immediate queue

1. Preserve VS-01 through VS-08.
2. Do not reopen PCRNF without a new exact merge mechanism and a global polynomial state bound.
3. Select another representation route or another P-versus-NP investigation before activating VS-09 through VS-12.

Computational results remain `COMPUTATIONAL` unless accompanied by a proof or complete exhaustiveness argument.
