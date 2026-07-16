# Investigations

Each directory is a concrete research environment used to test a route toward the broader P versus NP problem.

The canonical cross-investigation orientation is maintained separately in:

- [Research-programme landscape](../references/research-programme-landscape.md)
- [Problem-testbed landscape](../references/problem-testbed-landscape.md)
- [Canonical source map](../references/top-level-landscape-sources.md)

## Active

No investigation currently has an active route.

## Existing

- [Subset Sum](subset-sum/README.md) — two universal routes closed; retained as an arithmetic algorithmic landscape, adversarial reduction target, and source of restricted results.

## Prospective investigations

The canonical landscapes identify two leading candidates. A directory should be created only after a concrete route mechanism is selected.

1. **Exact-incidence constraint systems**
   - primary testbed: Positive 1-in-3 SAT;
   - hard controls: X3C and 3-Dimensional Matching;
   - tractable controls: XOR-SAT, perfect matching, and bounded-width CSPs;
   - required opening artifact: an exact propagation, decomposition, width, or composition mechanism with a decisive first audit.
2. **Circuit-SAT and restricted-circuit satisfiability**
   - purpose: algorithms-to-lower-bounds or explicit circuit-model lower bounds;
   - required opening artifact: the exact circuit class, desired algorithm or lower bound, transfer theorem, and barrier audit.

Another investigation may be selected from the canonical landscapes only with an explicit mathematical advantage and stop condition.

## Investigation requirements

An investigation must maintain:

- `README.md` — scope and navigation;
- `STATUS.md` — current operational state;
- `CLAIMS.md` — authoritative local claim ledger;
- `routes/` — distinct approaches kept separate.

An investigation is not itself a claim that resolving the chosen problem by a particular method is the only route to P versus NP.
