# Vertical Slices — Monotone NAE-3SAT

**Purpose:** Authoritative execution order and progress ledger.  
**Updated:** 2026-07-22

Every slice is governed by the mandatory [building-block quality gate](BUILDING-BLOCK-GATE.md). A dependent slice may begin only when every prerequisite is `COMPLETE / CHECKED` or stronger.

## Progress summary

| Slice | Name | Status | Current result | Next action |
|---:|---|---|---|---|
| `VS-01` | Canonical instance model | `COMPLETE / CHECKED` | Canonical model, parser, serialization, components, relabelling, verifier, exhaustive tests, and cross-version automation are green. | Preserve the exported contract. |
| `VS-02` | Exact small-instance oracle | `COMPLETE / CHECKED` | Exact decision, least witnesses, listing, counting, factorization, generator, Fano control, and deterministic 1045-instance census are checked. | Preserve as finite ground truth for VS-03. |
| `VS-03` | Exact extension-profile engine | `READY` | Exact equivalence and transition theorem `NAE-004` are proved; trusted VS-02 ground truth now exists. | Implement and quality-gate exact profiles. |
| `VS-04` | Control calibration | `BLOCKED` | Controls are identified. | Run after VS-03 is checked. |
| `VS-05` | Minimal obstruction atlas | `BLOCKED` | VS-02 provides exact decision and Fano verification; profile evidence remains unavailable. | Build after VS-03. |
| `VS-06` | Destroy naive summaries | `BLOCKED` | Candidate summaries are listed. | Search checked obstruction/profile data. |
| `VS-07` | Measure semantic merging | `BLOCKED` | Exact equivalence is defined. | Measure after VS-03. |
| `VS-08` | Extract first atomic invariant | `BLOCKED` | No representation language is selected. | Use checked VS-06 and VS-07 evidence. |
| `VS-09` | Prove restricted theorem | `PARTIAL` | `NAE-005` proves only the baseline bounded-boundary algorithm. | Prove a future invariant on an exact subclass. |
| `VS-10` | Attack with hard families | `BLOCKED` | Hard controls are registered. | Attack a checked VS-08 invariant. |
| `VS-11` | Global complexity audit | `BLOCKED` | Audit criteria exist. | Count the complete computation graph of a candidate mechanism. |
| `VS-12` | Route decision | `BLOCKED` | Claim discipline is prepared. | Classify the route after VS-08 through VS-11. |

## VS-01 — Canonical instance model

**Exit gate:** satisfied.

Evidence: [specification](VS-01-IMPLEMENTATION.md), [audit](VS-01-AUDIT.md), executable package, exhaustive labelled-domain checks through five vertices, independent sampled checks, determinism checks, and Python 3.11–3.13 automation.

## VS-02 — Exact small-instance oracle

**Exit gate:** satisfied.

Exports:

- exact satisfiability decision;
- true lexicographically least witness;
- complete satisfying-assignment listing;
- exact direct and factorized counting;
- edge-minimal-unsatisfiability testing;
- canonical labelled generation;
- deterministic finite census and CLI commands.

Checked results:

- complete domain `H_{<=5}` has `1045` labelled instances;
- `1044` are satisfiable;
- the unique unsatisfiable five-vertex instance is the complete 3-uniform hypergraph on five vertices;
- `33047` complete colourings were evaluated by the reference census;
- the Fano plane is unsatisfiable and edge-minimal unsatisfiable.

Evidence: [specification](VS-02-IMPLEMENTATION.md), [audit](VS-02-AUDIT.md), committed corpus, exhaustive production/reference tests, CLI reproduction, and Python 3.11–3.13 automation.

These are finite exact computations and proved oracle mechanisms, not a polynomial-time result.

## VS-03 — Exact extension-profile engine

**Goal:** compute the exact semantic state against which every proposed compression is judged.

For ordering `pi=(v1,...,vn)`, compute each prefix assignment's exact set of satisfying completions, quotient only equal completion sets, and construct both next-colour transitions.

**Exit gate:** every tested instance and ordering agrees with checked VS-02 final acceptance; transition well-definedness is verified; raw, boundary, quotient, and encoded-profile sizes are recorded; exhaustive and adversarial tests, complexity audit, cross-version automation, independent attack, and synchronized records are complete.

## VS-04 — Control calibration

Run checked VS-02 and VS-03 on bipartiteness, acyclic and bounded-width systems, meaningful XOR analogues, disconnected unions, and known planar or low-occurrence controls. Explain the source of tractability. Exit only with reproducible checked reports.

## VS-05 — Minimal obstruction atlas

Enumerate unsatisfiable instances in declared domains; verify edge-minimality and separately named vertex-minimality; include the Fano plane; record complete structural and profile evidence. Every object called minimal must have all relevant proper subinstances checked.

## VS-06 — Destroy naive summaries

For each proposed summary, produce a complete same-summary/different-semantics collision or retain its exact unresolved scope. Degree, intersection, pair co-occurrence, parity, local consistency, bounded-radius, spectral, and low-moment summaries are mandatory targets.

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

1. Implement and quality-gate VS-03 using checked VS-02 ground truth.
2. Run VS-04 and VS-05 only after VS-03 promotion.
3. Use VS-06 and VS-07 evidence before proposing VS-08.

Computational results remain `COMPUTATIONAL` unless accompanied by a proof or a complete exhaustiveness argument.
