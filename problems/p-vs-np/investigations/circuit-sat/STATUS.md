# Status — Circuit-SAT Algorithms to Lower Bounds

**Phase:** consequence-map construction and circuit-model selection  
**Updated:** 2026-07-23

## Current position

The investigation is open in orientation and verification mode.

`CS-VS-01 — Exact consequence map` is active. No circuit class or algorithmic route is selected.

## Current objective

Construct a primary-source map of statements of the form:

```text
specified SAT or #SAT improvement for circuit class C
implies
specified nonuniform lower bound against C or a related class.
```

The map must verify all class-closure, runtime, size, depth, randomness and uniformity hypotheses before recommending a target.

## Accepted state

- The Circuit-SAT algorithms-to-lower-bounds programme is a known research framework.
- Class-specific successes exist, including ACC and composed threshold classes.
- These successes do not automatically transfer to unrestricted Boolean circuits or other circuit classes.
- No project-original algorithmic or lower-bound claim has yet been accepted.

## Active slice

### CS-VS-01

Deliver:

- an exact theorem matrix;
- primary citations;
- a distinction between SAT, #SAT and approximate counting;
- the required savings for each transfer;
- current best algorithms;
- one recommended circuit class;
- one rejected or deferred alternative with reasons;
- a route stop condition.

## Blockers

`CS-VS-02` and all implementation work remain blocked until:

1. one circuit class is selected;
2. its exact encoding is fixed;
3. the transfer theorem is verified;
4. a candidate atomic mechanism is stated.

## Immediate next document

Create `CS-VS-01-CONSEQUENCE-MAP.md`.

## Scope boundary

This investigation currently contains workflow definitions and literature-orientation claims only. It does not claim a faster SAT algorithm or a new circuit lower bound.