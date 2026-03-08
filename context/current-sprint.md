# Current Sprint

## Goal

Deliver one small phase-1 slice from domain to integration, aligned with Hexagonal Architecture, DDD-lite, and TDD.

## Priorities (in order)

1. Model `InteractionSession` in the interaction domain.
2. Add unit tests for `InteractionSession`.
3. Define `ConversationRepositoryPort`.
4. Add contract tests for `ConversationRepositoryPort`.
5. Create the first interaction use case.
6. Add integration tests using in-memory adapters.

## Out of Scope for This Slice

- real database
- external services
- ROS2
- mobility
- complex distributed runtime
