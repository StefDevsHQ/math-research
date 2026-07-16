# Contributing

Contributions should make the research state easier to verify.

## Before changing a claim

1. Read [Research Standards](RESEARCH_STANDARDS.md).
2. Locate the nearest `CLAIMS.md` ledger.
3. Identify whether the change concerns a definition, proof, counterexample, experiment, citation, or review state.
4. Open or reference a focused issue when the work is substantial.

## Pull requests

Keep one main research purpose per pull request. Include:

- the exact claim or question affected;
- what changed;
- where the argument or evidence lives;
- dependencies and citations;
- unresolved gaps;
- any claim-status or review-status changes.

A pull request may improve documentation without changing mathematical status. Status changes require corresponding evidence in the repository.

## Review

Review the mathematics before style. Check assumptions, quantifiers, imported results, edge cases, and whether computation is being mistaken for proof.

Use comments for local defects. Use a requested change when the claim cannot currently be supported. Preserve rejected approaches when they remain useful to the research history.

## Commit messages

Use concise, descriptive messages, for example:

- `docs: define subset sum research scope`
- `proof: add residue-completion lemma`
- `counterexample: refute bundle lemma`
- `experiment: test bounded-modulus instances`
- `status: close structural-compression route`
