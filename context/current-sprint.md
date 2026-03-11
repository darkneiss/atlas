# Current Sprint

## Goal

Deliver the next small phase-1 interaction slice from contract to integration, aligned with Hexagonal Architecture, DDD-lite, and TDD.

## Priorities (in order)

1. Create the first interaction orchestration use case combining current conversation and operational-state slices.
2. Add unit tests for orchestration behavior and failure paths.
3. Add an integration test for the orchestration slice using in-test adapters.
4. Integrate memory fact persistence through `MemoryRepositoryPort` in the orchestration flow.
5. Add tests for memory persistence failures surfaced as error or degraded result.
6. Extend flow coverage toward AC-005 to AC-008 in small increments.

## Out of Scope for This Slice

- real database
- external services
- ROS2
- mobility
- complex distributed runtime
