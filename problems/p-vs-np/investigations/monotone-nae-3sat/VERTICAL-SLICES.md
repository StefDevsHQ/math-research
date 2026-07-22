# Vertical Slices — Monotone NAE-3SAT

**Purpose:** Authoritative execution order and progress ledger.  
**Updated:** 2026-07-23

Every slice is governed by the [building-block quality gate](BUILDING-BLOCK-GATE.md). Route ownership is recorded in the [route registry](routes/README.md).

## Progress summary

| Slice | Name | Status | Route ownership | Next action |
|---:|---|---|---|---|
| `VS-01` | Canonical instance model | `COMPLETE / CHECKED` | Shared laboratory | Preserve. |
| `VS-02` | Exact small-instance oracle | `COMPLETE / CHECKED` | Shared laboratory | Preserve as ground truth. |
| `VS-03` | Exact extension-profile engine | `COMPLETE / CHECKED` | `R1` foundation | Preserve as semantic reference. |
| `VS-04` | Control calibration | `COMPLETE / CHECKED` | `R2`, `R3`, `R5` controls | Preserve. |
| `VS-05` | Minimal obstruction atlas | `COMPLETE / CHECKED` | `R4`, `R6` evidence | Preserve. |
| `VS-06` | Destroy naive summaries | `COMPLETE / CHECKED` | `R4`, `R6` barriers | Preserve as falsification baseline. |
| `VS-07` | Measure semantic merging | `COMPLETE / CHECKED` | `R1`, `R2`, `R6` evidence | Preserve. |
| `VS-08` | Extract first atomic invariant | `COMPLETE / CHECKED` | `R1.1 PCRNF` | Retain `NAE-017`; keep `NAE-016` open. |
| `VS-09` | Prove restricted theorem or strengthen quotient | `PARTIAL / READY` | `R1.1-B`, `R1.2`, `R2.3` | Select one atomic continuation. |
| `VS-10` | Attack with hard families | `BLOCKED` | selected VS-09 subroute plus `R6` | Attack the precise candidate. |
| `VS-11` | Global complexity audit | `BLOCKED` | selected constructive subroute | Count the complete computation graph. |
| `VS-12` | Route decision | `BLOCKED` | parent and child route records | Prove, disprove, defer, restrict or close precisely. |

## Trusted laboratory — VS-01 through VS-08

**Status:** `COMPLETE / CHECKED`.

The laboratory includes exact residual syntax and attack records in addition to canonical instances, exact profiles, controls, obstruction evidence, summary collisions and semantic-merging measurements. It exports no universal polynomial algorithm or general lower bound.

## VS-08 result — R1.1 PCRNF

### Exact retained mechanism

Direct substitution of processed colours yields unary, signed-binary and ternary residual constraints. Deterministic propagation closure preserves exact labelled completion semantics.

Component complement requires an explicit orientation bit. With orientation recorded, restriction and re-closure give exact transitions. This is `NAE-017 — PROVED / CHECKED`.

### Semantic-completeness failure

The five-vertex instance with edges

```text
012,013,023,034,123,124
```

under ordering `(0,4,1,2,3)` has prefixes `00` and `01` with equal exact completion mask `40` but different oriented PCRNFs.

Therefore PCRNF byte equality is not exact completion equivalence. This is `NAE-018 — DISPROVED / CHECKED`.

### State-growth audit

PCRNF equality agrees with exact completion classes for every labelled instance and ordering through four vertices, but the five-vertex witness ends that pattern.

The fan family has peak PCRNF state count `2^(k+1)-1` under the bad ordering and at most five under the interleaved ordering. This yields neither a global polynomial bound nor an every-ordering lower bound.

### NAE-016 status

`NAE-016` remains `CONJECTURE / CHECKED`.

VS-08 disproved byte equality as a complete semantic quotient, but did not disprove the existential polynomial-state claim.

See [`R1.1 — PCRNF`](routes/exact-state-representations/pcrnf/README.md).

## VS-09 — route branches

### Track A — restricted PCRNF state theorem

**Route ownership:** `R1.1-B` and `R2.3`.

State and prove the largest class `C` for which an efficiently constructible ordering gives:

- polynomially many reachable oriented PCRNF states;
- polynomial maximum state size;
- polynomial total encoded state;
- polynomial transition and acceptance.

Candidate parameters include boundary width, incidence treewidth, residual component size and residual interaction width.

### Track B — stronger exact quotient over PCRNF

**Route ownership:** [`R1.2`](routes/exact-state-representations/semantic-quotient/README.md).

Define a merge relation or canonical semantic layer that is:

- strictly stronger than PCRNF byte equality;
- exact for labelled completion sets;
- polynomial-time constructible and comparable;
- transition-compatible;
- accompanied by a complete global state bound.

The five-vertex witness is the first mandatory positive merge test.

Candidate child subroutes already registered under R1 are decision diagrams and decomposable circuits. They are not active until one exact model is selected.

## VS-10 through VS-12

- `VS-10`: attack the selected VS-09 theorem or quotient using Fano, linear four-regular, high-width and reduction-generated controls.
- `VS-11`: audit input length, construction, equality, transitions, branching, complete state graph and total representation size.
- `VS-12`: classify both the child mechanism and its parent route independently.

## Immediate queue

1. Preserve VS-01 through VS-08.
2. Select VS-09 Track A or Track B and write one atomic theorem or conjecture in its route directory.
3. Do not treat a failed child mechanism as closure of its parent route.
4. Do not treat `NAE-018` as a disproof of `NAE-016`.
5. Do not infer tractability from polynomial individual state size or hardness from one bad ordering.

Computational results remain `COMPUTATIONAL` unless accompanied by a proof or complete exhaustiveness argument.