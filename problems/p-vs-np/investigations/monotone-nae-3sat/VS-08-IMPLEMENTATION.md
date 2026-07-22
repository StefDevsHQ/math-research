# VS-08 Implementation — Oriented PCRNF

**Status:** `COMPLETE / CHECKED`  
**Updated:** 2026-07-23

## Modules

- `nae3sat/pcrnf.py` — immutable residual objects, closure, orientation, transition, evaluation, serialization, traversal and exact-profile comparison.
- `nae3sat/pcrnf_atlas.py` — deterministic finite attack record.
- `nae3sat/pcrnf_validation.py` — strict record-envelope verifier.
- `nae3sat/pcrnf_cli.py` — atomic record writer.
- `tests/test_vs08.py` — independent exactness, orientation, incompleteness, fan, obstruction and byte-reproduction tests.

## Canonical object

A `SignedResidual` stores:

- sorted remaining original vertex labels;
- contradiction;
- sorted residual components.

Each `ResidualComponent` stores:

- sorted labelled vertices;
- one orientation bit;
- sorted unary records `(v,c)`;
- sorted signed binary records `(u,v,c)` representing `not(x_u=x_v=c)`;
- sorted ternary NAE records.

The orientation bit is part of equality. It records how canonical component colours map back to original labelled colours.

## Closure

Closure repeatedly:

1. applies unary requirements;
2. simplifies signed binaries;
3. lowers or deletes ternary constraints;
4. detects contradictory forces or violated constraints;
5. removes duplicates;
6. extracts residual incidence components;
7. selects the lexicographically smaller component payload under simultaneous complement while retaining the chosen orientation bit.

The process terminates because every rewrite deletes a constraint, lowers arity, or adds a previously absent unary force.

## Exact operations

- `build_pcrnf(instance, ordering, prefix)` constructs the direct closed residual.
- `transition_pcrnf(residual, vertex, colour)` restricts one variable and re-closes.
- `satisfies_pcrnf` evaluates a full remaining labelled assignment.
- `pcrnf_completion_mask` provides the exact finite semantic oracle.
- `traverse_pcrnf` builds the memoized level graph.
- `compare_pcrnf_profile` compares PCRNF equality with VS-03 exact completion equivalence.

## Reproduction

```bash
python3 -m nae3sat.pcrnf_cli --output /tmp/vs08.json
cmp /tmp/vs08.json pcrnf/vs08-pcrnf-attack.json
```

The full repository gate performs this comparison and runs all VS-08 tests.

## Complexity

One residual has polynomial explicit size in the original encoded instance. This does not imply polynomial traversal: the number of reachable residuals may be exponential. The implementation counts complete canonical JSON bytes for every unique state at each level.

## Decision

The implementation is retained as an exact reference representation. PCRNF byte equality is not promoted as exact semantic equivalence, and the universal polynomial-state conjecture is retracted.
