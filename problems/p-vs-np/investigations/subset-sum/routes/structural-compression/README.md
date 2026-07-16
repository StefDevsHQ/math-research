# Structural Compression Route

This route studied whether the exact reachable-sum state of Subset Sum could be represented and updated in size polynomial in the binary input length.

## Final conclusion

The route is closed as a universal polynomial-time strategy.

The original bundle composition claim was retracted. The refined forced/progression/lattice framework then failed its SAT-to-Subset-Sum audit because its modular states preserve the original assignment and clause-compatibility choices rather than compressing them.

Two restricted results remain:

- the residue-completion lemma;
- polynomial-time solvability for classes with an efficiently constructible decomposition whose branching, moduli, residue states, intermediate descriptions, and depth are polynomially bounded in the binary input length.

## Core records

- [Closeout](CLOSEOUT.md)
- [Route record](notes/route-record.md)
- [Residue-completion lemma](proofs/residue-completion-lemma.md)
- [Polynomially bounded decomposition class](proofs/polynomially-bounded-decomposition-class.md)
- [Bundle claim retraction](counterexamples/bundle-lemma.md)
- [Completed SAT-to-Subset-Sum audit](audits/sat-to-subset-sum.md)

## Administration

- [Route status](STATUS.md)
- [Route claim ledger](CLAIMS.md)
- [Proofs](proofs/README.md)
- [Counterexamples](counterexamples/README.md)
- [Audits](audits/README.md)
- [Experiments](experiments/README.md)
- [Working notes](notes/README.md)
- [Archive](archive/README.md)