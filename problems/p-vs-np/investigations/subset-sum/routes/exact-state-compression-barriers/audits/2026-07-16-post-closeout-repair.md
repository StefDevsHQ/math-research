# Post-Closeout Repository Repair — Exact-State Compression Barriers

**Route:** `SS-ECB`  
**Mode:** VERIFY / RECORD  
**Verdict:** Repository evidence repaired; mathematical disposition unchanged  
**Date:** 2026-07-16

## Audit trigger

A repository-wide review after the route closeout identified two classes of defects:

1. the committed evidence file for `SS-ECB-017` ended inside an unfinished display formula and did not contain the claimed proof;
2. several parent status and navigation files still described exact-state compression barriers as future work after the route had already been completed and closed.

These were repository-integrity defects. The route's final mathematical conclusion remained that only model-specific barriers had been established and that no lower bound for arbitrary Subset Sum algorithms followed.

## Mathematical reconstruction of `SS-ECB-017`

The restored proof uses the binary-payload target

\[
t=MH+c(\alpha),
\qquad M=2^n.
\]

For every variable index \(i<n\), divisibility \(2^{i+1}\mid M\) gives

\[
t\bmod 2^{i+1}=c(\alpha)\bmod 2^{i+1}.
\]

Hence the payload bit \(\alpha_i\) is one exactly when

\[
2^i\le t\bmod 2^{i+1}<2^{i+1}.
\]

A width-three clause can therefore be evaluated using at most three compact bounded residue-range branch predicates. Chaining the clause tests gives a deterministic directed acyclic graph with at most \(3m\) branch nodes. Its arithmetic constants have \(O(n)\) bits, so the complete encoded graph has polynomial size.

Combined with the binary-payload assignment-target embedding, this proves that compact bounded residue-range predicates plus unrestricted repeated branching evaluate every width-three CNF assignment slice in polynomial complete graph size.

The restored proof explicitly records that pure residue-equality branching remains unclassified.

## Repository repairs

The repair branch:

- replaced the truncated `SS-ECB-017` evidence with the complete claim, proof, size accounting, boundary cases, and scope;
- synchronized the repository root with the two closed Subset Sum routes;
- synchronized the P-versus-NP overview and operational status;
- replaced the structural-compression route's obsolete next-program text with historical successor information;
- preserved all claim identifiers and statuses;
- retained the distinction between internal `CHECKED` review and independent review.

## Claim-state determination

No mathematical claim state changed.

- `SS-ECB-017` remains `PROVED / CHECKED` because its complete proof is now recorded and has been rechecked against the binary-payload embedding.
- `SS-ECB-016` remains `RETRACTED / CHECKED` because the restored theorem refutes its natural bounded-residue completion, not every conceivable arithmetic proof graph.
- `SS-ECB-008` remains inactive and open only under the route's reopening conditions.
- No result implies a fixed-target Subset Sum lower bound, a lower bound for arbitrary exact algorithms, or `P != NP`.

## Final repository state

The Subset Sum investigation has completed and closed two universal routes:

1. structural compression as a universal polynomial-time algorithmic strategy;
2. exact-state compression barriers as a broad representation-model lower-bound strategy.

No active Subset Sum route is selected. The project is in route selection.