# Vertical Slices — Monotone NAE-3SAT

**Purpose:** Operational execution order and progress ledger for the Monotone NAE-3SAT attack programme.  
**Updated:** 2026-07-22

## Status vocabulary

- `COMPLETE` — the slice exit gate is satisfied and its evidence is recorded.
- `PARTIAL` — a theorem, specification, or implementation component exists, but the exit gate is not yet satisfied.
- `READY` — prerequisites are available and execution may begin.
- `BLOCKED` — execution depends on outputs from earlier slices.
- `NOT STARTED` — no substantive work has been recorded.

## Progress summary

| Slice | Name | Status | Current result | Next action |
|---:|---|---|---|---|
| `VS-01` | Canonical instance model | `PARTIAL` | Mathematical model and a reviewed implementation specification are complete. The specification fixes explicit labelled encoding, strict versioned JSON, invariants, APIs, fixtures, tests, CLI, complexity obligations, and exit gates. | Implement and test the package described in [VS-01-IMPLEMENTATION.md](VS-01-IMPLEMENTATION.md). |
| `VS-02` | Exact small-instance oracle | `READY` | Exhaustive-colouring decision method is defined conceptually; no executable oracle or exhaustively justified corpus is recorded. | Implement brute-force satisfiability and witness verification after the VS-01 model exists. |
| `VS-03` | Exact extension-profile engine | `READY` | Exact completion sets, equivalence classes, and well-defined transitions are formalized and proved in `NAE-004`. | Implement quotient construction after the VS-01 model and cross-check against `VS-02`. |
| `VS-04` | Control calibration | `BLOCKED` | Required controls are identified; bounded-boundary correctness is proved in `NAE-005`. No shared empirical run exists. | Run the oracle and profile engine on bipartite, XOR, acyclic, bounded-width, and disconnected controls. |
| `VS-05` | Minimal obstruction atlas | `BLOCKED` | Fano plane and minimally unsatisfiable instances are selected as targets. No exhaustive atlas exists. | Enumerate unsatisfiable instances and verify minimality by edge deletion. |
| `VS-06` | Destroy naive summaries | `BLOCKED` | Candidate summaries are listed, but no verified same-summary/different-future collision has been recorded. | Search the corpus for collisions in degree, intersection, parity, local-consistency, and bounded-radius summaries. |
| `VS-07` | Measure semantic merging | `BLOCKED` | Exact equivalence is defined; no measured quotient-growth or nontrivial merge dataset exists. | Compare raw prefix assignments, boundary states, complement pairs, and exact future classes across orderings. |
| `VS-08` | Extract first atomic invariant | `BLOCKED` | No representation language or atomic compatibility relation is selected. | Use the first failures from `VS-06` and `VS-07` to define one falsifiable invariant. |
| `VS-09` | Prove restricted theorem | `PARTIAL` | The bounded-boundary theorem `NAE-005` is proved. This is a baseline restricted theorem, not a theorem about a new invariant. | Prove the first new invariant on the largest exact subclass supported by evidence. |
| `VS-10` | Attack with hard families | `BLOCKED` | Linear 4-regular and reduction-generated families are mandatory controls; no candidate invariant exists to attack. | Apply the `VS-08` invariant to verified hard families. |
| `VS-11` | Global complexity audit | `BLOCKED` | Audit requirements are specified. No candidate algorithm exists whose total computation graph can be counted. | Audit construction, equivalence, transitions, branching, memory, and total encoded state. |
| `VS-12` | Route decision | `BLOCKED` | Investigation state and claim discipline are prepared; no route mechanism has reached a decision gate. | Classify the first mechanism after `VS-08` through `VS-11`. |

## Ordered slices

### `VS-01` — Canonical instance model

**Goal:** Establish one executable representation used by every proof and experiment.

**Work:**

- represent a simple 3-uniform hypergraph on explicitly listed indexed vertices;
- validate pairwise distinct vertices in every edge;
- sort and deduplicate edges;
- preserve isolated vertices in canonical identity and provide a separate active-core operation;
- split incidence-connected components;
- provide deterministic, versioned canonical serialization;
- verify a proposed two-colouring;
- record canonical encoded length and stable identifiers.

**Exit gate:** Parser, normalizer, serializer, relabelling operations, component decomposition, and witness verifier agree on the complete required test suite and reproducible CLI run.

**Evidence:**

- mathematical model: `OBJECT.md`;
- reviewed executable specification: [VS-01-IMPLEMENTATION.md](VS-01-IMPLEMENTATION.md).

### `VS-02` — Exact small-instance oracle

**Goal:** Create a trusted exact decision oracle for finite discovery experiments.

**Work:**

- enumerate colourings, fixing one colour per connected component to remove global complement duplication;
- return satisfiable/unsatisfiable and a witness when one exists;
- independently recheck every returned witness;
- generate instances under an explicitly stated labelled or isomorphism-reduced domain;
- record the exhaustiveness argument for every claimed finite domain.

**Exit gate:** The oracle is cross-checked against hand-certified examples and exhaustively evaluates the first declared domain with reproducible commands and counts.

### `VS-03` — Exact extension-profile engine

**Goal:** Compute the exact semantic state against which every proposed compression is judged.

For ordering \(\pi=(v_1,\ldots,v_n)\), compute

\[
\operatorname{Ext}_{I,i}(a)=\{c:R_i\to\{0,1\}:a\cup c\models I\}
\]

and quotient prefix assignments by equal completion sets.

**Work:**

- enumerate prefix assignments and completion bitsets;
- canonicalize exact future-equivalence classes;
- construct both colour transitions;
- mark the dead class explicitly;
- verify final acceptance against the oracle;
- record raw assignment count, boundary-state count, quotient count, and encoded profile size.

**Exit gate:** Every tested instance and ordering has a transition graph whose final acceptance equals `VS-02`, and transition well-definedness is checked computationally.

**Proof already available:** `NAE-004` in `OBJECT.md`.

### `VS-04` — Control calibration

**Goal:** Verify that the laboratory explains known easy cases before examining hard instances.

**Controls:** graph bipartiteness, acyclic incidence hypergraphs, bounded-boundary instances, meaningful XOR analogues, disconnected unions, and planar or occurrence-at-most-three NAE instances.

**Exit gate:** A report states why each control is easy, what exact state the engine observes, and whether compactness comes from small interfaces, algebraic closure, decomposition, or component factorization.

### `VS-05` — Minimal obstruction atlas

**Goal:** Identify the smallest exact failures of global compatibility.

**Work:** enumerate unsatisfiable instances in the declared domain; test edge-minimality and separately named vertex-minimality; independently verify the Fano plane; record structural and extension-profile data; separate disconnected copies from connected cores.

**Exit gate:** Every object called minimal has all relevant proper subinstances verified satisfiable, with complete instance data and reproducible verification.

### `VS-06` — Destroy naive summaries

**Goal:** Eliminate insufficient invariants with complete collisions.

**Summaries:** degree sequence, edge-intersection multiset, pair co-occurrence data, parity and affine summaries, local-consistency closure, bounded-radius incidence neighbourhoods, component counts, elementary spectral data, and fixed-order low-moment completion statistics.

**Required disproof:** Two complete instances or partial states with the same proposed summary but different satisfiability or exact completion sets.

**Exit gate:** Each rejected summary has a smallest known verified collision and a statement of remaining scope.

### `VS-07` — Measure genuine semantic merging

**Goal:** Determine what exact compression exists beyond trivial symmetry.

**Work:** compare raw prefix assignments, boundary colourings, and exact future classes; separate dead and live merging; quotient complement symmetry explicitly; optimize over small orderings; measure maximum and total quotient size; distinguish class count from representation size.

**Exit gate:** A reproducible dataset identifies the first nontrivial live semantic merge and the first family showing significant quotient growth.

### `VS-08` — Extract the first atomic invariant

**Goal:** Turn empirical failure structure into one precise mathematical mechanism.

**Required artifact:** One conjecture specifying representation language, semantics, construction and transitions, correctness target, predicted total-state bound, controls, first adversarial family, and stop condition.

**Exit gate:** The conjecture is falsifiable and does not hide satisfiability, equivalence, or transition computation inside an undefined operation.

### `VS-09` — Prove a restricted theorem first

**Goal:** Establish correctness before claiming universality.

**Work:** Prove the invariant on the largest exact subclass supported by evidence, including quantifiers, boundaries, encoding, runtime, memory, and total-state bounds.

**Existing baseline:** `NAE-005` proves the ordinary bounded-boundary dynamic programme. It does not validate a future stronger invariant.

**Exit gate:** A complete `PROVED / DRAFT` theorem for the new invariant, followed by an independent proof attack.

### `VS-10` — Attack with hard families

**Goal:** Test whether the candidate survives genuine hardness.

**Families:** Fano-derived and minimal obstructions, linear 4-regular Monotone NAE-3SAT, verified NP-hard reduction outputs, high-width instances, and defined transfers to Positive 1-in-3 SAT or graph 3-colouring.

**Exit gate:** Produce a complete counterexample, a sharply restricted surviving theorem, or a candidate that survives all recorded attacks.

### `VS-11` — Global complexity audit

**Goal:** Prevent local polynomial reasoning from hiding exponential total work.

**Audit:** input and intermediate bit lengths; construction cost; equivalence and transition cost; recursion depth and branching; complete generated-state graph; duplicate-state detection; memory; representation normalization; witness reconstruction; uniformity; deterministic correctness.

**Exit gate:** A complete polynomial bound or an explicit superpolynomial obstruction for the named algorithm and representation.

### `VS-12` — Route decision

**Goal:** Record the exact mathematical outcome.

**Possible decisions:** universal candidate survives; restricted theorem; conjecture disproved; representation-specific barrier; or no material mechanism.

**Exit gate:** Claim ledger, status, route record, evidence, limitations, and reopening conditions are synchronized.

## Immediate execution queue

1. Implement and close `VS-01` against [VS-01-IMPLEMENTATION.md](VS-01-IMPLEMENTATION.md).
2. Execute `VS-02` on the first exhaustively justified domain.
3. Implement `VS-03` and cross-check it against the oracle.
4. Run `VS-04` and `VS-05` before designing a new invariant.
5. Use `VS-06` and `VS-07` to extract the first atomic route candidate in `VS-08`.

## Progress discipline

A slice advances to `COMPLETE` only when its exit gate and evidence path are recorded. Computational results remain `COMPUTATIONAL`; they do not promote a universal statement without an exhaustiveness argument or proof.
