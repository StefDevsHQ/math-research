# Math Research

A public, versioned workspace for long-running mathematical investigations.

This repository preserves definitions, proof attempts, counterexamples, computational experiments, failed routes, and current research state. It is designed for traceability rather than performance: claims remain explicitly labelled, corrections remain visible, and unresolved gaps are not presented as results.

> Nothing in this repository should be interpreted as a resolution of an open problem unless a complete argument is explicitly identified, independently checked, and accepted through the relevant mathematical review process.

## Structure

```text
problems/                  Problem-specific research
  <problem>/
    README.md              Scope and entry point
    STATUS.md              Current position and next step
    CLAIMS.md              Authoritative claim ledger
templates/                 Reusable research-note templates
.github/                   Contribution and review workflows
RESEARCH_STANDARDS.md      Repository-wide research rules
CONTRIBUTING.md            How changes are proposed and reviewed
```

## Active research

- [P versus NP](problems/p-vs-np/README.md)
  - [Subset Sum](problems/p-vs-np/subset-sum/README.md)

## Working principles

- Separate known results, new arguments, conjectures, heuristics, and experiments.
- Record failed approaches and counterexamples; do not rewrite history.
- State dependencies and unresolved gaps explicitly.
- Treat computation as evidence, not proof, unless exhaustive verification is itself proved sufficient.
- Prefer small, reviewable research units over long unstructured transcripts.

See [Research Standards](RESEARCH_STANDARDS.md) before adding or promoting a claim.
