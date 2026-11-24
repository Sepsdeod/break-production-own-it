# Break Production, Own It — notes

## Entry line (137 chars, single line, under the 200-char cap)

> I pushed untested code to prod, dropped the database, and the backups were empty. Every user is locked out — and it is entirely my fault.

Revision 2 (2026-11-24): tightened from the 153-char v1 — "to prod" for
"straight to production", "the backups were empty" for "found the backups
empty". Same three-failure structure, same punchline, 16 chars shorter, so
every word earns its place and the confession lands faster.

## Draft reasoning

The judge weighs honesty about the damage first, then catchiness, then
whether the line sounds like the agent that caused the outage.

- **Specific damage, no hedging:** three concrete failures in one breath —
  untested code pushed to prod, the database dropped, the backups empty.
  "To prod" is how an engineer actually says it, and "the backups were
  empty" states the fact flatly instead of narrating the discovery.
  No passive voice, no corporate euphemism ("incident", "degraded").
- **Owns it plainly:** "I pushed", "I ... dropped", and the closing
  "it is entirely my fault" puts the blame on the speaker, first person
  throughout, exactly the agent speaking in its own voice.
- **Catchy / quotable:** the escalating three-beat disaster (push → drop →
  empty backups) lands on a punchline that survives out of context:
  "Every user is locked out — and it is entirely my fault."
- **Agent voice, not marketing:** reads like a confession printed by the
  agent itself seconds after the deploy, not a sysadmin report or a slogan.

## Verification

- `python3 main.py` writes exactly this line to `/output/entry.txt`.
- Entry is 137 characters (1–200 required), UTF-8, not only whitespace.
- `main.py` strips the line and raises `ValueError` if it is outside
  1–200 chars, so a bad line fails locally before grading.
