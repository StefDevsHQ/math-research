# Investigations

Each directory is a concrete research environment used to test a route toward the broader P versus NP problem.

The canonical cross-investigation orientation is maintained separately in:

- [Research-programme landscape](../references/research-programme-landscape.md)
- [Problem-testbed landscape](../references/problem-testbed-landscape.md)
- [Canonical source map](../references/top-level-landscape-sources.md)

## Active

- [Circuit-SAT algorithms to lower bounds](circuit-sat/README.md) — active in consequence-map construction and circuit-model selection. No circuit class or algorithmic mechanism has yet been selected.

## Retained and closed universal routes

- [Monotone NAE-3SAT](monotone-nae-3sat/README.md) — universal ordered-state and DNNF exact-representation routes closed; exact residualization, restricted decomposition results and model-specific barriers retained.
- [Subset Sum](subset-sum/README.md) — two universal routes closed; retained as an arithmetic algorithmic landscape, adversarial reduction target and source of restricted results.

## Prospective investigations

The canonical landscapes retain an exact-incidence sibling track:

1. **Exact-incidence constraint systems**
   - primary exactness-first testbed: Positive 1-in-3 SAT;
   - hard controls: X3C and 3-Dimensional Matching;
   - tractable controls: XOR-SAT, perfect matching and bounded-width CSPs;
   - required opening artifact: an exact propagation, decomposition, width or composition mechanism with a decisive first audit.

Another investigation may be selected from the canonical landscapes only with an explicit mathematical advantage and stop condition.

## Investigation requirements

An investigation must maintain:

- `README.md` — scope and navigation;
- `STATUS.md` — current operational state;
- `CLAIMS.md` — authoritative local claim ledger;
- `VERTICAL-SLICES.md` — execution order, gates and stop conditions;
- `routes/` — distinct approaches kept separate once activated.

An investigation may be opened in formalization mode before a route is selected, but no route is active until its mechanism, theorem target, controls, complete complexity accounting and stop condition are recorded.

An investigation is not itself a claim that resolving the chosen problem by a particular method is the only route to P versus NP.
