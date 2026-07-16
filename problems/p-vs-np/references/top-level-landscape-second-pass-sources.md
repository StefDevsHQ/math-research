# Second-Pass Sources — P versus NP Top-Level Landscapes

**Classification:** Supplementary primary-source map  
**Cutoff:** 2026-07-16  
**Use:** Supports the second-pass corrections to [research-programme-landscape.md](research-programme-landscape.md) and [problem-testbed-landscape.md](problem-testbed-landscape.md)

These sources fill gaps found during the second completeness and correctness audit. Each source supports only the role stated here.

## Hierarchies, nonuniformity, sparsity, and compression

### `[P37]` Hartmanis and Stearns — hierarchy and diagonalization foundations

Juris Hartmanis and Richard E. Stearns, “On the Computational Complexity of Algorithms,” *Transactions of the American Mathematical Society* 117, 1965, pp. 285–306.

- Role: time-complexity classes, hierarchy methods, and the scope of diagonalization-based separations.
- Stable source: https://doi.org/10.2307/1994208

### `[P38]` Karp and Lipton — polynomial advice and hierarchy collapse

Richard M. Karp and Richard J. Lipton, “Turing Machines That Take Advice,” *L’Enseignement Mathématique* 28, 1982, pp. 191–209; originating in STOC 1980 work on nonuniform complexity.

- Role: if `NP` has polynomial-size circuit families, then the polynomial hierarchy collapses; the modern Karp–Lipton formulation uses the second level.
- Scope: `NP not subseteq P/poly` is a stronger target than `P!=NP`; the collapse theorem is evidence, not a proof, that the containment fails.

### `[P39]` Mahaney — sparse NP-hard sets

Stephen R. Mahaney, “Sparse Complete Sets for NP: Solution of a Conjecture of Berman and Hartmanis,” *Journal of Computer and System Sciences* 25(2), 1982, pp. 130–143.

- Role: a sparse language cannot be NP-hard under polynomial-time many-one reductions unless `P=NP`.
- Scope: sparsity is a language-density property, not a generic bound on arbitrary data structures or circuit representations.

### `[P40]` Fortnow and Santhanam — instance compression barrier

Lance Fortnow and Rahul Santhanam, “Infeasibility of Instance Compression and Succinct PCPs for NP,” *Journal of Computer and System Sciences* 77(1), 2011, pp. 91–106.

- Role: rules out broad polynomial OR-compression schemes for NP-complete problems unless a major complexity collapse occurs.
- Scope: parameterized kernels and special-purpose compressions require their exact hypotheses; this is not an unconditional lower bound against every preprocessing method.

### `[P53]` Ladner — intermediate NP languages

Richard E. Ladner, “On the Structure of Polynomial Time Reducibility,” *Journal of the ACM* 22(1), 1975, pp. 155–171.

- Role: if `P!=NP`, then NP contains languages that are neither in P nor NP-complete under polynomial-time many-one reductions.
- Scope: the theorem is conditional and does not identify a natural intermediate problem.

## Matching, classical problem catalogues, and P-completeness

### `[P41]` Edmonds — polynomial-time matching

Jack Edmonds, “Paths, Trees, and Flowers,” *Canadian Journal of Mathematics* 17, 1965, pp. 449–467.

- Role: polynomial-time exact matching; mandatory rank-two tractable control for X3C and 3-Dimensional Matching.
- Stable source: https://doi.org/10.4153/CJM-1965-045-4

### `[P42]` Garey and Johnson — classical NP-complete problem catalogue

Michael R. Garey and David S. Johnson, *Computers and Intractability: A Guide to the Theory of NP-Completeness*, W. H. Freeman, 1979.

- Role: standard source for classical graph, scheduling, packing, covering, completion, and numerical NP-complete problems not all contained in Karp’s original list.

### `[P48]` Ladner — Circuit Value is P-complete

Richard E. Ladner, “The Circuit Value Problem Is Log Space Complete for P,” *SIGACT News* 7(1), 1975, pp. 18–20.

- Role: Circuit Value as a polynomial-time-complete control separating efficient sequential evaluation from NP-complete circuit satisfiability.

## Derandomization, learning, and circuit lower bounds

### `[P44]` Kabanets and Impagliazzo — PIT derandomization implies lower bounds

Valentine Kabanets and Russell Impagliazzo, “Derandomizing Polynomial Identity Tests Means Proving Circuit Lower Bounds,” *Computational Complexity* 13, 2004, pp. 1–46.

- Role: deterministic derandomization of polynomial identity testing yields a lower-bound disjunction involving Boolean or arithmetic circuits.
- Scope: `PIT in P` is not itself equivalent to `P=NP` or `P!=NP`.
- Stable source: https://doi.org/10.1007/s00037-004-0182-6

### `[P52]` Carmosino, Impagliazzo, Kabanets, and Kolokolova — learning from natural properties

Marco L. Carmosino, Russell Impagliazzo, Valentine Kabanets, and Antonina Kolokolova, “Learning Algorithms from Natural Proofs,” *Computational Complexity Conference*, 2016.

- Role: connects constructive circuit-lower-bound properties with nontrivial learning algorithms.
- Scope: the transfer is circuit-class specific and does not make general circuit learning tractable.

## Polyhedral and semialgebraic lower bounds

### `[P50]` Fiorini et al. — extension-complexity lower bounds

Samuel Fiorini, Serge Massar, Sebastian Pokutta, Hans Raj Tiwary, and Ronald de Wolf, “Exponential Lower Bounds for Polytopes in Combinatorial Optimization,” *Journal of the ACM* 62(2), 2015.

- Role: exponential linear-program extension-complexity lower bounds for TSP, cut, and stable-set polytopes.
- Scope: rules out compact LP formulations in the stated model, not arbitrary polynomial-time algorithms.
- Preprint: https://arxiv.org/abs/1111.0837

### `[P51]` Potechin — sum-of-squares lower bounds

Aaron Potechin, “Sum of Squares Lower Bounds from Symmetry and a Good Story,” 2017.

- Role: representative methodology and lower bounds for the Sum-of-Squares proof/relaxation hierarchy, including exact knapsack-style principles.
- Scope: degree or size lower bounds apply to the stated semialgebraic system.
- Preprint: https://arxiv.org/abs/1711.11469

## Intermediate, quantum, total-search, and stronger-than-NP controls

### `[P43]` Babai — Graph Isomorphism in quasipolynomial time

László Babai, “Graph Isomorphism in Quasipolynomial Time,” *Proceedings of STOC*, 2016.

- Role: quasipolynomial-time upper bound for Graph Isomorphism; supports its use as an intermediate-status control rather than an NP-complete testbed.
- Stable source: https://doi.org/10.1145/2897518.2897542

### `[P45]` Shor — quantum factoring and discrete logarithms

Peter W. Shor, “Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer,” *SIAM Journal on Computing* 26(5), 1997, pp. 1484–1509.

- Role: polynomial-time quantum algorithms for factoring and discrete logarithms.
- Scope: these are not known NP-complete problems, and quantum tractability does not imply classical `P=NP`.
- Preprint: https://arxiv.org/abs/quant-ph/9508027

### `[P46]` Chen, Deng, and Teng — PPAD-complete Nash equilibrium

Xi Chen, Xiaotie Deng, and Shang-Hua Teng, “Settling the Complexity of Computing Two-Player Nash Equilibria,” *Journal of the ACM* 56(3), 2009.

- Role: PPAD-completeness of computing a two-player Nash equilibrium; representative total-search problem.
- Preprint: https://arxiv.org/abs/0704.1678

### `[P58]` Papadimitriou — TFNP and PPAD foundations

Christos H. Papadimitriou, “On the Complexity of the Parity Argument and Other Inefficient Proofs of Existence,” *Journal of Computer and System Sciences* 48(3), 1994, pp. 498–532.

- Role: foundational total-search complexity and PPAD framework.
- Scope: total search has different quantifiers from NP decision completeness.

### `[P47]` Meyer and Stockmeyer — quantified Boolean formulas and PSPACE

Albert R. Meyer and Larry J. Stockmeyer, “The Equivalence Problem for Regular Expressions with Squaring Requires Exponential Space,” *Proceedings of FOCS*, 1972, together with their quantified-formula completeness work.

- Role: classical PSPACE-completeness infrastructure for quantified Boolean formulas.
- Scope: putting QBF in P would imply the stronger collapse `P=PSPACE`, hence also `P=NP`.

### `[P49]` Kreuzer and Nipkow — verified exact lattice hardness reductions

Katharina Kreuzer and Tobias Nipkow, “Verification of NP-Hardness Reduction Functions for Exact Lattice Problems,” 2023.

- Role: formally verified NP-hardness reductions for exact Closest Vector and Shortest Vector problems in the infinity norm, correcting defects in earlier proofs.
- Preprint: https://arxiv.org/abs/2306.08375

## Counting and descriptive controls

### `[P54]` Toda — counting access contains the polynomial hierarchy

Seinosuke Toda, “PP Is as Hard as the Polynomial-Time Hierarchy,” *SIAM Journal on Computing* 20(5), 1991, pp. 865–877.

- Role: the polynomial hierarchy is contained in polynomial time with access to a `#P` or equivalent counting oracle.
- Scope: strengthens the strategic importance of counting without equating counting and decision.
- Stable source: https://doi.org/10.1137/0220053

### `[P56]` Fagin — descriptive characterization of NP

Ronald Fagin, “Generalized First-Order Spectra and Polynomial-Time Recognizable Sets,” in *Complexity of Computation*, SIAM–AMS Proceedings 7, 1974, pp. 27–41.

- Role: existential second-order logic characterizes NP on finite structures.
- Scope: a logical characterization is not by itself a lower bound against polynomial-time algorithms.

## Scope determination

These additions sharpen the landscape without changing any project claim state. They distinguish direct P-versus-NP targets from stronger nonuniform, coNP, algebraic, quantum, total-search, and model-specific lower-bound programmes.