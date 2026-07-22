# Active verification scopes

This directory controls which research implementations participate in default local and continuous verification.

`active-paths` contains one scope identifier per line. Blank lines and lines beginning with `#` are ignored.

Current scope identifiers:

- `monotone-nae-3sat` — the active Monotone NAE-3SAT investigation laboratory.

## Lifecycle

A scope remains listed while research or implementation work is active.

Before removing a completed or deferred scope:

1. run its full gate on the exact final commit;
2. preserve canonical generated records, fixtures, commands, runtime versions, and mathematical audits;
3. synchronize `STATUS.md`, `CLAIMS.md`, route or investigation closeout records, and reopening conditions;
4. remove the scope from `active-paths` in the finalization change.

Removal retires the scope from routine local and CI execution. It does not delete or invalidate the evidence.

To reactivate a scope, record the reason for reopening, restore the identifier, audit dependency drift, and pass the full gate before promoting new claims.
