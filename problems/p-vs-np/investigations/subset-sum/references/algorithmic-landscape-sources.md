# Source Map — Subset Sum Algorithmic Landscape

**Classification:** Primary-source literature map  
**Cutoff:** 2026-07-16  
**Use:** Supports [algorithmic-landscape.md](algorithmic-landscape.md)

## Source policy

- Prefer the original paper, proceedings version, journal version, or author preprint.
- A source marked **preprint** has not been treated as independently established merely because it is recent.
- The landscape uses representative sources for each paradigm; it is not a complete bibliography of every refinement.
- Project proofs and closeouts are cited separately from external literature.

## Complexity foundations and classical algorithms

### `[R01]` Karp — NP-completeness framework

Richard M. Karp, “Reducibility Among Combinatorial Problems,” in *Complexity of Computer Computations*, 1972, pp. 85–103.

- Role: classical NP-completeness foundation and knapsack/subset-sum context.
- Stable source: https://doi.org/10.1007/978-1-4684-2001-2_9

### `[R02]` Horowitz and Sahni — meet in the middle

Ellis Horowitz and Sartaj Sahni, “Computing Partitions with Applications to the Knapsack Problem,” *Journal of the ACM* 21(2), 1974, pp. 277–292.

- Role: \(O^*(2^{n/2})\)-time meet-in-the-middle algorithm.
- Stable source: https://doi.org/10.1145/321812.321823

### `[R03]` Schroeppel and Shamir — time-space tradeoff

Richard Schroeppel and Adi Shamir, “A \(T=O(2^{n/2}), S=O(2^{n/4})\) Algorithm for Certain NP-Complete Problems,” *SIAM Journal on Computing* 10(3), 1981, pp. 456–464.

- Role: classical \(O^*(2^{n/2})\)-time, \(O^*(2^{n/4})\)-space algorithm.
- Stable source: https://doi.org/10.1137/0210033

### `[R41]` Pisinger — bounded weights

David Pisinger, “Linear Time Algorithms for Knapsack Problems with Bounded Weights,” *Journal of Algorithms* 33(1), 1999, pp. 1–14.

- Role: classic bounded-weight improvements and grouped numerical-range methods.

### `[R45]` Martello and Toth — practical exact hybrids

Silvano Martello and Paolo Toth, “A Mixture of Dynamic Programming and Branch-and-Bound for the Subset-Sum Problem,” *Management Science*.

- Role: representative exact solver engineering combining DP and search.
- Scope: practical exact methodology; no universal polynomial guarantee is imported.

## Modern pseudopolynomial algorithms

### `[R04]` Koiliaris and Xu — deterministic convolutional algorithm

Konstantinos Koiliaris and Chao Xu, “A Faster Pseudopolynomial Time Algorithm for Subset Sum,” later journal version “Faster Pseudopolynomial Time Algorithms for Subset Sum.”

- Result used: \(\widetilde O(\min\{T\sqrt n,T^{4/3},\sigma\})\) all-target computation.
- Preprint: https://arxiv.org/abs/1507.02318

### `[R05]` Bringmann — randomized near-linear pseudopolynomial time

Karl Bringmann, “A Near-Linear Pseudopolynomial Time Algorithm for Subset Sum,” SODA 2017.

- Result used: randomized \(\widetilde O(n+T)\) time and related low-space consequences.
- Preprint: https://arxiv.org/abs/1610.04712

### `[R06]` Jin and Wu — generating functions and modular counting

Ce Jin and Hongxun Wu, “A Simple Near-Linear Pseudopolynomial Time Randomized Algorithm for Subset Sum,” SOSA 2019.

- Result used: randomized \(\widetilde O(n+T)\) algorithm through generating-function and FFT methods; counting modulo a prime.
- Preprint: https://arxiv.org/abs/1807.11597

### `[R07]` Chan — deterministic near-linear pseudopolynomial time

Timothy M. Chan, “Derandomizing Pseudopolynomial Algorithms for Subset Sum,” 2026.

- Status: **preprint at the cutoff date**.
- Result used: first deterministic \(\widetilde O(T)\) all-target algorithm and derandomization of output-sensitive algorithms.
- Preprint: https://arxiv.org/abs/2601.01390

### `[R08]` Bringmann and Nakos — output-sensitive sumsets

Karl Bringmann and Vasileios Nakos, “Top-k-Convolution and the Quest for Near-Linear Output-Sensitive Subset Sum,” STOC 2020 / later preprint version.

- Result used: \(\widetilde O(U_T^{4/3})\) output-sensitive computation.
- Preprint: https://arxiv.org/abs/2107.13206

### `[R09]` Bringmann, Fischer, and Nakos — beating Bellman in all output regimes

Karl Bringmann, Nick Fischer, and Vasileios Nakos, “Beating Bellman’s Algorithm for Subset Sum,” SODA 2025.

- Result used: \(\widetilde O(U_T\sqrt n)\) output-sensitive algorithm and additive-combinatorial method.
- Preprint: https://arxiv.org/abs/2410.21942

### `[R10]` Jin, Vyas, and Williams — low-space pseudopolynomial algorithms

Ce Jin, Nikhil Vyas, and Ryan Williams, “Fast Low-Space Algorithms for Subset Sum,” SODA 2021.

- Results used: near-Bellman time with logarithmic or polylogarithmic workspace under stated randomized/deterministic models and time-space tradeoffs.
- Preprint: https://arxiv.org/abs/2011.03819

### `[R11]` Sajith — near-linear pseudopolynomial time and polynomial space

Thejas Radhika Sajith, “Subset Sum in Near-Linear Pseudopolynomial Time and Polynomial Space,” 2025.

- Status: **preprint at the cutoff date**.
- Results tracked: randomized \(\widetilde O(n+T)\) time with polynomial space and deterministic \(\widetilde O(nT)\) polynomial-space algorithm.
- Preprint: https://arxiv.org/abs/2508.04726

### `[R12]` Polak, Rohwedder, and Węgrzycki — small items

Adam Polak, Lars Rohwedder, and Karol Węgrzycki, “Knapsack and Subset Sum with Small Items,” ICALP 2021.

- Result used: \(\widetilde O(n+w^{5/3})\) Subset Sum algorithm, including succinct multiplicities.
- Preprint: https://arxiv.org/abs/2105.04035

### `[R13]` Chen, Lian, Mao, and Zhang — \(\sqrt{wT}\) regime

Lin Chen, Jiayi Lian, Yuchen Mao, and Guochuan Zhang, “An Improved Pseudopolynomial Time Algorithm for Subset Sum,” 2024.

- Result used: \(\widetilde O(n+\sqrt{wT})\) time.
- Preprint: https://arxiv.org/abs/2402.14493

### `[R14]` Axiotis, Backurs, and Tzamos — modular subset sum

Kyriakos Axiotis, Arturs Backurs, and Christos Tzamos, “Fast Modular Subset Sum using Linear Sketching,” SODA 2019.

- Result used: near-linear \(\widetilde O(m)\) modular Subset Sum.
- Preprint: https://arxiv.org/abs/1807.04825

### `[R35]` Antonopoulos et al. — cardinality and multi-target variants

Antonis Antonopoulos, Aris Pagourtzis, Stavros Petsalakis, and Manolis Vasilakis, “Faster Algorithms for k-Subset Sum and Variations,” 2021.

- Role: multi-target and cardinality-constrained pseudopolynomial algorithms.
- Preprint: https://arxiv.org/abs/2112.04244

### `[R36]` Dutta and Rajasree — solution-count-sensitive search

Pranjal Dutta and Mahesh Sreekumar Rajasree, “Efficient Reductions and Algorithms for Variants of Subset Sum,” 2021.

- Role: algorithms parameterized by the number of realizable subsets and unique-solution hardness under randomized reductions.
- Preprint: https://arxiv.org/abs/2112.11020

## Structured and additive-combinatorial regimes

### `[R15]` Bringmann and Wellnitz — dense Subset Sum dichotomy

Karl Bringmann and Philip Wellnitz, “On Near-Linear-Time Algorithms for Dense Subset Sum,” SODA 2021.

- Result used: near-linear algorithm under an explicit dense-regime inequality and matching conditional boundaries.
- Preprint: https://arxiv.org/abs/2010.09096

### `[R16]` Randolph and Węgrzycki — small doubling

Tim Randolph and Karol Węgrzycki, “Parameterized Algorithms on Integer Sets with Small Doubling: Integer Programming, Subset Sum and k-SUM,” 2024.

- Result used: Subset Sum in \(n^{O_C(1)}\) for doubling constant \(C\), plus constructive Freiman machinery.
- Preprint: https://arxiv.org/abs/2407.18228

### `[R17]` Lagarias and Odlyzko — low-density lattice algorithm

Jeffrey C. Lagarias and Andrew M. Odlyzko, “Solving Low-Density Subset Sum Problems,” *Journal of the ACM* 32(1), 1985, pp. 229–246.

- Role: foundational almost-all polynomial-time low-density lattice result.
- Stable source: https://doi.org/10.1145/2455.2461

### `[R18]` Joux and Węgrzycki — improved average-case lattice guarantee

Antoine Joux and Karol Węgrzycki, “Improving Lagarias-Odlyzko Algorithm For Average-Case Subset Sum: Modular Arithmetic Approach,” 2024.

- Result used: improved density guarantee and multi-target modular-lattice method.
- Preprint: https://arxiv.org/abs/2408.16108

### `[R19]` Austrin et al. — collision multiplicity and dense hardness

Per Austrin, Mikko Koivisto, Petteri Kaski, and Jesper Nederlof, “Dense Subset Sum may be the Hardest,” 2015.

- Result used: faster algorithms in low- and high-bin-size regimes and density reduction insights.
- Preprint: https://arxiv.org/abs/1508.06019

### `[R39]` DeVos et al. — structural subset-sum bounds in groups

Matt DeVos, Luis Goddyn, Bojan Mohar, and Robert Šámal, “A Quadratic Lower Bound for Subset Sums,” 2006.

- Role: representative additive-combinatorial lower bound on subset-sum growth in finite abelian groups.
- Preprint: https://arxiv.org/abs/math/0612045

### `[R40]` Pataki and Tural — low-density infeasibility certificates

Gábor Pataki and Mustafa Tural, “Branching Proofs of Infeasibility in Low Density Subset Sum Problems,” 2008.

- Role: polynomially computable branching certificates under low-density and almost-all-right-hand-side promises.
- Preprint: https://arxiv.org/abs/0808.0023

## Exact exponential algorithms and cryptanalytic representations

### `[R20]` Chen, Jin, Randolph, and Servedio — polynomial-factor worst-case improvement

Xi Chen, Yaonan Jin, Tim Randolph, and Rocco A. Servedio, “Subset Sum in Time \(2^{n/2}/\mathrm{poly}(n)\),” 2023.

- Result used: first worst-case improvement over meet-in-the-middle by a polynomial factor in standard RAM models.
- Preprint: https://arxiv.org/abs/2301.07134

### `[R21]` Austrin, Kaski, Koivisto, and Määttä — worst-case dissection

Per Austrin, Petteri Kaski, Mikko Koivisto, and Jussi Määttä, “Space-Time Tradeoffs for Subset Sum: An Improved Worst Case Algorithm,” 2013.

- Role: worst-case dissection time-space curves using random composite moduli and bailout controls.
- Preprint: https://arxiv.org/abs/1303.0609

### `[R22]` Nederlof and Węgrzycki — Orthogonal Vectors space improvement

Jesper Nederlof and Karol Węgrzycki, “Improving Schroeppel and Shamir’s Algorithm for Subset Sum via Orthogonal Vectors,” STOC 2021.

- Result used: randomized \(O^*(2^{0.5n})\) time and \(O^*(2^{0.249999n})\) space.
- Preprint: https://arxiv.org/abs/2010.08576

### `[R23]` Belova et al. — further space improvement

Tatiana Belova, Nikolai Chukhin, Alexander S. Kulikov, and Ivan Mihajlin, “Improved Space Bounds for Subset Sum,” 2024.

- Result used: improved exponential-space exponent while retaining \(O^*(2^{n/2})\) time.
- Preprint: https://arxiv.org/abs/2402.13170

### `[R24]` Howgrave-Graham and Joux — representation technique

Nick Howgrave-Graham and Antoine Joux, “New Generic Algorithms for Hard Knapsacks,” EUROCRYPT 2010.

- Role: introduced the modern representation technique for random/hard knapsack instances.
- Scope note: not a general worst-case polynomial algorithm.

### `[R25]` Becker, Coron, and Joux — improved representation algorithm

Anja Becker, Jean-Sébastien Coron, and Antoine Joux, “Improved Generic Algorithms for Hard Knapsacks,” EUROCRYPT 2011.

- Role: improved random-instance representation-method exponent.
- Scope note: cryptanalytic/random-instance regime.

### `[R26]` Esser and May — heuristic sampling representation method

André Esser and Alexander May, “Better Sample — Random Subset Sum in \(2^{0.255n}\) and its Impact on Decoding Random Linear Codes,” 2019.

- Role: heuristic random-instance search-tree and sampling analysis.
- Preprint: https://arxiv.org/abs/1907.04295

## Quantum algorithms

### `[R27]` Allcock et al. — quantum dynamic-programming approach

Jonathan Allcock, Yassine Hamoudi, Antoine Joux, Felix Klingelhöfer, and Miklos Santha, “Classical and Quantum Algorithms for Variants of Subset-Sum via Dynamic Programming,” 2021.

- Result used: general classical and quantum Subset Sum algorithms around \(\widetilde O(2^{n/2})\) and \(\widetilde O(2^{n/3})\), plus related variants.
- Preprint: https://arxiv.org/abs/2111.07059

## Fine-grained and representation lower bounds

### `[R28]` Abboud et al. — SETH lower bound

Amir Abboud, Karl Bringmann, Danny Hermelin, and Dvir Shabtay, “SETH-Based Lower Bounds for Subset Sum and Bicriteria Path,” 2017 / journal version 2022.

- Result used: excludes \(T^{1-\varepsilon}2^{o(n)}\)-time algorithms under SETH and supplies a Direct-OR theorem.
- Preprint: https://arxiv.org/abs/1704.04546

### `[R29]` Razgon — OBDD lower bounds for monotone 2-CNF

Igor Razgon, “Classification of OBDD Size for Monotone 2-CNFs,” 2021.

- Role: imported OBDD lower bound used by the project’s ordered assignment-query theorem.
- Preprint: https://arxiv.org/abs/2103.09115

### `[R30]` Capelli et al. — Tree Decision Diagrams

Florent Capelli, YooJung Choi, Stefan Mengel, Martín Muñoz, and Guy Van den Broeck, “A Canonical Generalization of OBDD,” 2026.

- Status: **preprint at the cutoff date**.
- Role: TDD definition, tractable operations, and bounded-width compilation framework.
- Preprint: https://arxiv.org/abs/2604.05537

### `[R31]` Mengel — DNNF compilation lower bounds

Stefan Mengel, “Parameterized Compilation Lower Bounds for Restricted CNF-formulas,” 2016.

- Role: unconditional parameterized lower bounds for DNNF representations under graph-structure parameters.
- Preprint: https://arxiv.org/abs/1604.06715

### `[R32]` Włodarczyk — certification complexity

Michał Włodarczyk, “Does Subset Sum Admit Short Proofs?” 2024.

- Role: systematic study of certificate length parameterized by item precision and equivalences with other problems.
- Preprint: https://arxiv.org/abs/2409.03526

## Approximation

### `[R33]` Kellerer et al. — Subset Sum FPTAS

Hans Kellerer, Renata Mansini, Ulrich Pferschy, and Maria Grazia Speranza, “An Efficient Fully Polynomial Approximation Scheme for the Subset-Sum Problem,” *Journal of Computer and System Sciences* 66(2), 2003, pp. 349–370.

- Role: representative exact statement of successful lossy list compression.

### `[R34]` Chen et al. — near-linear Partition FPTAS

Lin Chen, Jiayi Lian, Yuchen Mao, and Guochuan Zhang, “Approximating Partition in Near-Linear Time,” 2024.

- Result used: \(\widetilde O(n+1/\varepsilon)\) FPTAS for Partition through weak Subset Sum approximation.
- Preprint: https://arxiv.org/abs/2402.11426

## Project records

### `[R37]` Structural compression route

Repository records under:

- `../routes/structural-compression/README.md`
- `../routes/structural-compression/CLAIMS.md`
- `../routes/structural-compression/CLOSEOUT.md`

Results used:

- residue-completion lemma;
- polynomially bounded exact-decomposition theorem;
- failure of the universal bundle and forced/progression/lattice routes on canonical reduction-generated instances.

### `[R38]` Exact-state compression barrier route

Repository records under:

- `../routes/exact-state-compression-barriers/README.md`
- `../routes/exact-state-compression-barriers/CLAIMS.md`
- `../routes/exact-state-compression-barriers/CLOSEOUT.md`

Results used:

- unrestricted representation-size boundary;
- assignment-target embedding and ordered model lower bound;
- exact Minkowski semantics;
- unevaluated-DAG, unrestricted-intersection, progression-union, and bounded-residue branching boundaries;
- closeout of the broad exact-state model search.

## Literature determination

The literature currently supports two strong general frontiers:

1. deterministic near-linear pseudopolynomial dependence on the numeric target range;
2. worst-case exact exponential dependence near \(2^{n/2}\) on the item count.

The literature also supplies numerous polynomial or faster algorithms under explicit promises—dense regimes, small maximum item, small doubling, low density, bounded collision multiplicity, and related parameters—but no known theorem bounds one of these favourable parameters on every binary-encoded instance.

No source in this map establishes classical polynomial-time Subset Sum, a general lower bound proving \(P\ne NP\), or a universal exact compression theorem.
