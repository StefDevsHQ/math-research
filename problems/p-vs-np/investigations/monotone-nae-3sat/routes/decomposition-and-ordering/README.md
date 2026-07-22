# R2 — Decomposition and Ordering

**Operational status:** `RESTRICTED RESULTS / OPEN CANDIDATES`

## Thesis

Exploit a polynomial-time constructible processing order or decomposition whose complete exact interface state is polynomially bounded.

This route includes ordinary width only as a baseline. A universal result requires more than defining a new width parameter: every input must admit an efficiently constructible decomposition with polynomial total state.

## Subroute registry

| ID | Subroute | Status | Result or objective |
|---|---|---|---|
| `R2.1` | [Boundary-width dynamic programming](boundary-width/README.md) | `PROVED / RESTRICTED` | `NAE-005`: time and space `2^{O(w)} poly(L)`. |
| `R2.2` | [Incidence-forest decomposition](incidence-forest/README.md) | `PROVED / RESTRICTED` | `NAE-008`: constructive linear-incidence-time colouring. |
| `R2.3` | [Beyond-width exact decomposition](beyond-width/README.md) | `READY / OPEN` | Prove PCRNF or exact-interface polynomial state under structural hypotheses stronger than the known controls. |
| `R2.4` | Semantic-state ordering algorithms | `CANDIDATE` | Construct orders controlling exact semantic or representation state rather than only boundary size. |

## Central obligation

Track the complete computation graph. Polynomial decomposition depth and polynomial local state do not imply polynomial total work.

## Mandatory attacks

- fan bad-versus-good ordering separation;
- high-width satisfiable instances;
- linear four-regular hard instances;
- reduction-generated logical compatibility;
- examples where decomposition components retain correlated choices.

## Stop conditions

A subroute is restricted or closed when:

- the parameter is unbounded on hard instances;
- finding the decomposition is itself intractable;
- the exact interface has exponential state;
- the method reduces to known bounded-width dynamic programming;
- cross-component compatibility invalidates local composition.

## Relationship to R1

`R2` supplies orderings and decompositions. `R1` supplies symbolic exact state. A combined claim must account for both costs and must not count either layer twice.