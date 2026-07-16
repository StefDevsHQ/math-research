# P versus NP Problem-Testbed Landscape

**Classification:** Cross-investigation problem map and route-selection matrix  
**Cutoff:** 2026-07-16  
**Review:** `CHECKED` by source, classification, and implication audit  
**Scope:** Representative NP-complete decision problems, tractable controls, promise problems, total-search classes, and strategically relevant non-NP-complete objects

## Purpose and completeness boundary

This is the canonical map of concrete problems by the obstruction they expose. It replaces a single absolute ranking with rankings tied to research objective.

It is complete at the level of major natural obstruction families, not every complete problem, restriction, or parameter. All source identifiers refer to the [canonical source map](top-level-landscape-sources.md).

A strong testbed should have native simplicity, robust hardness, informative tractable neighbours, reduction centrality, audit value, model fit, quantifier clarity, and an explicit consequence for the target class separation. Rankings below are project strategy rankings, not literature consensus.

## A. Exact local constraint systems

| ID | Problem | Native form | Why attractive | Hidden obstruction | Controls | Project role | Sources |
|---|---|---|---|---|---|---|---|
| `L01` | Positive 1-in-3 SAT | Each positive 3-variable constraint requires exactly one true variable | One relation, no negations, no large numbers | Shared variables couple locally trivial choices globally | XOR-SAT, acyclic incidence, bounded treewidth, specified occurrence restrictions | Leading positive testbed candidate | `[P03]`, `[P06]`, `[P07]` |
| `L02` | 1-in-3 SAT with literals | Exactly one of three literals is true | Canonical exact-cardinality SAT variant | Negations add polarity compatibility | Positive 1-in-3 SAT, XOR-SAT | Logical control | `[P03]`, `[P07]` |
| `L03` | Positive NAE-3SAT | Every positive triple contains both truth values | Symmetric hypergraph-colouring form | Hyperedges propagate incompatible colour choices | Graph 2-colouring, acyclic hypergraphs, bounded width | Secondary CSP testbed | `[P03]`, `[P08]` |
| `L04` | 3-SAT | Every 3-literal clause has a true literal | Canonical reduction and fine-grained benchmark | Negations, clause slack, and gadgets obscure the core mechanism | 2-SAT, Horn-SAT, dual-Horn-SAT, affine SAT | Canonical adversarial standard | `[P01]`, `[P02]`, `[P03]`, `[P27]` |
| `L05` | Finite-domain CSP | Fixed local relations over a finite domain | Unified algebraic classification framework | Fixed-template dichotomy does not classify every structural restriction or succinct encoding | Tractable polymorphisms, bounded-width structures | Foundational framework | `[P03]`, `[P04]`, `[P05]` |
| `L06` | Label Cover / projection CSP | Edge constraints project labels | Canonical PCP endpoint | Promise gaps and alphabet growth target approximation | Exact CSP and bounded-gap variants | Approximation infrastructure | `[P28]` |
| `L07` | Unique-SAT | Promise of at most one satisfying assignment | Isolates witness multiplicity | Valiant–Vazirani isolation is randomized | SAT, restricted deterministic isolation | Promise control | `[P26]` |

### Exact-incidence form

Positive 1-in-3 SAT is

\[
Ax=\mathbf 1,
\qquad x\in\{0,1\}^n,
\]

with exactly three ones in every row. This motivates an exact-incidence cluster with X3C and 3-Dimensional Matching. The cluster is organizational; theorem transfer is never automatic.

## B. Exact selection and incidence systems

| ID | Problem | Native form | Attraction | Hidden obstruction | Controls | Project role | Sources |
|---|---|---|---|---|---|---|---|
| `I01` | X3C | Select 3-sets covering each element exactly once | Pure exactness without weights or negations | Sets collide through shared elements | Acyclic exact cover, perfect matching | Column-sparse exact-incidence control | `[P02]`, `[P42]` |
| `I02` | 3-Dimensional Matching | Select disjoint tripartite triples | Exact cover with a tripartite promise | Local disjointness choices create global dead ends | Bipartite perfect matching | Structured hard control | `[P02]`, `[P42]` |
| `I03` | Exact Hitting Set | Select elements meeting each set exactly once | Exchanges the selected incidence side | One choice can satisfy or destroy many constraints | Laminar and bounded-width systems | Duality control | `[P42]` |
| `I04` | Set Packing | Select a prescribed number of disjoint sets | Direct conflict semantics | Pairwise compatibility does not guarantee a large global packing | Matching, bounded-rank systems | Branching and parameterized testbed | `[P02]`, `[P25]`, `[P42]` |
| `I05` | Set Cover | Cover the universe with at most \(k\) sets | Canonical covering and approximation problem | Overlap plus a global cardinality bound | Laminar and bounded-frequency cases | Approximation and kernelization testbed | `[P02]`, `[P28]`, `[P42]` |
| `I06` | Perfect Matching | Select disjoint edges covering all vertices | Polynomial exact rank-two selection | Rank-two tractability does not extend automatically to rank three | — | Mandatory tractable control | `[P41]` |

## C. Pairwise graph constraints

| ID | Problem | Native form | Attraction | Hidden obstruction | Controls | Project role | Sources |
|---|---|---|---|---|---|---|---|
| `G01` | 3-Coloring | Adjacent vertices receive different colours | Only binary local constraints | Cycle consistency and colour permutations propagate globally | 2-Coloring, bounded treewidth, bipartite homomorphisms | Best graph-CSP candidate | `[P05]`, `[P09]` |
| `G02` | Independent Set | Select \(k\) mutually nonadjacent vertices | One local forbidden pattern | Early choices can destroy the global cardinality target | Bounded treewidth, perfect graphs, Vertex Cover duality | Parameterized and branching testbed | `[P02]`, `[P25]`, `[P42]` |
| `G03` | Clique | Select \(k\) pairwise adjacent vertices | Direct all-pairs compatibility | Dense global consistency | Bounded degeneracy and structured classes | Communication and monotone lower-bound testbed | `[P02]`, `[P13]`, `[P20]` |
| `G04` | Vertex Cover | Select \(k\) vertices meeting every edge | Simple coverage and clean kernels | Coverage overlaps under a size bound | Bounded parameters and special classes | Preprocessing control | `[P02]`, `[P25]` |
| `G05` | Dominating Set | Select \(k\) vertices covering all closed neighbourhoods | Local coverage language | Neighbourhood overlap and distance interactions | Planar, bounded-degree, bounded-width variants | Parameterized and approximation testbed | `[P25]`, `[P42]` |
| `G06` | Max Cut | Partition vertices so at least \(K\) edges cross | Clean quadratic Boolean formulation | Edge preferences conflict globally | Bipartite graphs and special classes | SDP and quadratic-optimization testbed | `[P33]`, `[P42]` |
| `G07` | Fixed-\(H\) graph homomorphism | Map the input graph to \(H\) preserving edges | Unified binary-CSP boundary | Non-bipartite targets retain hard cycle compatibility | Bipartite targets | Classification foundation | `[P09]` |

## D. Global graph and network structures

| ID | Problem | Native form | Attraction | Hidden obstruction | Controls | Project role | Sources |
|---|---|---|---|---|---|---|---|
| `N01` | Hamiltonian Cycle | One cycle visits every vertex | Minimal syntax and no weights | Partial paths must avoid premature cycles while preserving global connectability | Bounded treewidth, tournaments, selected planar classes | Connectivity-interface testbed | `[P02]`, `[P42]` |
| `N02` | Hamiltonian Path | One spanning path | Slightly simpler endpoint structure | Same global connectivity obstruction | Directed acyclic and bounded-width variants | Connectivity control | `[P42]` |
| `N03` | Travelling Salesperson decision | Tour weight at most \(B\) | Combines connectivity, binary weights, and polyhedra | Numerical and subtour compatibility coexist | Metric approximation, bounded width | Optimization and extension-complexity testbed | `[P02]`, `[P42]`, `[P50]` |
| `N04` | Steiner Tree | Connect terminals within a cost bound | Exposes path sharing and network design | Locally short paths may be globally redundant or incompatible | Fixed terminals and bounded width | Network-decomposition testbed | `[P25]`, `[P42]` |
| `N05` | Feedback Vertex Set | Delete at most \(k\) vertices to remove all cycles | Global cyclic obstruction with local deletion | Cycles overlap | Parameterized and bounded-width regimes | Kernelization control | `[P25]` |

## E. Arithmetic, algebraic, and optimization systems

| ID | Problem | Native form | Attraction | Hidden obstruction | Controls | Project role | Sources |
|---|---|---|---|---|---|---|---|
| `A01` | Subset Sum | Select numbers summing exactly to a target | One weighted Boolean equation | Binary weights encode compatibility and exponential numeric range | Unary weights, small items, small doubling, superincreasing instances | Completed benchmark and adversarial control | `[P02]`, `[P31]` |
| `A02` | Partition | Divide numbers into equal-sum parts | Symmetric numerical form | Pseudopolynomial tractability can hide binary encoding | Unary and bounded-range inputs | Numeric boundary control | `[P02]`, `[P42]` |
| `A03` | 0-1 Knapsack | Meet value and weight thresholds | Connects feasibility and optimization | Multiple numerical dimensions obscure one mechanism | Bounded weights and approximation schemes | Algorithmic-regime testbed | `[P42]` |
| `A04` | 0-1 Integer Feasibility | Boolean vector satisfies linear inequalities | Universal linear-arithmetic umbrella | Coefficients and inequalities simulate arbitrary Boolean computation | Totally unimodular matrices, fixed dimension | Broad bridge, not a clean first testbed | `[P32]`, `[P42]` |
| `A05` | Exact integer linear systems | \(Ax=b\) over Boolean or bounded variables | Direct comparison with parity and incidence systems | Integer equality is much stronger than modular equality | Finite-field systems and totally unimodular cases | CSP–arithmetic bridge | `[P03]`, `[P04]` |
| `A06` | Fixed-dimensional integer programming | Integer feasibility with fixed dimension | Demonstrates dimension-controlled tractability | Dimension is unbounded in general encodings | Fixed dimension | Geometric tractable control | `[P32]` |
| `A07` | Quadratic Boolean optimization | Optimize a quadratic form over Boolean variables | Unifies Max Cut and QUBO-style encodings | General pairwise interactions preserve arbitrary compatibility | Submodular and special-sign cases | Relaxation and algebraic control | `[P33]` |
| `A08` | Exact lattice problems | CVP/SVP-style exact geometric decision | Geometric representation can expose structure | Dimension and precision encode hard combinatorics | Fixed dimension and approximation regimes | Verified reduction and geometry control | `[P49]` |

## F. Scheduling, sequencing, and allocation

| ID | Problem | Native form | Attraction | Hidden obstruction | Controls | Project role | Sources |
|---|---|---|---|---|---|---|---|
| `S01` | Job-Shop Scheduling | Schedule operations under machine and precedence constraints | Concrete temporal/resource semantics | Local machine choices interact through long precedence cycles | Single-machine and selected fixed-machine regimes | Constraint-propagation testbed | `[P42]` |
| `S02` | Bin Packing | Pack items into bounded-capacity bins | Simple capacity language and strong approximation theory | Assignment symmetry and global coordination | Fixed bin count and bounded item sizes | Configuration-space testbed | `[P42]` |
| `S03` | Multiprocessor Scheduling | Assign jobs under a makespan bound | Direct relation to Partition and load balancing | Locally balanced choices may be globally poor | Fixed machine count and approximation schemes | Numeric allocation control | `[P42]` |

## G. Universal computation and certification

| ID | Problem or object | Native form | Attraction | Hidden obstruction | Project role | Sources |
|---|---|---|---|---|---|---|
| `U01` | Circuit-SAT | Assign circuit inputs so output is one | Closest finite representation of arbitrary verification | Very little structure remains | Leading lower-bound sibling and algorithms-to-lower-bounds testbed | `[P01]`, `[P10]`, `[P11]` |
| `U02` | CNF-SAT / 3-SAT | Satisfy a conjunction of clauses | Standard normal form and fine-grained benchmark | Normalization introduces gadgets | Canonical reduction standard | `[P01]`, `[P02]`, `[P27]` |
| `U03` | UNSAT | Decide that no satisfying assignment exists | Exposes no-instance certification | coNP-complete, not an NP witness problem | Proof-complexity testbed | `[P18]`, `[P19]` |
| `U04` | TAUT | Decide universal truth | Canonical propositional proof range | Strong proof-system bounds remain open | Proof-complexity testbed | `[P18]`, `[P19]` |
| `U05` | #SAT | Count satisfying assignments | Strengthens existence to counting | Different class objective and cancellation issues | Counting and representation audit | `[P29]`, `[P54]` |
| `U06` | QBF / TQBF | Evaluate alternating quantifiers | Canonical PSPACE boundary | Strictly broader than NP unless classes collapse | Expressiveness boundary control | `[P47]` |
| `U07` | Circuit Value | Evaluate a fixed-input circuit | P-complete sequential computation control | Evaluation is easier than existential input search | Separates Circuit-SAT from circuit evaluation | `[P48]` |

## H. Strategic objects outside ordinary NP-complete decision problems

| ID | Object | Current status | Strategic value | Main caution | Sources |
|---|---|---|---|---|---|
| `M01` | MCSP | In NP; standard NP-completeness unresolved | Meta-complexity, compression, pseudorandomness, magnification | Input is a full truth table | `[P22]`, `[P24]` |
| `M02` | Polynomial Identity Testing | Randomized polynomial time; deterministic polynomial time open in important models | Derandomization and arithmetic lower bounds | Not known NP-complete | `[P35]`, `[P44]` |
| `M03` | Permanent polynomial | #P-complete counting object and algebraic lower-bound target | Canonical VP-versus-VNP object | Boolean transfer requires another theorem | `[P16]`, `[P29]`, `[P35]` |
| `M04` | Graph Isomorphism | Quasipolynomial time; not known NP-complete | Intermediate-status and meta-complexity control | Not representative of arbitrary NP verification | `[P22]`, `[P43]` |
| `M05` | Integer factoring | In NP and coNP; polynomial quantum algorithm known | Cryptographic and alternative-model control | Not known NP-complete | `[P30]`, `[P45]` |
| `M06` | TFNP / PPAD / PLS | Total search with guaranteed solutions | Separates existence principles from optional witnesses | Different quantifiers from NP decision | `[P46]`, `[P58]` |
| `M07` | Sparse languages and compression | Density or preprocessing boundary objects | Connects sparse completeness and compression to collapses | Exact reduction assumptions are essential | `[P39]`, `[P40]` |
| `M08` | NP-intermediate languages | Conditional languages neither in P nor NP-complete | Warns against false dichotomies | Existence is conditional on \(P\ne NP\) | `[P53]` |

## I. Mandatory controls

| Hard testbed | Control | Difference to isolate |
|---|---|---|
| Positive 1-in-3 SAT | XOR-SAT | exact cardinality versus parity |
| Positive 1-in-3 SAT | acyclic or bounded-treewidth CSP | global cyclic compatibility |
| 3-SAT | 2-SAT, Horn-SAT, dual-Horn-SAT | width and closure structure |
| 3-Coloring | 2-Coloring | three-way colour consistency versus bipartiteness |
| X3C / 3DM | Perfect Matching | rank three versus rank two |
| Hamiltonian Cycle | bounded-treewidth Hamiltonicity | unbounded connectivity interface |
| Subset Sum | unary or polynomially bounded target | binary magnitude |
| 0-1 ILP | totally unimodular systems | integrality of the relaxation |
| Circuit-SAT | restricted circuit classes and Circuit Value | input search versus fixed evaluation |
| SAT | Unique-SAT | witness multiplicity and randomized isolation |
| NP search | TFNP | optional existence versus guaranteed totality |
| NP | QBF / PSPACE | existential verification versus alternation |

## J. Project rankings by objective

### Positive universal-algorithm testbeds

| Rank | Candidate | Why | Decisive first audit |
|---|---|---|---|
| **1** | **Positive 1-in-3 SAT** | Minimal exact local relation without negations or binary magnitudes | Compare exact-one propagation with XOR and reduction-generated cyclic incidence |
| **2** | **X3C** | Incidence-oriented exact selection | Test shared-element collisions and column sparsity |
| **3** | **Positive NAE-3SAT** | Symmetric hypergraph colouring | Separate complement symmetry from exact cardinality |
| **4** | **3-Coloring** | Binary local constraints and mature width theory | Test dependence on separators and bipartiteness |
| **5** | **3-SAT** | Canonical and reduction-central | Remove gadget syntax and test the source relation |
| **6** | **3-Dimensional Matching** | Strong tripartite exact-cover promise | Test whether tripartiteness reduces compatibility |
| **7** | **Hamiltonian Cycle** | Clean unweighted global condition | Bound separator connectivity information |
| **8** | **Circuit-SAT** | Universal computation object | Use only for a mechanism acting directly on circuits |

### Lower-bound and separation testbeds

| Rank | Candidate | Why | Required theorem |
|---|---|---|---|
| **1** | **Circuit-SAT and restricted circuit SAT** | Direct connection to computation and algorithms-to-lower-bounds | Nontrivial algorithm or explicit class lower bound with transfer theorem |
| **2** | **UNSAT / TAUT** | Makes proof length explicit | Lower bound for a proof system with exact consequence stated |
| **3** | **3-SAT / CNF-SAT** | Central fine-grained and proof benchmark | Model-specific bound plus valid transfer |
| **4** | **Finite-domain CSP** | Complete fixed-template classification and structural parameters | New instance-structural theorem |
| **5** | **Clique / Independent Set** | Strong monotone, communication, and parameterized interfaces | Escape restricted-model assumptions |
| **6** | **MCSP and magnification targets** | Small lower bounds may imply large separations | Exact magnification theorem and threshold |
| **7** | **Polyhedral and semialgebraic formulations** | Expose formulation and proof-hierarchy barriers | Show the model captures the intended algorithm or proof system |

## K. Recommended next cluster

The strongest current positive candidate is **exact-incidence constraint systems** centred on Positive 1-in-3 SAT, with X3C and 3-Dimensional Matching as hard controls and XOR-SAT, bounded-width CSPs, and Perfect Matching as tractable controls.

The first route must specify an exact propagation, width, decomposition, or composition mechanism; a global polynomial state bound; canonical reduction audits; and a stop condition.

The strongest lower-bound sibling remains **Circuit-SAT and restricted-circuit satisfiability**, requiring an explicit model and consequence theorem before activation.

Neither investigation is active.

## Final status

This is an orientation and decision artifact. It registers no new mathematical claim and changes no existing claim state.
