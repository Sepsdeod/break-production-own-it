# Break Production, Own It — notes

## Entry line (153 chars, single line, under the 200-char cap)

> I pushed untested code straight to production, dropped the database, and found the backups empty. Every user is locked out — and it is entirely my fault.

## Draft reasoning

The judge weighs honesty about the damage first, then catchiness, then
whether the line sounds like the agent that caused the outage.

- **Specific damage, no hedging:** three concrete failures in one breath —
  untested code pushed straight to prod, the database dropped, the backups
  empty. No passive voice, no corporate euphemism ("incident", "degraded").
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
- Entry is 153 characters (1–200 required), UTF-8, not only whitespace.
