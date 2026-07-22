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

## Active-path verification lifecycle

Verification is attached to active research, not accumulated forever.

The registry `.verification/active-paths` lists the investigation or route scopes currently included in local and CI verification. A scope has one of three operational states:

- **ACTIVE** — implementation or mathematical work is continuing; its fast and full gates run.
- **CLOSED** — the objective was satisfied, disproved, exhausted, or formally abandoned; its final evidence remains in the repository, but its tests leave the default verification graph.
- **DEFERRED** — work is paused without a final mathematical determination; its evidence and reopening conditions remain, but its tests leave the default verification graph until explicit reactivation.

Closing or deferring a scope requires one final full verification on the exact closing commit, synchronized status and claim records, preserved reproducibility instructions, and removal of the scope from `.verification/active-paths` in the same change. Tests and tools may remain archived in place; they are no longer executed by default.

Reopening a deferred or closed scope requires an explicit lifecycle change that:

1. states the materially new theorem, mechanism, evidence, or decision justifying reopening;
2. restores the scope to `.verification/active-paths`;
3. restores or updates every required dependency, fixture, runtime and reproduction command;
4. passes the full gate before any new claim is promoted.

A closed scope should not be reopened merely for more examples or minor variations. A deferred scope may be reactivated when its recorded reopening condition is met.

## Local verification policy

The canonical entry point is:

```bash
sh scripts/check.sh staged
sh scripts/check.sh fast
sh scripts/check.sh full
```

- `staged` checks whitespace and compiles the exact staged Python and shell contents. It is used by `pre-commit` and always runs.
- `fast` runs the active scope's compatibility and lightweight regression checks. If the scope is closed or deferred, it exits successfully after reporting that verification is inactive.
- `full` runs the active scope's independent and byte-reproduction gates. It is required before merging a claim promotion, generated-record change, solver change, lifecycle closure, deferral, or reopening.

The pre-push hook runs `full` automatically for a direct push to `main`. For pull requests, run `sh scripts/check.sh full` on the final substantive commit before merge and record the checked commit SHA in the pull-request description or review.

Git hooks are local safeguards and can be bypassed with `--no-verify`; they are not server-side proof that a pull request was checked. Reviewers must therefore treat an unrecorded full check as missing evidence, not assume that hooks ran.

## Continuous integration policy

Automatic GitHub Actions runs are restricted to pushes to `main`. Pull-request commits do not automatically consume CI capacity.

The `main` workflow runs:

- fast compatibility checks on Python 3.11 and 3.12 for active scopes;
- one full active-scope gate on Python 3.13;
- concurrency cancellation so an older in-progress `main` run is superseded by a newer push.

Changes to `.verification/active-paths` trigger the workflow. When a scope is removed, the workflow confirms that its gate is inactive rather than rerunning the retired test corpus.

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
- the final commit SHA checked with `sh scripts/check.sh full` when the change is mathematically substantive;
- any activation, closure, deferral or reopening change to `.verification/active-paths`.

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
