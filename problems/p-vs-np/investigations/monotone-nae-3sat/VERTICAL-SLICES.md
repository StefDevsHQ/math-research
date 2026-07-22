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
| `VS-08` | Exact PCRNF construction | `COMPLETE / CHECKED` | `R1.1 PCRNF` | Retain `NAE-017`. |
| `VS-09A` | Universal PCRNF state bound | `COMPLETE / CHECKED` | `R1.1`, `R6` | Close `NAE-016`; retain restricted PCRNF classes. |
| `VS-09B` | Collective exact representation | `READY / REFORMULATE` | `R1.2`, `R1.4` | Select a representation sharing many distinct residual functions collectively. |
| `VS-10` | Attack with hard families | `BLOCKED` | selected collective subroute plus `R6` | Attack the precise candidate. |
| `VS-11` | Global complexity audit | `BLOCKED` | selected constructive subroute | Count the complete collective representation and all intermediate objects. |
| `VS-12` | Route decision | `BLOCKED` | parent and child route records | Prove, disprove, defer, restrict or close precisely. |

## Trusted laboratory — VS-01 through VS-08

**Status:** `COMPLETE / CHECKED`.

The laboratory includes exact residual syntax and attack records in addition to canonical instances, exact profiles, controls, obstruction evidence, summary collisions and semantic-merging measurements.

## VS-08 result — exact PCRNF

`NAE-017 — PROVED / CHECKED` establishes exact oriented residualization and exact transitions.

`NAE-018 — DISPROVED / CHECKED` establishes that PCRNF byte equality is not complete semantic equality.

These results remain valid.

## VS-09A — all-ordering PCRNF attack

### Semantic projection

`NAE-019` proves that distinct exact completion functions require distinct oriented PCRNF states.

### Every-ordering hard family

For a constant-degree expander graph `G`, form the central lift with hyperedges `{c,u,v}` for every graph edge `{u,v}`.

For every ordering:

1. cut after the first `floor(n/2)` graph vertices;
2. expansion gives linearly many crossing edges;
3. bounded degree gives a linear crossing induced matching;
4. subsets of its processed endpoints define `2^{Omega(n)}` live prefixes;
5. explicit suffix assignments distinguish every pair semantically.

Therefore one level has `2^{Omega(n)}` exact completion classes and at least that many PCRNF states.

### Result

```text
NAE-016 — DISPROVED / CHECKED
NAE-019 — PROVED / CHECKED
NAE-020 — PROVED / CHECKED
```

Proof: [NAE-016 expander disproof](routes/exact-state-representations/pcrnf/proofs/NAE-016-expander-disproof.md).

## VS-09B — reformulated continuation

A stronger equality test cannot solve the expander family by merging states, because its residual functions are already pairwise distinct.

The next representation must encode many distinct residual functions collectively, for example through:

- deterministic decomposable circuits;
- non-ordered decomposition structures;
- algebraic family representations;
- another explicitly defined global object.

## Mandatory controls for the next candidate

- central lifts of constant-degree expanders;
- four-vertex genuine semantic merge;
- five-vertex PCRNF incompleteness witness;
- both fan orderings;
- Fano and `K_5^(3)`;
- linear four-regular instances;
- VS-06 collision pairs;
- verified reduction-generated instances.

## Scope

The disproof is model-specific. It does not prove `P!=NP`, disprove `NAE-006`, or lower-bound arbitrary circuits or algorithms.