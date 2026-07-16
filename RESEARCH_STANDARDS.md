# Research Standards

These rules apply to every problem, investigation, route, and research record.

## 1. Claim ledger

Every substantive claim belongs in the nearest `CLAIMS.md` with a stable ID, precise statement, mathematical status, review maturity, dependencies, evidence location, known gaps, and absolute updated date.

### Mathematical status

| Status | Meaning |
|---|---|
| `ESTABLISHED` | External result supported by a primary citation. |
| `PROVED` | A complete proof is recorded in this repository. |
| `DISPROVED` | An explicit counterexample or contradiction is recorded. |
| `CONJECTURE` | Precise unresolved statement proposed for investigation. |
| `OPEN` | Required result or question with no current resolution. |
| `COMPUTATIONAL` | Supported only over a stated finite domain. |
| `HEURISTIC` | Strategic intuition or informal expectation. |
| `RETRACTED` | Withdrawn claim whose history remains visible. |

### Review maturity

| Review | Meaning |
|---|---|
| `DRAFT` | Not checked end to end. |
| `CHECKED` | Internally checked against definitions and edge cases. |
| `INDEPENDENTLY-CHECKED` | Checked by someone who did not produce the argument. |
| `EXTERNALLY-REVIEWED` | Reviewed outside this repository or through a recognized formal process. |

Status and review are separate. `PROVED / DRAFT` means a proof has been written, not that it is accepted or reliable.

## 2. Repository model

```text
problem → investigation → route → atomic record
```

Shared foundations and reductions belong above individual investigations. Route-specific conclusions stay inside their route.

Atomic directories have distinct roles:

- `proofs/` — complete positive arguments;
- `counterexamples/` — explicit refutations;
- `audits/` — adversarial evaluations with pass conditions;
- `experiments/` — reproducible computation;
- `notes/` — incomplete exploratory work;
- `archive/` — superseded work retained for provenance;
- `journal/` — concise handoffs linking to durable records.

A note or handoff is never the sole authoritative location of a result.

## 3. Proof standard

A proof must state all assumptions and quantifiers, define notation, cite imported results, justify nontrivial implications, address boundary cases, identify its proof type, account for input encoding and complexity measures when algorithmic, and list unresolved dependencies.

A proof by computation must also establish why the checked domain is sufficient.

## 4. Counterexample standard

A counterexample must state the exact claim, give the complete instance, verify every hypothesis, show directly that the conclusion fails, and delimit the scope of the refutation.

## 5. Audit standard

An audit must define its target, adversarial family, pass condition, tested properties, complexity accounting, and a verdict of `survives`, `fails`, or `inconclusive`. An audit is not automatically a proof or counterexample.

## 6. Computational standard

Every experiment records its question, method, input domain, generation process, dependencies, command, output, interpretation, and limitations. Generated results should be reproducible from committed source where practical.

## 7. Sources and provenance

Prefer primary sources. Cite the exact theorem, page, or stable section used. Distinguish external results from repository-originated arguments.

Preserve failed routes, corrections, and superseded statements. Never silently strengthen, weaken, or rewrite a claim's history.

## 8. Research state

Each active problem, investigation, and route contains:

- `README.md` — scope and navigation;
- `STATUS.md` — current position, blockers, and next action;
- `CLAIMS.md` — authoritative claim ledger.

`STATUS.md` is operational. `CLAIMS.md` changes only when the epistemic state changes.

## 9. Change discipline

- Use lowercase kebab-case paths.
- Keep one main mathematical purpose per pull request.
- Update the relevant ledger with every status change.
- Link corrections to the records they replace.
- Use absolute dates.
- Track binary input length, not only numerical magnitude, in complexity work.
- Preserve uncertainty.

## 10. Open-problem restraint

Work on major open problems remains exploratory unless a complete argument survives independent expert review. Repository labels are workflow metadata, not declarations of mathematical acceptance.