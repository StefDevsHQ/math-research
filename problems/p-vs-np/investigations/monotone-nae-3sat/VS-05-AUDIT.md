# VS-05 Audit — Minimal Obstruction Atlas

**Status:** `COMPLETE / CHECKED`  
**Updated:** 2026-07-22

## Scope

VS-05 constructs a deterministic exact atlas of the first two calibrated non-two-colourable 3-uniform hypergraphs:

- the dense complete hypergraph `K_5^(3)`;
- the sparse Fano plane.

It also exhausts every labelled 3-uniform hypergraph through five vertices and checks edge-minimality and vertex-minimality separately.

## Definitions

An unsatisfiable hypergraph is:

- **edge-minimal unsatisfiable** when every one-edge deletion is satisfiable;
- **vertex-minimal unsatisfiable** when every one-vertex induced deletion is satisfiable.

### Single-deletion sufficiency — `NAE-009`

If every one-edge deletion `H-e` is satisfiable, then every proper edge-subhypergraph `G` is satisfiable: choose an edge `e` omitted by `G`; then `G` is an edge-subhypergraph of `H-e`, and restricting a colouring of `H-e` colours `G`.

If every one-vertex induced deletion `H-v` is satisfiable, then every proper induced vertex subhypergraph is satisfiable: choose a vertex omitted by that subinstance and restrict a colouring of `H-v`.

Both converses are immediate because single deletions are proper subinstances.

**Status:** `PROVED / CHECKED`.

## Exhaustive small domain — `NAE-010`

The generator enumerates exactly

\[
\sum_{n=0}^{5}2^{\binom n3}=1045
\]

labelled 3-uniform hypergraphs.

Independent direct colouring enumeration agrees with VS-02 on every instance. Exactly one instance is unsatisfiable:

\[
K_5^{(3)}.
\]

It is both edge-minimal and vertex-minimal. There are no unsatisfiable instances on at most four vertices.

**Status:** `COMPUTATIONAL / CHECKED`.

## Named obstruction certificates

### `K_5^(3)`

- vertices: `5`;
- edges: `10`;
- degree sequence: `(6,6,6,6,6)`;
- pair codegree: every pair has codegree `3`;
- connected, regular, nonlinear;
- all `10` edge deletions have stored lexicographically least witnesses;
- all `5` vertex deletions have stored lexicographically least witnesses;
- both minimality predicates independently verify.

### Fano plane

- vertices: `7`;
- edges: `7`;
- degree sequence: `(3,3,3,3,3,3,3)`;
- pair codegree: every pair has codegree `1`;
- connected, regular, linear;
- all `7` edge deletions have stored lexicographically least witnesses;
- all `7` vertex deletions have stored lexicographically least witnesses;
- both minimality predicates independently verify.

The Fano plane's edge-minimal non-two-colourability is also recorded in the primary literature. The project does not rely on the name: it independently enumerates all colourings and verifies every deletion certificate.

## Exact all-ordering profile evidence

Every permutation is included:

| Obstruction | Orderings | Classes per level | Total classes | Boundary width | Profile bytes |
|---|---:|---:|---:|---:|---:|
| `K_5^(3)` | `120` | `1` | `6` | `4` | `2280` |
| Fano plane | `5040` | `1` | `8` | `6` | `3425` |

Profile sequence digests:

- `K_5^(3)`: `928209993696b4033dd5da339642236f110708d229d1dac98f0e78228639d405`;
- Fano: `a9df380a61f17bcaee6f40d956914bc400ab3796473d85220dcb246c6798864a`.

### Interpretation

This is the central VS-05 finding.

For an unsatisfiable instance, no prefix has a satisfying full completion. Therefore every exact completion set is empty, at every level and under every ordering. VS-03 consequently collapses every prefix to one dead semantic class.

The exact completion quotient correctly detects rejection at the root but does not explain why rejection occurs or distinguish dense from sparse minimal obstructions internally.

This is not a defect in VS-03: it follows exactly from its definition. It is a limitation of using only successful full completions as the semantic observable. VS-06 must therefore test richer local summaries or failure semantics rather than expecting the accepting-completion quotient alone to expose obstruction structure.

## Deterministic record

Format: `nae3-vs05-obstruction-atlas-v1`.

Payload SHA-256:

```text
e620f0bf57330223f35c52bb3a6d4d84758c0ed9732930a7523aa83f0e2aa2ec
```

The committed record contains:

- all `1045` small-domain decisions and aggregate minimality counts;
- all deletion certificates for both named obstructions;
- complete structural evidence;
- all-ordering aggregate distributions and sequence digests;
- explicit finite-domain and complexity limitations.

## Complexity audit

The atlas is deliberately not an efficient general algorithm.

- exact decisions inherit the exponential VS-02 oracle;
- edge-minimality requires one exact solve per edge deletion;
- vertex-minimality requires one exact solve per vertex deletion;
- all-ordering profiles require `n!` exact VS-03 constructions;
- the Fano profile census includes `5040` orderings;
- the output stores aggregate ordering evidence, not all full profiles;
- no exponential or factorial quantity is called polynomial.

## Independent break pass

Checked attacks:

- satisfiable inputs are rejected by certificate producers;
- missing and malformed edges and vertices are rejected;
- edge and vertex minimality are not conflated;
- every certificate witness is independently verified and compared with the true lexicographically least reference witness;
- the full `n<=5` generator is independently enumerated;
- dense and sparse structural invariants are independently recomputed;
- all ordering counts equal `5!` and `7!`;
- canonical atlas bytes reproduce across Python 3.11, 3.12, and 3.13;
- VS-01 through VS-04 remain green.

No unresolved substantive defect remains.

## Claim boundary

VS-05 does not classify all critical 3-uniform hypergraphs, exhaust six or seven vertices, establish asymptotic quotient growth, prove a compression lower bound, or change the status of `P` versus `NP`.
