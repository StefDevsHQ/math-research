# R1.2 — Collective Exact Representation over PCRNF

**Subroute:** `R1.2`  
**Status:** `REFORMULATION REQUIRED`  
**Dependencies:** `NAE-017`, `NAE-019`, `NAE-020`

## Original objective

The original proposal was to construct a polynomial-time exact equivalence or canonicalization over oriented PCRNF residuals that identifies semantically equal but byte-distinct states.

That objective is no longer sufficient.

`NAE-020` gives instances where every ordering has exponentially many pairwise semantically distinct live residual functions. No exact quotient that stores one state per semantic class can reduce this to polynomially many states.

## Surviving objective

Construct a polynomial-size collective object that represents or shares structure across many distinct exact residual functions without materializing each residual function as an individual traversal state.

Possible mechanisms include:

1. deterministic decomposable circuits;
2. non-ordered decision structures with global sharing;
3. algebraic objects representing families of residual functions;
4. exact decomposition interfaces that combine many residual states symbolically;
5. another explicitly defined collective representation.

## Required distinction

The route must distinguish:

```text
number of distinct residual functions
```

from

```text
size of one collective representation of all required residual behaviour.
```

`NAE-020` proves the first quantity can be exponential under every ordering. It does not prove that every collective representation of those functions is exponentially large.

## Exact obligations

A surviving candidate must specify:

- represented semantics;
- how multiple distinct residual functions share one structure;
- exact restriction, transition, or composition;
- acceptance;
- construction and equality costs;
- complete binary encoding;
- maximum and total representation size;
- whether any step silently enumerates all residual functions.

## Hard controls

- central lifts of constant-degree expanders from `NAE-020`;
- VS-07 four-vertex genuine merge;
- VS-08 five-vertex byte-equality failure;
- both fan orderings;
- `K_5^(3)` and Fano;
- VS-06 collision pairs;
- linear four-regular instances;
- verified canonical reduction outputs.

## Stop conditions

Close a candidate when:

1. it enumerates one object per exact residual function;
2. its collective representation is superpolynomial on the `NAE-020` family;
3. equality or minimization requires an NP-hard hidden primitive;
4. transition or composition expands to superpolynomial total size;
5. it reduces only to an already known restricted-width method.

## Promotion condition

Promote only after proving exactness and a polynomial bound on the complete collective representation and all generated intermediate objects. Finite compression evidence alone is insufficient.