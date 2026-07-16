# P versus NP Research-Programme Landscape

**Classification:** Literature audit and top-level route-selection framework  
**Cutoff:** 2026-07-16  
**Review:** `CHECKED` against the source map and current project records  
**Scope:** Classical deterministic P versus NP unless a row explicitly states another model or conditional hypothesis

## Purpose

This document records the major known research programmes relevant to P versus NP and clarifies how this repository uses concrete NP-complete problems.

It is intended to be complete at the level of major paradigms. It does not enumerate every circuit class, proof system, parameter, reduction, or paper.

Source identifiers refer to [top-level-landscape-sources.md](top-level-landscape-sources.md).

## The repository method

The repository uses a **testbed-and-audit method**:

1. choose a concrete NP-complete problem whose native representation exposes a candidate mechanism;
2. state the strongest exact universal claim suggested by that mechanism;
3. distinguish polynomial dependence on encoded input length from pseudopolynomial, parameterized, average-case, or heuristic performance;
4. prove correctness in both directions and count the complete computation graph;
5. attack the mechanism with canonical reductions and neighbouring tractable or hard problems;
6. retain local theorems, retract unsupported universal claims, and close a route when its pass condition fails.

For a positive route, one polynomial-time algorithm for any NP-complete language proves `P=NP`.

For a negative route, failure of one problem representation, algorithm family, proof system, or compression language does **not** prove `P!=NP`. A valid negative programme must establish a lower bound in a model broad enough to imply the desired class separation.

## A. Positive algorithmic programmes

| ID | Programme | Strongest precise objective | What it already achieves | Central obstacle | Suitable testbed | Project disposition | Sources |
|---|---|---|---|---|---|---|---|
| `A01` | Direct algorithm for an NP-complete problem | Give a deterministic algorithm polynomial in total binary input length for one NP-complete language | Would immediately prove `P=NP` | Every known general method leaves an exponential, pseudopolynomial, or unbounded structural parameter | Positive 1-in-3 SAT, 3-SAT, X3C, 3-Coloring, Circuit-SAT | Core positive route form | `[P01]`, `[P02]` |
| `A02` | Constraint-language classification | Classify fixed local relations by polymorphisms or equivalent algebraic structure | Boolean and finite-domain fixed-template CSPs satisfy P-versus-NP-complete dichotomies | The dichotomy classifies relation languages; it does not make NP-complete templates tractable | Positive 1-in-3 SAT, NAE-3SAT, 3-Coloring | Foundation for choosing tractable neighbours and hard templates | `[P03]`, `[P04]`, `[P05]` |
| `A03` | Structural-instance tractability | Prove polynomial time under bounded treewidth, hypertree width, degree, occurrence, genus, doubling, or another explicit instance parameter | Produces rigorous tractable subclasses and exact dynamic programmes | The parameter may be unbounded on reduction-generated instances or merely restate input magnitude | CSPs, graph problems, exact incidence systems, Subset Sum | Strong source of local theorems; not universal without a global bound | `[P04]`, `[P05]`, `[P25]` |
| `A04` | Algebraic algorithms | Translate constraints into linear algebra, polynomial systems, group equations, transforms, or spectral objects | Explains tractability of affine CSPs and powers many restricted algorithms | Exact Boolean compatibility can survive the algebraic projection; general polynomial-system solving remains hard | XOR-SAT as control; 1-in-3 SAT and Circuit-SAT as adversaries | Use only with exact lifting and encoding analysis | `[P03]`, `[P04]`, `[P35]` |
| `A05` | Geometric and polyhedral algorithms | Use linear programming, semidefinite programming, lattices, convexity, or cutting planes | Solves important relaxations and structured integer instances | Integrality gaps, adversarial lattice geometry, and exponentially complex polytopes remain | 0-1 ILP, Max Cut, TSP, Subset Sum | Restricted or approximation route unless an exact integrality theorem is proved | `[P32]`, `[P33]` |
| `A06` | Decomposition and dynamic programming | Decompose an instance along separators and retain exact boundary states | Polynomial algorithms on bounded-width structures | Interface state may grow exponentially; a compact final description does not bound all intermediate work | CSP incidence graphs, 3-Coloring, Hamiltonian Cycle | Promising positive subclass method with mandatory global-state accounting | `[P04]`, `[P05]`, `[P25]` |
| `A07` | Algorithms-to-lower-bounds | Design a nontrivial SAT or counting algorithm for a restricted circuit class and convert it into a circuit lower bound | Has yielded unconditional lower bounds for several restricted circuit classes | The algorithm must beat exhaustive search for a sufficiently expressive class; unrestricted Circuit-SAT remains untouched | Circuit-SAT and restricted circuit SAT | Highest-leverage bridge between positive and negative work | `[P10]`, `[P11]` |
| `A08` | Derandomization through hardness | Build pseudorandom generators from circuit lower bounds, or derive lower bounds from derandomization | Connects `P=BPP`-type questions with circuit hardness | The needed hardness or generator often presupposes a major lower bound | Circuit evaluation, PIT, BPP-complete promise problems | Cross-cutting programme; not a direct NP-complete testbed route | `[P12]` |
| `A09` | Exact search-to-decision and isolation | Reduce witness recovery, unique solutions, or counting to decision through isolation or parsimonious reductions | Clarifies relations among SAT, Unique-SAT, search, and counting | Random isolation does not automatically yield deterministic polynomial time | SAT, Exact Cover, matching systems | Useful reduction infrastructure, not an independent resolution | `[P26]` |

## B. Lower-bound and separation programmes

| ID | Programme | Desired conclusion | Established reach | Main barrier | Best testbed or object | Project disposition | Sources |
|---|---|---|---|---|---|---|---|
| `B01` | Direct Boolean circuit lower bounds | Prove an explicit NP language requires superpolynomial-size general Boolean circuits | Strong lower bounds for restricted models such as monotone circuits, formulas, constant depth, and selected modular classes | General circuit lower bounds are far beyond current techniques | Circuit-SAT, explicit Boolean functions | Central negative route, but not currently operational without a restricted target model | `[P10]`, `[P13]`, `[P14]`, `[P15]` |
| `B02` | Restricted-circuit SAT and lower bounds | Extend nontrivial SAT algorithms and lower bounds through a hierarchy of circuit classes | Successful for several classes below general circuits | Expressiveness increases faster than known algorithms and lower-bound methods | ACC, threshold, symmetric, sparse-composition circuits | Mathematically productive incremental programme | `[P10]`, `[P11]` |
| `B03` | Arithmetic circuit lower bounds | Prove superpolynomial lower bounds for explicit polynomials such as the permanent | Stronger lower bounds and richer algebraic tools than in the Boolean setting | Known rank, shifted-partial-derivative, and geometric techniques have their own barriers | Permanent versus determinant, polynomial identity testing | Separate but strategically connected programme | `[P16]`, `[P17]`, `[P35]` |
| `B04` | Geometric Complexity Theory | Use representation theory and algebraic geometry to separate orbit closures associated with easy and hard polynomials | Unifies and extends many algebraic lower-bound viewpoints | Explicit useful obstructions and sufficiently strong lower bounds remain unresolved | Permanent versus determinant | Long-horizon algebraic programme, not a concrete NP-complete investigation | `[P16]` |
| `B05` | Propositional proof complexity | Prove superpolynomial proof-length lower bounds for strong proof systems | Exponential lower bounds are known for many restricted systems | Frege and Extended Frege remain resistant; a system-specific bound need not imply `P!=NP` | UNSAT, TAUT, pigeonhole and Tseitin formulas | Best route for certifying no-instances, separate from positive SAT algorithms | `[P18]`, `[P19]` |
| `B06` | Communication and branching-program lower bounds | Lower-bound information crossing partitions, variable orders, or interfaces | Strong unconditional results for many restricted models | A lower bound transfers only if actual algorithms compile into the model with polynomial overhead | Clique, disjointness, CSP interfaces, ordered decision diagrams | Use only with a natural subsumption theorem | `[P20]`, `[P21]` |
| `B07` | Data-structure and preprocessing lower bounds | Rule out compact preprocessing with fast exact queries | Strong conditional and cell-probe lower bounds exist for many query problems | Static query models may be much weaker than unrestricted algorithms | Repeated target queries, reachability, dynamic graph problems | Model-specific barrier programme | `[P20]` |
| `B08` | Monotone lower bounds | Restrict circuits or algorithms to preserve a natural order structure | Exponential monotone circuit lower bounds are known for problems such as Clique | Negation can collapse monotone complexity; monotone bounds do not imply general bounds | Clique and matching-related functions | Valuable warning against monotone reasoning, not a direct P-versus-NP proof | `[P13]` |
| `B09` | Descriptive and logical lower bounds | Separate definability or fixed-point logics corresponding to restricted computation | Gives precise lower bounds for restricted logical formalisms | Capturing all of P or NP in a controllable logic is itself difficult | Graph properties and finite structures | Foundational restricted-model programme | `[P36]` |

## C. Magnification, meta-complexity, and indirect programmes

| ID | Programme | Core idea | Established value | Central obstacle | Project role | Sources |
|---|---|---|---|---|---|---|
| `C01` | Minimum Circuit Size Problem and meta-complexity | Study the complexity of recognizing whether a truth table has a small circuit | Connects compression, pseudorandomness, cryptography, and lower bounds | MCSP is not known to be NP-complete under standard deterministic reductions, and its input is already a full truth table | Strategic non-NP-complete testbed | `[P22]` |
| `C02` | Hardness magnification | Show that a modest lower bound for a carefully selected problem implies a major circuit lower bound or `P!=NP` | Reduces some major goals to seemingly smaller quantitative lower bounds | Localization and natural-proof-type barriers can reappear; the target problem and threshold must be exact | MCSP variants, sparse languages, streaming or formula models | High-risk lower-bound sibling programme | `[P23]`, `[P24]` |
| `C03` | Hardness versus randomness | Trade average-case pseudorandomness or derandomization for worst-case circuit hardness | Supplies equivalences and conditional constructions central to modern complexity | Requires either hard explicit functions or strong derandomization beyond known reach | Circuit complexity, BPP, PIT | Cross-cutting bridge | `[P12]` |
| `C04` | Average-case complexity and cryptographic hardness | Prove that natural distributions are hard or base cryptography on worst-case problems | Explains practical hardness and supplies pseudorandom objects | Worst-case NP-completeness does not automatically imply average-case hardness | Lattice problems, one-way functions, random SAT | Separate quantifier regime; never substitute for worst-case proof | `[P12]`, `[P22]` |
| `C05` | Instance compression and kernelization | Reduce an instance to an equivalent smaller instance under a parameter | Gives exact preprocessing theorems and conditional lower bounds | A useful parameter may be unbounded; unrestricted compression can encode the whole problem | Vertex Cover, CSP width, arithmetic parameters | Strong restricted-class methodology | `[P25]` |

## D. Conditional and quantitative landscapes

| ID | Programme | What it asks | What it establishes | Limitation | Project use | Sources |
|---|---|---|---|---|---|---|
| `D01` | ETH and SETH fine-grained complexity | Determine whether exponential bases or polynomial exponents can be improved | Conditional lower bounds and tight reductions among SAT and many problems | Does not prove `P!=NP`; all conclusions inherit the hypothesis | Audit allegedly fast algorithms and parameter dependence | `[P27]` |
| `D02` | Parameterized complexity | Separate fixed-parameter tractability, XP, W-hardness, and kernelization | Refines which structural parameters genuinely control difficulty | FPT or hardness in one parameter does not classify unrestricted polynomial time | Choose tractable-subclass routes and expose hidden parameters | `[P25]` |
| `D03` | PCP and hardness of approximation | Convert exact satisfiability gaps into approximation hardness | Explains why many optimisation problems resist approximation | Gap hardness does not directly settle exact decision P versus NP | Label Cover, Max-3SAT, Set Cover | Reduction and approximation infrastructure | `[P28]` |
| `D04` | Counting complexity | Count witnesses rather than decide existence | Establishes `#P`-complete problems and sharper distinctions among representations | Counting may be strictly harder than decision; a counting lower bound need not transfer automatically | `#SAT`, permanent, exact counting CSPs | Adversarial strengthening and representation audit | `[P29]` |
| `D05` | Quantum complexity | Ask whether quantum algorithms solve NP-complete problems efficiently | Gives alternative-model algorithms and oracle separations | Even `NP subseteq BQP` would not prove classical `P=NP` | Quantum SAT and search | Track separately; never merge with classical claims | `[P30]` |

## E. Known proof barriers

These are limitations of broad classes of techniques, not proofs that P versus NP is impossible to resolve.

| Barrier | Precise warning | What it blocks | What it does not show | Sources |
|---|---|---|---|---|
| **Relativization** | There are oracle worlds in which `P=NP` and oracle worlds in which `P!=NP` | Any proof that remains valid under arbitrary oracle substitution | That all diagonalization or oracle-inspired ideas fail | `[P14]` |
| **Natural proofs** | Under strong pseudorandom-function assumptions, constructive and large combinatorial properties cannot prove strong general circuit lower bounds | A broad family of known combinatorial circuit-lower-bound strategies | Unnatural, nonconstructive, or model-specific lower bounds | `[P15]` |
| **Algebrization** | Many arithmetizing techniques still hold relative to algebraic oracle extensions where the target separation can fail | Techniques extending both relativization and standard arithmetization | All algebraic methods or arithmetic circuit programmes | `[P17]` |
| **Model-transfer failure** | A lower bound for a representation model constrains an algorithm only after a polynomial-overhead compilation theorem | Informal claims that decision diagrams, automata, monotone circuits, or interfaces capture all algorithms | Model-specific theorems inside their exact scope | `[P20]`, `[P21]`, `[P31]` |
| **Compact-syntax vacuity** | An input or unresolved computation can always be stored as a small exact expression | Lower bounds based only on final description length | Lower bounds that count construction, normalization, queries, and all intermediate states | `[P31]` |

## F. Research-objective matrix

| Objective | Best primary object | Best neighbouring controls | Why |
|---|---|---|---|
| Find a clean positive NP-complete algorithmic testbed | Positive 1-in-3 SAT | XOR-SAT, acyclic CSP, bounded-occurrence and bounded-treewidth variants | One exact local relation, no negations, no large weights; hardness comes from global incidence compatibility |
| Study exact-incidence compatibility | Positive 1-in-3 SAT, X3C, 3-Dimensional Matching | Perfect matching and affine systems | Row-sparse, column-sparse, and tripartite forms expose the same exact-cover equation from different sides |
| Connect algorithms to lower bounds | Circuit-SAT | Restricted circuit SAT classes | Direct access to arbitrary Boolean computation and established algorithms-to-lower-bounds theorems |
| Study proof length for no-instances | UNSAT and TAUT | Resolution, Cutting Planes, Polynomial Calculus, Frege | Makes certification complexity explicit |
| Test additive or arithmetic compression | Subset Sum and 0-1 ILP | Unary weights, small doubling, affine equations | Binary magnitude and common-witness compatibility are explicit |
| Study global graph interfaces | Hamiltonian Cycle, Steiner Tree | Bounded-treewidth and planar variants | Separators must preserve connectivity and subtour information |
| Study pairwise local constraints | 3-Coloring, Independent Set | 2-Coloring, 2-SAT, bipartite homomorphism | Clean transition from tractable binary constraints to globally inconsistent cycles |
| Study approximation gaps | Label Cover and Max-3SAT | Exact SAT and bounded-gap CSPs | Canonical PCP endpoints |
| Pursue magnification | MCSP and selected sparse/meta-complexity problems | Restricted formula and streaming models | Small lower bounds can imply major separations under exact magnification theorems |

## G. Project determination

The repository should maintain **two separate top-level tracks**:

1. **Positive investigation track:** choose a concrete NP-complete testbed and seek a universal polynomial-time mechanism, while comparing it with tractable neighbours and canonical reductions.
2. **Negative or barrier track:** choose an explicit computation, proof, circuit, communication, or magnification model and state exactly which class separation follows from the desired lower bound.

The completed Subset Sum work belongs to the positive-testbed history and remains an adversarial arithmetic control.

The strongest next positive candidate is the **exact-incidence cluster** centred on Positive 1-in-3 SAT, with X3C and 3-Dimensional Matching as dual controls.

The strongest lower-bound sibling candidate is **Circuit-SAT and restricted circuit satisfiability**, because nontrivial algorithms can sometimes be converted into circuit lower bounds.

Neither candidate is activated by this landscape. Route selection remains a separate project decision.

## Final status

This document is an orientation and decision artifact. It registers no new mathematical claim. External results retain their source status, and project results retain the statuses in their authoritative ledgers.
