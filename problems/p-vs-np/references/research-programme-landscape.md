# P versus NP Research-Programme Landscape

**Classification:** Literature audit and top-level route-selection framework  
**Cutoff:** 2026-07-16  
**Review:** `CHECKED` by second-pass source, implication, and scope audit  
**Scope:** Classical deterministic P versus NP unless a row explicitly states another class, model, promise, or conditional hypothesis

## Purpose

This document records the major research programmes relevant to P versus NP and clarifies how this repository uses concrete testbeds. It is complete at the level of major paradigms, not every model, proof system, parameter, or paper.

Sources:

- [primary source map](top-level-landscape-sources.md);
- [specialist source map](top-level-landscape-specialist-sources.md);
- [second-pass source map](top-level-landscape-second-pass-sources.md).

## Repository method

The repository uses a **testbed-and-audit method**:

1. choose a concrete problem whose native representation exposes a candidate mechanism;
2. state the strongest exact claim and the precise class consequence;
3. distinguish encoded-input polynomial time from pseudopolynomial, parameterized, average-case, promise, randomized, or heuristic performance;
4. prove correctness in both directions and count the complete computation graph;
5. attack the mechanism with canonical reductions, tractable neighbours, and expressiveness controls;
6. retain local theorems, retract unsupported universal claims, and close a route when its pass condition fails.

A deterministic polynomial-time algorithm for one NP-complete language proves \(P=NP\). Failure of one representation or algorithm family proves no unrestricted separation.

## Consequence map

| Target theorem | Immediate consequence | Relation to classical P versus NP |
|---|---|---|
| An NP-complete language is in \(P\) | \(P=NP\) | Direct positive resolution |
| \(NP\not\subseteq P/\mathrm{poly}\) | NP has no polynomial-size nonuniform circuits | Strictly stronger than \(P\ne NP\) |
| \(NP\ne coNP\) | No polynomially bounded Cook–Reckhow proof system | Implies \(P\ne NP\), but is a distinct target |
| \(VP\ne VNP\) | Algebraic circuit separation | Algebraic analogue; transfer to Boolean \(P\ne NP\) requires an additional theorem |
| ETH or SETH lower bound | Quantitative conditional hardness | Does not prove \(P\ne NP\) unconditionally |
| Lower bound in a restricted model | Separation only inside that model | Needs a polynomial-overhead subsumption theorem to affect unrestricted algorithms |
| \(NP\subseteq BQP\) | Efficient quantum solution of NP problems | Does not imply classical \(P=NP\) |

## A. Positive and structural algorithmic programmes

| ID | Programme | Precise objective | Established value | Central obstacle | Project disposition | Sources |
|---|---|---|---|---|---|---|
| `A01` | Direct NP-complete algorithm | Put one NP-complete language in deterministic polynomial time | Would prove \(P=NP\) | Every general method retains exponential, pseudopolynomial, or unbounded structural cost | Core positive route form | `[P01]`, `[P02]` |
| `A02` | Constraint-language classification | Classify fixed local relations by algebraic invariants | Boolean and finite-domain CSP dichotomies are complete | Classification does not make an NP-complete template tractable | Foundation for selecting hard templates and tractable controls | `[P03]`, `[P04]`, `[P05]` |
| `A03` | Structural-instance tractability | Prove polynomial time under bounded width, degree, occurrence, genus, rank, doubling, or another parameter | Produces exact tractable subclasses | The parameter may be unbounded or encode the original difficulty | Strong source of local theorems | `[P25]` |
| `A04` | Algebraic algorithms | Translate constraints into linear algebra, polynomial systems, groups, transforms, or spectral objects | Explains affine CSPs, matching algorithms, and restricted arithmetic algorithms | Projection may lose exact Boolean witness compatibility | Use only with exact lifting and bit-complexity accounting | `[P03]`, `[P35]` |
| `A05` | Geometric and polyhedral algorithms | Use LP, SDP, lattices, convexity, or cutting planes | Solves relaxations and structured integer programmes | Integrality gaps and exponential polyhedral complexity remain | Restricted or approximation route absent an exact integrality theorem | `[P32]`, `[P33]`, `[P38]` |
| `A06` | Decomposition and dynamic programming | Retain exact interface states across separators | Polynomial algorithms on bounded-width structures | Boundary state and total generated-state size can be exponential | Viable only with a global state bound | `[P25]` |
| `A07` | Search, isolation, and self-reduction | Relate decision, witness recovery, uniqueness, and counting | Supplies search-to-decision and randomized isolation reductions | Random isolation is not deterministic polynomial time | Reduction infrastructure, not an independent resolution | `[P26]` |
| `A08` | Learning algorithms | Learn functions represented by restricted circuits and derive lower bounds or algorithms | Creates connections among learning, natural proofs, and circuit complexity | Efficient learnability weakens rapidly as circuit expressiveness grows | Indirect restricted-model programme | `[P49]` |

## B. Circuit, proof, and representation lower bounds

| ID | Programme | Exact target | Established reach | Main barrier | Project disposition | Sources |
|---|---|---|---|---|---|---|
| `B01` | General Boolean circuit lower bounds | Prove an explicit NP language requires superpolynomial-size circuits | Strong bounds for restricted models | General circuits remain beyond known methods | Central negative target, not currently operational without a restricted model | `[P10]`, `[P13]`, `[P14]`, `[P15]` |
| `B02` | Algorithms-to-lower-bounds | Give nontrivial SAT or counting algorithms for a circuit class and derive lower bounds | Successful for several restricted circuit classes | Must beat exhaustive search for a sufficiently expressive class | Highest-leverage positive-to-negative bridge | `[P10]`, `[P11]` |
| `B03` | Arithmetic circuit lower bounds | Separate explicit polynomial families, typically \(VP\) from \(VNP\) | Rich algebraic techniques and restricted-model bounds | Strong general lower bounds remain open; Boolean transfer is separate | Independent algebraic programme | `[P16]`, `[P35]` |
| `B04` | Geometric Complexity Theory | Separate orbit closures using representation theory and geometry | Unifies algebraic obstruction programmes | Explicit useful obstructions remain elusive | Long-horizon algebraic route | `[P16]` |
| `B05` | Propositional proof complexity | Lower-bound proof length in strong proof systems | Exponential bounds for many restricted systems | Frege and Extended Frege remain resistant | Best no-instance certification route | `[P18]`, `[P19]` |
| `B06` | Algebraic and semialgebraic proof systems | Lower-bound Polynomial Calculus, Nullstellensatz, Sum-of-Squares, or Cutting Planes | Strong degree, rank, and size bounds in restricted settings | Bounds do not automatically transfer to stronger systems | Important proof-complexity subprogramme | `[P50]`, `[P51]` |
| `B07` | Communication and branching programmes | Lower-bound information crossing a partition or variable order | Strong unconditional model-specific results | Transfer requires a natural polynomial-overhead compilation theorem | Use only with explicit model subsumption | `[P20]`, `[P21]` |
| `B08` | Monotone complexity | Lower-bound circuits without negation | Exponential bounds for Clique and related functions | Negation may collapse complexity | Warning and restricted-model evidence only | `[P13]` |
| `B09` | Formula, bounded-depth, and restricted gate lower bounds | Separate increasingly expressive circuit hierarchies | Deep results for formulas, AC0, selected modular and threshold models | Progress may not extend to general circuits | Incremental lower-bound programme | `[P10]`, `[P11]`, `[P15]` |
| `B10` | Polyhedral extension complexity | Prove no small LP extended formulation represents a combinatorial polytope | Exponential lower bounds for TSP and other polytopes | LP formulations are only one algorithmic model | Model-specific geometric barrier | `[P38]` |
| `B11` | Descriptive complexity | Separate definability in logics corresponding to restricted computation | Precise logical characterizations and inexpressibility results | Capturing unrestricted P and NP in manageable logics is difficult | Foundational restricted-model programme | `[P36]` |
| `B12` | Time and space hierarchy / diagonalization | Construct languages outside smaller resource classes | Proves unconditional hierarchy theorems | Standard diagonalization relativizes and has not separated P from NP | Foundational method and barrier control | `[P40]`, `[P41]`, `[P14]` |

## C. Meta-complexity, compression, and indirect programmes

| ID | Programme | Core idea | Established value | Central obstacle | Sources |
|---|---|---|---|---|---|
| `C01` | MCSP and meta-complexity | Decide whether an explicit truth table has a small circuit | Links compression, pseudorandomness, cryptography, and lower bounds | Standard NP-completeness is unresolved and truth-table inputs are already exponential in variable count | `[P22]` |
| `C02` | Hardness magnification | Derive major separations from modest lower bounds on carefully selected problems | Reduces large goals to smaller quantitative thresholds | Localization and natural-proof-type barriers may reappear | `[P23]`, `[P24]` |
| `C03` | Hardness versus randomness | Build pseudorandom generators from hardness or infer hardness from derandomization | Central equivalences between pseudorandomness and circuits | Requires strong explicit hardness or derandomization | `[P12]` |
| `C04` | Polynomial Identity Testing derandomization | Give deterministic polynomial-time identity testing | Derandomization implies arithmetic circuit lower bounds under standard formulations | Does not directly settle Boolean \(P\) versus \(NP\) | `[P35]`, `[P48]` |
| `C05` | Instance compression and kernelization | Reduce instances to equivalent smaller encodings | Gives exact preprocessing and conditional lower bounds | The parameter may be unbounded; general compression implies collapses | `[P25]`, `[P44]` |
| `C06` | Sparse complete sets | Study whether NP-complete information can live in sparse languages | Mahaney's theorem rules out sparse many-one complete sets unless \(P=NP\) | Depends on exact reduction and sparsity notions | Compression boundary theorem | `[P43]` |
| `C07` | Advice and nonuniformity | Study \(P/\mathrm{poly}\), advice, and small circuit families | Karp–Lipton collapse consequences constrain NP having small circuits | Nonuniform algorithms need not be constructible uniformly | Separate nonuniform target | `[P42]` |
| `C08` | Average-case complexity and cryptography | Prove distributional hardness and one-wayness | Supplies practical hardness and pseudorandom objects | Worst-case NP-completeness does not imply average-case hardness | `[P12]`, `[P22]` |
| `C09` | Total search complexity | Study guaranteed-solution classes such as TFNP, PPAD, and PLS | Isolates equilibrium, parity, and local-optimum principles | Totality changes the problem type and blocks ordinary NP-completeness under standard assumptions | `[P47]` |

## D. Conditional, quantitative, and neighbouring landscapes

| ID | Programme | What it establishes | Limitation | Project use | Sources |
|---|---|---|---|---|---|
| `D01` | ETH and SETH | Conditional exponential and fine-grained lower bounds | Does not prove \(P\ne NP\) | Audit runtime exponents and parameter dependence | `[P27]` |
| `D02` | Parameterized complexity | FPT, XP, W-hardness, and kernelization classifications | Does not classify unrestricted polynomial time | Identify genuine structural parameters | `[P25]` |
| `D03` | PCP and hardness of approximation | Gap reductions and approximation lower bounds | Does not directly settle exact decision | Approximation infrastructure and adversarial controls | `[P28]` |
| `D04` | Counting complexity | `#P`-completeness and witness-counting distinctions | Counting can be harder than decision | Strengthen representation audits | `[P29]` |
| `D05` | Quantum complexity | Alternative-model algorithms and separations | \(NP\subseteq BQP\) would not imply classical \(P=NP\) | Keep quantum claims separate | `[P30]` |
| `D06` | Ladner intermediate degrees | If \(P\ne NP\), NP contains languages neither in P nor NP-complete | Conditional on the unresolved separation | Warns against assuming every natural unresolved NP problem is complete | `[P46]` |
| `D07` | PSPACE and alternation controls | QBF and alternating computation expose stronger quantifier structure | Targets a larger class than NP | Detect accidental expressiveness beyond existential verification | `[P39]` |

## E. Proof barriers and audit rules

| Barrier or rule | Precise warning | Sources |
|---|---|---|
| **Relativization** | Oracle worlds realize both \(P=NP\) and \(P\ne NP\); fully relativizing techniques cannot resolve the question | `[P14]` |
| **Natural proofs** | Under pseudorandom-function assumptions, constructive large properties cannot prove strong general circuit lower bounds | `[P15]` |
| **Algebrization** | Many arithmetizing techniques still survive algebraic oracle extensions where the desired separation fails | `[P17]` |
| **Model-transfer failure** | A model-specific lower bound affects unrestricted algorithms only after a polynomial-overhead subsumption theorem | `[P20]`, `[P21]`, `[P31]` |
| **Compact-syntax vacuity** | Storing the input or unevaluated computation as a small expression is not a solution | `[P31]` |
| **Uniform/nonuniform confusion** | Small circuits or advice do not automatically give a uniform polynomial-time algorithm | `[P42]` |
| **Decision/counting confusion** | Counting or proof lower bounds do not automatically transfer to decision | `[P18]`, `[P29]` |
| **Promise/totality confusion** | Promise problems and total-search problems have different quantifiers from ordinary NP decision languages | `[P26]`, `[P47]` |
| **Conditional/unconditional confusion** | ETH, SETH, cryptographic, and average-case assumptions must remain explicit | `[P27]` |

## F. Objective matrix

| Objective | Best primary object | Required control |
|---|---|---|
| Clean positive NP-complete testbed | Positive 1-in-3 SAT | XOR-SAT, acyclic CSP, bounded width, canonical 3-SAT reductions |
| Exact-incidence compatibility | Positive 1-in-3 SAT, X3C, 3DM | Perfect matching and affine systems |
| Algorithms-to-lower-bounds | Circuit-SAT | Explicit restricted circuit class and transfer theorem |
| No-instance certification | UNSAT and TAUT | Exact proof system and consequence map |
| Additive compression | Subset Sum and 0-1 ILP | Unary weights, affine equations, reduction-generated instances |
| Global connectivity interfaces | Hamiltonian Cycle and TSP | Bounded-width controls and extension-complexity models |
| Meta-complexity and magnification | MCSP variants | Exact reduction, input model, and magnification threshold |
| Derandomization | PIT and BPP-related problems | Exact arithmetic-to-Boolean consequence |

## Project determination

Maintain two separate tracks:

1. **Positive track:** select an NP-complete testbed and a concrete exact mechanism.
2. **Negative track:** select an explicit circuit, proof, communication, polyhedral, logical, or magnification model and state the exact class consequence.

The strongest current positive candidate is the exact-incidence cluster centred on Positive 1-in-3 SAT. The strongest lower-bound sibling is Circuit-SAT and restricted-circuit satisfiability. Neither is activated by this landscape.

## Final status

This is an orientation artifact. It registers no new mathematical claim and changes no existing claim state.