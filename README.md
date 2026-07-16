# Math Research

A public, versioned workspace for long-running mathematical investigations.

This repository preserves definitions, known results, proof attempts, counterexamples, audits, computational experiments, failed routes, and current research state. It is designed for traceability: claims remain explicitly labelled, corrections remain visible, and unresolved gaps are not presented as results.

> Nothing here should be interpreted as a resolution of an open problem unless a complete argument is explicitly identified, independently checked, and accepted through the relevant mathematical review process.

## Research model

```text
problem
└── investigation
    └── route
        ├── proof
        ├── counterexample
        ├── audit
        ├── experiment
        ├── note
        └── archive
```

- **Problems** provide the broad mathematical context.
- **Investigations** provide concrete test environments.
- **Routes** isolate distinct proposed mechanisms or obstruction programs.
- **Atomic records** preserve one proof, counterexample, audit, experiment, or handoff per file.

## Repository structure

```text
problems/                 Problem programs and investigations
templates/                Reusable research record templates
tools/                    Reproducible scripts and notebooks
.github/                  Issue and pull-request workflows
RESEARCH_STANDARDS.md     Claim, proof, evidence, and review rules
CONTRIBUTING.md           Contribution workflow
LICENSES.md               License map
CITATION.cff              Repository citation metadata
```

## Active research

- [P versus NP](problems/p-vs-np/README.md)
  - [Subset Sum investigation](problems/p-vs-np/investigations/subset-sum/README.md)
    - [Structural compression route](problems/p-vs-np/investigations/subset-sum/routes/structural-compression/README.md)

## Working principles

- Separate established results, repository proofs, conjectures, heuristics, and computation.
- Keep mathematical status separate from review maturity.
- Record failed approaches and counterexamples; do not rewrite history.
- State dependencies, input encodings, complexity measures, and unresolved gaps explicitly.
- Prefer small, reviewable research records over long unstructured transcripts.

Read [Research Standards](RESEARCH_STANDARDS.md) before adding or promoting a claim.

## Licensing

Research content is licensed under [CC BY 4.0](LICENSE). Executable material under `tools/` is licensed under [MIT](tools/LICENSE). See [LICENSES.md](LICENSES.md) for boundaries.