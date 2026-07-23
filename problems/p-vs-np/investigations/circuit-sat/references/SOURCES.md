# Sources — Circuit-SAT Algorithms to Lower Bounds

## Primary transfer and application sources

- Ryan Williams, “Improving Exhaustive Search Implies Superpolynomial Lower Bounds,” *SIAM Journal on Computing* 42(3):1218–1244, 2013. DOI: `10.1137/10080703X`. Establishes algorithm-to-lower-bound connections in which small improvements over exhaustive simulation for specified natural problems imply consequences including `NEXP not subseteq P/poly`. Exact theorem statements must be audited before use.

- Ryan Williams, “Nonuniform ACC Circuit Lower Bounds,” *Journal of the ACM* 61(1), Article 2, 2014. DOI: `10.1145/2559903`. Proves `NEXP` does not have polynomial-size nonuniform `ACC` circuits using faster satisfiability algorithms for `ACC`. This is a class-specific success, not a generic unrestricted-circuit theorem.

- Ryan Williams, “New Algorithms and Lower Bounds for Circuits With Linear Threshold Gates,” *Theory of Computing* 14(17):1–25, 2018. Gives nontrivial counting algorithms and lower bounds for composed classes including `ACC o THR`, with explicit size, depth and coefficient regimes.

- Nikhil Vyas and Ryan Williams, “Lower Bounds Against Sparse Symmetric Functions of ACC Circuits: Expanding the Reach of #SAT Algorithms,” *STACS 2020*, LIPIcs 154:59:1–59:16; extended journal version in *Theory of Computing Systems* 67:149–174, 2023. Gives explicit #SAT-to-lower-bound transfer statements, including polynomial-factor and `2^{n-n^epsilon}` savings regimes.

## Foundational supporting sources

- Russell Impagliazzo, Valentine Kabanets, and Avi Wigderson, “In Search of an Easy Witness: Exponential Time vs. Probabilistic Polynomial Time,” *Journal of Computer and System Sciences* 65(4):672–694, 2002. DOI: `10.1016/S0022-0000(02)00024-7`. Supplies easy-witness and nonuniform-hardness machinery used in later algorithms-to-lower-bounds developments.

- Alexander Razborov and Steven Rudich, “Natural Proofs,” *Journal of Computer and System Sciences* 55(1):24–35, 1997. DOI: `10.1006/jcss.1997.1494`. Records the natural-proofs barrier. It constrains classes of proof techniques; it does not say circuit lower bounds are impossible.

## Secondary orientation

- Igor C. Oliveira, “Algorithms versus Circuit Lower Bounds,” arXiv:`1309.0249`, 2013. Survey of transfers from satisfiability, learning, compression and derandomization to circuit lower bounds. Use for orientation only; accepted theorem statements must cite primary sources.

## Source-use rules

1. Record the exact theorem number and hypotheses before marking any transfer statement `ESTABLISHED / CHECKED`.
2. Do not cite an abstract as sufficient evidence for detailed quantifiers.
3. Distinguish SAT from #SAT and approximate counting.
4. Distinguish polynomial-factor savings from exponential savings.
5. State whether the result is deterministic, randomized, worst-case or expected-time.
6. State circuit size, depth, gate basis, modulus and weight restrictions.
7. State the precise complexity-class separation obtained.
8. Do not transfer a theorem from `ACC`, threshold circuits or formulas to unrestricted Boolean circuits without a proved simulation or inclusion satisfying the needed size bounds.