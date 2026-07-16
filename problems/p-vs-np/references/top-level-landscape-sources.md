# Source Map — P versus NP Top-Level Landscapes

**Classification:** Primary-source and project-record map  
**Cutoff:** 2026-07-16  
**Use:** Supports [research-programme-landscape.md](research-programme-landscape.md) and [problem-testbed-landscape.md](problem-testbed-landscape.md)

## Source policy

- Prefer original papers, journal versions, proceedings versions, author preprints, or standard monographs.
- A source supports only the role stated below.
- A barrier theorem limits a family of techniques; it is not evidence that P versus NP is unresolvable.
- Project records are cited separately from external literature.

## Foundations and NP-completeness

### `[P01]` Cook — satisfiability and efficient verification

Stephen A. Cook, “The Complexity of Theorem-Proving Procedures,” *Proceedings of STOC*, 1971, pp. 151–158.

- Role: Cook–Levin foundation; Boolean satisfiability captures polynomial-time nondeterministic verification.
- Stable source: https://doi.org/10.1145/800157.805047

### `[P02]` Karp — natural NP-complete problems and reductions

Richard M. Karp, “Reducibility Among Combinatorial Problems,” in *Complexity of Computer Computations*, 1972, pp. 85–103.

- Role: polynomial reductions among logical, graph, covering, matching, routing, scheduling, and numerical problems.
- Stable source: https://doi.org/10.1007/978-1-4684-2001-2_9

## Constraint satisfaction and exact local relations

### `[P03]` Schaefer — Boolean CSP dichotomy

Thomas J. Schaefer, “The Complexity of Satisfiability Problems,” *Proceedings of STOC*, 1978, pp. 216–226.

- Role: dichotomy for fixed Boolean constraint languages; includes the NP-completeness of positive 1-in-3 SAT and positive NAE-SAT outside the tractable classes.
- Stable source: https://doi.org/10.1145/800133.804350

### `[P04]` Bulatov — finite-domain CSP dichotomy

Andrei A. Bulatov, “A Dichotomy Theorem for Nonuniform CSPs,” 2017.

- Role: independent proof of the finite-domain fixed-template CSP dichotomy.
- Preprint: https://arxiv.org/abs/1703.03021

### `[P05]` Zhuk — finite-domain CSP dichotomy

Dmitriy Zhuk, “A Proof of the CSP Dichotomy Conjecture,” 2017 / journal version.

- Role: independent proof and polynomial algorithm for finite constraint languages with the required polymorphism structure.
- Preprint: https://arxiv.org/abs/1704.01914

### `[P06]` Hasan, Mondal, and Rahman — robust positive planar 1-in-3 SAT hardness

Md. Manzurul Hasan, Debajyoti Mondal, and Md. Saidur Rahman, “Positive Planar Satisfiability Problems under 3-Connectivity Constraints,” 2021.

- Role: evidence that Positive 1-in-3 SAT remains NP-complete under strong planarity, connectivity, and occurrence restrictions; also records tractable neighbouring conditions.
- Preprint: https://arxiv.org/abs/2108.12500

### `[P07]` Bonnet and Paschos — exact 1-in-3 SAT algorithm

Édouard Bonnet and Vangelis Th. Paschos, “An Exact Algorithm for 1-in-3 SAT,” 2013.

- Role: representative exact-exponential algorithm for the selected exact-one relation.
- Preprint: https://arxiv.org/abs/1307.5776

### `[P08]` Darmann and Döcker — restricted monotone NAE-3SAT hardness

Andreas Darmann and Janosch Döcker, “On Simplified NP-Complete Variants of Not-All-Equal 3-SAT and 3-SAT,” 2019.

- Role: NP-completeness of strongly restricted positive NAE-3SAT variants.
- Preprint: https://arxiv.org/abs/1908.04198

### `[P09]` Hell and Nešetřil — graph homomorphism dichotomy

Pavol Hell and Jaroslav Nešetřil, “On the Complexity of H-Coloring,” *Journal of Combinatorial Theory, Series B* 48(1), 1990, pp. 92–110.

- Role: fixed undirected graph homomorphism is polynomial-time for bipartite targets and NP-complete for non-bipartite targets; 3-Coloring is a clean hard graph-CSP boundary case.
- Stable source: https://doi.org/10.1016/0095-8956(90)90132-J

## Algorithms to circuit lower bounds

### `[P10]` Williams — SAT algorithms and restricted circuit lower bounds

Ryan Williams, “New Algorithms and Lower Bounds for Circuits with Linear Threshold Gates,” 2014.

- Role: nontrivial satisfiability and evaluation algorithms yielding lower bounds for restricted circuit classes.
- Preprint: https://arxiv.org/abs/1401.2444

### `[P11]` Vyas and Williams — expanding algorithms-to-lower-bounds

Nikhil Vyas and Ryan Williams, “Lower Bounds Against Sparse Symmetric Functions of ACC Circuits: Expanding the Reach of #SAT Algorithms,” 2020.

- Role: representative modern theorem converting faster counting algorithms into stronger restricted-circuit lower bounds.
- Preprint: https://arxiv.org/abs/2001.07788

## Hardness versus randomness and meta-complexity

### `[P12]` Impagliazzo — hardness and derandomization survey

Russell Impagliazzo, “Hardness as Randomness: A Survey of Universal Derandomization,” 2003.

- Role: representative account of the hardness-versus-randomness connection and its relation to circuit lower bounds.
- Preprint: https://arxiv.org/abs/cs/0304040

### `[P22]` Allender et al. — MCSP and related meta-complexity

Eric Allender, Joshua A. Grochow, Dieter van Melkebeek, Cristopher Moore, and Andrew Morgan, “Minimum Circuit Size, Graph Isomorphism, and Related Problems,” 2017.

- Role: MCSP, compression, pseudorandomness, and reductions to meta-complexity problems.
- Preprint: https://arxiv.org/abs/1710.09806

### `[P23]` Chen et al. — hardness magnification and locality

Lijie Chen, Shuichi Hirahara, Igor C. Oliveira, Jan Pich, Ninad Rajgopal, and Rahul Santhanam, “Beyond Natural Proofs: Hardness Magnification and Locality,” 2019.

- Role: systematic study of hardness magnification, its prospects, and the locality barrier.
- Preprint: https://arxiv.org/abs/1911.08297

### `[P24]` Atserias and Müller — general magnification

Albert Atserias and Moritz Müller, “Simple General Magnification of Circuit Lower Bounds,” 2025.

- Status: preprint at the cutoff date.
- Role: modern general magnification theorems, including uniform MCSP-related consequences and thresholds below known lower bounds in selected models.
- Preprint: https://arxiv.org/abs/2503.24061

## Boolean and arithmetic circuit lower bounds

### `[P13]` Razborov — monotone circuit lower bounds

Alexander A. Razborov, “Lower Bounds on the Monotone Complexity of Some Boolean Functions,” *Soviet Mathematics Doklady* 31, 1985.

- Role: representative exponential lower bounds in monotone circuit models, including Clique-related functions.
- Scope: monotone lower bounds do not automatically transfer to circuits with negation.

### `[P16]` Mulmuley and Sohoni — Geometric Complexity Theory

Ketan D. Mulmuley and Milind Sohoni, “Geometric Complexity Theory I: An Approach to the P vs. NP and Related Problems,” *SIAM Journal on Computing* 31(2), 2001, pp. 496–526.

- Role: representation-theoretic and algebraic-geometric programme centred on permanent versus determinant.
- Stable source: https://doi.org/10.1137/S009753970038715X

## Proof barriers

### `[P14]` Baker, Gill, and Solovay — relativization

Theodore Baker, John Gill, and Robert Solovay, “Relativizations of the P =? NP Question,” *SIAM Journal on Computing* 4(4), 1975, pp. 431–442.

- Role: oracle worlds with opposite answers to P versus NP; barrier to relativizing proofs.
- Stable source: https://doi.org/10.1137/0204037

### `[P15]` Razborov and Rudich — natural proofs

Alexander A. Razborov and Steven Rudich, “Natural Proofs,” *Journal of Computer and System Sciences* 55(1), 1997, pp. 24–35.

- Role: conditional barrier to constructive, large combinatorial properties proving strong general circuit lower bounds.
- Stable source: https://doi.org/10.1006/jcss.1997.1494

### `[P17]` Aaronson and Wigderson — algebrization

Scott Aaronson and Avi Wigderson, “Algebrization: A New Barrier in Complexity Theory,” *ACM Transactions on Computation Theory* 1(1), 2009.

- Role: barrier extending relativization to many arithmetizing techniques.
- Preprint: https://arxiv.org/abs/0807.0261

## Proof complexity

### `[P18]` Cook and Reckhow — propositional proof systems

Stephen A. Cook and Robert A. Reckhow, “The Relative Efficiency of Propositional Proof Systems,” *Journal of Symbolic Logic* 44(1), 1979, pp. 36–50.

- Role: general proof-system framework and connection between polynomially bounded proof systems and `NP=coNP`.
- Stable source: https://doi.org/10.2307/2273702

### `[P19]` Krajíček — Cook–Reckhow framework review

Jan Krajíček, “The Cook-Reckhow Definition,” 2019.

- Role: modern explanation of proof systems, p-simulation, and their complexity-theoretic significance.
- Preprint: https://arxiv.org/abs/1909.03691

## Communication, branching, and representation models

### `[P20]` Kushilevitz and Nisan — communication complexity

Eyal Kushilevitz and Noam Nisan, *Communication Complexity*, Cambridge University Press, 1997.

- Role: foundational framework for interface and partition lower bounds.

### `[P21]` Razgon — ordered decision-diagram lower bounds

Igor Razgon, “Classification of OBDD Size for Monotone 2-CNFs,” 2021.

- Role: representative explicit lower bounds for ordered Boolean decision diagrams; imported by the closed Subset Sum exact-state route.
- Preprint: https://arxiv.org/abs/2103.09115

## Parameterized and fine-grained complexity

### `[P25]` Cygan et al. — parameterized algorithms

Marek Cygan, Fedor V. Fomin, Łukasz Kowalik, Daniel Lokshtanov, Dániel Marx, Marcin Pilipczuk, Michał Pilipczuk, and Saket Saurabh, *Parameterized Algorithms*, Springer, 2015.

- Role: fixed-parameter tractability, width-based dynamic programming, kernelization, and parameterized reductions.
- Stable source: https://doi.org/10.1007/978-3-319-21275-3

### `[P27]` Impagliazzo, Paturi, and Zane — exponential-time hypotheses

Russell Impagliazzo, Ramamohan Paturi, and Francis Zane, “Which Problems Have Strongly Exponential Complexity?” *Journal of Computer and System Sciences* 63(4), 2001, pp. 512–530.

- Role: ETH-style quantitative complexity and reductions.
- Stable source: https://doi.org/10.1006/jcss.2001.1774

## Isolation, approximation, counting, and quantum controls

### `[P26]` Valiant and Vazirani — unique solutions and isolation

Leslie G. Valiant and Vijay V. Vazirani, “NP Is as Easy as Detecting Unique Solutions,” *Theoretical Computer Science* 47, 1986, pp. 85–93.

- Role: randomized reduction from SAT to unique-solution SAT and isolation-based search relations.
- Stable source: https://doi.org/10.1016/0304-3975(86)90135-0

### `[P28]` Arora et al. — PCP theorem

Sanjeev Arora, Carsten Lund, Rajeev Motwani, Madhu Sudan, and Mario Szegedy, “Proof Verification and the Hardness of Approximation Problems,” *Journal of the ACM* 45(3), 1998, pp. 501–555.

- Role: PCP theorem and gap reductions underlying hardness of approximation and Label Cover infrastructure.
- Stable source: https://doi.org/10.1145/278298.278306

### `[P29]` Valiant — counting complexity

Leslie G. Valiant, “The Complexity of Enumeration and Reliability Problems,” *SIAM Journal on Computing* 8(3), 1979, pp. 410–421.

- Role: `#P` framework and completeness of natural counting problems.
- Stable source: https://doi.org/10.1137/0208032

### `[P30]` Bernstein and Vazirani — quantum complexity

Ethan Bernstein and Umesh Vazirani, “Quantum Complexity Theory,” *SIAM Journal on Computing* 26(5), 1997, pp. 1411–1473.

- Role: foundational quantum complexity model and separation from classical complexity claims.
- Stable source: https://doi.org/10.1137/S0097539796300921

## Project records

### `[P31]` Subset Sum investigation

Repository records under:

- `../investigations/subset-sum/README.md`
- `../investigations/subset-sum/STATUS.md`
- `../investigations/subset-sum/references/algorithmic-landscape.md`
- `../investigations/subset-sum/routes/structural-compression/CLOSEOUT.md`
- `../investigations/subset-sum/routes/exact-state-compression-barriers/CLOSEOUT.md`

Role:

- records two closed universal routes;
- supplies the reduction-generated compatibility audit;
- supplies model-specific representation boundaries;
- retains Subset Sum as an arithmetic adversarial control rather than an active route.

## Literature determination

The literature supports no single universally best NP-complete testbed.

- CSP and homomorphism dichotomies classify fixed local relation languages and identify tractable neighbours.
- Circuit-SAT is the closest direct object to arbitrary computation and the strongest algorithms-to-lower-bounds testbed.
- Proof complexity isolates no-instance certification.
- Meta-complexity and hardness magnification seek major consequences from smaller lower bounds.
- Exact-incidence systems provide unusually clean positive algorithmic testbeds because the local rule is simple while global compatibility remains NP-complete.

No source in this map resolves P versus NP or licenses promotion of a model-specific lower bound to an unrestricted class separation.