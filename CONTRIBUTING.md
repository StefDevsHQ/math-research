# Contributing

Contributions should make the research state easier to verify.

## Before contributing

1. Read [Research Standards](RESEARCH_STANDARDS.md).
2. Locate the nearest `README.md`, `STATUS.md`, and `CLAIMS.md`.
3. Identify the record type: definition, proof, counterexample, audit, experiment, note, citation, or administration.
4. Open or reference a focused issue when the work is substantial.

## Where work belongs

- Shared definitions and established results: `foundations/`
- Reusable reductions: `reductions/`
- Concrete test environments: `investigations/`
- Distinct approaches: `routes/<route>/`
- Complete arguments: `proofs/`
- Refutations: `counterexamples/`
- Adversarial stress tests: `audits/`
- Reproducible computation: `experiments/`
- Incomplete reasoning: `notes/`
- Dated operational handoffs: `journal/`

Do not use a note or session handoff as the only durable record of a mathematical result.

## Pull requests

Keep one main research purpose per pull request. Include:

- the exact claim or question affected;
- what changed and why;
- where the argument or evidence lives;
- dependencies and primary citations;
- unresolved gaps;
- any mathematical-status or review-maturity changes.

Documentation may improve without changing claim status. A status change requires corresponding evidence and a ledger update.

## Review

Review the mathematics before style. Check assumptions, quantifiers, imported results, edge cases, encoding size, complexity accounting, and whether computation is being mistaken for proof.

Use comments for local defects. Request changes when a claim is unsupported. Preserve rejected approaches when they remain useful to the research history.

## Licensing

By contributing, you agree that your contribution is licensed under the license governing its destination path:

- research content and templates: CC BY 4.0;
- executable material under `tools/`: MIT.

Identify all third-party material and its license. See [LICENSES.md](LICENSES.md).

## Commit messages

Use concise messages such as:

- `docs: define subset sum investigation scope`
- `proof: add residue-completion lemma`
- `counterexample: refute bundle lemma`
- `audit: test structural compression against SAT reduction`
- `experiment: test bounded-modulus instances`
- `status: close structural-compression route`