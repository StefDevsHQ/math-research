# Vertical Slices — Monotone NAE-3SAT

**Purpose:** Authoritative execution order and progress ledger.  
**Updated:** 2026-07-22

Every slice is governed by the [building-block quality gate](BUILDING-BLOCK-GATE.md). A dependent slice may begin only when every prerequisite is `COMPLETE / CHECKED` or stronger.

## Progress summary

| Slice | Name | Status | Current result | Next action |
|---:|---|---|---|---|
| `VS-01` | Canonical instance model | `COMPLETE / CHECKED` | Canonical labelled model, strict parsing, serialization, components, relabelling, and witness verification. | Preserve. |
| `VS-02` | Exact small-instance oracle | `COMPLETE / CHECKED` | Exact decision, least witnesses, listing, counting, factorization, generator, and finite census. | Preserve as ground truth. |
| `VS-03` | Exact extension-profile engine | `COMPLETE / CHECKED` | Exact completion masks, semantic classes, transitions, boundary metrics, and profile census. | Preserve as semantic reference. |
| `VS-04` | Control calibration | `COMPLETE / CHECKED` | Graph parity, affine XOR, incidence forests, bounded boundaries, and disconnected products. | Use as controls only. |
| `VS-05` | Minimal obstruction atlas | `COMPLETE / CHECKED` | `K_5^(3)`, Fano certificates, all-ordering profiles, and dead-quotient theorem. | Preserve as obstruction baseline. |
| `VS-06` | Destroy naive summaries | `COMPLETE / CHECKED` | Ten explicit collisions and a proved fixed-radius locality-failure family; exact boundary assignment retained. | Preserve as falsification baseline. |
| `VS-07` | Measure semantic merging | `COMPLETE / CHECKED` | Genuine all-live merges, exact symmetry separation, exhaustive `n<=4` census, and fan ordering-separation theorem. | Use to define VS-08 representation. |
| `VS-08` | Extract first atomic invariant | `READY` | Residual exact merging exists, but no representation language is selected. | Specify and attack one exact residual representation. |
| `VS-09` | Prove restricted theorem | `PARTIAL` | Bounded-boundary and incidence-forest theorems are checked. | Extend only after VS-08. |
| `VS-10` | Attack with hard families | `BLOCKED` | Hard controls are registered. | Attack a checked VS-08 invariant. |
| `VS-11` | Global complexity audit | `BLOCKED` | Audit criteria exist. | Count the complete computation graph of a candidate. |
| `VS-12` | Route decision | `BLOCKED` | Claim discipline is prepared. | Decide after VS-08 through VS-11. |

## Trusted laboratory — VS-01 through VS-07

**Status:** `COMPLETE / CHECKED`.

The laboratory exports canonical instances, exact finite solving, exact fixed-order completion semantics, tractable controls, obstruction and summary-collision atlases, and exact live semantic-merging measurements. It exports no universal polynomial algorithm or general representation lower bound.

## VS-06 retained boundary

The committed collision atlas destroys ten explicit summaries and the fixed-radius theorem destroys every constant locality radius in the stated residual graph model. Exact boundary assignment remains complete but may expose `2^w` states.

Evidence: [VS-06 implementation](VS-06-IMPLEMENTATION.md) and [VS-06 audit](VS-06-AUDIT.md).

## VS-07 — Measure genuine semantic merging

**Exit gate:** satisfied.

### Separated quantities

The executable measurement distinguishes:

1. raw prefixes;
2. live and dead prefixes;
3. exact live and dead classes;
4. component-complement prefix orbits;
5. semantic mask orbits under suffix complement;
6. genuine exact merges across prefix-orbit boundaries;
7. processed-valid and live boundary states;
8. reference representation bytes;
9. ordering dependence.

### First genuine all-live merge

For the instance with edges `{012,013}`, ordering `(0,2,3,1)`, and level three, the eight completion masks are

```text
2,2,2,3,3,1,1,1.
```

All prefixes are live. Three exact classes merge four prefix complement orbits into two semantic complement orbits. This is finite checked evidence, not an asymptotic theorem.

### Fan ordering-separation theorem

For `F_k` with edges `{c,a_i,b_i}`:

- order `c,a_1,...,a_k,b_1,...,b_k` has `2^(k+1)-1` live exact classes at level `k+1` and `2^k` symmetry-normalized semantic orbits;
- no exact class at that level merges distinct prefix complement orbits;
- the interleaved order `c,a_1,b_1,...,a_k,b_k` has boundary width at most two and at most four live exact classes.

Therefore exponential fixed-order growth can be entirely ordering-induced. This does not lower-bound all orderings or symbolic representations.

### Finite exhaustive census

Every labelled instance and every ordering through four vertices is included. The record contains 384 four-vertex profiles and 96 all-live levels with genuine cross-orbit exact merging.

Evidence: [VS-07 implementation](VS-07-IMPLEMENTATION.md), [VS-07 audit](VS-07-AUDIT.md), deterministic semantic-merging record, and independent exact tests.

## VS-08 — Extract first atomic invariant

State one falsifiable representation language with:

- exact semantics;
- construction and canonical equality;
- restriction, transition, conjunction, and merge;
- acceptance;
- encoded size;
- proposed total-state bound;
- tractable controls;
- adversarial high-width and reduction-generated families;
- a precise stop condition.

The recommended first target is residual-constraint normalization under component complement, because VS-07 demonstrates genuine future-equivalence merging not explained by direct boundary equality while also showing that complement symmetry alone can be exponentially insufficient.

## VS-09 through VS-12

- `VS-09`: prove any surviving invariant first on its largest exact restricted class.
- `VS-10`: attack with Fano, linear 4-regular, high-width, and reduction-generated controls.
- `VS-11`: audit input length, construction, equality, transitions, branching, complete state graph, and total representation size.
- `VS-12`: retain a universal candidate, restricted theorem, model-specific barrier, disproof, or closeout.

## Immediate queue

1. Preserve `VS-01` through `VS-07` without expanding completed-slice scope.
2. Execute `VS-08` only after writing the full atomic representation contract.
3. Do not infer tractability from semantic merging or hardness from a bad ordering.

Computational results remain `COMPUTATIONAL` unless accompanied by a proof or complete exhaustiveness argument.
