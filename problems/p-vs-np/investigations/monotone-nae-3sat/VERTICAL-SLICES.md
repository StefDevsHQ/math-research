# Vertical Slices — Monotone NAE-3SAT

**Purpose:** Authoritative execution order and progress ledger.  
**Updated:** 2026-07-23

Every slice is governed by the [building-block quality gate](BUILDING-BLOCK-GATE.md). Route ownership is recorded in the [route registry](routes/README.md).

## Progress summary

| Slice | Name | Status | Route ownership | Determination |
|---:|---|---|---|---|
| `VS-01` | Canonical instance model | `COMPLETE / CHECKED` | Shared laboratory | Preserve. |
| `VS-02` | Exact small-instance oracle | `COMPLETE / CHECKED` | Shared laboratory | Preserve as ground truth. |
| `VS-03` | Exact extension-profile engine | `COMPLETE / CHECKED` | `R1` foundation | Preserve as semantic reference. |
| `VS-04` | Control calibration | `COMPLETE / CHECKED` | `R2`, `R3`, `R5` controls | Preserve. |
| `VS-05` | Minimal obstruction atlas | `COMPLETE / CHECKED` | `R4`, `R6` evidence | Preserve. |
| `VS-06` | Destroy naive summaries | `COMPLETE / CHECKED` | `R4`, `R6` barriers | Preserve as falsification baseline. |
| `VS-07` | Measure semantic merging | `COMPLETE / CHECKED` | `R1`, `R2`, `R6` evidence | Preserve. |
| `VS-08` | Exact PCRNF construction | `COMPLETE / CHECKED` | `R1.1` | Retain `NAE-017`. |
| `VS-09A` | Universal PCRNF state bound | `COMPLETE / CHECKED` | `R1.1`, `R6` | `NAE-016` disproved by `NAE-020`. |
| `VS-09B` | Collective exact representation selection | `COMPLETE / CHECKED` | `R1.2`, `R1.4` | DNNF selected as the precise collective candidate. |
| `VS-10` | Attack selected representation | `COMPLETE / CHECKED` | `R1.4`, `R6` | `NAE-021` proves exponential DNNF size. |
| `VS-11` | Global complexity audit | `COMPLETE / CHECKED` | `R1.4`, `R6` | Arity, degree, treewidth, conditioning, circuit size, and binary encoding audited. |
| `VS-12` | Route decision | `COMPLETE / CHECKED` | `R1` | Universal exact-representation programme closed; restricted results retained. |

## Trusted laboratory — VS-01 through VS-08

**Status:** `COMPLETE / CHECKED`.

The laboratory includes canonical instances, exact profiles, controls, obstruction evidence, summary collisions, semantic-merging measurements, and exact residual syntax.

## VS-09A — all-ordering PCRNF attack

For a constant-degree expander graph `G`, form the central lift with hyperedges `{c,u,v}` for every graph edge `{u,v}`.

For every ordering, a balanced prefix cut and a linear crossing induced matching produce `2^{Omega(n)}` live prefixes with pairwise distinct exact completion functions. By `NAE-019`, the PCRNF state count is at least this large.

```text
NAE-016 — DISPROVED / CHECKED
NAE-019 — PROVED / CHECKED
NAE-020 — PROVED / CHECKED
```

Proof: [NAE-016 expander disproof](routes/exact-state-representations/pcrnf/proofs/NAE-016-expander-disproof.md).

## VS-09B through VS-11 — DNNF selection and attack

DNNF was selected as the precise collective representation candidate because decomposability can share subcircuits across many distinct residual functions.

The same central-lift family defeats the candidate:

1. conditioning the centre to zero produces the monotone two-CNF `and_{{u,v} in E(G)} (u or v)`;
2. conditioning preserves DNNF and does not increase size;
3. constant-degree edge expanders have linear treewidth;
4. the established monotone-CNF compilation theorem gives DNNF size exponential in treewidth;
5. the lifted input has binary encoding length `L=O(n log n)`.

Therefore every DNNF for the central lift has size

```text
2^{Omega(n)} = 2^{Omega(L/log L)}.
```

```text
NAE-021 — PROVED / CHECKED
```

Proof: [NAE-021 DNNF lower bound](routes/exact-state-representations/decomposable-circuits/proofs/NAE-021-dnnf-expander-lower-bound.md).

## VS-12 — final route decision

The following universal mechanisms are closed:

- ordered PCRNF state enumeration;
- one-state-per-residual-function semantic quotients;
- reduced ordered decision diagrams;
- DNNF and all DNNF subclasses.

The following remain outside the proved barriers:

- unrestricted Boolean circuits;
- arbitrary non-DNNF collective structures;
- algebraic global methods;
- arbitrary algorithms.

`NAE-006` remains a conjecture but is dormant pending a materially new fixed representation language. Restricted PCRNF, bounded-width compilation, incidence-forest colouring, and decomposition classification remain retained secondary programmes.

## Reopening controls

Any reopened universal candidate must:

- specify exact syntax, semantics, operations, and total size;
- explain why `NAE-020` and `NAE-021` do not apply;
- face the semantic-merge and PCRNF witnesses;
- face both fan orderings, Fano, `K_5^(3)`, linear four-regular instances, collision pairs, and reduction-generated controls.

## Scope

The closeout is model-specific. It proves neither `P=NP` nor `P!=NP` and does not lower-bound arbitrary circuits or algorithms.
