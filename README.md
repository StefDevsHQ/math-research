# Math Research

A public, versioned workspace for long-running mathematical investigations.

This repository preserves definitions, known results, proof attempts, counterexamples, audits, computational experiments, failed routes, literature landscapes, and current research state. It is designed for traceability: claims remain explicitly labelled, corrections remain visible, and unresolved gaps are not presented as results.

> Nothing here should be interpreted as a resolution of an open problem unless a complete argument is explicitly identified, independently checked, and accepted through the relevant mathematical review process.

## Research model

```text
problem
├── foundations
├── references and landscapes
└── investigation
    └── route
        ├── proof
        ├── counterexample
        ├── audit
        ├── experiment
        ├── note
        └── archive
```

- **Problems** provide the broad mathematical programme and authoritative status.
- **Foundations** preserve shared definitions, models, and established results.
- **References and landscapes** map known programmes, testbeds, barriers, and primary sources across investigations.
- **Investigations** provide concrete research environments.
- **Routes** isolate distinct proposed mechanisms or obstruction programmes.
- **Atomic records** preserve one proof, counterexample, audit, experiment, or handoff per file.

## Repository structure

```text
problems/                 Problem programmes, landscapes, and investigations
templates/                Reusable research record templates
tools/                    Reproducible scripts and notebooks
.github/                  Issue and pull-request workflows
RESEARCH_STANDARDS.md     Claim, proof, evidence, and review rules
CONTRIBUTING.md           Contribution workflow
LICENSES.md               License map
CITATION.cff              Repository citation metadata
```

## Current research state

### P versus NP

The [P-versus-NP programme](problems/p-vs-np/README.md) is in **top-level route selection**. No investigation or route is currently active.

The programme maintains two canonical cross-investigation orientation artifacts:

- [Research-programme landscape](problems/p-vs-np/references/research-programme-landscape.md) — direct algorithms, structural classifications, circuit and proof lower bounds, algorithms-to-lower-bounds, meta-complexity, derandomization, conditional programmes, and proof barriers, with explicit consequence mapping.
- [Problem-testbed landscape](problems/p-vs-np/references/problem-testbed-landscape.md) — NP-complete testbeds, tractable controls, promise problems, total-search classes, and strategic non-NP-complete objects organized by the obstruction they expose.

The current strategic candidates are:

1. **Positive investigation:** exact-incidence constraint systems centred on Positive 1-in-3 SAT, with X3C and 3-Dimensional Matching as paired hard controls.
2. **Lower-bound sibling:** Circuit-SAT and restricted-circuit satisfiability, with the exact circuit model and transfer theorem stated before activation.
3. **Alternative route:** another programme or testbed from the canonical landscapes, selected with an explicit mathematical advantage and stop condition.

The completed [Subset Sum investigation](problems/p-vs-np/investigations/subset-sum/README.md) remains an arithmetic benchmark and adversarial reduction target:

- [Structural compression](problems/p-vs-np/investigations/subset-sum/routes/structural-compression/README.md) — closed as a universal algorithmic route; restricted results retained.
- [Exact-state compression barriers](problems/p-vs-np/investigations/subset-sum/routes/exact-state-compression-barriers/README.md) — closed as a broad model-barrier route; model-specific results retained.

No repository result currently resolves `P=NP`, `P!=NP`, proves a general Boolean circuit lower bound, or gives a lower bound for arbitrary Subset Sum algorithms.

## Working principles

- Separate established results, repository proofs, conjectures, heuristics, and computation.
- Keep mathematical status separate from review maturity.
- Record failed approaches and counterexamples; do not rewrite history.
- State dependencies, input encodings, complexity measures, model restrictions, and unresolved gaps explicitly.
- Prefer small, reviewable research records over long unstructured transcripts.

Read [Research Standards](RESEARCH_STANDARDS.md) before adding or promoting a claim.

## Licensing

Research content is licensed under [CC BY 4.0](LICENSE). Executable material under `tools/` is licensed under [MIT](tools/LICENSE). See [LICENSES.md](LICENSES.md) for boundaries.
