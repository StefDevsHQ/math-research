# R6 — Representation-Specific Barriers

**Operational status:** `BARRIER PROGRAMME / NOT A P VERSUS NP PROOF ROUTE`

## Thesis

Prove explicit lower bounds or model boundaries for precisely defined exact representation and algorithm families.

This route may explain why a proposed mechanism fails. It cannot establish `P != NP` without a theorem connecting the restricted model to all polynomial-time algorithms.

## Subroute registry

| ID | Subroute | Status | Existing or proposed boundary |
|---|---|---|---|
| `R6.1` | Naive summary barriers | `COMPLETE / CHECKED` | VS-06 gives ten explicit same-summary/different-semantics collisions. |
| `R6.2` | Fixed-radius locality barrier | `PROVED / CHECKED` | `NAE-012` defeats every fixed-radius residual neighbourhood summary. |
| `R6.3` | PCRNF byte-equality boundary | `DISPROVED / CHECKED` | `NAE-018` shows exact semantics can merge byte-distinct PCRNFs. |
| `R6.4` | Ordered state-growth lower bounds | `PARTIAL` | Fan bad ordering has exponential exact and PCRNF state growth. |
| `R6.5` | Decision-diagram or circuit lower bounds | `CANDIDATE` | Require a fixed model and explicit family. |
| `R6.6` | Every-ordering lower bounds | `OPEN / HIGH BAR` | Needed to refute existential ordering claims such as `NAE-016`. |

## Proof obligations

A barrier theorem must specify:

- the exact representation or algorithm model;
- permitted preprocessing and ordering choices;
- equality and transition operations;
- input and representation encoding;
- the explicit hard family;
- the quantified lower bound;
- what broader models, if any, are subsumed with polynomial overhead.

## Prohibited inferences

- one bad ordering does not imply every ordering is bad;
- failure of one canonical form does not lower-bound all symbolic representations;
- exponentially many exact semantic classes do not automatically imply large circuits;
- a model-specific lower bound does not prove `P != NP`.

## Relationship to constructive routes

Every activated constructive subroute should register its likely barrier model here. Negative findings remain useful even when the constructive route closes.