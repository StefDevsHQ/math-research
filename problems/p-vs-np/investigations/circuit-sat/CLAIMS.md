# Claim Ledger — Circuit-SAT Algorithms to Lower Bounds

This is the authoritative investigation-level claim ledger.

## Claims

| ID | Statement | Status | Review | Evidence | Updated |
|---|---|---|---|---|---|
| `CS-001` | The Circuit-SAT investigation is in consequence-map construction; no circuit class or algorithmic route has been selected. | `OPEN` | `CHECKED` | [Status](STATUS.md) and [vertical slices](VERTICAL-SLICES.md) | 2026-07-23 |
| `CS-002` | There are established class-specific results converting nontrivial satisfiability or counting algorithms into nonuniform circuit lower bounds, but the circuit class, savings regime and theorem hypotheses must be verified separately in each application. | `ESTABLISHED` | `DRAFT` | [Primary sources](references/SOURCES.md) | 2026-07-23 |

## Planned identifiers

Reserve identifiers only when the statements are precise:

- `CS-MOD-###` — circuit models and encodings;
- `CS-ALG-###` — algorithmic claims;
- `CS-TR-###` — transfer and consequence claims;
- `CS-LB-###` — project lower-bound conclusions;
- `CS-COMP-###` — finite computational evidence.

Stable identifiers must not be reused after retraction or disproof.

## Claim boundaries

- An established transfer theorem is not a project-original lower bound.
- A faster algorithm on a restricted subclass does not activate a theorem for a larger class.
- SAT, #SAT, approximate counting and evaluation are distinct problems.
- Runtime is measured against the complete binary circuit encoding.
- Randomized, deterministic, expected-time and worst-case algorithms must be labelled separately.
- A conditional lower-bound consequence remains conditional until its algorithmic premise is proved.
- Failure of one algorithmic mechanism does not imply the corresponding circuit lower bound is false.
- No current claim resolves `P=NP` or `P!=NP`.