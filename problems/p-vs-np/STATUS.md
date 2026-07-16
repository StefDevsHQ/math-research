# Status — P versus NP

**Phase:** First route consolidated; adversarial audit pending  
**Updated:** 2026-07-16

## Current position

The repository foundation is complete and the first Subset Sum route has been decomposed into atomic records.

The structural-compression route no longer supports its original universal bundle claim. It retains one proved local lemma and a refined framework that must be tested against SAT-derived instances.

## Active work

1. Open the SAT-to-Subset-Sum audit as the first research issue.
2. Execute the audit and update the route claims.
3. Decide whether the route survives in restricted form only.
4. If it fails as a universal strategy, begin the exact-state compression barrier program.

## Current blocker

The refined framework has no proved strictly decreasing polynomially bounded complexity measure on hard reduction families.

## Next action

Run the audit defined at `investigations/subset-sum/routes/structural-compression/audits/sat-to-subset-sum.md`.
