# Current Sprint

## Goal

Deliver the next small phase-1 interaction slice from contract to integration, aligned with Hexagonal Architecture, DDD-lite, and TDD.

## Priorities (in order)

1. Define `MemoryRepositoryPort` as the next interaction boundary contract.
2. Add contract tests for `MemoryRepositoryPort`.
3. Create the first interaction orchestration use case combining current conversation and operational-state slices.
4. Add unit tests for orchestration behavior and failure paths.
5. Add an integration test for the orchestration slice using in-test adapters.
6. Extend flow coverage toward AC-005 to AC-008 in small increments.

## Out of Scope for This Slice

- real database
- external services
- ROS2
- mobility
- complex distributed runtime
