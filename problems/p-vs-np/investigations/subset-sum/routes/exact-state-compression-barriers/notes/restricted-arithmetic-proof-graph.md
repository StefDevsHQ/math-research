# Restricted Arithmetic Proof Graph — Candidate Model

**Claim:** `SS-ECB-016`  
**Classification:** Definition and open model candidate  
**Status:** `OPEN / DRAFT`  
**Updated:** 2026-07-16

## 1. Purpose

The preceding boundaries rule out three naive model choices:

1. unevaluated Minkowski-expression DAGs are linearly small for every instance;
2. normalized unions of arithmetic progressions are exponentially large even on easy superincreasing instances;
3. unrestricted intersection of compact arithmetic target sets can encode arbitrary CNF conjunctions on the assignment-target slice.

The candidate below is designed to contain the retained structural-compression mechanisms without treating arbitrary Boolean conjunction or arbitrary programs as free.

No lower bound is claimed yet.

## 2. Objects

A **restricted arithmetic proof graph** for a Subset Sum instance \((A,t)\) is a finite directed acyclic graph. Each node is one of the following.

### 2.1 Exact-summary node

An exact-summary node is attached to an item block \(B\subseteq A\) and denotes exactly \(\Sigma_t(B)\). Its syntax is a finite union of atoms of the form

\[
\{x\in\mathbb Z: \ell\le x\le u,\ x\equiv r\pmod q\},
\]

plus an explicit finite exception set. All integers are encoded in binary.

The union is extensional: its atoms must denote the exact truncated reachable set, not merely a subset or superset.

### 2.2 Coverage-certificate node

A coverage node attached to \(B\) certifies

\[
K\subseteq\Sigma_t(B),
\]

where \(K\) is represented by the same atom syntax. It must include polynomial-time-verifiable witness data for the claimed rule. The residue-completion lemma is an admissible certificate schema.

Coverage nodes cannot be used as exact child summaries unless all omitted reachable sums are represented separately.

### 2.3 Residual-transformation node

A residual node records an exact equivalence

\[
(B,t)\equiv(B',t')
\]

for the decision question, together with a polynomial-time-verifiable local rule. Forced inclusion, forced exclusion, and immediate rejection are admissible schemas.

### 2.4 Exact-merge node

For disjoint child blocks \(B_0,B_1\), an exact-merge node may derive an exact summary for \(B_0\uplus B_1\) only by a counted normalization procedure implementing

\[
\Sigma_t(B_0\uplus B_1)
=
(\Sigma_t(B_0)+\Sigma_t(B_1))\cap[0,t].
\]

The node must explicitly record the generated output atoms and all intermediate atoms or compatibility states created by normalization.

### 2.5 Branch node

A branch node may split into finitely many exact residual subinstances only when the branches are jointly exhaustive and sound. The branch condition must be one of a fixed list of local arithmetic predicates, not an arbitrary Boolean circuit over the target bits.

## 3. Forbidden free operations

The model does not permit the following as unit-cost syntax:

- arbitrary unevaluated Minkowski-sum nodes;
- arbitrary intersection of two summary expressions;
- arbitrary complement;
- arbitrary Boolean circuits or general programs stored at nodes;
- oracle transitions whose internal computation is not counted;
- target-bit tests unrelated to a declared local arithmetic rule.

Clipping by the global interval \([0,t]\) is permitted because it is part of the exact truncated composition identity. This is not unrestricted intersection.

## 4. Cost measure

The complete cost is the sum of:

1. binary encoding length of every node and constant;
2. all exact-summary and coverage atoms, including discarded intermediate atoms;
3. every branch and residual edge;
4. all merge-normalization work and compatibility states;
5. certificate generation and verification time;
6. terminal query time.

Shared nodes are counted once, but constructing a shared node is not free.

A family is polynomially represented only if the complete graph, total encoded intermediate state, construction time, and query time are polynomial in the original binary input length.

## 5. Containment audit

### Contained

- forced inclusion and exclusion;
- immediate target-range rejection;
- exact intervals and bounded progressions;
- binary-encoded congruence atoms;
- explicit finite exceptions;
- residue-completion coverage certificates;
- exact recursively generated subinstances;
- exact item-block composition when normalization is fully counted.

### Not automatically contained

- arbitrary persistent-lattice analysis described only informally;
- arbitrary symbolic formulas over target bits;
- a compact recursive rule whose complete generated graph is exponential;
- any operation whose exactness or verification cost is not specified.

## 6. Immediate attacks

### Attack A — input retention

The model cannot call an unevaluated Minkowski tree a completed summary. Every exact merge must normalize or otherwise produce a query-decidable counted state.

### Attack B — progression normalization

`SS-ECB-015` shows that exact progression-union summaries alone can require exponentially many atoms on ternary superincreasing instances. Such instances must therefore be handled by residual nodes, not by full-set normalization.

### Attack C — Boolean conjunction escape

`SS-ECB-014` shows that unrestricted intersection of compact arithmetic target sets represents arbitrary width-three CNF assignment slices in polynomial size. The model permits only target clipping and fixed local certificate predicates, not general expression intersection.

### Attack D — hidden circuit simulation

The remaining unresolved question is whether repeated local branching, residue tests, and shared residual nodes can collectively simulate polynomial-size Boolean circuits. This must be attacked before any lower-bound theorem is attempted.

## 7. Precise open requirements

The candidate survives only if all of the following are proved:

1. **well-definedness:** every permitted rule has explicit syntax and exact semantics;
2. **structural subsumption:** every retained operation from the closed route compiles with polynomial local overhead;
3. **non-universality:** the graph language cannot encode arbitrary polynomial-size Boolean circuits with polynomial complete cost;
4. **hard family:** an explicit Subset Sum family requires superpolynomial complete cost in this model;
5. **robustness:** the lower bound holds despite target-relative residual rules and sharing.

At present only the semantic framework and the three boundary attacks are established. Requirements 2–5 remain open.

## 8. Stop condition

Reject this candidate immediately if either:

- a polynomial-size simulation of arbitrary Boolean circuits is found; or
- one of the retained structural operations requires an uncounted oracle or cannot be expressed under the fixed local schemas.

Do not seek a lower bound until the hidden-circuit-simulation audit is complete.