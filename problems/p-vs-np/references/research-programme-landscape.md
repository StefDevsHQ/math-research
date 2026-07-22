# P versus NP Research-Programme Landscape

**Classification:** Literature audit and top-level route-selection framework  
**Cutoff:** 2026-07-22  
**Review:** `CHECKED` by source, implication, scope, and canonical-identifier audit  
**Scope:** Classical deterministic P versus NP unless a row explicitly states another class, model, promise, formal theory, or conditional hypothesis

## Purpose

This document records the major research programmes relevant to P versus NP and explains how this repository uses concrete testbeds. It is complete at the level of major established and currently prominent paradigms, not every circuit class, proof system, parameter, formal theory, or paper.

All identifiers resolve through the [canonical source map](top-level-landscape-sources.md). The [2026-07-22 completion audit](audits/2026-07-22-top-level-landscape-completion.md) records the inclusion test and the remaining non-exhaustiveness boundary.

## Repository method

1. Choose a concrete problem whose native representation exposes a candidate mechanism.
2. State the strongest exact claim and the precise class consequence.
3. Separate encoded-input polynomial time from pseudopolynomial, parameterized, average-case, promise, randomized, interactive, nonuniform, or heuristic performance.
4. Prove correctness in both directions and count the complete computation graph.
5. Attack the mechanism with canonical reductions, tractable neighbours, and expressiveness controls.
6. Retain local theorems, retract unsupported universal claims, and close a route when its pass condition fails.

A deterministic polynomial-time algorithm for one NP-complete language proves `P=NP`. Failure of one representation or algorithm family proves no unrestricted separation.

## Consequence map

| Target theorem | Immediate consequence | Relation to classical P versus NP |
|---|---|---|
| An NP-complete language is in `P` | `P=NP` | Direct positive resolution |
| `NP` is not contained in `P/poly` | NP has no polynomial-size nonuniform circuits | Stronger than `P!=NP` |
| `NP!=coNP` | No polynomially bounded Cook-Reckhow proof system | Implies `P!=NP`, but is a distinct target |
| `VP!=VNP` | Algebraic circuit separation | Needs a separate transfer theorem for Boolean `P!=NP` |
| ETH or SETH lower bound | Quantitative conditional hardness | Does not prove `P!=NP` unconditionally |
| Restricted-model lower bound | Separation only inside that model | Needs a polynomial-overhead subsumption theorem |
| Uniform restricted-circuit lower bound | Separation for a uniform language against a stated circuit class | Does not by itself separate `P` from `NP` |
| Independence from a weak arithmetic theory | That theory cannot prove the formalized statement | Does not decide the statement in standard mathematics |
| `IP=PSPACE` or another interactive-proof characterization | Equality in an interactive proof model | Does not imply `P=NP`; arithmetization may be nonrelativizing yet still algebrizing |
| `NP` contained in `BQP` | Efficient quantum solution of NP problems | Does not imply classical `P=NP` |

## A. Positive and structural algorithmic programmes

| ID | Programme | Precise objective | Established value | Central obstacle | Project disposition | Sources |
|---|---|---|---|---|---|---|
| `A01` | Direct NP-complete algorithm | Put one NP-complete language in deterministic polynomial time | Would prove `P=NP` | Known general methods retain exponential, pseudopolynomial, or unbounded structural cost | Core positive route form | `[P01]`, `[P02]` |
| `A02` | Constraint-language classification | Classify fixed local relations by algebraic invariants | Boolean and finite-domain CSP dichotomies are complete | Classification does not make a hard template tractable | Foundation for selecting hard templates and tractable controls | `[P03]`, `[P04]`, `[P05]` |
| `A03` | Structural-instance tractability | Prove polynomial time under bounded width, degree, occurrence, genus, rank, doubling, or another parameter | Produces exact tractable subclasses | The parameter may be unbounded or encode the original difficulty | Strong source of local theorems | `[P25]` |
| `A04` | Algebraic algorithms | Translate constraints into linear algebra, polynomial systems, groups, transforms, or spectral objects | Explains affine CSPs, matching, and restricted arithmetic algorithms | Projection may lose exact witness compatibility | Require exact lifting and bit-complexity accounting | `[P03]`, `[P35]`, `[P41]` |
| `A05` | Geometric and polyhedral algorithms | Use LP, SDP, lattices, convexity, or cutting planes | Solves relaxations and structured integer programmes | Integrality gaps and exponential polyhedral complexity remain | Restricted or approximation route absent exact integrality | `[P32]`, `[P33]`, `[P50]` |
| `A06` | Decomposition and dynamic programming | Retain exact interface states across separators | Polynomial algorithms on bounded-width structures | Boundary state and total generated-state size can be exponential | Viable only with a global state bound | `[P25]` |
| `A07` | Search, isolation, and self-reduction | Relate decision, witness recovery, uniqueness, and counting | Supplies search-to-decision and randomized isolation reductions | Random isolation is not deterministic polynomial time | Reduction infrastructure | `[P26]` |
| `A08` | Learning algorithms | Learn restricted circuit classes and derive algorithms or lower bounds | Connects learning, natural properties, and circuit complexity | Learnability weakens as expressiveness grows | Restricted-model programme | `[P52]` |

## B. Circuit, proof, and representation lower bounds

| ID | Programme | Exact target | Established reach | Main barrier | Project disposition | Sources |
|---|---|---|---|---|---|---|
| `B01` | General Boolean circuit lower bounds | Prove an explicit NP language requires superpolynomial-size circuits | Strong bounds for restricted models | General circuits remain beyond known methods | Central negative target | `[P10]`, `[P13]`, `[P14]`, `[P15]` |
| `B02` | Algorithms-to-lower-bounds | Give nontrivial SAT or counting algorithms for a circuit class and derive lower bounds | Successful for several restricted classes | Must beat exhaustive search for a sufficiently expressive class | Highest-leverage positive-to-negative bridge | `[P10]`, `[P11]` |
| `B03` | Arithmetic circuit lower bounds | Separate explicit polynomial families, typically `VP` from `VNP` | Rich algebraic techniques and restricted bounds | Strong general bounds remain open; Boolean transfer is separate | Independent algebraic programme | `[P16]`, `[P35]` |
| `B04` | Geometric Complexity Theory | Separate orbit closures using representation theory and geometry | Unifies algebraic obstruction programmes | Explicit useful obstructions remain elusive | Long-horizon algebraic route | `[P16]` |
| `B05` | Propositional proof complexity | Lower-bound proof length in strong proof systems | Exponential bounds for many restricted systems | Frege and Extended Frege remain resistant | Best no-instance certification route | `[P18]`, `[P19]` |
| `B06` | Algebraic and semialgebraic proof systems | Lower-bound Polynomial Calculus, Nullstellensatz, Sum-of-Squares, or Cutting Planes | Strong degree, rank, and size bounds in restricted settings | Bounds do not automatically transfer to stronger systems | Proof-complexity subprogramme | `[P51]` |
| `B07` | Communication and branching programmes | Lower-bound information crossing a partition or variable order | Strong model-specific results | Transfer requires a natural polynomial-overhead compilation theorem | Use only with explicit subsumption | `[P20]`, `[P21]` |
| `B08` | Monotone complexity | Lower-bound circuits without negation | Exponential bounds for Clique and related functions | Negation may collapse complexity | Restricted evidence only | `[P13]` |
| `B09` | Formula, bounded-depth, and restricted-gate lower bounds | Separate increasingly expressive circuit hierarchies | Deep results for several restricted classes | Progress may not extend to general circuits | Incremental programme | `[P10]`, `[P11]`, `[P15]` |
| `B10` | Polyhedral extension complexity | Rule out small LP extended formulations | Exponential bounds for TSP and other polytopes | LP formulations are one algorithmic model | Geometric model barrier | `[P50]` |
| `B11` | Descriptive complexity | Separate definability in logics corresponding to restricted computation | Precise characterizations and inexpressibility results | Capturing unrestricted P and NP is difficult | Foundational restricted-model programme | `[P36]`, `[P56]` |
| `B12` | Hierarchy and diagonalization | Construct languages outside smaller resource classes | Proves unconditional hierarchy theorems | Standard diagonalization relativizes and has not separated P from NP | Foundational method and barrier control | `[P37]`, `[P14]` |
| `B13` | Uniform lower bounds and resource-bounded Kolmogorov complexity | Derive lower bounds for uniform languages from compression, generation, or probabilistic Kolmogorov tasks | Gives algorithmic characterizations and lower bounds for stated uniform circuit classes | Uniform consequences remain class- and task-specific; nonuniform transfer is not automatic | Emerging algorithms-to-lower-bounds sibling | `[P63]`, `[P64]` |

## C. Meta-complexity, compression, and indirect programmes

| ID | Programme | Core idea | Established value | Central obstacle | Sources |
|---|---|---|---|---|---|
| `C01` | MCSP and meta-complexity | Decide whether an explicit truth table has a small circuit | Links compression, pseudorandomness, cryptography, and lower bounds | Standard NP-completeness is unresolved | `[P22]` |
| `C02` | Hardness magnification | Derive major separations from modest lower bounds | Reduces large goals to smaller thresholds | Localization and natural-proof-type barriers may reappear | `[P23]`, `[P24]` |
| `C03` | Hardness versus randomness | Build pseudorandom generators from hardness or infer hardness from derandomization | Central equivalences between pseudorandomness and circuits | Requires strong explicit hardness or derandomization | `[P12]` |
| `C04` | Polynomial Identity Testing derandomization | Give deterministic polynomial-time identity testing | Derandomization implies arithmetic or Boolean lower bounds under standard formulations | Does not directly settle Boolean P versus NP | `[P35]`, `[P44]` |
| `C05` | Instance compression and kernelization | Reduce instances to equivalent smaller encodings | Gives preprocessing theorems and conditional lower bounds | Parameters may be unbounded; general compression implies collapses | `[P25]`, `[P40]` |
| `C06` | Sparse complete sets | Study whether NP-complete information can live in sparse languages | Mahaney rules out sparse many-one complete sets unless `P=NP` | Depends on exact reduction and sparsity notions | `[P39]` |
| `C07` | Advice and nonuniformity | Study `P/poly`, advice, and small circuit families | Karp-Lipton collapse consequences constrain NP having small circuits | Nonuniform algorithms need not be constructible uniformly | `[P38]` |
| `C08` | Average-case complexity and cryptography | Prove distributional hardness and one-wayness | Supplies practical hardness and pseudorandom objects | Worst-case NP-completeness does not imply average-case hardness | `[P12]`, `[P22]` |
| `C09` | Total search complexity | Study guaranteed-solution classes such as TFNP, PPAD, and PLS | Isolates equilibrium, parity, and local-optimum principles | Totality changes the problem type | `[P46]`, `[P58]` |
| `C10` | Meta-mathematics and bounded arithmetic | Formalize complexity claims in weak theories and study feasible provability or independence | Connects proof complexity, bounded arithmetic, witnessing, and formal lower-bound statements | Independence from one theory does not decide truth; formalization strength must be explicit | `[P59]`, `[P60]` |

## D. Conditional, quantitative, and neighbouring landscapes

| ID | Programme | What it establishes | Limitation | Project use | Sources |
|---|---|---|---|---|---|
| `D01` | ETH and SETH | Conditional exponential and fine-grained lower bounds | Does not prove `P!=NP` | Audit runtime exponents and parameter dependence | `[P27]` |
| `D02` | Parameterized complexity | FPT, XP, W-hardness, and kernelization classifications | Does not classify unrestricted polynomial time | Identify genuine structural parameters | `[P25]` |
| `D03` | PCP and hardness of approximation | Gap reductions and approximation lower bounds | Does not directly settle exact decision | Approximation infrastructure | `[P28]` |
| `D04` | Counting complexity | `#P`-completeness and witness-counting distinctions | Counting can be harder than decision | Strengthen representation audits | `[P29]`, `[P54]` |
| `D05` | Quantum complexity | Alternative-model algorithms and separations | Quantum inclusion does not imply classical `P=NP` | Keep quantum claims separate | `[P30]`, `[P45]` |
| `D06` | Ladner intermediate degrees | If `P!=NP`, NP contains languages neither in P nor NP-complete | Conditional on the unresolved separation | Warn against assuming every unresolved NP problem is complete | `[P53]` |
| `D07` | PSPACE and alternation controls | QBF and alternating computation expose stronger quantifier structure | Targets a larger class than NP | Detect accidental expressiveness beyond existential verification | `[P47]` |
| `D08` | Interactive proofs and arithmetization | Characterize languages by randomized verifier-prover interaction using polynomial identities and sum-check-style methods | `IP=PSPACE` and related results show nonrelativizing power | Does not imply `P=NP`; many arithmetizing methods still algebrize | Cross-cutting bridge among proof, counting, and circuit programmes | `[P61]`, `[P62]`, `[P17]` |
| `D09` | Randomized, promise, and interactive class map | Track consequences among `RP`, `BPP`, `MA`, `AM`, `NP`, `coNP`, `PH`, and `PSPACE` | These classes use different error, promise, interaction, or quantifier conventions | Prevent accidental promotion to deterministic classical claims | `[P12]`, `[P26]`, `[P61]`, `[P62]`, `[P65]`, `[P66]` |

## E. Proof barriers and audit rules

| Barrier or rule | Precise warning | Sources |
|---|---|---|
| Relativization | Oracle worlds realize both answers; fully relativizing techniques cannot resolve the question | `[P14]` |
| Natural proofs | Under pseudorandom-function assumptions, constructive large properties cannot prove strong general circuit lower bounds | `[P15]` |
| Algebrization | Many arithmetizing techniques survive algebraic oracle extensions where the separation fails | `[P17]` |
| Model-transfer failure | A model-specific lower bound affects unrestricted algorithms only after a polynomial-overhead subsumption theorem | `[P20]`, `[P21]`, `[P31]` |
| Compact-syntax vacuity | Storing the input or unevaluated computation as a small expression is not a solution | `[P31]` |
| Uniform/nonuniform confusion | Small circuits or advice do not automatically give a uniform polynomial-time algorithm; a uniform lower bound need not imply an unrestricted nonuniform one | `[P38]`, `[P63]`, `[P64]` |
| Decision/counting/proof confusion | Counting, interactive-proof, or proof-system results do not automatically transfer to deterministic decision | `[P18]`, `[P29]`, `[P61]`, `[P62]` |
| Promise/totality/error confusion | Promise, total-search, randomized, and interactive problems have different quantifiers and acceptance conditions from NP decision languages | `[P26]`, `[P58]`, `[P65]`, `[P66]` |
| Formal-theory independence confusion | Unprovability in a named weak theory is not a proof that the statement is false or independent of stronger standard foundations | `[P59]`, `[P60]` |
| Conditional/unconditional confusion | ETH, SETH, cryptographic, and average-case assumptions must remain explicit | `[P27]` |

## F. Randomized, promise, and interactive consequence map

| Statement | Immediate reading | What it does not establish |
|---|---|---|
| `P=NP` | Deterministic polynomial-time verification search collapses to deterministic decision | Nothing stronger about `PSPACE`, counting, or quantum classes follows automatically |
| `P=BPP` | Randomness adds no power for bounded-error polynomial-time decision | Does not imply `P=NP` |
| `NP=coNP` | Yes- and no-instances both have polynomial certificates | Does not by itself imply `P=NP` |
| `NP=RP` | NP problems have one-sided-error randomized polynomial algorithms | Does not provide deterministic polynomial algorithms without derandomization |
| `NP` contained in `BPP` | NP has bounded-error randomized polynomial algorithms | Does not imply `P=NP` without a derandomization theorem |
| `NP` contained in `AM` | NP has public-coin interactive proofs, already true because `NP` is contained in `AM` | Gives no collapse toward `P` |
| `IP=PSPACE` | Polynomial-space languages have interactive proofs | Gives no deterministic polynomial-time algorithm for PSPACE or NP |
| Promise-problem algorithm | Correctness holds only on inputs satisfying the promise | Does not decide the corresponding unrestricted language |

## G. Objective matrix

| Objective | Best primary object | Required control |
|---|---|---|
| Clean positive NP-complete testbed | Positive 1-in-3 SAT | XOR-SAT, acyclic CSP, bounded width, canonical 3-SAT reductions |
| Exact-incidence compatibility | Positive 1-in-3 SAT, X3C, 3DM | Perfect matching and affine systems |
| Algorithms-to-lower-bounds | Circuit-SAT | Explicit restricted circuit class and transfer theorem |
| Uniform lower-bound route | Explicit generation, compression, or Kolmogorov task | Exact uniform class consequence and nonuniform boundary |
| No-instance certification | UNSAT and TAUT | Exact proof system and consequence map |
| Formal-provability route | Bounded arithmetic theory plus formalized complexity statement | Exact theory, encoding, witnessing theorem, and independence scope |
| Interactive-proof bridge | Arithmetized counting or proof task | Exact verifier model, error convention, and deterministic consequence |
| Additive compression | Subset Sum and 0-1 ILP | Unary weights, affine equations, reduction-generated instances |
| Global connectivity interfaces | Hamiltonian Cycle and TSP | Bounded-width controls and extension-complexity models |
| Meta-complexity and magnification | MCSP variants | Exact reduction, input model, and magnification threshold |
| Derandomization | PIT and BPP-related problems | Exact arithmetic-to-Boolean or randomized-to-deterministic consequence |

## Project determination

Maintain two separate active-track types and four cross-cutting controls:

1. **Positive track:** select an NP-complete testbed and a concrete exact mechanism.
2. **Negative track:** select an explicit circuit, proof, communication, polyhedral, logical, magnification, or uniform model and state the exact class consequence.
3. **Formal-theory control:** state the exact arithmetic theory before making provability or independence claims.
4. **Interactive/randomized control:** state error, promise, interaction, and derandomization assumptions.
5. **Uniformity control:** separate uniform languages and algorithms from nonuniform circuit families.
6. **Transfer control:** require an explicit theorem before moving between decision, counting, proof, algebraic, or restricted-model claims.

The strongest current positive candidate remains the exact-incidence cluster centred on Positive 1-in-3 SAT. The strongest lower-bound sibling remains Circuit-SAT and restricted-circuit satisfiability. Neither is activated by this landscape.

## Final status

This is an orientation artifact. It registers no new mathematical claim and changes no existing claim state. The completion pass broadens the programme map but does not alter the current route recommendation.