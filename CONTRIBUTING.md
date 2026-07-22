# Contributing

Contributions should make the research state easier to verify.

## Before contributing

1. Read [Research Standards](RESEARCH_STANDARDS.md).
2. Locate the nearest `README.md`, `STATUS.md`, and `CLAIMS.md`.
3. Identify the record type: definition, proof, counterexample, audit, experiment, note, citation, or administration.
4. Open or reference a focused issue when the work is substantial.
5. Install the repository-local Git hooks once per clone:

   ```bash
   sh scripts/install-hooks.sh
   ```

The hooks use only Git, POSIX shell, and the existing Python toolchain. This repository deliberately does not add Node.js or Husky solely for hook management.

## Local verification policy

The canonical entry point is:

```bash
sh scripts/check.sh staged
sh scripts/check.sh fast
sh scripts/check.sh full
```

- `staged` checks whitespace and compiles the exact staged Python and shell contents. It is used by `pre-commit`.
- `fast` compiles the package, runs the ordinary regression suite and lightweight VS-05 checks, exercises representative CLI commands, and verifies committed record digests. It is used by `pre-push` for feature branches.
- `full` additionally runs the independent VS-03 and VS-05 gates and regenerates the VS-02, VS-03, and VS-04 committed records byte for byte. It is required before merging a claim promotion, generated-record change, solver change, or other mathematically substantive pull request.

The pre-push hook runs `full` automatically for a direct push to `main`. For pull requests, run `sh scripts/check.sh full` on the final commit before merge and record the checked commit SHA in the pull-request description or review.

Git hooks are local safeguards and can be bypassed with `--no-verify`; they are not server-side proof that a pull request was checked. Reviewers must therefore treat an unrecorded full check as missing evidence, not assume that hooks ran.

## Continuous integration policy

Automatic GitHub Actions runs are restricted to pushes to `main`. Pull-request commits do not automatically consume CI capacity.

The `main` workflow runs:

- fast compatibility checks on Python 3.11 and 3.12;
- one full research gate on Python 3.13;
- concurrency cancellation so an older in-progress `main` run is superseded by a newer push.

A manual workflow dispatch remains available for exceptional independent verification. Because the automatic gate runs after merge, branch protection must not require this `main`-only status check on pull requests. Correctness before merge instead rests on the recorded local full check and mathematical review; the `main` run is the final integration and reproducibility gate.

If stronger server-side pre-merge enforcement becomes necessary, add an explicitly requested or label-triggered pull-request workflow rather than restoring an expensive run on every commit.

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
- any mathematical-status or review-maturity changes;
- the final commit SHA checked with `sh scripts/check.sh full` when the change is mathematically substantive.

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
