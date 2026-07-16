# P versus NP Research-Programme Landscape

**Classification:** Literature audit and top-level route-selection framework  
**Cutoff:** 2026-07-16  
**Review:** `CHECKED` by source, implication, scope, and canonical-identifier audit  
**Scope:** Classical deterministic P versus NP unless a row explicitly states another class, model, promise, or conditional hypothesis

## Purpose

This document records the major research programmes relevant to P versus NP and clarifies how this repository uses concrete testbeds. It is complete at the level of major paradigms, not every model, proof system, parameter, or paper.

All source identifiers resolve through the single [canonical source map](top-level-landscape-sources.md).

## Repository method

The repository uses a **testbed-and-audit method**:

1. choose a concrete problem whose native representation exposes a candidate mechanism;
2. state the strongest exact claim and the precise class consequence;
3. distinguish encoded-input polynomial time from pseudopolynomial, parameterized, average-case, promise, randomized, or heuristic performance;
4. prove correctness in both directions and count the complete computation graph;
5. attack the mechanism with canonical reductions, tractable neighbours, and expressiveness controls;
6. retain local theorems, retract unsupported universal claims, and close a route when its pass condition fails.

A deterministic polynomial-time algorithm for one NP-complete language proves \