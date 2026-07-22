# Vertical Slices — Monotone NAE-3SAT

**Purpose:** Authoritative execution order and progress ledger for the Monotone NAE-3SAT attack programme.  
**Updated:** 2026-07-22

## Status vocabulary

- `COMPLETE` — the exit gate and evidence are recorded.
- `PARTIAL` — substantive work exists, but the exit gate is not met.
- `READY` — prerequisites exist and execution may begin.
- `BLOCKED` — earlier outputs are required.
- `NOT STARTED` — no substantive work is recorded.

## Progress summary

| Slice | Name | Status | Current result | Next action |
|---:|---|---|---|---|
| `VS-01` | Canonical instance model | `COMPLETE` | Strict versioned parser, canonical model, serialization, identifiers, components, relabelling, verifier, CLI, fixtures, tests, and checked audit are complete. | Preserve the accepted format while building the exact oracle. |
| `VS-02` | Exact small-instance oracle | `READY` | The trusted VS-01 model and witness verifier exist. No exhaustively justified corpus is recorded. | Implement exhaustive satisfiability and declare the first complete labelled domain. |
| `VS-03` | Exact extension-profile engine | `READY` | Completion equivalence and transitions are proved in `NAE-004`; implementation remains. | Implement after or alongside VS-02 and cross-check final acceptance. |
| `VS-04` | Control calibration | `BLOCKED` | Controls are identified; no shared oracle/profile run exists. | Run VS-02 and VS-03 on tractable controls. |
| `VS-05` | Minimal obstruction atlas | `BLOCKED` | Targets are identified; no exhaustive atlas exists. | Enumerate and verify minimal unsatisfiable instances after VS-02. |
| `VS-06` | Destroy naive summaries | `BLOCKED` | Candidate summaries are listed; no verified collisions exist. | Search the VS-05 corpus using exact profiles. |
| `VS-07` | Measure semantic merging | `BLOCKED` | Exact equivalence is defined; no quotient-growth dataset exists. | Measure raw, boundary, and exact semantic states after VS-03. |
| `VS-08` | Extract first atomic invariant | `BLOCKED` | No representation language is selected. | Use VS-06 and VS-07 failures to define one falsifiable invariant. |
| `VS-09` | Prove restricted theorem | `PARTIAL` | `NAE-005` proves the baseline bounded-boundary algorithm only. | Prove the future invariant on an exact subclass. |
| `VS-10` | Attack with hard families | `BLOCKED` | Hard controls are registered; no candidate invariant exists. | Attack the VS-08 invariant. |
| `VS-11` | Global complexity audit | `BLOCKED` | Audit criteria exist; no candidate algorithm exists. | Count the complete computation graph of the VS-08 mechanism. |
| `VS-12` | Route decision | `BLOCKED` | Claim discipline is prepared. | Classify the route after VS-08 through VS-11. |

## `VS-01` — Canonical instance model

**Goal:** Establish one executable representation used by every later proof check and experiment.

**Completed work:**

- represent a labelled simple 3-uniform hypergraph on explicitly listed vertices;
- enforce canonical immutable invariants;
- normalize unsorted and duplicate input edges;
- preserve isolated vertices in canonical identity;
- provide a separate active-core operation;
- compute incidence-connected components;
- produce deterministic versioned JSON and stable labelled identifiers;
- relabel induced subinstances with explicit maps;
- validate and check proposed two-colourings;
- provide fixed fixtures, a CLI, and reproducible tests;
- audit complete encoded-size and runtime accounting.

**Evidence:**

- [mathematical object](OBJECT.md);
- [implementation specification](VS-01-IMPLEMENTATION.md);
- [completion audit](VS-01-AUDIT.md);
- executable package under `tools/monotone-nae-3sat/`.

**Exit gate:** Satisfied. The slice is complete only as infrastructure and makes no satisfiability claim.

## `VS-02` — Exact small-instance oracle

**Goal:** Create a trusted exact decision oracle for finite discovery experiments.

**Work:**

- enumerate binary colourings;
- use component and complement symmetry only after proving the optimization preserves correctness;
- return satisfiable/unsatisfiable and a witness when one exists;
- independently recheck every returned witness;
- generate instances under an explicitly stated labelled or isomorphism-reduced domain;
- record the exhaustiveness argument for every claimed finite domain;
- record commands, environment, counts, runtime, and limitations.

**Exit gate:** The oracle agrees with hand-certified controls and exhaustively evaluates the first declared domain with reproducible counts.

## `VS-03` — Exact extension-profile engine

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
- verify final acceptance against VS-02;
- record raw assignment count, boundary-state count, quotient count, and encoded profile size.

**Exit gate:** Every tested instance and ordering has a transition graph whose final acceptance equals VS-02, and transition well-definedness is checked computationally.

## `VS-04` — Control calibration

**Goal:** Verify that the laboratory explains known easy cases before examining hard instances.

**Controls:**

- graph bipartiteness;
- acyclic incidence hypergraphs;
- bounded-boundary instances;
- meaningful XOR-SAT analogues;
- disconnected unions;
- planar and occurrence-at-most-three NAE instances.

**Exit gate:** A report identifies why each control is easy and whether compactness comes from small interfaces, algebraic closure, decomposition, or component factorization.

## `VS-05` — Minimal obstruction atlas

**Goal:** Identify the smallest exact failures of global compatibility.

**Work:**

- enumerate unsatisfiable instances in a declared domain;
- test edge-minimal unsatisfiability;
- test vertex-minimality separately when claimed;
- include and independently verify the Fano plane;
- record degree, linearity, incidence-cycle, automorphism, and extension-profile data;
- separate disconnected copies from connected cores.

**Exit gate:** Every object called minimal has all relevant proper subinstances verified satisfiable, with complete instance data and reproducible verification.

## `VS-06` — Destroy naive summaries

**Goal:** Eliminate insufficient invariants with complete collisions.

**Summaries:**

- degree sequence;
- edge-intersection multiset;
- pair co-occurrence data;
- parity and affine summaries;
- local-consistency closure;
- bounded-radius incidence neighbourhoods;
- component counts and elementary spectral data;
- fixed-order low-moment completion statistics.

**Required disproof:** Two complete instances or partial states with the same proposed summary but different satisfiability or different exact completion sets.

**Exit gate:** Each rejected summary has a smallest known verified collision and a statement of remaining scope.

## `VS-07` — Measure genuine semantic merging

**Goal:** Determine what exact compression exists beyond trivial symmetry.

**Work:**

- compare raw prefix assignments, boundary colourings, and exact future classes;
- separate dead-state merging from live-state merging;
- quotient global complement symmetry explicitly;
- optimize over small orderings;
- measure maximum and total quotient size;
- distinguish number of classes from representation size.

**Exit gate:** A reproducible dataset identifies the first nontrivial live semantic merge and the first family showing significant quotient growth.

## `VS-08` — Extract the first atomic invariant

**Goal:** Turn empirical failure structure into one precise mathematical mechanism.

**Required artifact:** One conjecture specifying:

- representation language and semantics;
- construction and transition operations;
- soundness and completeness target;
- predicted total-state bound;
- mandatory controls;
- first adversarial family;
- stop condition.

**Exit gate:** The conjecture is falsifiable and does not hide satisfiability, equivalence, or transitions inside an undefined operation.

## `VS-09` — Prove a restricted theorem first

**Goal:** Establish correctness before universality.

**Work:** Prove the invariant on the largest exact subclass supported by evidence, including all quantifiers, boundary cases, encoding, runtime, memory, and total-state bounds.

**Existing baseline:** `NAE-005` proves the ordinary bounded-boundary algorithm. It does not validate a future stronger invariant.

**Exit gate:** A complete `PROVED / DRAFT` theorem for the new invariant, followed by an independent proof attack.

## `VS-10` — Attack with hard families

**Goal:** Test whether the candidate survives genuine hardness rather than curated examples.

**Families:**

- Fano-derived and minimal obstructions;
- linear 4-regular Monotone NAE-3SAT;
- verified NP-hard reduction outputs;
- high-width instances;
- defined transfers to Positive 1-in-3 SAT or graph 3-colouring.

**Exit gate:** Produce a complete counterexample, a sharply restricted surviving theorem, or a candidate that survives all recorded attacks.

## `VS-11` — Global complexity audit

**Goal:** Prevent local polynomial reasoning from hiding exponential total work.

**Audit:**

- input and intermediate bit lengths;
- construction cost;
- equivalence and transition cost;
- recursion depth and branching;
- complete generated-state graph;
- duplicate-state detection;
- memory;
- representation normalization;
- witness reconstruction;
- uniformity and deterministic correctness.

**Exit gate:** A complete polynomial bound or an explicit superpolynomial obstruction for the named algorithm and representation.

## `VS-12` — Route decision

**Goal:** Record the exact mathematical outcome.

**Possible decisions:**

- universal algorithm candidate survives;
- restricted theorem retained with exact hypotheses;
- conjecture disproved by a complete counterexample;
- representation-specific barrier retained without inferring `P!=NP`;
- no material mechanism and return to route selection.

**Exit gate:** Claim ledger, status, route record, evidence, limitations, and reopening conditions are synchronized.

## Immediate queue

1. Execute VS-02 using the completed canonical model.
2. Implement VS-03 and cross-check it against the oracle.
3. Run VS-04 and VS-05 before designing a new invariant.
4. Use VS-06 and VS-07 to extract the first atomic candidate in VS-08.

Computational results remain `COMPUTATIONAL` unless accompanied by a complete exhaustiveness argument or proof.
