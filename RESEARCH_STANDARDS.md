# Research Standards

These rules apply to every problem and research note in this repository.

## 1. Claim records

Every substantive claim must appear in the nearest `CLAIMS.md` ledger with:

- a stable identifier;
- a precise statement;
- mathematical status;
- review maturity;
- dependencies;
- evidence or proof location;
- known gaps or counterexamples.

### Mathematical status

| Status | Meaning |
|---|---|
| `ESTABLISHED` | External result supported by a primary citation. |
| `PROVED` | A complete proof is recorded in this repository. |
| `DISPROVED` | An explicit counterexample or contradiction is recorded. |
| `CONJECTURE` | Precise unresolved statement proposed for investigation. |
| `OPEN` | Required result or question with no current resolution. |
| `COMPUTATIONAL` | Supported only by finite computation or exhaustive search over a stated domain. |
| `HEURISTIC` | Strategic intuition or informal expectation. |
| `RETRACTED` | Previously recorded claim withdrawn, with the reason preserved. |

### Review maturity

| Review | Meaning |
|---|---|
| `DRAFT` | Not yet checked end to end. |
| `CHECKED` | Internally checked against definitions, dependencies, and edge cases. |
| `INDEPENDENTLY-CHECKED` | Checked by a contributor who did not produce the argument. |
| `EXTERNALLY-REVIEWED` | Reviewed outside this repository or through a recognized formal process. |

Mathematical status and review maturity are separate. A claim may be `PROVED / DRAFT`; this means a proof has been written, not that it is reliable or accepted.

## 2. Proof standard

A proof note must:

1. state the claim and all assumptions precisely;
2. define nonstandard notation;
3. identify every imported theorem and cite its source;
4. justify each nontrivial implication;
5. address boundary cases and quantifiers;
6. state whether the argument is constructive, existential, probabilistic, or computational;
7. list unresolved dependencies explicitly.

A proof by computation must also show why the checked domain is sufficient for the stated claim.

## 3. Counterexample standard

A counterexample must include:

- the exact claim being refuted;
- the complete instance;
- a direct verification that the hypotheses hold;
- a direct verification that the conclusion fails;
- the smallest or simplest known instance when practical.

Refuted routes remain in history and are marked `DISPROVED` or moved to an `archive/` directory with links from the claims ledger.

## 4. Computational work

Every experiment must record:

- question and tested claim;
- method or algorithm;
- input domain and generation procedure;
- software and dependency versions;
- command or entry point;
- output and interpretation;
- limitations.

Generated outputs should be reproducible from committed source where practical. Large or external data must be identified by a stable source and checksum.

## 5. Sources

Prefer primary sources: original papers, books, formal documentation, and authoritative datasets. Secondary explanations may aid orientation but should not carry a central mathematical claim.

Citations must identify the exact result used, not merely a related work. Record theorem numbers, page numbers, or stable section anchors when available.

## 6. Research state

Each active problem contains:

- `README.md`: scope, definitions, and map;
- `STATUS.md`: current position, blockers, and next action;
- `CLAIMS.md`: authoritative claim ledger.

`STATUS.md` is operational and may change often. `CLAIMS.md` is epistemic and changes only when a claim, proof, dependency, counterexample, or review state changes.

## 7. Change discipline

- Use lowercase kebab-case paths.
- Keep one main mathematical purpose per pull request.
- Do not silently strengthen or weaken a claim.
- Link corrections to the claim and note they replace.
- Preserve uncertainty; do not promote a result because it is promising.
- Use absolute dates in research records.

## 8. Open-problem restraint

For major open problems, repository work is exploratory unless and until a complete argument survives independent expert review. Repository labels are workflow metadata, not declarations of mathematical acceptance.
