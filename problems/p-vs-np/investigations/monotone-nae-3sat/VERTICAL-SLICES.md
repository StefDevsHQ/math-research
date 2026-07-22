# Vertical Slices — Monotone NAE-3SAT

**Purpose:** Authoritative execution order and progress ledger.  
**Updated:** 2026-07-22

## Status vocabulary

- `COMPLETE` — exit gate and evidence are recorded.
- `PARTIAL` — substantive work exists but the exit gate is not met.
- `READY` — prerequisites exist and execution may begin.
- `BLOCKED` — earlier outputs are required.

## Progress summary

| Slice | Name | Status | Current result | Next action |
|---:|---|---|---|---|
| `VS-01` | Canonical instance model | `COMPLETE` | Strict versioned parser, canonical model, serialization, identifiers, components, relabelling, verifier, CLI, fixtures, tests, and audit are complete. | Preserve the accepted format while building the exact oracle. |
| `VS-02` | Exact small-instance oracle | `READY` | The trusted VS-01 model and witness verifier now exist. | Implement exhaustive satisfiability and declare the first exhaustive labelled domain. |
| `VS-03` | Exact extension-profile engine | `READY` | Completion equivalence and transitions are proved in `NAE-004`; the canonical model exists. | Implement after, or alongside, VS-02 and cross-check final acceptance. |
| `VS-04` | Control calibration | `BLOCKED` | Controls are identified; no shared oracle/profile run exists. | Run VS-02 and VS-03 on tractable controls. |
| `VS-05` | Minimal obstruction atlas | `BLOCKED` | Targets are identified; no exhaustive atlas exists. | Enumerate and verify minimal unsatisfiable instances after VS-02. |
| `VS-06` | Destroy naive summaries | `BLOCKED` | Candidate summaries are listed; no verified collisions exist. | Search the VS-05 corpus using exact profiles. |
| `VS-07` | Measure semantic merging | `BLOCKED` | Exact equivalence is defined; no quotient-growth dataset exists. | Measure raw, boundary, and exact semantic states after VS-03. |
| `VS-08` | Extract first atomic invariant | `BLOCKED` | No representation language is selected. | Use VS-06 and VS-07 failures to define one falsifiable invariant. |
| `VS-09` | Prove restricted theorem | `PARTIAL` | `NAE-005` proves the baseline bounded-boundary algorithm. | Prove the future invariant on an exact subclass. |
| `VS-10` | Attack with hard families | `BLOCKED` | Hard controls are registered; no candidate invariant exists. | Attack the VS-08 invariant. |
| `VS-11` | Global complexity audit | `BLOCKED` | Audit criteria exist; no candidate algorithm exists. | Count the complete computation graph of the VS-08 mechanism. |
| `VS-12` | Route decision | `BLOCKED` | Claim discipline is prepared. | Classify the route after VS-08 through VS-11. |

## `VS-01` evidence

- mathematical object: [OBJECT.md](OBJECT.md);
- accepted specification: [VS-01-IMPLEMENTATION.md](VS-01-IMPLEMENTATION.md);
- completion audit: [VS-01-AUDIT.md](VS-01-AUDIT.md);
- executable package: `tools/monotone-nae-3sat/`.

The slice is complete only as infrastructure. It makes no claim about the satisfiability of arbitrary instances.

## Remaining slices

### `VS-02` — Exact small-instance oracle

Enumerate binary colourings, exploit only proved component/complement symmetry, return and independently verify witnesses, define the generated labelled domain precisely, and record an exhaustiveness argument. Exit when the first complete domain is reproducibly evaluated.

### `VS-03` — Exact extension-profile engine

For every ordering and prefix assignment, compute the exact set of satisfying completions, quotient equal completion sets, construct both colour transitions, and verify final acceptance against VS-02. Exit when transition well-definedness and oracle agreement are checked.

### `VS-04` — Control calibration

Run the shared laboratory on bipartiteness, acyclic and bounded-width systems, meaningful XOR analogues, disconnected unions, and known planar or low-occurrence NAE controls. Explain the actual source of tractability in each case.

### `VS-05` — Minimal obstruction atlas

Enumerate unsatisfiable instances in a declared domain, verify edge-minimality and separately named vertex-minimality, include the Fano plane, and record complete structural and profile evidence.

### `VS-06` — Destroy naive summaries

Find complete pairs with equal degree, intersection, pair-co-occurrence, affine, local-consistency, bounded-radius, spectral, or low-moment summaries but different satisfiability or completion behaviour.

### `VS-07` — Measure semantic merging

Separate raw assignments, boundary states, dead-state merging, complement symmetry, live semantic merging, quotient count, and representation size across orderings.

### `VS-08` — Extract first atomic invariant

State one exact representation language with semantics, construction, transitions, correctness target, proposed total-state bound, controls, adversarial family, and stop condition.

### `VS-09` — Prove restricted theorem

Prove the invariant first on the largest supported exact subclass, including all quantifiers, boundary cases, encoding, runtime, memory, and total-state bounds. Then independently attack the proof.

### `VS-10` — Attack with hard families

Test the candidate against minimal obstructions, linear 4-regular instances, verified reduction outputs, high-width families, and defined sibling transfers.

### `VS-11` — Global complexity audit

Count input and intermediate bit lengths, construction, equivalence, transitions, branching, duplicate detection, the complete generated-state graph, memory, normalization, witness reconstruction, uniformity, and deterministic correctness.

### `VS-12` — Route decision

Record a universal surviving candidate, restricted theorem, disproof, representation-specific barrier, or closure. Synchronize claims, evidence, limitations, and reopening conditions.

## Immediate queue

1. Execute `VS-02` using the completed canonical model.
2. Implement `VS-03` and cross-check it against the oracle.
3. Run controls and construct the minimal obstruction atlas before proposing an invariant.

Computational results remain `COMPUTATIONAL` unless accompanied by a complete exhaustiveness argument or proof.
