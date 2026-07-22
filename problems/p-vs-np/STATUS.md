# Status — P versus NP

**Phase:** Monotone NAE-3SAT VS-07 complete; atomic representation selection next  
**Updated:** 2026-07-22

## Current position

The repository foundation and canonical landscapes are complete. The active Monotone NAE-3SAT investigation has completed `VS-01` through `VS-07` as checked infrastructure, falsification, and semantic-measurement work. No proof route, universal polynomial-time mechanism, or general representation lower bound has been accepted.

The Subset Sum investigation remains closed after two universal strategies failed within their stated models.

## Active investigation

[Monotone NAE-3SAT](investigations/monotone-nae-3sat/README.md) now provides:

- canonical labelled instances;
- an exact exponential oracle and exhaustive `n<=5` census;
- exact successful-completion profiles for fixed orderings;
- calibrated parity, affine, acyclic, bounded-boundary, and component controls;
- exact `K_5^(3)` and Fano obstruction evidence;
- the dead-successful-completion theorem for globally unsatisfiable instances;
- ten explicit same-summary/different-semantics collisions;
- a proved family showing every fixed locality radius can miss conditioned residual satisfiability;
- exact measurements separating live semantic merging from dead collapse, complement symmetry, boundary states, representation bytes, and ordering effects;
- a proved fan family with exponential live quotient growth under one order and constant-width behaviour under another;
- finite exhaustive evidence of genuine all-live merging beyond complement-related prefix identification.

These results constrain specified mechanisms only. They do not lower-bound arbitrary exact representations.

## Current mathematical target

Execute `VS-08`: define one atomic residual representation language motivated by the genuine merging observed in VS-07.

Before implementation, the candidate must specify:

- exact represented semantics;
- canonical equality;
- restriction, transition, conjunction, and merge;
- acceptance;
- encoded size;
- proposed polynomial global state bound;
- tractable controls;
- adversarial high-width and reduction-generated families;
- a stop condition.

The recommended first target is residual-constraint normalization under component complement. Complement symmetry alone is insufficient on the bad-order fan family, so the candidate must also explain the additional all-live merging seen in the four-vertex witness.

## Mandatory controls

- graph 2-colouring;
- XOR-SAT;
- acyclic and bounded-width CSPs;
- Positive 1-in-3 SAT;
- canonical 3-SAT reductions;
- linear 4-regular Monotone NAE-3SAT;
- dense `K_5^(3)` and sparse linear Fano obstructions;
- the VS-06 collision atlas;
- the VS-07 first genuine merge and fan ordering-separation family.

## Retained Subset Sum results

- the residue-completion lemma;
- polynomial-time solvability under an efficiently constructible exact decomposition with polynomial total encoded state;
- assignment-target embeddings and ordered-model lower bounds;
- exact Minkowski composition identities;
- representation-boundary theorems.

No retained result proves `P=NP`, `P!=NP`, a general circuit lower bound, or a lower bound for arbitrary Subset Sum or Monotone NAE-3SAT algorithms.

## Next decision

Open `VS-08` only with a complete atomic representation contract. If no candidate can explain the first genuine merge while surviving the fan, Fano, linear 4-regular, and reduction-generated controls, close or pivot rather than preserving an undefined compression narrative.
