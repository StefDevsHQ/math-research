# R5 — Propagation and Exact Branching

**Operational status:** `PARTIAL FOUNDATION / OPEN CANDIDATES`

## Thesis

Use exact forced-colour propagation and controlled branching to reduce the residual problem while proving that the complete branching and memoization graph is polynomially bounded.

## Subroute registry

| ID | Subroute | Status | Result or objective |
|---|---|---|---|
| `R5.1` | PCRNF propagation closure | `PROVED / RETAINED` | `NAE-017` proves exact deterministic closure and transition. |
| `R5.2` | Implication and signed-graph systems | `CANDIDATE` | Identify classes where conditional NAE implications become tractable graph structure. |
| `R5.3` | Measure-decreasing branching | `CANDIDATE` | Find a polynomial global bound, not merely polynomial depth. |
| `R5.4` | Memoized branching quotients | `CANDIDATE` | Merge branches by an exact semantic invariant stronger than syntax. |
| `R5.5` | Kernelization or preprocessing | `CANDIDATE` | Reduce every instance to polynomially bounded exact cores under a proved safe rule set. |

## Required accounting

For every branching proposal record:

- recursion depth;
- branching factor;
- repeated and distinct states;
- memoization key and equality cost;
- maximum and total residual size;
- complete runtime and space in binary input length.

Polynomial depth with binary branching is generally exponential.

## Mandatory attacks

- instances where no initial propagation occurs;
- cycles of conditional implications;
- alternative equal-pair choices inside one edge;
- fan bad ordering;
- high-width satisfiable instances;
- reduction gadgets preserving unresolved assignments.

## Stop conditions

Close or restrict a subroute when its progress measure permits exponentially many leaves, memoization equality is incomplete or intractable, preprocessing preserves an unbounded hard core, or the method collapses to bounded-width search.