# Polynomially Bounded Decomposition Class

**Claim:** `SS-SC-005`  
**Mathematical status:** `PROVED`  
**Review maturity:** `CHECKED`  
**Recorded:** 2026-07-16

## Statement

Consider a class of Subset Sum instances for which there is a deterministic exact decomposition procedure. On every instance of binary length \(N\), the procedure generates a computation graph satisfying all of the following for some polynomial \(p\):

1. the graph contains at most \(p(N)\) states;
2. the total encoded size of all states, certificates, moduli, and residue tables is at most \(p(N)\);
3. every transition is one of:
   - forced inclusion or exclusion of an item;
   - application of a valid progression-plus-residue completion certificate;
   - replacement by exact subinstances;
4. every transition and certificate is generated and verified in time \(p(N)\);
5. every terminal state is decidable in time \(p(N)\).

Then Subset Sum is decidable in polynomial time on this class.

## Proof

The computation graph has at most \(p(N)\) states and total polynomial encoding size. Each state transition, certificate verification, and terminal decision takes polynomial time. Processing the entire graph therefore requires only polynomially many polynomial-time operations. Exactness follows because every permitted transition preserves target reachability. ∎

## Scope

This theorem records the precise sufficient condition needed by the route: a globally polynomial-size exact computation, not merely polynomial branching and polynomial depth. Polynomial branching across polynomial depth can still generate exponentially many states.

The theorem does not show that arbitrary Subset Sum instances admit such a decomposition. The SAT-to-Subset-Sum audit shows that this route did not establish the required global state bound on the canonical hard family.