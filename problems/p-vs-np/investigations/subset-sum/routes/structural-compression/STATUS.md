# Status — Structural Compression

**State:** Closed as a universal strategy; restricted results retained  
**Updated:** 2026-07-16

## Final disposition

- The universal dense-or-separated bundle composition claim is retracted.
- The residue-completion lemma is proved and internally checked.
- The forced/progression/lattice universal algorithm claim is retracted.
- The SAT-to-Subset-Sum audit failed the route's pass condition: modular states preserve the original assignment and clause-compatibility choices.
- A restricted polynomial-time theorem survives when the entire exact decomposition and all associated state bounds are polynomial in the binary input length.

## Retained records

- [Closeout](CLOSEOUT.md)
- [Route record](notes/route-record.md)
- [Residue-completion lemma](proofs/residue-completion-lemma.md)
- [Polynomially bounded decomposition class](proofs/polynomially-bounded-decomposition-class.md)
- [Bundle claim retraction](counterexamples/bundle-lemma.md)
- [Completed SAT-to-Subset-Sum audit](audits/sat-to-subset-sum.md)

## Reopening condition

Reopen this route only if a new exact composition theorem preserves cross-component compatibility, is efficiently constructible, bounds all intermediate states polynomially in binary input length, and supplies a strict progress measure on reduction-generated hard instances.

## Next program

Develop exact-state compression barriers: identify and formalize the information that prevents exact dynamic-programming states from being merged.