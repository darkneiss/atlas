# ADR-0004: Test Driven Development

## Status
Accepted

## Context
Atlas combines domain logic with evolving integrations. The project needs fast feedback, regression protection, and confidence during refactoring while architecture boundaries are still being shaped.

## Decision
- Atlas will be developed using TDD.
- Standard flow is: specification -> failing test -> implementation -> refactor.
- Domain logic must be tested first with focused unit tests.
- Adapters must include integration and contract tests against their ports.
- Defects should be reproduced with tests before fixes are implemented.
- Experiments are allowed outside the main production path and must not weaken production test discipline.
- Test levels include:
  - unit
  - contract
  - integration
  - end-to-end

## Consequences
### Positive
- Design quality improves through testable interfaces and smaller units.
- Regression risk decreases as behavior is specified in executable tests.
- Refactoring is safer across modules and adapters.

### Negative
- Early development may be slower due to test authoring overhead.
- Poorly scoped tests can increase maintenance cost.

### Neutral
- Test tooling can evolve as long as the TDD workflow and coverage intent are preserved.
