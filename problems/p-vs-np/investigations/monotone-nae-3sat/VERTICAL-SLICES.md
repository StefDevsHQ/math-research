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
| `VS-08` | Extract first atomic invariant | `COMPLETE / CHECKED` | Oriented PCRNF is exact; byte equality is semantically incomplete. | Retain `NAE-017`; keep `NAE-016` open. |
| `VS-09` | Prove restricted theorem or strengthen quotient | `PARTIAL / READY` | Bounded-boundary and incidence-forest theorems are checked; exact PCRNF substrate now exists. | Select one continuation and state its theorem before implementation. |
| `VS-10` | Attack with hard families | `BLOCKED` | Hard controls are prepared. | Attack the precise VS-09 candidate. |
| `VS-11` | Global complexity audit | `BLOCKED` | Audit criteria exist. | Count the complete computation graph of the surviving candidate. |
| `VS-12` | Route decision | `BLOCKED` | Claim discipline is prepared. | Prove, disprove, defer or retain after VS-09 through VS-11. |

## Trusted laboratory — VS-01 through VS-08

**Status:** `COMPLETE / CHECKED`.

The laboratory includes exact residual syntax and attack records in addition to canonical instances, exact profiles, controls, obstruction evidence, summary collisions and semantic-merging measurements. It exports no universal polynomial algorithm or general lower bound.

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

The fan family has peak PCRNF state count `2^(k+1)-1` under the bad ordering and at most five under the interleaved ordering. This preserves ordering dependence and yields neither a global polynomial bound nor an every-ordering lower bound.

### NAE-016 status

`NAE-016` is `CONJECTURE / CHECKED`.

The previous `RETRACTED` label confused failure of one proof mechanism with resolution of the quantified conjecture. VS-08 disproved byte equality as a complete semantic quotient, but did not prove that every ordering of some family has superpolynomial PCRNF state growth.

## VS-09 — next continuation

VS-09 must choose one of two exact targets.

### Track A — restricted PCRNF state theorem

State and prove the largest class `C` for which an efficiently constructible ordering gives:

- polynomially many reachable oriented PCRNF states;
- polynomial maximum state size;
- polynomial total encoded state;
- polynomial transition and acceptance.

Candidate parameters include boundary width, incidence treewidth, residual component size and residual interaction width.

### Track B — stronger exact quotient over PCRNF

Define a merge relation or canonical semantic layer that is:

- strictly stronger than PCRNF byte equality;
- exact for labelled completion sets;
- polynomial-time constructible and comparable;
- transition-compatible;
- accompanied by a complete global state bound.

The five-vertex witness is the first mandatory positive merge test.

## VS-10 through VS-12

- `VS-10`: attack the selected VS-09 theorem or quotient using Fano, linear four-regular, high-width and reduction-generated controls.
- `VS-11`: audit input length, construction, equality, transitions, branching, complete state graph and total representation size.
- `VS-12`: classify the route as proved, disproved, deferred, restricted, model-specific or closed.

## Immediate queue

1. Preserve VS-01 through VS-08.
2. Select VS-09 Track A or Track B and write one atomic theorem or conjecture.
3. Do not treat `NAE-018` as a disproof of `NAE-016`.
4. Do not infer tractability from polynomial individual state size or hardness from one bad ordering.

Computational results remain `COMPUTATIONAL` unless accompanied by a proof or complete exhaustiveness argument.
