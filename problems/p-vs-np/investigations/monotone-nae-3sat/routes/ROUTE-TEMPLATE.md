# Route and Subroute Template

Use this structure whenever activating a new route or subroute.

## Required identity

```text
ID:
Name:
Parent route:
Operational status:
Primary claim IDs:
Dependencies:
```

## README.md

Every activated route or subroute README must state:

1. precise thesis;
2. represented mathematical object;
3. exact assumptions and quantifiers;
4. operations and correctness target;
5. binary encoding and size measure;
6. global computation-graph obligation;
7. mandatory controls;
8. first decisive attack;
9. stop and reopening conditions;
10. links to status, claims and evidence.

## STATUS.md

Required for every active route and any subroute with more than one execution slice.

Record:

- current operational state;
- accepted results;
- failed mechanisms;
- smallest unresolved gap;
- next decisive test;
- blocker and stop condition.

## CLAIMS.md

Required when the route introduces route-local claims or owns multiple investigation claims.

Every row must include:

- stable identifier;
- exact statement;
- mathematical status;
- review maturity;
- evidence;
- scope limitation.

## Recommended directories

Create only when they contain real records:

```text
proofs/
counterexamples/
audits/
experiments/
notes/
archive/
```

Do not create empty decorative trees.

## Route branching rule

A parent route and child mechanism are not the same claim.

When a child fails:

- close or disprove that child precisely;
- preserve retained lemmas and tools;
- keep the parent open if materially different mechanisms remain;
- record the handoff to the next sibling subroute.

## Promotion rule

A candidate becomes active only after it has one atomic conjecture or algorithm, exact operations, complete state accounting, hard controls, and a stop condition.