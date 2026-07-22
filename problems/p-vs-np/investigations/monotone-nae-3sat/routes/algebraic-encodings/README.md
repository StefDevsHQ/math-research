# R3 — Algebraic Encodings

**Operational status:** `CANDIDATE / NOT ACTIVATED`

## Thesis

Translate Monotone NAE-3SAT exactly into an algebraic object whose satisfiability, restriction and composition can be decided in polynomial total time.

## Subroute registry

| ID | Subroute | Status | Central question |
|---|---|---|---|
| `R3.1` | XOR and affine structure | `CONTROL / RESTRICTED` | Which residual classes become exact affine systems? |
| `R3.2` | Finite-field polynomial systems | `CANDIDATE` | Can low-degree algebra preserve NAE exactly with polynomial elimination state? |
| `R3.3` | Integer and polyhedral formulations | `CANDIDATE` | Can `1 <= x+y+z <= 2` be solved exactly without exponential branching or nonintegral relaxation gaps? |
| `R3.4` | Cut and signed-graph formulations | `CANDIDATE` | Can hypergraph two-colouring be converted to a tractable exact cut object? |
| `R3.5` | Ideal or canonical algebraic normal forms | `CANDIDATE` | Can semantic equivalence be canonicalized with polynomial construction and representation size? |

## Exactness obligations

Every transformation must be proved in both directions. Relaxations, rounding, randomization, case splits and elimination must include their complete computation graph and encoded intermediate size.

## Mandatory controls

- recover XOR-SAT without unnecessary blow-up;
- separate rank-two graph bipartiteness from ternary hardness;
- survive Fano and `K_5^(3)`;
- preserve reduction-generated clause compatibility;
- compare algebraic equality with the VS-08 five-vertex semantic merge.

## Main risks

- exact polynomial systems can require exponential Gröbner or elimination structure;
- a compact equation system can leave satisfiability NP-hard;
- linear or convex relaxations may admit false solutions;
- branching needed to restore exactness may be exponential.

## Activation gate

Select one field, ring or polyhedral language, state the exact algorithmic operations and size measure, and specify a first falsification family.