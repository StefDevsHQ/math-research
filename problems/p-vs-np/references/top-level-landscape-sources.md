# Source Map — P versus NP Top-Level Landscapes

**Classification:** Canonical primary-source and project-record map  
**Cutoff:** 2026-07-22  
**Use:** Supports [research-programme-landscape.md](research-programme-landscape.md) and [problem-testbed-landscape.md](problem-testbed-landscape.md)

This is the single authoritative source map for the top-level landscapes. Source identifiers are stable within the repository. A source supports only the role stated below. Barrier theorems constrain technique families; they are not evidence that P versus NP is unresolvable.

## Foundations, NP-completeness, and constraint satisfaction

### `[P01]` Cook — satisfiability and verification
Stephen A. Cook, “The Complexity of Theorem-Proving Procedures,” *STOC*, 1971.  
Role: Cook–Levin foundation. https://doi.org/10.1145/800157.805047

### `[P02]` Karp — natural NP-complete problems
Richard M. Karp, “Reducibility Among Combinatorial Problems,” 1972.  
Role: polynomial reductions among logical, graph, covering, matching, routing, scheduling, and numerical problems. https://doi.org/10.1007/978-1-4684-2001-2_9

### `[P03]` Schaefer — Boolean CSP dichotomy
Thomas J. Schaefer, “The Complexity of Satisfiability Problems,” *STOC*, 1978.  
Role: Boolean fixed-language dichotomy; Positive 1-in-3 SAT and positive NAE-SAT hardness. https://doi.org/10.1145/800133.804350

### `[P04]` Bulatov — finite-domain CSP dichotomy
Andrei A. Bulatov, “A Dichotomy Theorem for Nonuniform CSPs,” 2017.  
Role: independent finite-domain fixed-template dichotomy proof. https://arxiv.org/abs/1703.03021

### `[P05]` Zhuk — finite-domain CSP dichotomy
Dmitriy Zhuk, “A Proof of the CSP Dichotomy Conjecture,” 2017.  
Role: independent dichotomy proof and algorithmic classification. https://arxiv.org/abs/1704.01914

### `[P06]` Hasan, Mondal, and Rahman — robust Positive 1-in-3 SAT hardness
“Positive Planar Satisfiability Problems under 3-Connectivity Constraints,” 2021.  
Role: hardness under strong planarity, connectivity, and occurrence restrictions. https://arxiv.org/abs/2108.12500

### `[P07]` Bonnet and Paschos — exact 1-in-3 SAT algorithm
“An Exact Algorithm for 1-in-3 SAT,” 2013.  
Role: representative exact-exponential algorithm. https://arxiv.org/abs/1307.5776

### `[P08]` Darmann and Döcker — restricted monotone NAE-3SAT
“On Simplified NP-Complete Variants of Not-All-Equal 3-SAT and 3-SAT,” 2019.  
Role: hardness of strongly restricted positive NAE-3SAT variants. https://arxiv.org/abs/1908.04198

### `[P09]` Hell and Nešetřil — graph-homomorphism dichotomy
“On the Complexity of H-Coloring,” *JCTB* 48(1), 1990.  
Role: fixed-target undirected homomorphism dichotomy. https://doi.org/10.1016/0095-8956(90)90132-J

## Circuit algorithms, lower bounds, and derandomization

### `[P10]` Williams — SAT algorithms and circuit lower bounds
“New Algorithms and Lower Bounds for Circuits with Linear Threshold Gates,” 2014.  
Role: representative algorithms-to-lower-bounds theorem. https://arxiv.org/abs/1401.2444

### `[P11]` Vyas and Williams — expanded algorithms-to-lower-bounds
“Lower Bounds Against Sparse Symmetric Functions of ACC Circuits,” 2020.  
Role: faster counting algorithms transferred to restricted-circuit lower bounds. https://arxiv.org/abs/2001.07788

### `[P12]` Impagliazzo — hardness versus randomness
“Hardness as Randomness: A Survey of Universal Derandomization,” 2003.  
Role: hardness–randomness and derandomization framework. https://arxiv.org/abs/cs/0304040

### `[P13]` Razborov — monotone circuit lower bounds
“Lower Bounds on the Monotone Complexity of Some Boolean Functions,” 1985.  
Role: exponential monotone lower bounds; no automatic transfer to circuits with negation.

### `[P14]` Baker, Gill, and Solovay — relativization
“Relativizations of the P =? NP Question,” *SICOMP* 4(4), 1975.  
Role: oracle worlds with opposite P-versus-NP answers. https://doi.org/10.1137/0204037

### `[P15]` Razborov and Rudich — natural proofs
“Natural Proofs,” *JCSS* 55(1), 1997.  
Role: conditional barrier to broad constructive large circuit properties. https://doi.org/10.1006/jcss.1997.1494

### `[P16]` Mulmuley and Sohoni — Geometric Complexity Theory
“Geometric Complexity Theory I,” *SICOMP* 31(2), 2001.  
Role: algebraic-geometric programme centred on permanent versus determinant. https://doi.org/10.1137/S009753970038715X

### `[P17]` Aaronson and Wigderson — algebrization
“Algebrization: A New Barrier in Complexity Theory,” 2009.  
Role: barrier extending relativization to many arithmetizing techniques. https://arxiv.org/abs/0807.0261

## Proof, communication, and representation complexity

### `[P18]` Cook and Reckhow — propositional proof systems
“The Relative Efficiency of Propositional Proof Systems,” *JSL* 44(1), 1979.  
Role: Cook–Reckhow proof systems and polynomial boundedness versus NP=coNP. https://doi.org/10.2307/2273702

### `[P19]` Krajíček — proof-system review
“The Cook-Reckhow Definition,” 2019.  
Role: modern proof-complexity framework and p-simulation. https://arxiv.org/abs/1909.03691

### `[P20]` Kushilevitz and Nisan — communication complexity
*Communication Complexity*, 1997.  
Role: foundational partition and interface lower-bound framework.

### `[P21]` Razgon — ordered decision diagrams
“Classification of OBDD Size for Monotone 2-CNFs,” 2021.  
Role: explicit OBDD lower bounds used by the closed Subset Sum route. https://arxiv.org/abs/2103.09115

## Meta-complexity, parameters, reductions, counting, and quantum models

### `[P22]` Allender et al. — MCSP and meta-complexity
“Minimum Circuit Size, Graph Isomorphism, and Related Problems,” 2017.  
Role: MCSP, compression, pseudorandomness, and meta-complexity. https://arxiv.org/abs/1710.09806

### `[P23]` Chen et al. — hardness magnification and locality
“Beyond Natural Proofs: Hardness Magnification and Locality,” 2019.  
Role: magnification prospects and locality barriers. https://arxiv.org/abs/1911.08297

### `[P24]` Atserias and Müller — general magnification
“Simple General Magnification of Circuit Lower Bounds,” 2025 preprint.  
Role: modern magnification thresholds and consequences. https://arxiv.org/abs/2503.24061

### `[P25]` Cygan et al. — parameterized algorithms
*Parameterized Algorithms*, 2015.  
Role: fixed-parameter tractability, width-based dynamic programming, kernelization, and reductions. https://doi.org/10.1007/978-3-319-21275-3

### `[P26]` Valiant and Vazirani — unique solutions
“NP Is as Easy as Detecting Unique Solutions,” *TCS* 47, 1986.  
Role: randomized isolation reduction to unique satisfiability. https://doi.org/10.1016/0304-3975(86)90135-0

### `[P27]` Impagliazzo, Paturi, and Zane — ETH framework
“Which Problems Have Strongly Exponential Complexity?” *JCSS* 63(4), 2001.  
Role: exponential-time hypotheses and quantitative reductions. https://doi.org/10.1006/jcss.2001.1774

### `[P28]` Arora et al. — PCP theorem
“Proof Verification and the Hardness of Approximation Problems,” *JACM* 45(3), 1998.  
Role: PCP theorem and gap-reduction infrastructure. https://doi.org/10.1145/278298.278306

### `[P29]` Valiant — counting complexity
“The Complexity of Enumeration and Reliability Problems,” *SICOMP* 8(3), 1979.  
Role: #P and natural counting-complete problems. https://doi.org/10.1137/0208032

### `[P30]` Bernstein and Vazirani — quantum complexity
“Quantum Complexity Theory,” *SICOMP* 26(5), 1997.  
Role: foundational quantum complexity and separation from classical claims. https://doi.org/10.1137/S0097539796300921

### `[P31]` Subset Sum project records
Repository records under `../investigations/subset-sum/`.  
Role: two closed universal routes, retained restricted results, reduction audits, and model-boundary theorems.

## Optimisation, algebraic circuits, and descriptive complexity

### `[P32]` Lenstra — fixed-dimensional integer programming
“Integer Programming with a Fixed Number of Variables,” *MOR* 8(4), 1983.  
Role: polynomial time for fixed dimension. https://doi.org/10.1287/moor.8.4.538

### `[P33]` Goemans and Williamson — semidefinite Max Cut
“Improved Approximation Algorithms for Maximum Cut and Satisfiability Problems,” *JACM* 42(6), 1995.  
Role: representative SDP relaxation achievement. https://doi.org/10.1145/227683.227684

### `[P35]` Shpilka and Yehudayoff — arithmetic circuits
“Arithmetic Circuits: A Survey of Recent Results and Open Questions,” 2010.  
Role: arithmetic circuit models, PIT, and lower-bound techniques. https://doi.org/10.1561/0400000039

### `[P36]` Immerman — descriptive complexity
*Descriptive Complexity*, 1999.  
Role: logical characterizations and restricted-formalism lower bounds. https://doi.org/10.1007/978-1-4612-0539-5

## Hierarchy, nonuniformity, sparsity, and compression

### `[P37]` Hartmanis and Stearns — hierarchy methods
“On the Computational Complexity of Algorithms,” 1965.  
Role: time-complexity classes and diagonalization foundations. https://doi.org/10.2307/1994208

### `[P38]` Karp and Lipton — advice and nonuniformity
“Turing Machines That Take Advice,” 1982.  
Role: polynomial advice and polynomial-hierarchy collapse consequences.

### `[P39]` Mahaney — sparse NP-hard sets
“Sparse Complete Sets for NP,” *JCSS* 25(2), 1982.  
Role: sparse many-one NP-hard sets imply P=NP.

### `[P40]` Fortnow and Santhanam — instance compression
“Infeasibility of Instance Compression and Succinct PCPs for NP,” *JCSS* 77(1), 2011.  
Role: OR-compression barriers under class-collapse assumptions. https://doi.org/10.1016/j.jcss.2010.06.007

### `[P41]` Edmonds — polynomial-time matching
“Paths, Trees, and Flowers,” *Canadian Journal of Mathematics* 17, 1965.  
Role: polynomial exact matching; rank-two tractable control. https://doi.org/10.4153/CJM-1965-045-4

### `[P42]` Garey and Johnson — classical catalogue
*Computers and Intractability*, 1979.  
Role: standard catalogue for classical graph, scheduling, packing, covering, and numerical problems.

### `[P43]` Babai — Graph Isomorphism
“Graph Isomorphism in Quasipolynomial Time,” *STOC*, 2016.  
Role: quasipolynomial upper bound and intermediate-status control. https://doi.org/10.1145/2897518.2897542

### `[P44]` Kabanets and Impagliazzo — PIT derandomization
“Derandomizing Polynomial Identity Tests Means Proving Circuit Lower Bounds,” 2004.  
Role: PIT derandomization yields a Boolean-or-arithmetic lower-bound disjunction. https://doi.org/10.1007/s00037-004-0182-6

### `[P45]` Shor — quantum factoring
“Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer,” 1997.  
Role: polynomial quantum algorithms for factoring and discrete logarithms. https://arxiv.org/abs/quant-ph/9508027

### `[P46]` Chen, Deng, and Teng — PPAD-complete equilibrium
“Settling the Complexity of Computing Two-Player Nash Equilibria,” *JACM* 56(3), 2009.  
Role: representative PPAD-complete total-search problem. https://arxiv.org/abs/0704.1678

### `[P47]` Chandra, Kozen, and Stockmeyer — alternation and QBF
“Alternation,” *JACM* 28(1), 1981.  
Role: alternating computation and PSPACE characterization; QBF boundary infrastructure. https://doi.org/10.1145/322234.322243

### `[P48]` Ladner — Circuit Value is P-complete
“The Circuit Value Problem Is Log Space Complete for P,” 1975.  
Role: P-complete control separating circuit evaluation from Circuit-SAT.

### `[P49]` Kreuzer and Nipkow — verified lattice reductions
“Verification of NP-Hardness Reduction Functions for Exact Lattice Problems,” 2023.  
Role: formally verified exact lattice hardness reductions. https://arxiv.org/abs/2306.08375

## Polyhedral, proof-hierarchy, learning, and intermediate controls

### `[P50]` Fiorini et al. — extension complexity
“Exponential Lower Bounds for Polytopes in Combinatorial Optimization,” *JACM* 62(2), 2015.  
Role: exponential LP extension-complexity lower bounds for TSP, cut, and stable-set polytopes. https://arxiv.org/abs/1111.0837

### `[P51]` Potechin — Sum-of-Squares lower bounds
“Sum of Squares Lower Bounds from Symmetry and a Good Story,” 2017.  
Role: representative SoS proof/relaxation lower-bound methodology. https://arxiv.org/abs/1711.11469

### `[P52]` Carmosino et al. — learning from natural properties
“Learning Algorithms from Natural Proofs,” CCC 2016.  
Role: circuit-class-specific connections between natural properties and learning algorithms.

### `[P53]` Ladner — intermediate NP languages
“On the Structure of Polynomial Time Reducibility,” *JACM* 22(1), 1975.  
Role: conditional existence of NP-intermediate languages. https://doi.org/10.1145/321864.321877

### `[P54]` Toda — counting and the polynomial hierarchy
“PP Is as Hard as the Polynomial-Time Hierarchy,” *SICOMP* 20(5), 1991.  
Role: polynomial hierarchy contained in polynomial time with counting access. https://doi.org/10.1137/0220053

### `[P56]` Fagin — descriptive characterization of NP
“Generalized First-Order Spectra and Polynomial-Time Recognizable Sets,” 1974.  
Role: existential second-order logic characterizes NP on finite structures.

### `[P58]` Papadimitriou — TFNP and PPAD
“On the Complexity of the Parity Argument and Other Inefficient Proofs of Existence,” *JCSS* 48(3), 1994.  
Role: total-search and PPAD foundations. https://doi.org/10.1016/S0022-0000(05)80063-7

## Meta-mathematics, interaction, and uniform lower bounds

### `[P59]` Cook and Nguyen — bounded arithmetic and proof complexity
*Logical Foundations of Proof Complexity*, Cambridge University Press, 2010.  
Role: bounded arithmetic, propositional translations, witnessing, and feasible reasoning. https://doi.org/10.1017/CBO9780511676277

### `[P60]` Krajíček — bounded arithmetic and propositional proof complexity
*Bounded Arithmetic, Propositional Logic, and Complexity Theory*, Cambridge University Press, 1995.  
Role: foundational connection between weak arithmetic theories, proof systems, and complexity statements. https://doi.org/10.1017/CBO9780511529948

### `[P61]` Lund, Fortnow, Karloff, and Nisan — arithmetized interactive proofs
“Algebraic Methods for Interactive Proof Systems,” *JACM* 39(4), 1992.  
Role: algebraic and sum-check methods for interactive proof systems; nonrelativizing proof technology. https://doi.org/10.1145/146585.146605

### `[P62]` Shamir — interactive proofs equal polynomial space
“IP = PSPACE,” *JACM* 39(4), 1992.  
Role: exact interactive-proof characterization of PSPACE; demonstrates the power and limits of arithmetization. https://doi.org/10.1145/146585.146609

### `[P63]` Allender, Hirahara, and others — probabilistic Kolmogorov complexity and circuit lower bounds
Representative programme on probabilistic time-bounded Kolmogorov complexity and uniform circuit lower bounds, 2023–2025.  
Role: algorithmic tasks and characterizations yielding uniform lower bounds for stated circuit classes. Canonical entry point: https://eccc.weizmann.ac.il/report/2023/028/

### `[P64]` Hirahara — meta-computational views of uniform lower bounds
Representative work on meta-complexity, generation, compression, and uniform circuit lower bounds.  
Role: emerging uniform algorithms-to-lower-bounds programme; exact consequences remain model-specific. https://eccc.weizmann.ac.il/

### `[P65]` Gill — probabilistic computation classes
John Gill, “Computational Complexity of Probabilistic Turing Machines,” *SICOMP* 6(4), 1977.  
Role: foundational definitions and relations for probabilistic polynomial-time classes. https://doi.org/10.1137/0206049

### `[P66]` Babai — Arthur–Merlin proof systems
László Babai, “Trading Group Theory for Randomness,” *STOC*, 1985.  
Role: Arthur–Merlin public-coin interactive proof classes and randomized-interactive consequence control. https://doi.org/10.1145/22145.22192

## Scope determination

The literature supports no single universally best NP-complete testbed. CSP dichotomies classify fixed relation languages; Circuit-SAT is closest to arbitrary computation; proof complexity isolates no-instance certification; meta-complexity and magnification target indirect separations; exact-incidence systems provide unusually clean positive testbeds; bounded arithmetic studies formal provability rather than truth alone; interactive proofs provide a cross-cutting arithmetization bridge; and uniform lower-bound programmes must remain separate from nonuniform circuit claims.

No source in this map resolves P versus NP or licenses promotion of a model-specific, formal-theory, randomized, interactive, promise, or uniform lower bound to an unrestricted classical class separation.