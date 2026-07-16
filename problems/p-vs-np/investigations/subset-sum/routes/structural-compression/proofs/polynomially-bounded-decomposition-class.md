# Polynomially Bounded Decomposition Class

**Claim:** `SS-SC-005`  
**Mathematical status:** `PROVED`  
**Review maturity:** `CHECKED`  
**Recorded:** 2026-07-16

## Statement

Consider a class of Subset Sum instances for which there is a deterministic procedure that, on every instance of binary length \(N\), produces a sequence of at most \(p(N)\) exact reductions for some polynomial \(p\). Each reduction is one of the following:

1. a forced inclusion or exclusion of an item;
2. replacement of a target interval by a valid progression-plus-residue completion certificate;
3. replacement by at most \(p(N)\) exact subinstances whose total encoded size is at most \(p(N)\).

Assume further that:

- every reduction and certificate is found and verified in time \(p(N)\);
- every modulus, residue table, and intermediate representation has size at most \(p(N)\);
- each recursive branch strictly decreases a nonnegative integer measure bounded by \(p(N)\);
- terminal instances are decidable in time \(p(N)\).

Then Subset Sum is decidable in polynomial time on this class.

## Proof

The decreasing measure bounds the recursion depth by \(p(N)\). The branching and total encoded size at every level are polynomially bounded by assumption, so the total number of generated states is polynomially bounded. Each transition, certificate check, and terminal decision takes polynomial time. Composing polynomially many polynomial-time operations gives a polynomial-time decision procedure. Exactness follows because every permitted reduction preserves target reachability. ∎

## Scope

This theorem states the exact boundary the route would need to cross. It does not show that arbitrary Subset Sum instances admit such a decomposition. The SAT-to-Subset-Sum audit shows that the route did not establish the required polynomial state bound or decreasing measure on the canonical hard family.