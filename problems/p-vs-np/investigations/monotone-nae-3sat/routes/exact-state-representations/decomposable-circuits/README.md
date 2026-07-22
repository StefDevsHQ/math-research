# R1.4 — Decomposable Circuit Representations

**Subroute:** `R1.4`  
**Status:** `CANDIDATE / NOT ACTIVATED`

## Thesis

Represent residual completion functions by structured deterministic decomposable circuits so that independent residual components can be composed while repeated semantic subproblems are shared.

Candidate languages include explicitly selected forms of deterministic decomposable negation normal form or structured decomposable circuits.

## Required properties

A selected model must provide:

- exact represented semantics;
- polynomial-time restriction;
- exact conjunction over compatible components;
- deterministic or canonical equality adequate for memoization;
- polynomial-time acceptance;
- complete node and edge encoding;
- a bound on all generated circuits, not only one residual.

## Main opportunities

- decomposability may exploit disconnected or weakly coupled residual components;
- shared subcircuits may capture semantic merges missed by PCRNF syntax;
- a fixed structural decomposition may make transition costs explicit.

## Main risks

- noncanonical circuits do not give cheap exact equality;
- minimization or equivalence may hide hard semantic work;
- determinism and decomposability can cause exponential blow-up;
- small individual circuits do not imply a polynomial total computation graph.

## First attacks

- VS-08 five-vertex equal-semantics/different-PCRNF pair;
- fan bad and good orderings;
- disconnected products;
- high-width satisfiable controls;
- reduction-generated instances.

## Activation gate

Choose one circuit language and one structural discipline. Do not activate a generic “knowledge compilation” route without fixed syntax, operations, size measure, and stop conditions.