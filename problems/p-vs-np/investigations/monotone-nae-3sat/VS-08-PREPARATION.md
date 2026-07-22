# VS-08 Preparation — Propagation-Closed Signed Residual Normal Form

**Slice:** `VS-08`  
**State:** `PREPARED`  
**Candidate claim:** `NAE-016 — CONJECTURE / DRAFT`  
**Updated:** 2026-07-22

## Decision inherited from VS-07

VS-07 leaves two facts that the next representation must handle simultaneously.

1. Exact future semantics can merge live boundary assignments beyond direct component complement.
2. A fixed ordering can expose exponentially many live exact classes even on an easy family, while another ordering has constant width.

Therefore VS-08 must not use:

- raw boundary assignments as the proposed compression;
- component complement as the only merge rule;
- one bad ordering as a lower bound;
- exact semantic equivalence as an assumed polynomial-time primitive.

## Candidate representation

For an instance `H`, an ordering `pi`, a level `i`, and a processed prefix assignment `p`, define the **propagation-closed signed residual normal form**, abbreviated `PCRNF(H,pi,i,p)`.

The residual language contains:

1. a contradiction flag;
2. the labelled unprocessed vertices;
3. unary colour requirements `x_v=c`;
4. signed binary constraints

   ```text
   not(x_u=x_v=c), c in {0,1};
   ```

5. ternary NAE constraints on three unprocessed vertices;
6. an ordered decomposition into residual incidence components.

### Direct residualization of one original edge

After substituting processed colours into an edge:

- zero processed vertices: retain the ternary NAE constraint;
- one processed vertex of colour `c`: retain the signed binary constraint forbidding both remaining vertices from colour `c`;
- two processed vertices:
  - equal colour `c`: force the remaining vertex to `1-c`;
  - different colours: the edge is already satisfied and is deleted;
- three processed vertices:
  - monochromatic: contradiction;
  - otherwise: delete the satisfied edge.

This transformation is exact before any closure rule.

## Deterministic closure

Apply the following rules to a fixed point in a specified lexicographic work-list order.

1. Substitute every unary requirement into every incident binary or ternary constraint.
2. From a signed binary constraint `not(x_u=x_v=c)`:
   - if `x_u=c`, force `x_v=1-c`;
   - if `x_u=1-c`, delete the satisfied constraint;
   - symmetrically for `x_v`.
3. From a ternary NAE constraint:
   - two equal fixed colours force the third vertex to the opposite colour;
   - two different fixed colours satisfy the constraint;
   - one fixed colour reduces it to the corresponding signed binary constraint.
4. Opposite unary requirements on one vertex produce contradiction.
5. Delete duplicate constraints and sort all labelled records canonically.
6. Split the remaining residual into incidence components.
7. For each residual component, compare its labelled encoding with the encoding obtained by complementing every unary colour and binary sign in that component; retain the lexicographically smaller encoding.
8. Sort component encodings lexicographically.

Component complement is semantic symmetry because NAE and the signed binary relations are invariant under simultaneous colour complement.

## Exact semantic contract

Let `R= PCRNF(H,pi,i,p)`.

The required correctness theorem is:

> For every assignment `q` to the unprocessed labelled vertices, `p q` satisfies `H` if and only if `q` satisfies `R`, after undoing only the explicitly recorded component-complement normalizations.

Consequences:

- contradiction is equivalent to no completion;
- an empty residual is equivalent to every remaining assignment being accepted;
- syntactically equal labelled normal forms have equal exact completion sets;
- restricting the next variable and re-closing gives an exact transition.

The converse is not assumed: semantically equal residuals may have different PCRNFs.

## Operations and required bounds

Every operation must be specified in complete binary encoding length.

### Construction

Input: canonical instance, ordering, level, prefix.

Output: canonical PCRNF.

Required initial theorem: construction terminates and is polynomial in the explicit instance and residual size.

### Equality

Byte equality of canonical PCRNF encodings.

No graph-isomorphism quotient is permitted in the first version. Labels are retained.

### Transition

For next vertex `v` and colour `c`:

1. insert unary `x_v=c`;
2. run deterministic closure;
3. remove `v` from the unprocessed set;
4. normalize components.

### Acceptance

- contradiction: reject;
- at final level, empty noncontradictory residual: accept.

### Merge

Only byte-identical canonical PCRNFs merge in the first version.

### Encoded size

Count:

- contradiction bit;
- vertex identifiers;
- unary records;
- signed binary records;
- ternary records;
- component framing;
- all length and cardinality metadata.

Raw constraint counts without framing are insufficient.

## Atomic universal conjecture — `NAE-016`

> Every encoded Monotone NAE-3SAT instance has an ordering, constructible in polynomial time, for which memoized exact traversal by PCRNF produces only polynomially many distinct residual normal forms of polynomial maximum and polynomial total encoded size, with polynomial-time transition, equality, and acceptance.

If proved together with the exact semantic contract, this would yield a deterministic polynomial-time algorithm for Monotone NAE-3SAT and therefore, by `NAE-002`, prove `P=NP`.

**Current status:** `CONJECTURE / DRAFT`.

The conjecture is not accepted merely because each individual residual has polynomial explicit size. The complete reachable state graph and total encoded state must be polynomially bounded.

## Why the candidate explains the VS-07 witness

For the instance with edges `{012,013}`, ordering `(0,2,3,1)`, and level three, the only unprocessed vertex is `1`.

Each processed edge either:

- is already satisfied; or
- forces vertex `1` to colour zero or one.

After closure, the eight prefixes reduce to exactly three labelled residual forms:

```text
x_1=0
x_1=1
no remaining constraint
```

These are exactly the three completion masks `1`, `2`, and `3`. Thus PCRNF captures the first genuine all-live merge without calling an exact solver during equality.

## Immediate attacks

### Attack A — closure correctness and confluence

Prove:

- every rewrite preserves the exact labelled completion set;
- the specified work-list order terminates;
- the output is deterministic;
- component normalization preserves labelled completion semantics up to the recorded complement action.

If deterministic output depends on arbitrary rule order, the candidate is not canonical and must be repaired before measurement.

### Attack B — fan family

Measure both fan orderings.

Expected:

- the bad ordering produces `2^(k+1)-1` distinct live PCRNFs at level `k+1`, consisting of different sets of labelled unary forces;
- the interleaved ordering has bounded residual interface and bounded PCRNF state count.

This confirms ordering sensitivity but does not refute `NAE-016`.

### Attack C — exact-profile comparison

For all labelled instances and all orderings through the feasible domain:

- compare PCRNF equality with exact completion-mask equality;
- any same-PCRNF/different-mask pair is a complete correctness counterexample;
- different-PCRNF/same-mask pairs measure incompleteness of the merge rule;
- record first incompleteness witness and quotient ratios.

### Attack D — unsatisfiable controls

Use `K_5^(3)` and the Fano plane.

PCRNF must not report useful compression merely because every state is semantically dead. Record live and dead states separately as in VS-07.

### Attack E — tractable controls

PCRNF must recover, without unnecessary blow-up:

- graph bipartiteness after anchored binary reduction;
- affine XOR controls only when translated by an explicitly exact encoding;
- incidence forests;
- bounded-boundary instances;
- disconnected products.

### Attack F — hard structural controls

Before promotion, test:

- linear four-regular Monotone NAE-3SAT samples;
- verified canonical reduction outputs;
- high-width satisfiable instances;
- the VS-06 collision pairs;
- instances with little or no unit propagation.

## Stop conditions

Close or narrow the candidate when any of the following is established.

1. A complete same-PCRNF/different-completion-set counterexample exists.
2. Canonicalization requires semantic equivalence, satisfiability, or another NP-hard primitive.
3. Exact transition or normalization requires exponential intermediate state on a polynomial-size family.
4. A proved family has exponentially many distinct PCRNFs for every ordering in the claimed ordering class.
5. The mechanism reduces to ordinary `2^w` boundary dynamic programming without a stronger global bound.
6. Reduction-generated instances preserve exponentially many unresolved labelled residual choices and no new exact merge rule is identified.

Failure on one ordering alone does not satisfy stop condition 4.

## Implementation slices

### VS-08A — formal residual object

- immutable labelled representation;
- strict validation and serialization;
- direct edge residualization;
- no semantic claim beyond direct substitution.

### VS-08B — deterministic closure

- unary propagation;
- binary and ternary simplification;
- contradiction;
- duplicate removal;
- termination and exactness proof.

### VS-08C — component-complement normalization

- component extraction;
- complement action;
- canonical labelled encoding;
- exact transition.

### VS-08D — falsification harness

- compare against VS-03 exact masks;
- exhaustive small-domain census;
- first incompleteness and correctness collisions;
- fan and obstruction controls;
- encoded-size accounting.

### VS-08E — route decision

Promote only if:

- exactness survives exhaustive comparison;
- the candidate merges the VS-07 witness;
- state growth is materially below raw boundary states on nontrivial live instances;
- no hidden semantic oracle is used;
- one precise polynomial total-state conjecture remains plausible after hard controls.

Otherwise retain restricted results and close or replace the candidate.

## Review boundary

Preparing VS-08 does not establish `NAE-016`, does not activate VS-09 through VS-12, and does not claim novelty. Literature and reduction checks remain mandatory before any promotion beyond a project conjecture.
