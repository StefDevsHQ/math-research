# Vertical Slices — Circuit-SAT Algorithms to Lower Bounds

**Purpose:** Authoritative execution order for the Circuit-SAT investigation.  
**Phase:** consequence-map construction and model selection  
**Updated:** 2026-07-23

## 1. Investigation objective

This investigation studies the following programme:

```text
nontrivial satisfiability or counting algorithm
for one precisely defined circuit class C

                implies

an explicit nonuniform circuit lower bound
through a verified transfer theorem.
```

The investigation is not a generic search for a faster SAT solver. Every active algorithmic claim must name:

1. the circuit class;
2. the circuit encoding and size measure;
3. the allowed depth, fan-in, gate basis, weights and uniformity;
4. the input regime in which the algorithm is claimed;
5. the baseline exhaustive-search runtime;
6. the exact improvement required;
7. the imported algorithms-to-lower-bounds theorem;
8. the exact lower-bound consequence;
9. every closure property required by the transfer theorem;
10. the complete runtime and generated-state accounting.

No class is selected merely because its circuits look structurally simple.

## 2. Governing mathematical distinction

The investigation separates three logically different statements:

### Algorithm statement

```text
SAT_C(n,s,d,...) is decidable in time T(n,s,d,...).
```

### Transfer theorem

```text
If C-SAT or #C-SAT satisfies a specified improvement,
then complexity class A is not contained in nonuniform C-circuits
of a specified size regime.
```

### Lower-bound conclusion

```text
A not subseteq C-SIZE[g(n)].
```

The algorithm statement does not imply the lower bound without a theorem whose hypotheses are all verified. A lower bound for one class does not transfer to a larger class without a separate inclusion or simulation theorem.

## 3. Progress dashboard

| Slice | Name | Status | Required output | Promotion gate |
|---:|---|---|---|---|
| `CS-VS-01` | Exact consequence map | `ACTIVE` | Primary-source matrix of circuit class, SAT improvement and lower-bound consequence. | Every row has an exact theorem statement and checked hypotheses. |
| `CS-VS-02` | Canonical circuit model and encoding | `BLOCKED` | One selected circuit language with full binary encoding and semantic definition. | One class survives `CS-VS-01` and the selection audit. |
| `CS-VS-03` | Exact evaluator and exhaustive oracle | `BLOCKED` | Reference evaluator, SAT/#SAT oracle and canonical instance serialization. | Independent agreement on exhaustive small instances. |
| `CS-VS-04` | Baselines and tractable controls | `BLOCKED` | Known algorithms, trivial bounds and restricted subclasses reproduced. | Runtime and correctness match primary sources or complete project proofs. |
| `CS-VS-05` | Hard-family and reduction controls | `BLOCKED` | Canonical adversarial circuits and reduction-generated instances. | Candidate mechanisms fail or survive for mathematically explained reasons. |
| `CS-VS-06` | Atomic algorithmic mechanism | `BLOCKED` | One precise lemma or algorithm improving a stated baseline. | Complete correctness and total-runtime proof; no hidden exponential subroutine. |
| `CS-VS-07` | Transfer-hypothesis audit | `BLOCKED` | Verification that the algorithm meets every imported theorem hypothesis. | Exact class closure, size regime, uniformity and savings conditions verified. |
| `CS-VS-08` | End-to-end consequence theorem | `BLOCKED` | Conditional theorem from the project algorithm to the precise lower bound. | Both the algorithm and transfer proof are complete. |
| `CS-VS-09` | Adversarial and independent audit | `BLOCKED` | Proof-break attempt, implementation checks and source verification. | No unresolved correctness, encoding or theorem-import gap. |
| `CS-VS-10` | Route decision | `BLOCKED` | Prove, restrict, defer, retract or close the selected route. | Claim ledger and all status documents agree. |

## 4. CS-VS-01 — exact consequence map

**Status:** `ACTIVE`  
**Mode:** `ORIENT / VERIFY`

### 4.1 Question

Which precisely stated satisfiability or counting improvements for which circuit classes have established nonuniform lower-bound consequences?

### 4.2 Required matrix

Each candidate receives one row with these fields:

| Field | Required content |
|---|---|
| Circuit class | Exact gate basis and structural restrictions. |
| Circuit size regime | Polynomial, quasipolynomial, subexponential or another explicit bound. |
| Depth and fan-in | Fixed, bounded, unbounded or input-dependent. |
| Parameter encoding | Binary cost of gates, edges, moduli, weights and thresholds. |
| Problem | SAT, #SAT, approximate counting, evaluation or another exact task. |
| Baseline | Full brute-force runtime including circuit evaluation cost. |
| Required improvement | Exact asymptotic savings, with all quantifiers. |
| Transfer theorem | Primary theorem number, statement and publication. |
| Closure assumptions | Composition, negation, projections, constants, AND/OR closure or other hypotheses. |
| Consequence | Exact separation, such as `NEXP not subseteq C/poly-size`. |
| Known algorithm | Best relevant published algorithm and parameter regime. |
| Remaining margin | What improvement is not already known. |
| Main obstruction | Known barrier or missing technical ingredient. |
| Project verdict | `SELECT`, `CONTROL`, `DEFER` or `REJECT`. |

### 4.3 Initial candidate families

The initial map must cover at least:

1. polynomial-size unrestricted Boolean circuits;
2. Boolean formulas and bounded fan-in formulas;
3. constant-depth `AC0` circuits;
4. `AC0[p]` and `ACC0` circuits;
5. threshold circuits, including selected depth-two or shallow subclasses;
6. `ACC0 o THR` and related composed classes with published SAT/#SAT consequences;
7. any additional class proposed for activation.

These are comparison families, not presumed active routes.

### 4.4 Primary transfer sources

At minimum, audit:

- Ryan Williams, *Improving Exhaustive Search Implies Superpolynomial Lower Bounds*, SIAM Journal on Computing 42(3), 2013;
- Ryan Williams, *Nonuniform ACC Circuit Lower Bounds*, Journal of the ACM 61(1), 2014;
- Ryan Williams, *New Algorithms and Lower Bounds for Circuits With Linear Threshold Gates*, Theory of Computing 14, 2018;
- Nikhil Vyas and Ryan Williams, *Lower Bounds Against Sparse Symmetric Functions of ACC Circuits: Expanding the Reach of #SAT Algorithms*, STACS 2020 / Theory of Computing Systems 2023;
- Igor Oliveira, *Algorithms versus Circuit Lower Bounds*, for orientation only, with primary papers used for accepted theorem statements.

### 4.5 Promotion gate

`CS-VS-01` is complete only when:

- every accepted row has a checked primary citation;
- theorem quantifiers are copied accurately;
- SAT and #SAT consequences are not conflated;
- polynomial-factor savings are distinguished from `2^{n-n^epsilon}` savings;
- circuit size regimes are explicit;
- uniform and nonuniform classes are separated;
- no survey is the sole authority for an accepted theorem;
- one model is recommended with a stated reason and stop condition.

## 5. CS-VS-02 — canonical circuit model and encoding

**Status:** `BLOCKED`  
**Mode:** `FORMALIZE`

### 5.1 Required definition

For the selected class `C`, define a circuit as a finite directed acyclic graph with:

- indexed input variables;
- gate records in topological order;
- exact gate type and arity;
- ordered or unordered incoming-wire semantics as appropriate;
- constant gates if allowed;
- negation placement rules;
- modulus or threshold data if applicable;
- one or more designated outputs;
- a complete validity predicate.

### 5.2 Encoding accounting

The binary input length `L` must include:

- number of variables;
- number of gates and wires;
- gate-type tags;
- wire endpoint indices;
- depth metadata only if explicitly encoded;
- moduli in binary;
- threshold weights and thresholds in signed binary;
- output indices;
- delimiters and length fields up to constant-factor equivalence.

Runtime may be stated in `n` and circuit size `s` only after proving their relation to `L` in the selected regime.

### 5.3 Semantic obligations

Prove:

- evaluation is well-defined;
- the validity predicate is decidable in polynomial time;
- evaluation time is polynomial in the full encoding;
- the circuit class is closed under exactly the operations required by the transfer theorem;
- any normalization preserves both semantics and size within the required bound.

### 5.4 Stop conditions

Reject or reformulate the model if:

- gate weights or moduli hide exponential bit complexity;
- the transfer theorem uses a different circuit convention;
- closure under required operations causes uncontrolled size or depth growth;
- class membership is not efficiently checkable in the claimed representation.

## 6. CS-VS-03 — exact evaluator and exhaustive oracle

**Status:** `BLOCKED`  
**Mode:** `FORMALIZE / VERIFY`

### 6.1 Deliverables

Implement or formally specify:

- parser and validity checker;
- deterministic circuit evaluator;
- exhaustive SAT solver;
- exhaustive #SAT solver where relevant;
- witness extraction;
- canonical serialization;
- random and exhaustive small-circuit generators;
- independent truth-table cross-checks.

### 6.2 Correctness claims

The reference oracle must prove:

```text
SAT(C)=1 iff there exists a in {0,1}^n with C(a)=1.
```

For counting:

```text
#SAT(C)=|{a in {0,1}^n : C(a)=1}|.
```

### 6.3 Complexity baseline

For evaluation cost `E(C)`, record the exact exhaustive baseline:

```text
O(2^n E(C)) time
```

plus memory and serialization costs. Never abbreviate the baseline to `2^n` when circuit evaluation or coefficient arithmetic is not polynomially negligible in the selected regime.

### 6.4 Verification domain

Small-instance tests must vary:

- variable count;
- circuit size;
- depth;
- fan-in;
- sharing versus formulas;
- constant and negation placement;
- gate-specific parameters;
- satisfiable, uniquely satisfiable and unsatisfiable cases.

Finite tests are controls, not universal proofs.

## 7. CS-VS-04 — baselines and tractable controls

**Status:** `BLOCKED`  
**Mode:** `ORIENT / VERIFY`

Record the best relevant algorithms and easy subclasses before proposing a new mechanism.

Mandatory comparisons include, where applicable:

- exhaustive assignment search;
- split-and-list or meet-in-the-middle baselines;
- formula-specific algorithms;
- bounded-treewidth or bounded-pathwidth dynamic programming;
- bounded-depth simplification;
- switching-lemma or polynomial-representation algorithms already known for the class;
- published SAT/#SAT algorithms that already yield lower bounds.

For every imported algorithm, record:

- exact input model;
- randomized or deterministic status;
- one-sided or two-sided error;
- expected or worst-case time;
- preprocessing cost;
- parameter restrictions;
- whether the savings meet a transfer theorem.

## 8. CS-VS-05 — hard-family and reduction controls

**Status:** `BLOCKED`  
**Mode:** `ATTACK`

### 8.1 Purpose

Destroy mechanisms that exploit accidental properties of random or tree-like circuits.

### 8.2 Mandatory controls

The selected class must be tested against applicable examples of:

- high-sharing circuits where formula expansion is exponential;
- circuits with no useful local simplification;
- parity or modular structure;
- threshold gates with large binary weights;
- balanced circuits whose every variable has weak local influence;
- circuits produced by Cook-Levin-style or verifier-to-circuit reductions;
- circuits encoding canonical hard SAT and CSP instances;
- unsatisfiable circuits with no short propagation refutation;
- satisfiable circuits with isolated witnesses;
- circuits at the size and depth boundary of the transfer theorem.

### 8.3 Reduction audit

Reduction-generated controls must preserve:

- variable count;
- circuit class membership;
- size and depth bounds;
- binary encoding length;
- satisfiability in both directions;
- any promise used by the algorithm.

## 9. CS-VS-06 — atomic algorithmic mechanism

**Status:** `BLOCKED`  
**Mode:** `FORMALIZE / ATTACK`

Only one mechanism may be active at a time. Candidate mechanism families include:

- gate elimination;
- restriction and simplification;
- switching-style decomposition;
- polynomial or low-rank representations;
- meet-in-the-middle over an exact interface;
- correlation exploitation;
- batch evaluation;
- sparse counting transforms.

This list creates no presumption of viability.

### 9.1 Required algorithm statement

State:

```text
For every valid C-circuit with n variables and encoded size L
in regime R, algorithm A returns SAT(C) [or #SAT(C)] correctly
in time T(n,L) and space S(n,L).
```

Include determinism, error probability and amplification cost.

### 9.2 Complete cost graph

Account for:

- preprocessing;
- every branch and recursive call;
- number and size of generated restrictions;
- normalization;
- arithmetic bit complexity;
- memoization keys and equality tests;
- intermediate representation size;
- total generated work, not only maximum local state;
- success-probability amplification;
- witness recovery if claimed.

Polynomial recursion depth with polynomial branching is not a polynomial algorithm.

### 9.3 Immediate falsification tests

Before protection, attack the mechanism on:

- maximal sharing;
- maximal allowed depth;
- maximal gate fan-in;
- adversarial variable occurrence;
- all-zero and all-one degeneracies;
- parity and residue obstructions;
- coefficient bit-length extremes;
- reduction-generated instances;
- cases where each local step improves but the total computation tree is exponential.

## 10. CS-VS-07 — transfer-hypothesis audit

**Status:** `BLOCKED`  
**Mode:** `VERIFY`

Create a theorem-hypothesis checklist with one line per imported assumption.

Mandatory items:

- exact circuit class equality or valid inclusion;
- closure under AND, OR, negation, projections or constants if required;
- constructibility or recognizability assumptions;
- circuit-size quantifiers;
- savings quantifiers, including whether they must hold for every polynomial size exponent;
- SAT versus #SAT requirement;
- deterministic versus randomized requirement;
- error model;
- uniform algorithm requirement;
- advice and nonuniformity conventions;
- output complexity class and circuit lower-bound size regime.

The verdict is one of:

```text
TRANSFER VERIFIED
TRANSFER NOT APPLICABLE
TRANSFER GAP
```

No lower-bound language may appear in project status while the verdict is `TRANSFER GAP`.

## 11. CS-VS-08 — end-to-end consequence theorem

**Status:** `BLOCKED`  
**Mode:** `PROVE`

The final conditional theorem must have the form:

> Assuming project claim `CS-ALG-###`, all hypotheses of established theorem `T` hold for class `C`; therefore complexity class `A` is not contained in nonuniform `C`-circuits of size `g(n)`.

The proof must explicitly compose:

1. the algorithm theorem;
2. parameter conversion from repository encoding to theorem notation;
3. closure and constructibility lemmas;
4. the imported transfer theorem;
5. the exact lower-bound conclusion.

A result is conditional until the algorithm theorem is independently accepted.

## 12. CS-VS-09 — adversarial and independent audit

**Status:** `BLOCKED`  
**Mode:** `VERIFY`

Audit separately:

- algorithm correctness;
- asymptotic runtime;
- binary input length;
- arithmetic cost;
- randomness and amplification;
- class membership;
- transfer theorem statement;
- every theorem hypothesis;
- claimed consequence;
- scope language.

The author of the proof may mark it `CHECKED`, not `INDEPENDENTLY-CHECKED`, unless a genuinely independent reviewer completes the audit.

## 13. CS-VS-10 — route decision

**Status:** `BLOCKED`  
**Mode:** `DECIDE / RECORD`

Possible outcomes:

- `PROVED`: the algorithm and consequence theorem are complete;
- `RESTRICTED`: a valid improvement exists only on an explicit subclass;
- `DISPROVED`: a precise algorithmic or structural claim has a complete counterexample;
- `RETRACTED`: the route lacks enough precision or evidence for formal disproof;
- `DEFERRED`: the model is valid but no current atomic mechanism survives;
- `CLOSED`: a stated stop condition has been reached.

Failure to obtain an algorithm does not imply a circuit lower bound is false. Failure of one class does not imply `P != NP`.

## 14. Selection criteria after CS-VS-01

Score each candidate from zero to four on:

1. exactness of the transfer theorem;
2. strength of the consequence;
3. distance from the best known algorithm to the required threshold;
4. implementability of exact small-instance controls;
5. availability of a distinct atomic mechanism;
6. resistance to immediate known barriers;
7. clarity of the stop condition.

The selected class must have:

- no zero on criteria 1, 4 or 7;
- a concrete mechanism, not merely a class name;
- a reason the mechanism is not already subsumed by known algorithms;
- one decisive first falsification test.

## 15. Current recommendation hierarchy

Pending `CS-VS-01`, the provisional order is:

1. **restricted circuit class with a clean Williams-style SAT transfer theorem and a small remaining algorithmic gap;**
2. **a #SAT class where counting gives a strictly stronger verified consequence;**
3. **formula or bounded-width controls as implementation laboratories;**
4. **unrestricted polynomial-size Boolean circuits only as an orientation endpoint, not as the first active mechanism.**

This hierarchy is strategic and may change after the source audit.

## 16. Immediate queue

1. build `CS-VS-01-CONSEQUENCE-MAP.md` from primary theorem statements;
2. define candidate-class comparison rows without selecting a winner prematurely;
3. verify the exact generic Williams transfer hypotheses;
4. separate known ACC-class successes from open threshold and general-circuit targets;
5. recommend one class, one algorithmic threshold and one stop condition;
6. activate `CS-VS-02` only after that decision.

## 17. Scope restraint

This documentation establishes a research workflow, not a new theorem.

No claim is made that:

- a faster Circuit-SAT algorithm has been found;
- any new circuit lower bound has been proved;
- the selected route will resolve `P` versus `NP`;
- a lower bound for one restricted class separates `P` from `NP`.

All mathematical claims must be entered in `CLAIMS.md` with stable identifiers and evidence.