# P versus NP Problem-Testbed Landscape

**Classification:** Cross-investigation problem map and route-selection matrix  
**Cutoff:** 2026-07-16  
**Review:** `CHECKED` by source, classification, implication, and canonical-identifier audit  
**Scope:** Representative NP-complete decision problems, tractable controls, promise problems, total-search classes, and strategically relevant non-NP-complete objects

## Purpose and completeness boundary

This document organizes concrete problems by the kind of obstruction they expose. It replaces a single absolute ranking with rankings tied to research objective.

It is complete at the level of major natural obstruction families. It does not list every NP-complete problem, every restriction, or every complete problem for every class.

All source identifiers resolve through the [canonical source map](top-level-landscape-sources.md). Rankings are project strategy rankings, not claims of literature consensus.

## Selection criteria

A strong testbed should have transparent encoding, robust hardness, nearby tractable cases, reduction centrality, high audit value, a close fit to the proposed mechanism, and clear worst-case or promise quantifiers.

## A. Exact local constraint systems

| ID | Problem | Native form | Why attractive | Hidden obstruction | Controls | Project role | Sources |
|---|---|---|---|---|---|---|---|
| `L01` | Positive 1-in-3 SAT | Exactly one variable is true in each positive triple | One relation, no negations, no large numbers | Shared variables couple trivial local choices globally | XOR-SAT, acyclic CSP, bounded width | Leading positive candidate | `[P03]`, `[P06]`, `[P07]` |
| `L02` | 1-in-3 SAT with literals | Exactly one of three literals is true | Canonical exact-cardinality SAT form | Polarity adds compatibility constraints | Positive 1-in-3 SAT, XOR-SAT | Logical control | `[P03]`, `[P07]` |
| `L03` | Positive NAE-3SAT | Every positive triple contains both truth values | Symmetric hypergraph-colouring form | Hyperedges create global colour incompatibility | Graph 2-colouring, bounded width | Secondary CSP testbed | `[P03]`, `[P08]` |
| `L04` | 3-SAT | Every clause has at least one true literal | Canonical reduction hub | Negation, slack, and gadgets obscure structure | 2-SAT, Horn-SAT, affine SAT | Adversarial standard | `[P01]`, `[P02]`, `[P03]`, `[P27]` |
| `L05` | Finite-domain CSP | Variables satisfy fixed finite relations | Unified algebraic framework | A dichotomy classifies templates, not every structural restriction | Tractable polymorphisms, bounded width | Classification foundation | `[P03]`, `[P04]`, `[P05]` |
| `L06` | Label Cover | Projection constraints on labelled edges | Canonical PCP endpoint | Promise gaps and alphabet growth target approximation | Exact CSP, bounded-gap variants | Approximation infrastructure | `[P28]` |
| `L07` | Unique-SAT | Promise of at most one satisfying assignment | Isolates witness multiplicity | Isolation is randomized in general | SAT, restricted deterministic isolation | Promise control | `[P26]` |

Positive 1-in-3 SAT has the exact-incidence form `A x = 1` over Boolean vectors, with three ones per constraint row. This is a project organizing relation, not an automatic theorem transfer to other incidence problems.

## B. Exact selection and incidence systems

| ID | Problem | Native form | Why attractive | Hidden obstruction | Controls | Project role | Sources |
|---|---|---|---|---|---|---|---|
| `I01` | Exact Cover by 3-Sets | Select 3-sets covering each element exactly once | Pure exactness without numerical magnitude | Sets collide through shared elements | Acyclic incidence, perfect matching | Column-sparse control | `[P02]`, `[P42]` |
| `I02` | 3-Dimensional Matching | Select disjoint tripartite triples | Structured exact cover | Local disjointness causes global dead ends | Bipartite perfect matching | Tripartite control | `[P02]`, `[P41]`, `[P42]` |
| `I03` | Exact Hitting Set | Select elements meeting each set exactly once | Incidence-side duality | One choice affects many constraints | Laminar and bounded-width systems | Interface testbed | `[P42]` |
| `I04` | Set Packing | Select many pairwise disjoint sets | Direct conflict semantics | Pairwise compatibility does not ensure global size | Matching, bounded rank | Parameterized testbed | `[P02]`, `[P25]` |
| `I05` | Set Cover | Cover the universe with few sets | Canonical covering problem | Overlap plus global cardinality | Laminar and bounded-frequency cases | Approximation testbed | `[P02]`, `[P28]`, `[P42]` |
| `I06` | Perfect Matching | Select disjoint edges covering all vertices | Polynomial exact selection | Rank two does not extend to rank three | — | Mandatory tractable control | `[P41]` |

## C. Pairwise graph constraints

| ID | Problem | Native form | Why attractive | Hidden obstruction | Controls | Project role | Sources |
|---|---|---|---|---|---|---|---|
| `G01` | 3-Coloring | Adjacent vertices receive different colours | Only binary local constraints | Cycle consistency and colour permutations propagate globally | 2-Coloring, bounded treewidth | Best graph-CSP candidate | `[P05]`, `[P09]` |
| `G02` | Independent Set | Select `k` vertices with no internal edge | One local forbidden pattern | Early choices block the global target | Bounded treewidth, perfect graphs | Branching and kernelization | `[P02]`, `[P25]` |
| `G03` | Clique | Select `k` mutually adjacent vertices | Direct all-pairs compatibility | Dense global consistency | Bounded degeneracy, special classes | Monotone and communication testbed | `[P02]`, `[P13]`, `[P20]` |
| `G04` | Vertex Cover | Select `k` vertices meeting every edge | Simple local coverage | Overlap under a global budget | Parameterized regimes | Compression control | `[P02]`, `[P25]` |
| `G05` | Dominating Set | Select vertices covering all closed neighbourhoods | Local coverage language | Overlapping neighbourhoods interact globally | Planar, bounded-degree, bounded-width cases | Parameterized testbed | `[P02]`, `[P25]` |
| `G06` | Max Cut | Partition vertices to cross at least `K` edges | Clean quadratic formulation | Edge preferences conflict globally | Bipartite graphs, SDP relaxation | Optimisation control | `[P02]`, `[P33]` |
| `G07` | Fixed-target graph homomorphism | Map an input graph to fixed `H` | Unifies colouring and binary CSPs | Non-bipartite targets retain hard cycle compatibility | Bipartite targets | Dichotomy control | `[P09]` |

## D. Global graph and network structures

| ID | Problem | Native form | Why attractive | Hidden obstruction | Controls | Project role | Sources |
|---|---|---|---|---|---|---|---|
| `N01` | Hamiltonian Cycle | One cycle visits every vertex | No weights and minimal syntax | Partial paths must avoid subtours and remain connectable | Bounded treewidth | Connectivity-interface testbed | `[P02]`, `[P42]` |
| `N02` | Hamiltonian Path | One path visits every vertex | Slightly simpler endpoint structure | Same global connectivity obstruction | DAG and bounded-width variants | Connectivity control | `[P02]`, `[P42]` |
| `N03` | Travelling Salesperson | Tour under a weight bound | Combines connectivity, weights, and polyhedra | Numerical encoding and subtours coexist | Metric and bounded-width cases | Polyhedral testbed | `[P02]`, `[P42]`, `[P50]` |
| `N04` | Steiner Tree | Connect terminals within a budget | Exposes path sharing | Locally short paths can be globally redundant | Fixed terminals, bounded width | Network-decomposition testbed | `[P42]`, `[P25]` |
| `N05` | Feedback Vertex Set | Delete few vertices to remove all cycles | Global cyclic obstruction with local deletion | Cycles overlap | Parameterized regimes | Iterative-compression testbed | `[P25]`, `[P42]` |

## E. Arithmetic, algebraic, and optimisation systems

| ID | Problem | Native form | Why attractive | Hidden obstruction | Controls | Project role | Sources |
|---|---|---|---|---|---|---|---|
| `A01` | Subset Sum | Choose numbers summing to a target | One weighted Boolean equation | Binary weights encode logical compatibility | Unary weights, small doubling | Completed arithmetic benchmark | `[P02]`, `[P31]` |
| `A02` | Partition | Divide numbers into equal-sum parts | Symmetric numerical form | Pseudopolynomial tractability hides binary magnitude | Unary inputs | Numeric boundary control | `[P02]`, `[P42]` |
| `A03` | 0-1 Knapsack | Meet value and weight thresholds | Links exact and optimisation formulations | Multiple numerical dimensions | Bounded weights, approximation | Regime testbed | `[P02]`, `[P42]` |
| `A04` | 0-1 Integer Feasibility | Boolean linear inequalities | Universal linear formulation | Coefficients and constraints simulate Boolean computation | Totally unimodular and fixed-dimensional cases | Umbrella control | `[P02]`, `[P32]` |
| `A05` | Exact integer linear system | Boolean or bounded integer equality system | Bridges CSP, parity, and arithmetic | Integer equality is stronger than modular equality | Finite-field systems, total unimodularity | Bridge testbed | `[P03]`, `[P04]` |
| `A06` | Fixed-dimensional integer programming | Integer feasibility with fixed dimension | Shows dimension can control complexity | Dimension grows in hard encodings | Fixed dimension | Tractable geometric control | `[P32]` |
| `A07` | Quadratic Boolean optimisation | Optimise a quadratic form over Boolean variables | Unifies Max Cut and QUBO | Pairwise terms preserve arbitrary compatibility | Submodular and special-sign cases | Relaxation control | `[P33]` |

## F. Scheduling, sequencing, and allocation

| ID | Problem | Native form | Hidden obstruction | Project role | Sources |
|---|---|---|---|---|---|
| `S01` | Job-shop scheduling | Machine and precedence constraints under a deadline | Resource choices interact through long precedence cycles | Constraint-propagation testbed | `[P42]` |
| `S02` | Bin Packing | Assign items to capacity-limited bins | Assignment symmetry and global capacity | Approximation and configuration testbed | `[P42]` |
| `S03` | Multiprocessor scheduling | Assign jobs under a makespan bound | Local balance can create global imbalance | Numeric allocation control | `[P42]` |

## G. Universal computation and logical certification

| ID | Object | Native form | Strategic value | Caution | Sources |
|---|---|---|---|---|---|
| `U01` | Circuit-SAT | Assign inputs so a circuit outputs one | Closest finite representation of arbitrary verification | Generality leaves little exploitable structure | `[P01]`, `[P10]`, `[P11]` |
| `U02` | CNF-SAT / 3-SAT | Satisfy a conjunction of clauses | Canonical normal form and fine-grained benchmark | Normalization introduces gadgets | `[P01]`, `[P02]`, `[P27]` |
| `U03` | UNSAT | Prove no assignment satisfies a formula | No-instance certification | coNP-complete, not an NP witness problem | `[P18]`, `[P19]` |
| `U04` | TAUT | Prove every assignment satisfies a formula | Canonical proof-system range | Strong proof lower bounds remain open | `[P18]`, `[P19]` |
| `U05` | `#SAT` | Count satisfying assignments | Strengthens existence to counting | Different class objective | `[P29]`, `[P54]` |
| `U06` | QBF / TQBF | Evaluate alternating quantifiers | PSPACE boundary control | Strictly broader target than NP | `[P47]` |
| `U07` | Circuit Value | Evaluate a fixed-input circuit | P-complete sequential-computation control | Evaluation is not satisfiability | `[P48]` |

## H. Strategic objects outside ordinary NP-complete decision search

| ID | Object | Status and value | Main caution | Sources |
|---|---|---|---|---|
| `M01` | MCSP | In NP; central to meta-complexity and magnification | Standard NP-completeness unresolved | `[P22]`, `[P24]` |
| `M02` | Polynomial Identity Testing | Randomized polynomial time; derandomization tied to lower bounds | Not an NP-complete testbed | `[P35]`, `[P44]` |
| `M03` | Permanent polynomial | `#P`-complete and central in algebraic complexity | Boolean transfer requires another theorem | `[P16]`, `[P29]`, `[P35]` |
| `M04` | Graph Isomorphism | Quasipolynomial time; intermediate-status control | Not known NP-complete | `[P22]`, `[P43]` |
| `M05` | Integer factoring | In NP and coNP; quantum polynomial time | Not known NP-complete | `[P30]`, `[P45]` |
| `M06` | TFNP / PPAD / PLS | Guaranteed-solution search classes | Totality changes the quantifiers | `[P46]`, `[P58]` |
| `M07` | Sparse languages and compression | Connects density and preprocessing to collapses | Requires exact reduction assumptions | `[P39]`, `[P40]` |
| `M08` | Exact lattice problems | Geometric hardness with formally verified reductions in selected norms | Approximation and norm choices materially change status | `[P49]` |

## I. Mandatory controls

| Hard testbed | Control | Difference to isolate |
|---|---|---|
| Positive 1-in-3 SAT | XOR-SAT | Exact cardinality versus parity |
| Positive 1-in-3 SAT | Acyclic or bounded-width CSP | Global cyclic compatibility |
| 3-SAT | 2-SAT, Horn-SAT | Clause width and closure structure |
| 3-Coloring | 2-Coloring | Three-way cycle compatibility |
| X3C / 3DM | Perfect Matching | Rank three versus rank two |
| Hamiltonian Cycle | Bounded-treewidth Hamiltonicity | Unbounded separator interface |
| Subset Sum | Unary or polynomial target | Binary numerical magnitude |
| 0-1 ILP | Totally unimodular systems | Integrality of the relaxation |
| Circuit-SAT | Restricted circuit classes | Source of nontrivial SAT algorithms |
| SAT | Unique-SAT | Witness multiplicity and isolation |
| NP search | TFNP | Optional existence versus guaranteed totality |
| NP | QBF / PSPACE | Existential versus alternating computation |

## J. Project rankings by objective

### Positive universal-algorithm testbeds

| Rank | Candidate | Decisive first audit |
|---|---|---|
| **1** | **Positive 1-in-3 SAT** | Compare exact-one propagation with XOR and reduction-generated cyclic incidence graphs |
| **2** | **X3C** | Test column sparsity and shared-element collisions |
| **3** | **Positive NAE-3SAT** | Separate complement symmetry from exact-cardinality hardness |
| **4** | **3-Coloring** | Test whether bounded separators or bipartiteness explain success |
| **5** | **3-SAT** | Strip away gadget syntax |
| **6** | **3-Dimensional Matching** | Test whether tripartiteness genuinely helps |
| **7** | **Hamiltonian Cycle** | Bound connectivity information across separators |
| **8** | **Circuit-SAT** | Use only for mechanisms acting directly on circuit structure |

### Lower-bound and separation testbeds

| Rank | Candidate or object | Decisive theorem required |
|---|---|---|
| **1** | **Circuit-SAT and restricted circuit SAT** | Nontrivial SAT/counting algorithm or direct class lower bound |
| **2** | **UNSAT / TAUT** | Lower bound for a proof system with an explicit class consequence |
| **3** | **3-SAT / CNF-SAT** | Model-specific lower bound plus a justified transfer theorem |
| **4** | **Finite-domain CSP** | New instance-structural theorem, not another template dichotomy |
| **5** | **Clique / Independent Set** | Escape monotone or interface restrictions |
| **6** | **MCSP and magnification targets** | Exact magnification threshold |
| **7** | **Polyhedral and semialgebraic formulations** | Show the model captures the proposed algorithm or proof system |

## K. Recommended next cluster

The strongest current positive candidate is **exact-incidence constraint systems**, centred on Positive 1-in-3 SAT and tested against X3C, 3-Dimensional Matching, XOR-SAT, perfect matching, bounded-width CSPs, and canonical 3-SAT reductions.

The first route must state a concrete propagation, decomposition, width, or composition mechanism; prove correctness; bound the complete global state; and survive all three incidence orientations.

The strongest lower-bound sibling remains Circuit-SAT and restricted-circuit satisfiability. Neither candidate is active.

## Final status

This is an orientation artifact. It registers no new mathematical claim and changes no existing investigation state.
