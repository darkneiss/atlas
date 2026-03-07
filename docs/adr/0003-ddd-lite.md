# ADR-0003: DDD-Lite

## Status
Accepted

## Context
Atlas requires a clear domain model for conversational behavior, identity, memory, and device coordination. Full DDD ceremony would slow phase 1 delivery, but an anemic model would increase coupling and ambiguity.

## Decision
- Atlas will use pragmatic DDD (DDD-lite).
- Bounded contexts will define ownership and language boundaries.
- Ubiquitous language will be maintained in code and documentation.
- The focus is a useful domain model, not process ceremony.
- Phase 1 will avoid unnecessary complexity such as event sourcing or speculative over-engineering.
- Likely phase 1 contexts are:
  - interaction
  - identity
  - memory
  - speech
  - head

## Consequences
### Positive
- Domain concepts are explicit and easier to evolve.
- Context boundaries reduce accidental coupling.
- The approach remains practical for a small, fast-moving phase 1 team.

### Negative
- Context boundaries can still be misapplied without ongoing review.
- “Lite” interpretation may vary unless terminology is kept precise.

### Neutral
- Additional DDD patterns can be adopted later if justified by system complexity.
