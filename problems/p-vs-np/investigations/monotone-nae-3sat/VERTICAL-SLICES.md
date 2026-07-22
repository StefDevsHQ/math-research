# Vertical Slices — Monotone NAE-3SAT

**Purpose:** Authoritative execution order and progress ledger for the Monotone NAE-3SAT attack programme.  
**Updated:** 2026-07-22

Every slice is governed by the mandatory [building-block quality gate](BUILDING-BLOCK-GATE.md). A dependent slice may begin only when each prerequisite is `COMPLETE / CHECKED` or stronger.

## Status vocabulary

- `COMPLETE / CHECKED` — exit gate, reproducible evidence, independent attack, and required automation are complete.
- `COMPLETE / DRAFT` — the exit gate appears satisfied, but independent attack or automation remains.
- `PARTIAL` — substantive work exists, but the exit gate is not met.
- `READY` — checked prerequisites exist and execution may begin.
- `BLOCKED` — earlier checked outputs are required.
- `NOT STARTED` — no substantive work is recorded.

## Progress summary

| Slice | Name | Status | Current result | Next action |
|---:|---|---|---|---|
| `VS-01` | Canonical instance model | `COMPLETE / CHECKED` | Canonical model, parser, serialization, identifiers, components, relabelling, verifier, exhaustive small-domain tests, cross-version automation, and audit are green. | Freeze the exported contract while building VS-02. |
| `VS-02` | Exact small-instance oracle | `READY` | VS-01 is a checked dependency. No exact oracle or exhaustively justified satisfiability corpus exists. | Specify, implement, attack, and quality-gate the oracle. |
| `VS-03` | Exact extension-profile engine | `READY` | Completion equivalence and transitions are proved in `NAE-004`; implementation remains. | Implement, but do not consume unpromoted VS-02 outputs. |
| `VS-04` | Control calibration | `BLOCKED` | Controls are identified; no checked oracle/profile run exists. | Run checked VS-02 and VS-03 on tractable controls. |
| `VS-05` | Minimal obstruction atlas | `BLOCKED` | Targets are identified; no checked exhaustive atlas exists. | Enumerate and verify minimal unsatisfiable instances after VS-02. |
| `VS-06` | Destroy naive summaries | `BLOCKED` | Candidate summaries are listed; no checked collisions exist. | Search the checked corpus using exact profiles. |
| `VS-07` | Measure semantic merging | `BLOCKED` | Exact equivalence is defined; no checked quotient-growth dataset exists. | Measure states after VS-03 is checked. |
| `VS-08` | Extract first atomic invariant | `BLOCKED` | No representation language is selected. | Use checked VS-06 and VS-07 evidence. |
| `VS-09` | Prove restricted theorem | `PARTIAL` | `NAE-005` proves only the baseline bounded-boundary algorithm. | Prove the future invariant on an exact subclass. |
| `VS-10` | Attack with hard families | `BLOCKED` | Hard controls are registered; no candidate invariant exists. | Attack the checked VS-08 invariant. |
| `VS-11` | Global complexity audit | `BLOCKED` | Audit criteria exist; no candidate algorithm exists. | Count the complete computation graph of the VS-08 mechanism. |
| `VS-12` | Route decision | `BLOCKED` | Claim discipline is prepared. | Classify the route after VS-08 through VS-11. |

## `VS-01` — Canonical instance model

**Goal:** Establish one executable representation used by every later proof check and experiment.

**Completed work:** canonical immutable labelled hypergraphs; strict versioned parsing; deterministic serialization and identifiers; isolated-vertex preservation; components; induced and active-core relabelling; strict total-colouring verification; CLI; fixtures; complexity audit.

**Quality evidence:**

- [mathematical object](OBJECT.md);
- [implementation specification](VS-01-IMPLEMENTATION.md);
- [completion and quality audit](VS-01-AUDIT.md);
- executable package under `tools/monotone-nae-3sat/`;
- all 1,045 labelled 3-uniform hypergraphs through five vertices;
- 33,047 colouring checks;
- 33,047 induced-subinstance checks;
- a separate 1,350-instance seeded reference cross-check;
- four hash-seed process checks;
- Python 3.11, 3.12, and 3.13 automation.

**Exit gate:** Satisfied. The slice exports infrastructure only and makes no satisfiability claim.

## `VS-02` — Exact small-instance oracle

**Goal:** Create a trusted exact decision oracle for finite discovery experiments.

**Work:**

- define the exact API and witness semantics;
- enumerate binary colourings;
- prove component and complement-symmetry optimizations before use;
- return satisfiable/unsatisfiable and a witness when one exists;
- independently recheck every returned witness;
- define the generated labelled or isomorphism-reduced domain;
- record an exhaustiveness argument, commands, counts, runtime, memory, and limitations;
- add exhaustive, adversarial, independent-reference, and cross-version tests.

**Exit gate:** The oracle agrees with independently certified controls, exhaustively evaluates the first declared domain with reproducible counts, passes the building-block gate, and is `COMPLETE / CHECKED` before any downstream result relies on it.

## `VS-03` — Exact extension-profile engine

**Goal:** Compute the exact semantic state against which every proposed compression is judged.

For ordering \(\pi=(v_1,\ldots,v_n)\), compute

\[
\operatorname{Ext}_{I,i}(a)=\{c:R_i\to\{0,1\}:a\cup c\models I\}
\]

and quotient prefix assignments by equal completion sets.

**Work:** enumerate prefix assignments and completion bitsets; canonicalize exact future classes; construct both colour transitions; mark the dead class; verify final acceptance against checked VS-02; record raw, boundary, quotient, and encoded-profile sizes.

**Exit gate:** Every tested instance and ordering agrees with checked VS-02, transition well-definedness is checked, representation sizes are recorded, and the building-block gate passes.

## `VS-04` — Control calibration

**Goal:** Verify that the laboratory explains known easy cases before examining hard instances.

**Controls:** graph bipartiteness; acyclic incidence hypergraphs; bounded-boundary instances; meaningful XOR-SAT analogues; disconnected unions; planar and occurrence-at-most-three NAE instances.

**Exit gate:** A checked report identifies why each control is easy and whether compactness comes from interfaces, algebra, decomposition, or component factorization.

## `VS-05` — Minimal obstruction atlas

**Goal:** Identify the smallest exact failures of global compatibility.

**Work:** enumerate unsatisfiable instances in a declared domain; test edge-minimality and separately named vertex-minimality; include and independently verify the Fano plane; record degree, linearity, incidence cycles, automorphisms, and profiles; separate disconnected copies from connected cores.

**Exit gate:** Every object called minimal has all relevant proper subinstances checked satisfiable, complete instance data, reproducible verification, and a passed building-block gate.

## `VS-06` — Destroy naive summaries

**Goal:** Eliminate insufficient invariants with complete collisions.

**Summaries:** degree sequence; edge-intersection multiset; pair co-occurrence; parity and affine summaries; local consistency; bounded-radius incidence neighbourhoods; component and elementary spectral data; fixed-order low-moment completion statistics.

**Exit gate:** Each rejected summary has a complete checked collision, a smallest-known statement, remaining scope, and a passed building-block gate.

## `VS-07` — Measure genuine semantic merging

**Goal:** Determine exact compression beyond trivial symmetry.

**Work:** compare raw prefix assignments, boundary colourings, and exact future classes; separate dead and live merging; quotient complement symmetry; optimize over small orders; measure maximum and total quotient size; distinguish class count from representation size.

**Exit gate:** A checked reproducible dataset identifies the first nontrivial live semantic merge and the first significant quotient-growth family.

## `VS-08` — Extract the first atomic invariant

**Goal:** Turn empirical failure structure into one precise mechanism.

**Required artifact:** one conjecture specifying representation language and semantics; construction and transitions; correctness target; predicted total-state bound; controls; first adversarial family; stop condition.

**Exit gate:** The conjecture is falsifiable, hides no satisfiability/equivalence operation, and passes the building-block specification gate.

## `VS-09` — Prove a restricted theorem first

**Goal:** Establish correctness before universality.

**Work:** Prove the invariant on the largest exact subclass supported by evidence, including quantifiers, boundary cases, encoding, runtime, memory, and total-state bounds.

**Existing baseline:** `NAE-005` proves the ordinary bounded-boundary algorithm only.

**Exit gate:** A complete `PROVED / DRAFT` theorem, independent proof attack, dependency audit, and building-block promotion.

## `VS-10` — Attack with hard families

**Goal:** Test genuine hardness rather than curated examples.

**Families:** Fano-derived and minimal obstructions; linear 4-regular Monotone NAE-3SAT; verified NP-hard reduction outputs; high-width instances; defined Positive 1-in-3 SAT or graph 3-colouring transfers.

**Exit gate:** Produce a checked counterexample, sharply restricted surviving theorem, or candidate surviving all recorded attacks.

## `VS-11` — Global complexity audit

**Goal:** Prevent local polynomial reasoning from hiding exponential total work.

**Audit:** input and intermediate bit lengths; construction; equivalence and transitions; recursion depth and branching; complete generated-state graph; duplicate detection; memory; normalization; witness reconstruction; uniformity; deterministic correctness.

**Exit gate:** A checked complete polynomial bound or explicit superpolynomial obstruction for the named algorithm and representation.

## `VS-12` — Route decision

**Goal:** Record the exact mathematical outcome.

**Possible decisions:** universal candidate survives; restricted theorem; complete disproof; representation-specific barrier without inferring `P!=NP`; no material mechanism and return to route selection.

**Exit gate:** Claim ledger, status, route record, evidence, dependency quality, limitations, and reopening conditions are synchronized.

## Immediate queue

1. Execute VS-02 using the frozen checked VS-01 contract.
2. Promote VS-02 only after its own complete quality gate.
3. Implement and cross-check VS-03 against checked VS-02.
4. Run VS-04 and VS-05 before designing a new invariant.
5. Use checked VS-06 and VS-07 evidence to extract VS-08.

Computational results remain `COMPUTATIONAL` unless accompanied by a complete exhaustiveness argument or proof.
