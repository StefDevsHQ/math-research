# Investigations

Each directory is a concrete research environment used to test a route toward the broader P versus NP problem.

## Active

No investigation currently has an active route.

## Existing

- [Subset Sum](subset-sum/README.md) — two universal routes closed; retained as an arithmetic algorithmic landscape and adversarial reduction target.

## Prospective investigations

The top-level landscapes identify two leading candidates. These directories should be created only after a concrete route mechanism is selected.

1. **Exact-incidence constraint systems**
   - primary testbed: Positive 1-in-3 SAT;
   - hard controls: X3C and 3-Dimensional Matching;
   - tractable controls: XOR-SAT, perfect matching, and bounded-width CSPs;
   - required opening artifact: an exact propagation, decomposition, width, or composition mechanism with a decisive first audit.
2. **Circuit-SAT and restricted-circuit satisfiability**
   - purpose: algorithms-to-lower-bounds or explicit circuit-model lower bounds;
   - required opening artifact: the exact circuit class, desired algorithm or lower bound, transfer theorem, and barrier audit.

See:

- [Research-programme landscape](../references/research-programme-landscape.md)
- [Problem-testbed landscape](../references/problem-testbed-landscape.md)

## Investigation requirements

An investigation must maintain:

- `README.md` — scope and navigation;
- `STATUS.md` — current operational state;
- `CLAIMS.md` — authoritative local claim ledger;
- `routes/` — distinct approaches kept separate.

An investigation is not itself a claim that resolving the chosen problem by a particular method is the only route to P versus NP.