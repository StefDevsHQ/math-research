# Source Map — P versus NP Top-Level Landscapes

**Classification:** Canonical primary-source and project-record map  
**Cutoff:** 2026-07-22  
**Use:** Supports [research-programme-landscape.md](research-programme-landscape.md) and [problem-testbed-landscape.md](problem-testbed-landscape.md)

This is the single authoritative source map for the top-level landscapes. Source identifiers are stable within the repository. Each source supports only the role stated here. Barrier, restricted-model, formal-theory, randomized, promise, interactive, and quantum results do not automatically transfer to classical unrestricted P versus NP.

## Foundations and concrete complexity

- `[P01]` Stephen A. Cook, “The Complexity of Theorem-Proving Procedures,” *STOC*, 1971 — Cook–Levin foundation. https://doi.org/10.1145/800157.805047
- `[P02]` Richard M. Karp, “Reducibility Among Combinatorial Problems,” 1972 — natural NP-complete problems and reductions. https://doi.org/10.1007/978-1-4684-2001-2_9
- `[P03]` Thomas J. Schaefer, “The Complexity of Satisfiability Problems,” *STOC*, 1978 — Boolean CSP dichotomy and exact-one hardness. https://doi.org/10.1145/800133.804350
- `[P04]` Andrei A. Bulatov, “A Dichotomy Theorem for Nonuniform CSPs,” 2017 — finite-domain CSP dichotomy. https://arxiv.org/abs/1703.03021
- `[P05]` Dmitriy Zhuk, “A Proof of the CSP Dichotomy Conjecture,” 2017 — independent finite-domain CSP dichotomy. https://arxiv.org/abs/1704.01914
- `[P06]` Hasan, Mondal, and Rahman, “Positive Planar Satisfiability Problems under 3-Connectivity Constraints,” 2021 — robust Positive 1-in-3 SAT hardness. https://arxiv.org/abs/2108.12500
- `[P07]` Bonnet and Paschos, “An Exact Algorithm for 1-in-3 SAT,” 2013 — representative exact-exponential algorithm. https://arxiv.org/abs/1307.5776
- `[P08]` Darmann and Döcker, “On Simplified NP-Complete Variants of Not-All-Equal 3-SAT and 3-SAT,” 2019 — restricted positive NAE-3SAT hardness. https://arxiv.org/abs/1908.04198
- `[P09]` Hell and Nešetřil, “On the Complexity of H-Coloring,” *JCTB* 48(1), 1990 — graph-homomorphism dichotomy. https://doi.org/10.1016/0095-8956(90)90132-J

## Circuits, barriers, proof, and representation

- `[P10]` Ryan Williams, “New Algorithms and Lower Bounds for Circuits with Linear Threshold Gates,” 2014 — algorithms-to-lower-bounds. https://arxiv.org/abs/1401.2444
- `[P11]` Vyas and Williams, “Lower Bounds Against Sparse Symmetric Functions of ACC Circuits,” 2020 — counting algorithms transferred to restricted-circuit lower bounds. https://arxiv.org/abs/2001.07788
- `[P12]` Russell Impagliazzo, “Hardness as Randomness: A Survey of Universal Derandomization,” 2003 — hardness versus randomness. https://arxiv.org/abs/cs/0304040
- `[P13]` Alexander Razborov, “Lower Bounds on the Monotone Complexity of Some Boolean Functions,” 1985 — exponential monotone lower bounds.
- `[P14]` Baker, Gill, and Solovay, “Relativizations of the P =? NP Question,” *SICOMP* 4(4), 1975 — relativization barrier. https://doi.org/10.1137/0204037
- `[P15]` Razborov and Rudich, “Natural Proofs,” *JCSS* 55(1), 1997 — natural-proofs barrier. https://doi.org/10.1006/jcss.1997.1494
- `[P16]` Mulmuley and Sohoni, “Geometric Complexity Theory I,” *SICOMP* 31(2), 2001 — GCT programme. https://doi.org/10.1137/S009753970038715X
- `[P17]` Aaronson and Wigderson, “Algebrization: A New Barrier in Complexity Theory,” 2009 — algebrization barrier. https://arxiv.org/abs/0807.0261
- `[P18]` Cook and Reckhow, “The Relative Efficiency of Propositional Proof Systems,” *JSL* 44(1), 1979 — Cook–Reckhow proof systems. https://doi.org/10.2307/2273702
- `[P19]` Jan Krajíček, “The Cook-Reckhow Definition,” 2019 — modern proof-complexity framework. https://arxiv.org/abs/1909.03691
- `[P20]` Kushilevitz and Nisan, *Communication Complexity*, 1997 — communication lower-bound framework.
- `[P21]` Igor Razgon, “Classification of OBDD Size for Monotone 2-CNFs,” 2021 — ordered-decision-diagram lower bounds. https://arxiv.org/abs/2103.09115

## Meta-complexity, parameters, reductions, counting, and quantum

- `[P22]` Allender et al., “Minimum Circuit Size, Graph Isomorphism, and Related Problems,” 2017 — MCSP and meta-complexity. https://arxiv.org/abs/1710.09806
- `[P23]` Chen et al., “Beyond Natural Proofs: Hardness Magnification and Locality,” 2019 — hardness magnification. https://arxiv.org/abs/1911.08297
- `[P24]` Atserias and Müller, “Simple General Magnification of Circuit Lower Bounds,” 2025 — modern magnification thresholds. https://arxiv.org/abs/2503.24061
- `[P25]` Cygan et al., *Parameterized Algorithms*, 2015 — width, fixed-parameter algorithms, and kernelization. https://doi.org/10.1007/978-3-319-21275-3
- `[P26]` Valiant and Vazirani, “NP Is as Easy as Detecting Unique Solutions,” *TCS* 47, 1986 — randomized isolation. https://doi.org/10.1016/0304-3975(86)90135-0
- `[P27]` Impagliazzo, Paturi, and Zane, “Which Problems Have Strongly Exponential Complexity?” *JCSS* 63(4), 2001 — ETH framework. https://doi.org/10.1006/jcss.2001.1774
- `[P28]` Arora et al., “Proof Verification and the Hardness of Approximation Problems,” *JACM* 45(3), 1998 — PCP theorem. https://doi.org/10.1145/278298.278306
- `[P29]` Leslie Valiant, “The Complexity of Enumeration and Reliability Problems,” *SICOMP* 8(3), 1979 — #P. https://doi.org/10.1137/0208032
- `[P30]` Bernstein and Vazirani, “Quantum Complexity Theory,” *SICOMP* 26(5), 1997 — quantum complexity. https://doi.org/10.1137/S0097539796300921
- `[P31]` Repository records under `../investigations/subset-sum/` — completed Subset Sum routes and representation-boundary results.

## Optimisation, algebra, hierarchy, and controls

- `[P32]` Hendrik Lenstra, “Integer Programming with a Fixed Number of Variables,” *MOR* 8(4), 1983 — fixed-dimensional integer programming. https://doi.org/10.1287/moor.8.4.538
- `[P33]` Goemans and Williamson, “Improved Approximation Algorithms for Maximum Cut and Satisfiability Problems,” *JACM* 42(6), 1995 — semidefinite relaxation. https://doi.org/10.1145/227683.227684
- `[P35]` Shpilka and Yehudayoff, “Arithmetic Circuits: A Survey of Recent Results and Open Questions,” 2010 — arithmetic circuits and PIT. https://doi.org/10.1561/0400000039
- `[P36]` Neil Immerman, *Descriptive Complexity*, 1999 — logical characterizations and restricted inexpressibility. https://doi.org/10.1007/978-1-4612-0539-5
- `[P37]` Hartmanis and Stearns, “On the Computational Complexity of Algorithms,” 1965 — hierarchy methods. https://doi.org/10.2307/1994208
- `[P38]` Karp and Lipton, “Turing Machines That Take Advice,” 1982 — advice, nonuniformity, and collapse consequences.
- `[P39]` Stephen Mahaney, “Sparse Complete Sets for NP,” *JCSS* 25(2), 1982 — sparse NP-hard sets.
- `[P40]` Fortnow and Santhanam, “Infeasibility of Instance Compression and Succinct PCPs for NP,” *JCSS* 77(1), 2011 — compression barriers. https://doi.org/10.1016/j.jcss.2010.06.007
- `[P41]` Jack Edmonds, “Paths, Trees, and Flowers,” *Canadian Journal of Mathematics* 17, 1965 — polynomial-time matching. https://doi.org/10.4153/CJM-1965-045-4
- `[P42]` Garey and Johnson, *Computers and Intractability*, 1979 — classical problem catalogue.
- `[P43]` László Babai, “Graph Isomorphism in Quasipolynomial Time,” *STOC*, 2016 — quasipolynomial Graph Isomorphism. https://doi.org/10.1145/2897518.2897542
- `[P44]` Kabanets and Impagliazzo, “Derandomizing Polynomial Identity Tests Means Proving Circuit Lower Bounds,” 2004 — PIT-to-lower-bound transfer. https://doi.org/10.1007/s00037-004-0182-6
- `[P45]` Peter Shor, “Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer,” 1997 — quantum factoring. https://arxiv.org/abs/quant-ph/9508027
- `[P46]` Chen, Deng, and Teng, “Settling the Complexity of Computing Two-Player Nash Equilibria,” *JACM* 56(3), 2009 — PPAD-complete equilibrium. https://arxiv.org/abs/0704.1678
- `[P47]` Chandra, Kozen, and Stockmeyer, “Alternation,” *JACM* 28(1), 1981 — alternation and PSPACE. https://doi.org/10.1145/322234.322243
- `[P48]` Richard Ladner, “The Circuit Value Problem Is Log Space Complete for P,” 1975 — P-complete evaluation control.
- `[P49]` Kreuzer and Nipkow, “Verification of NP-Hardness Reduction Functions for Exact Lattice Problems,” 2023 — verified reductions. https://arxiv.org/abs/2306.08375
- `[P50]` Fiorini et al., “Exponential Lower Bounds for Polytopes in Combinatorial Optimization,” *JACM* 62(2), 2015 — extension complexity. https://arxiv.org/abs/1111.0837
- `[P51]` Aaron Potechin, “Sum of Squares Lower Bounds from Symmetry and a Good Story,” 2017 — SoS lower-bound methodology. https://arxiv.org/abs/1711.11469
- `[P52]` Carmosino et al., “Learning Algorithms from Natural Proofs,” CCC 2016 — learning and natural properties.
- `[P53]` Richard Ladner, “On the Structure of Polynomial Time Reducibility,” *JACM* 22(1), 1975 — conditional NP-intermediate languages. https://doi.org/10.1145/321864.321877
- `[P54]` Seinosuke Toda, “PP Is as Hard as the Polynomial-Time Hierarchy,” *SICOMP* 20(5), 1991 — counting and PH. https://doi.org/10.1137/0220053
- `[P56]` Ronald Fagin, “Generalized First-Order Spectra and Polynomial-Time Recognizable Sets,” 1974 — existential second-order characterization of NP.
- `[P58]` Christos Papadimitriou, “On the Complexity of the Parity Argument and Other Inefficient Proofs of Existence,” *JCSS* 48(3), 1994 — TFNP and PPAD. https://doi.org/10.1016/S0022-0000(05)80063-7

## Completion-pass sources

- `[P59]` Cook and Nguyen, *Logical Foundations of Proof Complexity*, 2010 — bounded arithmetic, propositional translations, and witnessing. https://doi.org/10.1017/CBO9780511676277
- `[P60]` Jan Krajíček, *Bounded Arithmetic, Propositional Logic, and Complexity Theory*, 1995 — weak arithmetic theories and proof complexity. https://doi.org/10.1017/CBO9780511529948
- `[P61]` Lund, Fortnow, Karloff, and Nisan, “Algebraic Methods for Interactive Proof Systems,” *JACM* 39(4), 1992 — arithmetization and sum-check methods. https://doi.org/10.1145/146585.146605
- `[P62]` Adi Shamir, “IP = PSPACE,” *JACM* 39(4), 1992 — interactive-proof characterization of PSPACE. https://doi.org/10.1145/146585.146609
- `[P63]` Rahul Santhanam, “An Algorithmic Approach to Uniform Lower Bounds,” ECCC TR23-028, 2023 — sampling tasks and probabilistic Kolmogorov complexity yielding uniform circuit lower bounds. https://eccc.weizmann.ac.il/report/2023/028/
- `[P64]` Zhenjian Lu and Igor C. Oliveira, “Theory and Applications of Probabilistic Kolmogorov Complexity,” 2022 — survey of probabilistic time-bounded Kolmogorov complexity and applications. https://arxiv.org/abs/2205.14718
- `[P65]` John Gill, “Computational Complexity of Probabilistic Turing Machines,” *SICOMP* 6(4), 1977 — probabilistic polynomial-time classes. https://doi.org/10.1137/0206049
- `[P66]` László Babai, “Trading Group Theory for Randomness,” *STOC*, 1985 — Arthur–Merlin public-coin proof systems. https://doi.org/10.1145/22145.22192

## Scope determination

The map covers the major established and currently prominent programme families needed for route selection. It is intentionally non-exhaustive below the programme level: it does not enumerate every circuit class, proof system, bounded-arithmetic theory, randomized class, parameter, or paper.

The literature supports no single universally best NP-complete testbed. CSP dichotomies classify fixed relation languages; Circuit-SAT is closest to arbitrary computation; proof complexity isolates no-instance certification; meta-complexity and magnification target indirect separations; exact-incidence systems provide clean positive testbeds; bounded arithmetic studies formal provability; interactive proofs provide an arithmetization bridge; and uniform lower-bound programmes require separate uniformity accounting.

No source here resolves P versus NP or licenses promotion of a restricted-model, formal-theory, randomized, interactive, promise, uniform, algebraic, counting, or quantum result to an unrestricted classical separation without an explicit transfer theorem.