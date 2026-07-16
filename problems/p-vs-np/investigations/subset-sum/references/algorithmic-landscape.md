# Subset Sum Algorithmic Landscape

**Classification:** Literature audit and route-selection matrix  
**Cutoff:** 2026-07-16  
**Review:** `CHECKED` against the source map and current project records  
**Scope:** Classical positive-integer Subset Sum unless a row explicitly states otherwise

## Purpose and completeness boundary

This document replaces a flat list of techniques with a paradigm-level map of the currently known directions relevant to exact Subset Sum and the P-versus-NP programme.

It is intended to be complete at the level of major algorithmic, structural, representation, and lower-bound paradigms. It does not list every implementation, constant-factor improvement, application variant, or paper. A direction is included when it supplies at least one of:

- a general exact algorithm;
- a substantial pseudopolynomial improvement;
- a polynomial algorithm on a mathematically specified class;
- a reusable exact representation or compression mechanism;
- a serious lower-bound or model-barrier programme;
- evidence about what succeeds after relaxing exactness or changing the computational model.

The source identifiers refer to [algorithmic-landscape-sources.md](algorithmic-landscape-sources.md).

## Notation

Let the instance be positive integers \(A=(a_1,\ldots,a_n)\) and target \(T\).

- \(L\): total binary input length.
- \(\Sigma(A)\): the set of all subset sums.
- \(U_T=|\Sigma(A)\cap[0,T]|\): truncated output size.
- \(w=\max_i a_i\): maximum item value.
- \(\sigma=\sum_i a_i\): total item sum.
- \(\widetilde O\): suppresses polylogarithmic factors.
- \(O^*\): suppresses polynomial factors in the input length.

A running time polynomial in \(T\), \(w\), or \(\sigma\) is pseudopolynomial and may be exponential in \(L\).

---

## A. General exact algorithms

These algorithms are correct on every instance when run with the guarantee stated in the scope column. None is known to run in time polynomial in \(L\).

| ID | Direction | Core mechanism | Strongest established contribution | Exact scope | Central obstruction | Research disposition | Sources |
|---|---|---|---|---|---|---|---|
| `A01` | Exhaustive enumeration | Enumerate all \(2^n\) subsets or traverse the inclusion/exclusion tree | Exact decision in \(O^*(2^n)\) time and polynomial space | Deterministic, worst case | Full binary choice tree remains exponential | Baseline only | `[R01]` |
| `A02` | Branch and bound | Order items and prune when residual upper or lower bounds exclude the target | Often eliminates large practical search regions | Deterministic, exact; data dependent | Adversarial instances can preserve both branches at almost every level | Practical exact method; not a polynomial route without a global progress theorem | `[R45]` |
| `A03` | Meet in the middle | Split the items, enumerate both half-sum lists, and solve a two-list complement query | \(O^*(2^{n/2})\) time and \(O^*(2^{n/2})\) space | Deterministic, worst case | Half-list size is exponential | Established benchmark | `[R02]` |
| `A04` | Schroeppel-Shamir | Generate pair sums from four quarter lists lazily | \(O^*(2^{n/2})\) time and \(O^*(2^{n/4})\) space | Deterministic, worst case | Time exponent remains \(1/2\) | Established time-space benchmark | `[R03]` |
| `A05` | Worst-case bit-packed meet in the middle | Combine representation ideas with word-RAM packing | \(2^{n/2}/\operatorname{poly}(n)\) worst-case time | Exact, worst case in stated RAM models | No known \(O^*(2^{(1/2-c)n})\) algorithm for constant \(c>0\) | Active exact-exponential line | `[R20]` |
| `A06` | Dissection algorithms | Recursively split list-merging constraints through random moduli | Improved worst-case time-space tradeoff curves | Randomized, with worst-case resource bounds and the error model stated by each construction | Every known curve remains exponential | Active time-space line | `[R21]` |
| `A07` | Representation technique | Give a solution many decompositions and filter partial lists by modular constraints | Strong algorithms on random or cryptographic-density instances | Usually average-case, heuristic, or one-sided depending on the variant | Worst-case inputs need not supply enough balanced representations | Powerful outside universal worst-case guarantees | `[R24]`, `[R25]`, `[R26]` |
| `A08` | Orthogonal-vectors-assisted representations | Reduce filtered half-list matching to structured Orthogonal Vectors | Improves exponential space below the Schroeppel-Shamir exponent while retaining \(O^*(2^{n/2})\) time | Randomized, with worst-case time-space guarantees as stated in the source | Does not reduce the time exponent | Retained exact time-space direction | `[R22]`, `[R23]` |
| `A09` | Polynomial-space exhaustive algorithms | Recompute or recursively generate partial sums instead of storing exponential lists | Exact polynomial-space algorithms, generally with larger time | Deterministic or randomized depending on construction | Avoiding storage normally causes extensive recomputation | Space-focused direction, not polynomial time | `[R10]`, `[R21]` |
| `A10` | Hybrid DP and meet in the middle | Use pseudopolynomial DP on one region and enumeration on another | Strong practical and parameter-regime tradeoffs | Exact, worst case when fully explored | One of the numerical range or subset-count dimensions can still be exponential | Useful regime selector | `[R05]`, `[R19]` |
| `A11` | SAT, integer-programming, SMT, and constraint encodings | Translate selection variables and the target equation into a general exact solver | Transfers clause learning, cutting planes, propagation, and mature engineering | Exact if the backend is exact | The encoding preserves NP-completeness; solver success has no universal polynomial bound | Practical and comparative, not an independent complexity collapse | `[R01]` |
| `A12` | Quantum meet in the middle and amplitude amplification | Search list pairs or modular buckets quantumly | General quantum algorithms around \(\widetilde O(2^{n/3})\) are known | Quantum, exact or bounded-error according to the algorithm | Still exponential; \(\mathrm{BQP}\) membership would not prove classical \(P=NP\) | Separate computational model | `[R27]` |

---

## B. Pseudopolynomial and all-target algorithms

These methods exploit the numerical target range. They are the strongest general algorithms when \(T\) is moderate, but they do not run in time polynomial in \(\log T\).

| ID | Direction | Core mechanism | Strongest established contribution | Exact scope | Central obstruction | Research disposition | Sources |
|---|---|---|---|---|---|---|---|
| `B01` | Bellman dynamic programming | Maintain the reachable sums after each item | \(O(nT)\) time and \(O(T)\) space; computes every reachable sum up to \(T\) | Deterministic, exact, worst case | \(T\) may be exponential in its binary length | Fundamental baseline | `[R04]`, `[R05]` |
| `B02` | Word-parallel bitset DP | Update a bit vector by shift and bitwise OR | Roughly \(O(nT/W)\) word operations on a \(W\)-bit word RAM | Deterministic, exact | Still linear in the numeric range | Important engineering realization of Bellman DP | `[R04]` |
| `B03` | Divide-and-conquer convolution | Combine cardinality-bounded sumsets using fast polynomial multiplication | Deterministic \(\widetilde O(\min\{T\sqrt n,T^{4/3},\sigma\})\) all-target computation | Deterministic, exact | Pseudopolynomial dependence remains | Established algebraic improvement | `[R04]` |
| `B04` | Randomized near-linear pseudopolynomial time | Color-code items into balanced groups and convolve | \(\widetilde O(n+T)\) randomized time | Monte Carlo, worst case, with bounded failure probability | Numeric range remains; randomness was originally required | Established; derandomized by `B06` | `[R05]` |
| `B05` | Generating-function power-series algorithms | Manipulate logarithms, exponentials, or counts of \(\prod_i(1+x^{a_i})\) modulo a prime | \(\widetilde O(n+T)\) randomized time, including modular counting in representative work | Monte Carlo; arithmetic operations are exact but the random choice controls correctness probability | Degree range is still \(T\); modular cancellation or prime selection must be controlled | Established algebraic route | `[R06]` |
| `B06` | Deterministic near-linear pseudopolynomial time | Deterministically construct halvers and combine bounded-cardinality sumsets | First deterministic \(\widetilde O(T)\) all-target algorithm, with input-reading overhead understood | Deterministic, exact; 2026 preprint | This is near optimal in \(T\), but not polynomial in \(\log T\) | Current pseudopolynomial frontier | `[R07]` |
| `B07` | Output-sensitive sparse convolution | Compute only the lowest nonzero monomials or reachable sums | \(\widetilde O(U_T^{4/3})\) output-sensitive all-target algorithm | Randomized originally; deterministic derandomization reported in 2026 | \(U_T\) can be \(\Theta(T)\) or exponential in \(L\) | Established sparse-output regime | `[R08]`, `[R07]` |
| `B08` | Bellman-beating output-sensitive algorithms | Use additive-combinatorial structure to reduce the per-output item factor | \(\widetilde O(U_T\sqrt n)\) all-target computation | Randomized in the original result; deterministic derandomization reported | Output itself can be enormous | Current output-sensitive frontier | `[R09]`, `[R07]` |
| `B09` | Low-space pseudopolynomial algebraization | Recover coefficients or witnesses without storing the full DP table | \(\widetilde O(nT)\) time with logarithmic random-access workspace in one randomized model; deterministic polylog-space variants with higher time | Exact with the randomness and failure guarantees stated by the source | Saves space, not pseudopolynomial time | Established space direction | `[R10]` |
| `B10` | Near-linear pseudopolynomial time with polynomial space | Use multipoint evaluation to reduce the low-space bottleneck | Randomized \(\widetilde O(n+T)\) time with polynomial space; deterministic \(\widetilde O(nT)\) with polynomial space in a 2025 preprint | Preprint; correctness and randomness as stated in the source | Still pseudopolynomial; result requires independent literature maturation | Track, do not overstate | `[R11]` |
| `B11` | Small-maximum-item algorithms | Parameterize by \(w=\max a_i\) and exploit proximity and additive structure | \(\widetilde O(n+w^{5/3})\) for Subset Sum with succinct multiplicities; later \(\widetilde O(n+\sqrt{wT})\) regimes | Deterministic exact, restricted parameter regime | \(w\) can be exponentially large in \(L\) | Strong tractable parameter | `[R12]`, `[R13]` |
| `B12` | Bounded-weight and bounded-multiplicity DP | Group equal weights and process bounded numerical ranges | Linear or near-linear dependence on \(n\) and the bounded maximum weight in classic regimes | Deterministic exact, restricted | Bound is numeric, not binary-length universal | Mature restricted algorithm family | `[R41]`, `[R12]` |
| `B13` | Modular Subset Sum algorithms | Compute reachable residues in \(\mathbb Z_m\) | Near-linear \(\widetilde O(m)\) algorithms, including linear-sketching methods | Exact for the modular problem | Modular reachability is weaker than exact integer reachability; witnesses across moduli need not agree | Useful subroutine and warning | `[R14]` |
| `B14` | Unbounded and multi-target variants | Permit item reuse or several target coordinates and adapt convolutional DP | Near-linear or improved pseudopolynomial algorithms exist for several variants | Exact for the stated variant | Variant structure may remove the 0-1 compatibility difficulty and does not transfer automatically | Source of techniques, not a solution to 0-1 Subset Sum | `[R05]`, `[R35]` |

---

## C. Structured and parameterized exact regimes

These directions give polynomial or improved algorithms when an explicit parameter is controlled. They are candidates for a positive tractable-subclass route, not universal algorithms unless the parameter is proved polynomially bounded on all instances.

| ID | Direction | Structural parameter or promise | Established achievement | Why attractive | Failure on unrestricted instances | Research disposition | Sources |
|---|---|---|---|---|---|---|---|
| `C01` | Dense additive-combinatorial regimes | Relations among \(n,T,w,\sigma\) force long intervals or dense sumsets | Near-linear algorithms in specified dense regimes, with matching conditional boundaries | Converts additive density into exact coverage | Reduction-generated instances can lie outside the favourable inequality | High-quality tractable-subclass candidate | `[R15]` |
| `C02` | Small doubling | \(C=|A+A|/|A|\) is bounded | Subset Sum solvable in \(n^{O_C(1)}\); constructive Freiman structure is algorithmic | Gives a rigorous global additive-structure parameter | \(C\) is unbounded on general inputs; FPT dependence remains open in stronger forms | Strong tractable-subclass candidate | `[R16]` |
| `C03` | Low-density lattice reduction | Number of items is small relative to item bit length and the solution behaves generically | Polynomial-time recovery for almost all sufficiently low-density instances in classical analyses | Geometric encoding can isolate the solution | Guarantee is average-case or promise-based, not adversarial worst case | Retain as structured/average-case route only | `[R17]` |
| `C04` | Improved modular-lattice average-case methods | Use primal and dual lattice information plus modular equations | Improves the classical density guarantee and supports multiple targets after one reduction call | Modernizes a foundational cryptanalytic route | Still an almost-all or distributional theorem | Active average-case lattice research | `[R18]` |
| `C05` | Collision multiplicity or maximum bin size | \(\beta=\max_s|\{S:\sum_{i\in S}a_i=s\}|\) | Truly faster exponential algorithms for low- and high-collision regimes | Identifies where list compression is possible | Intermediate collision regimes may remain hard; \(\beta\) is not efficiently known a priori | Useful exact-exponential parameter | `[R19]` |
| `C06` | Superincreasing and forced-separation instances | Each large item exceeds the sum of all smaller remaining items, or a similar residual dominance rule holds | Greedy or forced include/exclude reasoning solves the instance in polynomial time | Exact target-relative simplification without materializing all sums | General instances need not contain a forced item | Established restricted class; retained by the project | `[R37]` |
| `C07` | Succinct multiplicities and grouped values | A bounded weight range permits equal values to be represented by binary-encoded multiplicities | Polynomial or improved pseudopolynomial algorithms through proximity, bounded integer programming, and grouped DP | Compresses repeated values without expanding every occurrence | The maximum weight or number of represented values can grow exponentially with binary input length | Viable positive subclass when the numerical parameter is explicit | `[R12]` |
| `C08` | Unary or polynomially bounded numerical range | \(T\), \(w\), or \(\sigma\) is polynomial in the input-description parameter | Pseudopolynomial algorithms become genuine polynomial algorithms | Completely understood boundary of weak NP-completeness | Does not cover binary-encoded large numbers | Established baseline subclass | `[R01]`, `[R07]` |
| `C09` | Cardinality-constrained solutions | Bound the number of selected items or track exact cardinality | Faster pseudopolynomial algorithms and meet-in-the-middle variants for cardinality constraints | Separates small witnesses from large arbitrary subsets | Cardinality alone does not yield a universal polynomial algorithm and connects to k-SUM hardness | Restricted/parameterized direction | `[R35]` |
| `C10` | Few solutions or unique solutions | Bound the number of target-realizing subsets | Search and witness algorithms can scale with the number of solutions | Makes witness recovery output sensitive | Unique-solution Subset Sum remains hard under randomized reductions; few witnesses do not imply easy decision | Useful diagnostic, weak universal route | `[R36]` |
| `C11` | Random-instance and cryptanalytic density regimes | Items and targets follow a specified random modular distribution | Representation and sampling methods achieve substantially smaller heuristic exponents | Important for cryptography and average-case complexity | Distributional success supplies no worst-case guarantee | Separate average-case programme | `[R24]`, `[R25]`, `[R26]` |
| `C12` | Residue completion and central intervals | A long \(q\)-step progression plus disjoint representatives of all residues modulo \(q\) | Exact sufficient condition for a fully reachable central interval | Provides a proved local coverage mechanism | Does not describe all sums or guarantee a globally polynomial decomposition | `PROVED / CHECKED` project result; restricted use | `[R37]` |
| `C13` | Polynomially bounded exact decompositions | Every exact summary, branch, merge, and intermediate encoded state is globally polynomial | Polynomial-time decision on any class admitting such a constructible decomposition | States the correct success criterion for structural algorithms | Proving the criterion for a broad nontrivial class is the entire difficulty | `PROVED / CHECKED` project boundary theorem | `[R37]` |
| `C14` | Low-width Boolean or arithmetic decompositions | Bound treewidth, pathwidth, factor width, or an analogous item-interaction width | Knowledge-compilation models are fixed-parameter tractable on some bounded-width Boolean families | Offers a concrete interface-complexity parameter | A natural width that both describes arbitrary Subset Sum arithmetic and stays bounded is unknown | Open tractable-subclass design direction | `[R30]`, `[R31]`, `[R38]` |
| `C15` | Proofs of infeasibility in low-density regimes | Find a short branching hyperplane or Diophantine certificate | Polynomially computable infeasibility certificates for specified low-density promises and almost all right-hand sides | Targets no-instances directly rather than enumerating sums | Promise and almost-all quantifiers do not cover arbitrary instances | Restricted certificate route | `[R40]` |

---

## D. Candidate universal compression and representation mechanisms

These are mechanisms one might try to turn into a polynomial-time exact algorithm. A compact final syntax is not sufficient: construction time, query time, all intermediate objects, and witness compatibility must also be polynomially bounded.

| ID | Direction | Representation or operation | What it already achieves | Exact missing theorem | Known failure mode or boundary | Project assessment | Sources |
|---|---|---|---|---|---|---|---|
| `D01` | Generating-function product | \(F(x)=\prod_i(1+x^{a_i})\) | Compact exact syntax; \([x^T]F(x)\neq0\) exactly characterizes yes-instances | Polynomial-time random access to one coefficient of the succinct product | Unevaluated product syntax simply stores the original nondeterministic choices | Open only with a new coefficient-query theorem | `[R06]`, `[R38]` |
| `D02` | Direct zero-versus-nonzero coefficient testing | Decide whether \([x^T]F(x)=0\) without counting exactly | Avoids recovering the number of solutions | Exact deterministic polynomial-time nonzeroness test in binary input length | The query is definitionally the original Subset Sum decision problem | Not a separate route until a mechanism is specified | `[R06]` |
| `D03` | Truncated polynomial multiplication | Multiply factors modulo \(x^{T+1}\) using FFT or number-theoretic transforms | Accelerates all coefficients up to \(T\) | Remove dependence on polynomial degree while preserving exact target information | Dense polynomial operations inherently touch the pseudopolynomial range in current methods | Mature pseudopolynomial tool, not universal compression | `[R04]`, `[R06]`, `[R07]` |
| `D04` | Arithmetic circuits and power-series identities | Store or transform generating functions by compact circuits | Supports logarithm/exponential and modular-counting algorithms | Polynomial construction and exact coefficient extraction for arbitrary binary exponents | General circuits can hide hard coefficient computation | Candidate only under a sharply restricted circuit model | `[R06]`, `[R38]` |
| `D05` | Sparse reachable-set dictionaries | Store only sums actually reached | Output-sensitive algorithms avoid scanning gaps | Prove \(U_T\) polynomial or answer membership without enumerating \(U_T\) | Distinct reachable sums can be exponential in \(L\) | Strong adaptive algorithm, not universal route | `[R08]`, `[R09]` |
| `D06` | Exact state equivalence | Merge partial states having identical future target behaviour | Would directly repair dynamic programming | Efficiently construct a polynomial-index equivalence valid under all suffixes | Canonical SAT reductions preserve many incompatible assignment contexts | Broad route closed absent a new equivalence theorem | `[R37]`, `[R38]` |
| `D07` | Interval, progression, lattice, and semilinear summaries | Represent large regular reachable regions by few arithmetic atoms | Exact on highly structured blocks; supports coverage certificates | Exact composition with globally polynomial atom count and compatibility data | Progression unions can be exponential even on easy superincreasing instances | Broad normalized-set route rejected | `[R37]`, `[R38]` |
| `D08` | Item-block Minkowski composition | Compose disjoint blocks by \(\Sigma(B_0\uplus B_1)=\Sigma(B_0)+\Sigma(B_1)\) | Supplies exact compositional semantics | Normalize and query every sumset node in polynomial total cost | An unevaluated Minkowski DAG is always linear size but leaves membership unresolved | Syntax-size lower bounds are vacuous | `[R38]` |
| `D09` | Modular arithmetic | Track reachable sums in \(\mathbb Z_m\) | Small finite state spaces and fast modular algorithms | Lift modular membership to exact integer membership | Different exact sums collide in one residue | Useful subroutine; insufficient alone | `[R14]`, `[R38]` |
| `D10` | Multiple modular fingerprints and Chinese remaindering | Use several moduli whose product exceeds the numerical range | Can uniquely identify one fixed integer when all residues belong to the same witness | Preserve a common subset witness across every modulus | Marginal residue reachability may be witnessed by different subsets; joint states restore the large product space | Compatibility is the decisive unresolved information | `[R38]` |
| `D11` | Randomized hashing, color coding, and sketches | Map sums or items into smaller buckets while controlling collisions probabilistically | Gives near-linear pseudopolynomial and modular algorithms | Zero-error or deterministically exact polynomial-in-\(L\) algorithm | Derandomization does not remove numeric-range dependence; residual collision probability changes the complexity-class conclusion | Powerful algorithmic tool, not by itself a \(P=NP\) route | `[R05]`, `[R07]`, `[R14]` |
| `D12` | Compressed half-sum representations | Store meet-in-the-middle lists as generators, filters, or implicit queues | Improves space and average-case exponents | Worst-case polynomial representation with polynomial complement queries | Worst-case half sums may require exponentially many distinctions | Active exact-exponential, not polynomial | `[R21]`, `[R22]`, `[R23]` |
| `D13` | Ordered decision diagrams | Compile assignment-target membership into OBDDs or related ordered state graphs | Enables unconditional model-specific lower bounds | Show every relevant arithmetic algorithm compiles into the ordered model with polynomial overhead | Targets can expose assignment bits; unrestricted algorithms evaluate them directly | Model-specific barrier retained; broad transfer failed | `[R29]`, `[R38]` |
| `D14` | Tree Decision Diagrams and decomposable circuits | Compose disjoint variable blocks under a tree or vtree | More expressive than OBDDs; tractable operations and bounded-width compilation | Faithfully include large-modulus arithmetic summaries while excluding general circuit simulation | Explicit tables are too weak; succinct transitions can be as expressive as circuits | Open only with a materially new bridge theorem | `[R30]`, `[R31]`, `[R38]` |
| `D15` | Arithmetic proof graphs | Combine exact summaries, coverage certificates, residual transformations, and branching | Faithfully models more structural algorithms than one final set language | Fully specify a restricted grammar that contains needed arithmetic but cannot simulate polynomial Boolean computation | Compact bounded residue-range tests plus unrestricted repeated branching evaluate width-three CNF slices | Broad route closed under current grammar families | `[R38]` |
| `D16` | Lattice and geometric encodings | Map Boolean selections to short or special lattice vectors | Collapses many low-density or random instances | Worst-case guarantee that the desired vector remains uniquely recoverable and efficiently found | Adversarial high-density and structured reductions defeat the uniqueness promise | Restricted/average-case only | `[R17]`, `[R18]` |
| `D17` | Polynomial preprocessing plus exact target queries | Compile the item multiset once and answer arbitrary targets later | Separates representation construction from repeated queries | Polynomial compilation, polynomial representation, and polynomial exact query for every instance | Such a scheme exists for all instances if and only if \(P=NP\) | Boundary equivalence, not an easier intermediate goal | `[R38]` |
| `D18` | Short certificates and few nondeterministic bits | Seek compact certificates parameterized by item precision rather than item count | Connects Subset Sum to certification complexity and Boolean ILP | Polynomially bounded certificates verifiable in polynomial time for all yes/no instances under the chosen model | Certificate size questions can be as hard as major parameterized-complexity problems | Independent proof-complexity direction | `[R32]` |

---

## E. Lower bounds, barriers, and adversarial audits

These directions do not produce a positive algorithm. They delimit algorithm families or test whether a proposed route actually removes the hard information.

| ID | Direction | Strongest precise role | Established result or current state | Limitation | Project use | Sources |
|---|---|---|---|---|---|---|
| `E01` | NP-completeness baseline | Rules out a known polynomial algorithm unless \(P=NP\) | Positive-integer Subset Sum is NP-complete and weakly NP-complete | Does not identify which representation or step is hard | Mandatory starting point | `[R01]` |
| `E02` | SETH-based target-range lower bounds | Tests whether pseudopolynomial dependence on \(T\) can be reduced | No \(T^{1-\varepsilon}2^{o(n)}\)-time algorithm under SETH | Conditional; does not prove \(P\ne NP\) | Rejects naive sublinear-in-\(T\) universal claims | `[R28]` |
| `E03` | Direct-OR Subset Sum lower bounds | Controls batching, composition, and many-instance speedups | Conditional near-linear lower bounds for OR-composition under SETH | Conditional and tied to the stated batching model | Audits divide-and-conquer and batching claims | `[R28]` |
| `E04` | Worst-case exponential-time frontier | Measures progress against meet in the middle | Best worst-case time is \(2^{n/2}/\operatorname{poly}(n)\); a constant improvement in the exponent remains open | Failure to beat \(1/2\) is not a lower bound | Useful benchmark, not evidence for \(P\ne NP\) | `[R20]` |
| `E05` | Output-size barriers | Shows all-target algorithms cannot be faster than writing their output | \(U_T\) can be \(\Theta(T)\) and can be exponential in \(L\) | Single-target decision might avoid full output | Separates all-target from one-target goals | `[R07]`, `[R08]` |
| `E06` | OBDD and branching-program lower bounds | Proves many context-independent ordered states are necessary | Exponential or parameterized lower bounds for explicit restricted Boolean models | Arithmetic algorithms need not compile into those models | Retained model-specific evidence | `[R29]`, `[R31]`, `[R38]` |
| `E07` | Tree and decomposable-circuit lower bounds | Broadens lower bounds beyond one variable order | DNNF and structured-model lower bounds are known under graph restrictions | No polynomial-overhead inclusion of all Subset Sum arithmetic operations | Candidate bridge target, currently inactive | `[R30]`, `[R31]` |
| `E08` | Circuit-simulation escape tests | Attack a proposed compact language by showing it evaluates CNF | Unrestricted intersection, general circuits, or bounded residue-range branching defeat several assignment-query barriers | Applies to the specified query slices and languages | Decisive closeout tool for `SS-ECB` | `[R38]` |
| `E09` | Representation-size vacuity | Prevents mistaking stored syntax for solved structure | Storing the original instance or an unevaluated Minkowski product is a linear-size exact representation | Says nothing about restricted normalized languages | Mandatory audit for every compression proposal | `[R38]` |
| `E10` | Complete computation-graph accounting | Counts branching, recursion, discarded intermediates, transition tables, and encoded constants | Polynomial depth or compact final output does not imply polynomial total work | Requires model-specific formalization | Non-negotiable project standard | `[R37]`, `[R38]` |
| `E11` | Communication and interface complexity | Split items into components and lower-bound information crossing an exact merge boundary | A promising general methodology; no project theorem currently transfers it to unrestricted Subset Sum algorithms | Lower bounds usually apply only to the chosen interface model | Possible future barrier route only with a natural subsumption theorem | `[R38]` |
| `E12` | Kernelization and parameterized compression | Reduce an instance to size polynomial in a separately specified parameter | Powerful framework for restricted parameters and preprocessing | The parameter must be explicit and meaningfully smaller than the original binary input; an unrestricted instance already has polynomial size in itself | Use for positive subclasses, not as an unqualified universal claim | `[R16]`, `[R32]` |
| `E13` | Canonical reduction-generated audits | Run every proposed state representation on no-carry SAT-to-Subset-Sum instances | Detects preservation of assignment and clause compatibility | Failure on one model is not a lower bound against all algorithms | Successfully closed the structural-compression route | `[R37]` |
| `E14` | Randomization classification | Distinguish Monte Carlo, Las Vegas, RP, BPP, ZPP, and deterministic consequences | Randomized algorithms for an NP-complete problem do not automatically imply classical \(P=NP\) | Requires precise error and derandomization accounting | Mandatory when hashing or random primes appear | `[R05]`, `[R07]` |
| `E15` | Quantum-model separation | Prevents quantum speedups from being misreported as classical polynomial algorithms | Quantum Subset Sum algorithms improve exponential search exponents | Even polynomial quantum time would establish membership in BQP, not automatically \(P=NP\) | Track separately | `[R27]` |

---

## F. Relaxed, heuristic, and alternative-computation directions

These mechanisms are relevant because they demonstrate successful compression or search in a weaker setting. They are not direct classical exact routes without an additional exactification theorem.

| ID | Direction | What succeeds | Why it matters | Why it does not solve exact general Subset Sum | Sources |
|---|---|---|---|---|---|
| `F01` | FPTAS trimming and rounding | Keeps a polynomial-size representative list and returns a near-optimal sum | Demonstrates that lossy state compression is algorithmically powerful | Rounding can change exact equality | `[R33]` |
| `F02` | Near-linear approximation schemes | Partition and weak Subset Sum approximation can be achieved near-linearly in \(n+1/\varepsilon\) | Shows the approximate frontier is far ahead of exact binary-input decision | Exactification may require exponentially small \(\varepsilon\) | `[R34]` |
| `F03` | Greedy selection | Produces fast feasible or approximate solutions on ordered instances | Identifies dominance and residual rules that may become exact under promises | Local choices are not correct on arbitrary instances | `[R45]` |
| `F04` | Heuristic representation and sampling | Solves random cryptographic instances with substantially improved heuristic exponents | Reveals distributional collision structure | Analysis is not a worst-case exact guarantee | `[R26]` |
| `F05` | Quantum annealing and QUBO formulations | Maps Subset Sum to hardware-supported binary optimization | Useful experimental solver route | No imported worst-case polynomial guarantee; this is not the classical Turing model | No complexity claim imported |
| `F06` | Parallel, SIMD, and GPU bitset methods | Greatly accelerate DP and enumeration in wall-clock time | Important for experiments and counterexample searches | Polynomial hardware parallelism does not remove pseudopolynomial or exponential total work | `[R41]` |
| `F07` | Learned or adaptive branching heuristics | Choose promising branches, decompositions, or modulus schedules from instance features | Can improve solver performance and discover structure | Correctness still requires complete fallback search; learned success has no universal bound | No complexity claim |

---

## Cross-cutting conclusions

### 1. The current general frontiers are two-dimensional

For unrestricted exact Subset Sum, the best known methods are governed by either:

- the numerical range, now reaching deterministic \(\widetilde O(T)\) pseudopolynomial time; or
- the item count, with worst-case time just below \(2^{n/2}\) by a polynomial factor.

Neither dependence is polynomial in the total binary length on all instances.

### 2. The table contains no untested universal route

Every apparent compact object must answer four separate questions:

1. Can it be constructed in polynomial time?
2. Is its total encoded size polynomial, including all intermediate objects?
3. Can exact target membership be answered in polynomial time?
4. Does it preserve one common witness across components, moduli, branches, or residues?

Generating functions, Minkowski DAGs, modular fingerprints, and succinct transition programs each fail at least one of these questions under their unrestricted form.

### 3. The strongest positive next-route candidates are restricted classes

The most mathematically mature candidates for a new positive route are:

1. bounded doubling or efficiently constructible Freiman-type structure;
2. dense additive-combinatorial regimes with explicit parameter inequalities;
3. small maximum item or grouped values with succinct multiplicities;
4. a new decomposition-width parameter with a proved global state bound.

These routes can produce genuine theorems without implying a universal algorithm.

### 4. Broad exact-state compression has already been investigated

The project has closed:

- structural compression as a universal algorithmic strategy; and
- exact-state compression barriers as a broad model-lower-bound strategy.

A row involving intervals, progressions, residues, decision diagrams, or arithmetic proof graphs is not a new route unless it supplies a materially new exact composition theorem, global polynomial bound, or model bridge satisfying the recorded reopening conditions.

## Route-selection summary

| Candidate next programme | Mathematical upside | Main risk | Decisive first test | Recommendation |
|---|---|---|---|---|
| Small-doubling tractable subclass | Builds on a current constructive additive-combinatorics theorem | May remain only XP rather than FPT and cover a narrow family | Reproduce the exact parameter dependence and test canonical reductions for doubling growth | Strongest positive Subset Sum option |
| Dense-regime structural algorithm | Mature upper/lower-bound dichotomy and explicit inequalities | May mostly repackage known results | Identify a genuinely uncovered dense parameter regime | Secondary positive option |
| Small-item or succinct-multiplicity route | Clean exact algorithms and concise encodings of repeated values | Numeric parameters may merely restate pseudopolynomiality | Find a structural parameter not equivalent to bounded magnitude | Good restricted-class option |
| Communication/interface barrier | Could formalize cross-component compatibility directly | Easy to choose an artificially weak model | Define a natural model containing all retained operations before seeking a lower bound | High-risk barrier option |
| Short-certificate complexity | Connects exact arithmetic to proof and nondeterminism complexity | May move away from algorithm construction without resolving a central gap | Formalize the exact certificate model and imported lower-bound assumptions | Independent research option |
| Different NP-complete investigation | Avoids repeating the same additive compatibility obstruction | Loses continuity with retained Subset Sum lemmas | Choose a problem with explicit logical rather than numerical state | Recommended if no positive subclass is selected |

## Final status

This landscape is an orientation and decision artifact. It registers no new investigation-level mathematical claim. External results retain their source status; project results retain the statuses recorded in the authoritative claim ledgers.
