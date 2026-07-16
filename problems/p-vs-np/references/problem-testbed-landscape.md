# P versus NP Problem-Testbed Landscape

**Classification:** Cross-investigation problem map and route-selection matrix  
**Cutoff:** 2026-07-16  
**Review:** `CHECKED` by second-pass source, classification, and implication audit  
**Scope:** Representative NP-complete decision problems, tractable controls, promise problems, total-search classes, and strategically relevant non-NP-complete objects

## Purpose and completeness boundary

This document organizes concrete problems by the kind of obstruction they expose. It replaces a single absolute ranking with rankings tied to research objective.

It is intended to be complete at the level of major natural obstruction families. It does not list every NP-complete problem, every restriction, or every complete problem for every complexity class.

Source identifiers refer to:

- [top-level-landscape-sources.md](top-level-landscape-sources.md);
- [top-level-landscape-specialist-sources.md](top-level-landscape-specialist-sources.md);
- [top-level-landscape-second-pass-sources.md](top-level-landscape-second-pass-sources.md).

## Selection criteria

A strong testbed should score well on several of the following:

1. **native simplicity:** few constraint types, no unnecessary gadgets, and transparent encoding;
2. **hardness robustness:** NP-completeness survives meaningful syntactic or structural restrictions;
3. **tractable neighbours:** nearby polynomial cases reveal which feature may matter;
4. **reduction centrality:** canonical reductions connect it to arbitrary verification;
5. **audit value:** it exposes whether a proposed mechanism preserves hidden compatibility;
6. **model fit:** its native structure matches the proposed algorithmic or lower-bound mechanism;
7. **quantifier clarity:** worst-case, average-case, parameterized, promise, counting, and approximation claims remain separable;
8. **consequence clarity:** success on the object has an explicitly stated implication for the target class separation.

No problem is best for every objective. Rankings in this document are **project strategy rankings**, not claims of literature consensus.

## A. Exact local constraint systems

| ID | Problem | Native form | Why attractive | Hidden obstruction | Tractable or easier controls | Best project role | Sources |
|---|---|---|---|---|---|---|---|
| `L01` | Positive 1-in-3 SAT | Each positive 3-variable constraint requires exactly one true variable | One relation, no negations, no large numbers; equivalent to a sparse Boolean exact-equation system | Shared variables couple locally trivial exact-one choices globally | XOR-SAT, acyclic incidence graphs, bounded treewidth, and precisely specified occurrence restrictions | Strongest current project candidate for a positive testbed | `[P03]`, `[P06]`, `[P07]` |
| `L02` | 1-in-3 SAT with literals | Exactly one of three literals is true | Canonical exact-cardinality SAT variant with exact algorithms and reduction infrastructure | Negations add polarity compatibility but do not remove the shared-variable obstruction | Positive 1-in-3 SAT and XOR-SAT | Secondary logical control | `[P03]`, `[P07]` |
| `L03` | Positive NAE-3SAT | Every positive triple contains both truth values | Symmetric under global complementation; equivalent to 2-colouring a 3-uniform hypergraph | Hyperedges create globally incompatible colour choices | Graph 2-colouring, acyclic hypergraphs, bounded-width variants | Strong secondary CSP testbed | `[P03]`, `[P08]` |
| `L04` | 3-SAT | Every 3-literal clause contains at least one true literal | Canonical NP-complete reduction hub; extensive exact-algorithm, ETH, proof-complexity, and solver literature | Negations, clause slack, and gadget syntax can obscure the core compatibility mechanism | 2-SAT, Horn-SAT, dual-Horn-SAT, affine SAT | Canonical adversarial and reduction standard | `[P01]`, `[P02]`, `[P03]`, `[P27]` |
| `L05` | General finite-domain CSP | Variables take values in a finite domain under fixed relations | Unified language for SAT, graph homomorphism, colouring, and exact constraints; complete algebraic dichotomy | Too broad to be one concrete investigation; fixed-template classification does not classify every structural restriction or succinct representation | Languages with tractable polymorphisms; bounded-width incidence structures | Foundational classification framework | `[P03]`, `[P04]`, `[P05]` |
| `L06` | Label Cover / projection CSP | Edge constraints project labels from one endpoint to another | Canonical endpoint for PCP and hardness-of-approximation reductions | Promise gaps and alphabet growth target approximation rather than a clean exact positive algorithm | Exact CSP and bounded-gap variants | Approximation and reduction infrastructure | `[P28]` |
| `L07` | Unique-SAT / promise unique satisfiability | Promise that at most one satisfying assignment exists | Isolates witness multiplicity and search-to-decision issues | Promise is not generally deterministic; Valiant–Vazirani isolation is randomized | SAT, deterministic isolation on restricted classes | Promise and reduction control, not an ordinary NP-complete testbed | `[P26]` |

### Exact-incidence equation

Positive 1-in-3 SAT can be written as

\[
Ax=\mathbf 1,
\qquad
x\in\{0,1\}^n,
\]

where every row of \(A\) contains exactly three ones.

This makes it the row-sparse member of an exact-incidence cluster that also contains Exact Cover by 3-Sets and 3-Dimensional Matching. The cluster is a project organizing device: it does not claim that every structural theorem transfers automatically among the three formulations.

## B. Exact selection and incidence systems

| ID | Problem | Native form | Why attractive | Hidden obstruction | Tractable or easier controls | Best project role | Sources |
|---|---|---|---|---|---|---|---|
| `I01` | Exact Cover by 3-Sets (X3C) | Select 3-element sets so each universe element is covered exactly once | Pure exactness with no negation, arithmetic magnitude, or objective function | Candidate sets collide through shared elements | Exact cover on acyclic incidence hypergraphs; bipartite perfect matching | Column-sparse control for Positive 1-in-3 SAT | `[P02]` |
| `I02` | 3-Dimensional Matching | Select disjoint triples from \(X\times Y\times Z\) covering the required vertices | Exact cover with a tripartite incidence promise | Local disjointness choices create global dead ends | Bipartite perfect matching | Strong structured exact-incidence control | `[P02]` |
| `I03` | Exact Hitting Set | Select elements meeting every set exactly once | Exchanges the selected side of the incidence relation | One selected element can satisfy or destroy many constraints | Laminar and bounded-width set systems | Duality and interface testbed | `[P02]` |
| `I04` | Set Packing | Select a prescribed number of pairwise disjoint sets | Direct conflict semantics; generalizes matching and Independent Set | Pairwise compatibility does not guarantee a globally large packing | Matching and bounded-rank or bounded-intersection systems | Branching and parameterized testbed | `[P02]`, `[P25]` |
| `I05` | Set Cover decision | Cover the universe using at most \(k\) sets | Canonical covering and approximation problem | Overlap and global cardinality create optimisation structure rather than exact equality | Laminar set cover, bounded-frequency cases | Approximation and kernelization testbed | `[P02]`, `[P28]` |
| `I06` | Perfect matching | Select disjoint edges covering every vertex | Polynomial-time exact selection with strong algebraic and combinatorial algorithms | Rank-two matching does not extend automatically to rank-three hypergraph matching | — | Mandatory tractable control for X3C and 3DM | `[P02]` |

### Incidence orientations

| Form | Boolean variables select | Uniformity condition |
|---|---|---|
| Positive 1-in-3 SAT | truth values attached to variable columns | every constraint row has three ones |
| X3C | 3-element sets | every selectable column has three ones |
| 3-Dimensional Matching | tripartite triples | every selectable column has one one in each of three row parts |

A mechanism proposed for one member should be tested on all three forms. Success caused only by row sparsity, column sparsity, or tripartiteness is a restricted theorem, not a universal exact-incidence method.

## C. Pairwise graph constraints

| ID | Problem | Native form | Why attractive | Hidden obstruction | Tractable or easier controls | Best project role | Sources |
|---|---|---|---|---|---|---|---|
| `G01` | 3-Coloring | Assign one of three colours so adjacent vertices differ | Only binary local constraints; cycles, separators, and treewidth are visible | Colour permutations and cycle consistency propagate globally | 2-Coloring, bounded treewidth, fixed bipartite homomorphisms | Best graph-CSP positive candidate | `[P05]`, `[P09]` |
| `G02` | Independent Set | Select \(k\) vertices with no selected edge | One local forbidden pattern and a global cardinality target | Early selections can block the global target without local contradiction | Bounded-treewidth and selected perfect-graph classes; Vertex Cover duality | Parameterized, branching, and kernelization testbed | `[P02]`, `[P25]` |
| `G03` | Clique | Select \(k\) pairwise adjacent vertices | Direct all-pairs compatibility and extensive lower-bound literature | Requires dense global consistency among every selected pair | Bounded degeneracy or special graph classes | Communication, monotone-circuit, and parameterized lower-bound testbed | `[P02]`, `[P13]`, `[P20]` |
| `G04` | Vertex Cover | Select \(k\) vertices meeting every edge | Simple local coverage and one of the cleanest kernelization examples | Coverage overlaps under a global cardinality limit | Bounded parameters and special graph classes | Parameterized and preprocessing control | `[P02]`, `[P25]` |
| `G05` | Dominating Set | Select \(k\) vertices whose closed neighbourhoods cover all vertices | Local coverage phrasing on a graph | Neighbourhood overlaps and distance interactions are globally coupled | Bounded-degree, planar, or bounded-treewidth variants | Parameterized and approximation testbed | `[P02]`, `[P25]` |
| `G06` | Max Cut decision | Partition vertices so at least \(K\) edges cross | Clean \(\{\pm1\}\) quadratic formulation and strong relaxation theory | Edge preferences cannot generally be satisfied simultaneously | Bipartite recognition and selected graph classes | Optimisation, algebraic, and semidefinite-relaxation testbed | `[P02]`, `[P33]` |
| `G07` | Graph homomorphism to fixed \(H\) | Map vertices of an input graph to \(H\) preserving edges | Unifies colouring and binary CSPs; has a clean fixed-template dichotomy | Non-bipartite targets retain NP-complete cycle compatibility | Bipartite target graphs | Structural-classification foundation | `[P09]` |

## D. Global graph and network structures

| ID | Problem | Native form | Why attractive | Hidden obstruction | Tractable or easier controls | Best project role | Sources |
|---|---|---|---|---|---|---|---|
| `N01` | Hamiltonian Cycle | Find one cycle visiting every vertex exactly once | No weights and minimal local syntax; exposes global connectivity directly | Partial paths must avoid premature cycles while remaining globally connectable | Bounded treewidth, tournaments, selected planar classes | Separator and connectivity-state testbed | `[P02]` |
| `N02` | Hamiltonian Path | Find a spanning path | Slightly simpler endpoint structure than a cycle | Same global connectivity and subtour obstruction | Directed acyclic or bounded-width variants | Connectivity control | `[P02]` |
| `N03` | Travelling Salesperson decision | Find a tour of total weight at most \(B\) | Combines Hamiltonicity, binary weights, polyhedral structure, and approximation | Global connectivity and numerical encoding coexist | Metric approximation, bounded-treewidth graphs | Optimisation and polyhedral testbed | `[P02]`, `[P38]` |
| `N04` | Steiner Tree decision | Connect specified terminals using a bounded-size or bounded-cost subgraph | Exposes sharing and network design | Locally short paths can be globally incompatible or redundantly connected | Fixed terminal count and bounded treewidth | Network-decomposition testbed | `[P02]`, `[P25]` |
| `N05` | Feedback Vertex Set | Remove at most \(k\) vertices to eliminate all cycles | Global cyclic obstruction with a local deletion action | Cycles overlap in complicated ways | Bounded treewidth and parameterized regimes | Kernelization and iterative-compression testbed | `[P25]` |

## E. Arithmetic, algebraic, and optimisation systems

| ID | Problem | Native form | Why attractive | Hidden obstruction | Tractable or easier controls | Best project role | Sources |
|---|---|---|---|---|---|---|---|
| `A01` | Subset Sum | Choose numbers summing exactly to a target | One weighted Boolean equation; rich exact-algorithm and additive-combinatorics literature | Binary weights encode logical compatibility and exponential numerical range | Unary weights, small items, small doubling, superincreasing instances | Completed arithmetic benchmark and adversarial control | `[P02]`, `[P31]` |
| `A02` | Partition | Divide numbers into two equal-sum parts | Symmetric numerical formulation and weak NP-completeness | Pseudopolynomial tractability can obscure the binary-encoding obstruction | Unary and bounded-range inputs | Numeric boundary control | `[P02]` |
| `A03` | 0-1 Knapsack decision | Meet value and weight thresholds with Boolean selections | Connects exact feasibility, optimisation, and pseudopolynomial algorithms | Multiple numerical dimensions and objective thresholds obscure one mechanism | Bounded weights and approximation schemes | Algorithmic-regime testbed | `[P02]` |
| `A04` | 0-1 Integer Feasibility | Find \(x\in\{0,1\}^n\) satisfying linear inequalities | Universal linear-arithmetic formulation containing many testbeds | Coefficients and many inequalities simulate arbitrary Boolean computation | Totally unimodular matrices, bounded dimension, fixed constraints | Umbrella formulation; too broad for a first positive route | `[P02]`, `[P32]` |
| `A05` | Exact integer linear system | Solve \(Ax=b\) over Boolean or bounded integer variables | Makes incidence, parity, and arithmetic relaxations directly comparable | Integer equality is much stronger than modular equality and can encode exact cover | Linear systems over finite fields and totally unimodular cases | Bridge between CSP and arithmetic investigations | `[P03]`, `[P04]` |
| `A06` | Integer programming in fixed dimension | Optimise or decide feasibility with dimension fixed | Polynomial algorithms show dimension can control integer complexity | Dimension is unbounded in general NP-complete encodings | Fixed dimension | Tractable geometric control | `[P32]` |
| `A07` | Quadratic 0-1 optimisation | Optimise a quadratic form over Boolean variables | Unifies Max Cut, QUBO, and many physical encodings | General quadratic interactions preserve arbitrary pairwise compatibility | Submodular or special-sign cases | Algebraic and relaxation control | `[P33]` |

## F. Scheduling, sequencing, and allocation

| ID | Problem | Native form | Why attractive | Hidden obstruction | Easier controls | Best project role | Sources |
|---|---|---|---|---|---|---|---|
| `S01` | Job-shop scheduling decision | Schedule operations with machine and precedence constraints within a deadline | Concrete temporal constraints and resource contention | Local machine choices interact through long precedence cycles | Single-machine and selected fixed-machine regimes | Constraint-propagation and optimisation testbed | `[P02]` |
| `S02` | Bin Packing decision | Pack items into a bounded number of capacity-limited bins | Simple capacity constraints and strong approximation theory | Assignment symmetry and global capacity coordination | Fixed bin count, bounded item sizes, approximation schemes | Approximation and configuration-space testbed | `[P02]` |
| `S03` | Multiprocessor scheduling / Partition scheduling | Assign jobs to machines under a makespan bound | Direct relation to Partition and load balancing | Many locally balanced allocations can create global imbalance | Fixed number of machines and approximation schemes | Numeric allocation control | `[P02]` |

## G. Universal computation and logical certification

| ID | Problem or object | Native form | Why attractive | Hidden obstruction | Best project role | Sources |
|---|---|---|---|---|---|---|
| `U01` | Circuit-SAT | Assign circuit inputs so the output is one | Closest finite representation of arbitrary polynomial-time verification; gate structure is explicit | So general that little exploitable structure remains; unrestricted lower bounds are the main problem itself | Strongest lower-bound sibling and algorithms-to-lower-bounds testbed | `[P01]`, `[P10]`, `[P11]` |
| `U02` | CNF-SAT / 3-SAT | Satisfy a conjunction of clauses | Standard normal form and central fine-grained benchmark | Clause normalization may introduce gadgets and hide circuit structure | Canonical reduction and adversarial standard | `[P01]`, `[P02]`, `[P27]` |
| `U03` | UNSAT | Decide that a Boolean formula has no satisfying assignment | Directly exposes no-instance certification and proof search | coNP-complete rather than an NP-complete positive witness problem | Proof-complexity testbed | `[P18]`, `[P19]` |
| `U04` | TAUT | Decide that every assignment satisfies a formula | Canonical propositional proof-system range | Strong proof-system lower bounds remain open | Proof-complexity testbed | `[P18]`, `[P19]` |
| `U05` | `#SAT` | Count satisfying assignments | Strengthens existence to exact witness counting | Counting is a different class objective; cancellation and representation issues appear | Counting-complexity and representation audit | `[P29]` |
| `U06` | QBF / TQBF | Evaluate alternating existential and universal quantifiers | Canonical PSPACE-complete control for alternation and game semantics | Strictly broader target than NP unless major classes collapse | Boundary control: detect accidental movement from NP to PSPACE | `[P39]` |

## H. Strategic objects outside ordinary NP-complete decision search

These are included because they support major P-versus-NP programmes, not because they are all known NP-complete under standard reductions.

| ID | Object | Current status | Strategic value | Main caution | Sources |
|---|---|---|---|---|---|
| `M01` | Minimum Circuit Size Problem (MCSP) | In NP; not known NP-complete under standard deterministic many-one reductions | Central to meta-complexity, pseudorandomness, cryptography, and hardness magnification | Its input is a full truth table and standard NP-completeness remains unresolved | `[P22]`, `[P24]` |
| `M02` | Polynomial Identity Testing | Randomized polynomial-time algorithms are known; deterministic polynomial time is open in important models | Flagship derandomization problem tied to arithmetic circuit lower bounds | Not known NP-complete and belongs to a different algebraic interface | `[P12]`, `[P17]`, `[P35]`, `[P48]` |
| `M03` | Permanent polynomial | `#P`-complete as a counting problem and central in arithmetic complexity | Canonical explicit polynomial for algebraic lower bounds and GCT | Arithmetic lower bounds do not automatically imply Boolean \(P\ne NP\) without a transfer theorem | `[P16]`, `[P29]`, `[P35]` |
| `M04` | Graph Isomorphism | In quasipolynomial time; not known NP-complete | Useful intermediate-complexity and meta-complexity control | NP-completeness would have unexpected hierarchy consequences under standard assumptions | `[P22]` |
| `M05` | Integer factoring | In NP and coNP; polynomial-time quantum algorithm known, classical polynomial time open | Clean average-case, cryptographic, and alternative-model control | Not known NP-complete and not representative of arbitrary NP verification | `[P30]` |
| `M06` | TFNP / PPAD / PLS problems | Total search: a solution is guaranteed to exist | Separates existence complexity from verification of optional witnesses | Totality prevents ordinary NP-completeness unless strong collapses occur | `[P47]` |
| `M07` | Sparse languages and instance compression | Small density or compressed output rather than a native search problem | Links sparse completeness and polynomial compression to class collapses | A sparse or compressed representation theorem requires exact reduction assumptions | `[P43]`, `[P44]` |

## I. Mandatory tractable and boundary controls

A new mechanism should be tested not only on hard problems but on nearby polynomial or differently classified cases to identify what it is actually using.

| Hard testbed | Control | Structural or class difference to isolate |
|---|---|---|
| Positive 1-in-3 SAT | XOR-SAT | exact integer cardinality versus parity |
| Positive 1-in-3 SAT | acyclic or bounded-treewidth CSP | global cyclic incidence compatibility |
| 3-SAT | 2-SAT | clause width and implication-graph structure |
| 3-SAT | Horn-SAT and dual-Horn-SAT | closure operations and one-sided implication structure |
| 3-Coloring | 2-Coloring | non-bipartite cycle and three-way colour compatibility |
| X3C / 3DM | bipartite perfect matching | hyperedge rank three versus edge rank two |
| Clique | selected perfect-graph classes | unrestricted pairwise compatibility versus structured graph classes |
| Hamiltonian Cycle | bounded-treewidth Hamiltonicity | unbounded separator interface |
| Subset Sum | unary or polynomially bounded target | binary numerical magnitude |
| 0-1 ILP | totally unimodular linear systems | integrality of the relaxation |
| Circuit-SAT | restricted circuit classes | exact source of nontrivial SAT algorithms and lower bounds |
| SAT | Unique-SAT promise | witness multiplicity and randomized isolation |
| NP search | TFNP | optional witness existence versus guaranteed totality |
| NP | QBF / PSPACE | existential verification versus alternating computation |

## J. Rankings by research objective

These are project rankings under the stated criteria, not external consensus rankings.

### J.1 Positive universal-algorithm testbeds

| Rank | Candidate | Why it ranks here | Decisive first audit |
|---|---|---|---|
| **1** | **Positive 1-in-3 SAT** | Minimal exact local relation; no negations or binary magnitudes; robust NP-completeness | Compare exact-one propagation with XOR relaxation and reduction-generated cyclic incidence graphs |
| **2** | **X3C** | Incidence-oriented exact-selection form with transparent combinatorics | Test whether a mechanism survives column sparsity and shared-element collisions |
| **3** | **Positive NAE-3SAT** | Symmetric hypergraph-colouring form with a clean local relation | Separate complement symmetry from exact-cardinality hardness |
| **4** | **3-Coloring** | Binary local constraints and mature width/homomorphism theory | Identify whether the mechanism depends on bounded separators or bipartiteness |
| **5** | **3-SAT** | Canonical and reduction-central | Strip away gadget syntax and test the mechanism on the exact source relation |
| **6** | **3-Dimensional Matching** | Strong structural promise inside exact cover | Determine whether tripartiteness genuinely reduces compatibility |
| **7** | **Hamiltonian Cycle** | Extremely clean statement without weights | Bound the connectivity information crossing every separator |
| **8** | **Circuit-SAT** | Universal computation object | Use only when the proposed mechanism acts directly on circuit structure |

### J.2 Lower-bound and separation testbeds

| Rank | Candidate or object | Why it ranks here | Decisive theorem required |
|---|---|---|---|
| **1** | **Circuit-SAT and restricted circuit SAT** | Direct relation to general computation and established algorithms-to-lower-bounds frameworks | Nontrivial SAT or counting algorithm for a sufficiently expressive circuit class, or a direct class lower bound |
| **2** | **UNSAT / TAUT** | Makes proof length and no-instance certification explicit | Superpolynomial lower bound for a proof system whose consequence is stated exactly |
| **3** | **3-SAT / CNF-SAT** | Central ETH, SETH, proof-complexity, and reduction benchmark | Model-specific lower bound plus a justified transfer to the target computational class |
| **4** | **Finite-domain CSP** | Complete algebraic classification of fixed templates and rich structural parameters | New instance-structural theorem, not another fixed-language dichotomy |
| **5** | **Clique / Independent Set** | Strong monotone, communication, branching, and parameterized lower-bound interfaces | Escape monotone or interface restrictions through a valid subsumption theorem |
| **6** | **MCSP and magnification targets** | Modest lower bounds may imply major separations | Prove the exact magnification threshold while avoiding localization and natural-proof barriers |
| **7** | **Polyhedral and semialgebraic formulations** | Expose extension complexity and proof-rank barriers | Prove the lower-bound model captures the proposed exact algorithm or proof system |

### J.3 Adversarial controls retained by the project

| Control | What it detects | Current project status |
|---|---|---|
| Subset Sum | Hidden logical compatibility encoded by binary arithmetic | Two universal routes closed; retained as reduction and compression audit target |
| Circuit-SAT | Whether a proposed language simply simulates general Boolean computation | Mandatory expressiveness audit |
| Canonical no-carry SAT-to-Subset-Sum | Whether arithmetic summaries preserve assignment and clause choices | Existing reusable reduction audit |
| XOR-SAT | Whether the proposed method merely exploits affine structure | Tractable algebraic control |
| 2-SAT | Whether local implication closure is sufficient | Tractable logical control |
| Perfect matching | Whether rank-two exact incidence is the actual tractable boundary | Tractable combinatorial control |
| Bounded-treewidth instances | Whether separator width, rather than the proposed universal mechanism, explains success | Structural control |
| Unique-SAT | Whether multiplicity is the real obstruction | Promise/randomization control |
| QBF | Whether a proposed formalism has silently gained alternation beyond NP | Complexity-boundary control |

## K. Recommended next investigation cluster

The strongest current project candidate for a positive investigation is:

# Exact-incidence constraint systems

Primary testbed:

\[
Ax=\mathbf 1,
\qquad
x\in\{0,1\}^n,
\]

with every row of \(A\) containing exactly three ones, equivalently Positive 1-in-3 SAT.

Paired hard controls:

- X3C;
- 3-Dimensional Matching;
- unrestricted 3-SAT reductions into the exact-one relation.

Paired tractable or boundary controls:

- affine equations over \(\mathbb F_2\);
- acyclic and bounded-treewidth incidence graphs;
- bipartite perfect matching;
- precisely cited bounded-occurrence or planar subclasses;
- Unique-SAT-style witness restrictions where applicable.

The first route must state a concrete mechanism before activation. Candidate questions include:

1. Is there an exact propagation closure stronger than local consistency but polynomially bounded globally?
2. Is there a natural incidence-width parameter whose complete state graph is polynomial and which strictly extends known bounded-treewidth cases?
3. Can row-sparse and column-sparse exact-incidence systems be related without exponential compatibility states?
4. Which cycles, hypergraph obstructions, or algebraic signatures are minimal obstacles to local exact-one propagation?
5. Does any proposed compression survive canonical reductions and all three incidence orientations?
6. Does the mechanism exploit exact cardinality, bounded width, bounded occurrence, planarity, uniqueness, or another hidden promise?

The strongest lower-bound sibling remains Circuit-SAT and restricted-circuit satisfiability.

Neither investigation is activated by this landscape.

## Final status

This document is an orientation and decision artifact. It registers no new mathematical claim and does not alter the status of any existing investigation.