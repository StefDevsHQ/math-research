# Audit — Top-Level P versus NP Landscape Completion

**Classification:** Literature-landscape completeness audit  
**Status:** `CHECKED`  
**Date:** 2026-07-22  
**Scope:** Programme-level coverage for route selection, not exhaustive submodel or paper coverage

## Question audited

Does the canonical P-versus-NP landscape cover the major established and currently prominent top-level programme families needed to choose and constrain a research route?

This audit does not ask whether every circuit class, proof system, bounded-arithmetic theory, parameter, promise class, or paper has been listed. That stronger requirement is neither operationally useful nor permanently certifiable.

## Inclusion test

A topic receives a top-level programme row when it satisfies at least one of the following:

1. it gives a direct route to `P=NP` or an explicitly stated stronger or sibling separation;
2. it supplies a major transfer theorem from algorithms, derandomization, proof complexity, algebra, or meta-complexity to lower bounds;
3. it is a standard barrier constraining broad technique families;
4. it changes the quantifiers, model, uniformity, proof strength, error convention, or consequence map enough that omission risks a false inference;
5. it is a currently prominent programme with a distinct route design and stop condition.

A topic remains subordinate when it is one circuit class, one proof system, one parameter, one problem restriction, or one theorem inside an already represented programme.

## Completion findings

The previous landscape already covered direct NP-complete algorithms, CSP classifications, structural tractability, algebraic and geometric algorithms, decomposition, circuit and proof lower bounds, algorithms-to-lower-bounds, communication, monotonicity, arithmetic circuits, Geometric Complexity Theory, descriptive complexity, meta-complexity, hardness magnification, derandomization, compression, average-case complexity, parameterized and fine-grained complexity, approximation, counting, quantum computation, total search, and the standard relativization, natural-proofs, algebrization, and transfer barriers.

Four underrepresented areas met the inclusion test:

### 1. Meta-mathematics and bounded arithmetic

Added as `C10`. This programme studies formalization, witnessing, feasible provability, unprovability, and independence relative to explicitly named weak arithmetic theories.

Boundary: unprovability in one weak theory does not establish falsity or independence from stronger standard foundations.

### 2. Interactive proofs and arithmetization

Added as `D08`. Interactive proofs are not a direct classical P-versus-NP route, but arithmetization and sum-check methods form a major nonrelativizing bridge among proof, counting, and circuit programmes.

Boundary: `IP=PSPACE` does not imply `P=NP`, and arithmetizing methods may still encounter algebrization.

### 3. Uniform lower bounds and resource-bounded Kolmogorov complexity

Added as `B13`. Sampling, generation, compression, and probabilistic Kolmogorov tasks can imply lower bounds for explicitly stated uniform circuit classes.

Boundary: uniform and nonuniform lower bounds are distinct; every claimed consequence must identify the language, circuit class, uniformity convention, and transfer theorem.

### 4. Randomized, promise, and interactive consequence control

Added as `D09` plus a dedicated consequence table. This consolidates distinctions already present separately in derandomization, isolation, quantum, promise, total-search, and alternation records.

Boundary: bounded error, one-sided error, promises, interaction, totality, and deterministic decision use different quantifiers and cannot be silently interchanged.

## Source audit

The completion introduced canonical source identifiers `P59`–`P67`:

- Cook–Nguyen, Krajíček, and Jeřábek for bounded arithmetic, proof complexity, and current metamathematical orientation;
- Lund–Fortnow–Karloff–Nisan and Shamir for arithmetized interactive proofs and `IP=PSPACE`;
- Santhanam and Lu–Oliveira for uniform lower bounds and probabilistic Kolmogorov complexity;
- Gill and Babai for probabilistic and Arthur–Merlin class foundations.

Each new source is used only for the stated programme or consequence-control role. No source is treated as resolving classical P versus NP.

## Adversarial checks

- **No duplicate top-level landscape:** changes were applied to the canonical programme document and source map rather than creating a competing landscape.
- **No claim promotion:** the additions are orientation records, not repository mathematical claims.
- **No route activation:** Positive 1-in-3 SAT and Circuit-SAT remain candidates only.
- **No model transfer:** formal-theory, uniform, randomized, interactive, promise, counting, algebraic, proof, and quantum results remain explicitly scoped.
- **No false exhaustiveness:** completeness is claimed only at the level of major established and currently prominent programme families.
- **No strategic displacement without mechanism:** the new programmes do not outrank the current candidate tracks absent a concrete theorem or route mechanism.

## Determination

The canonical landscape is now adequate for top-level route selection under the following precise statement:

> It covers the major established and currently prominent P-versus-NP programme families, consequence distinctions, and proof barriers needed by this repository, while remaining intentionally non-exhaustive below the programme level.

This is a literature-audit determination, not a theorem about the mathematical completeness of all possible approaches.

## Reopening condition

Reopen this completion audit when a new programme has a distinct consequence map or technique family not subsumed by an existing row, or when a new transfer theorem materially changes the route ranking.
