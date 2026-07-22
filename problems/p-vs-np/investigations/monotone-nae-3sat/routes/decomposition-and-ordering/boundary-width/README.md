# R2.1 — Boundary-Width Dynamic Programming

**Subroute:** `R2.1`  
**Status:** `PROVED / RESTRICTED`  
**Primary claim:** `NAE-005 — PROVED / CHECKED`

## Result

Given a variable ordering with maximum processed boundary width `w`, Monotone NAE-3SAT is decidable in

```text
2^{O(w)} poly(L)
```

time and space, with exact boundary assignments as the interface state.

## Scope

This is an exact restricted algorithm. It is polynomial only when `w = O(log L)` or another explicit bound makes `2^{O(w)}` polynomial.

## Limitation

The theorem does not show that every instance has an efficiently constructible low-width ordering. High-width hard instances remain possible.

## Relationship to other subroutes

- baseline for `R2.3` beyond-width decomposition;
- control for `R1` symbolic-state representations;
- the fan family demonstrates that ordering can radically change width and exact-state growth.

## Evidence

See the investigation object specification, claim ledger, VS-04 controls, and exact-profile laboratory.