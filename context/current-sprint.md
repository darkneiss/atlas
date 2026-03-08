# Current Sprint

## Goal

Deliver the next small phase-1 interaction slice from contract to integration, aligned with Hexagonal Architecture, DDD-lite, and TDD.

## Priorities (in order)

1. Create the first operational-state application use case using `OperationalStateStorePort`.
2. Add unit tests for that use case.
3. Add a minimal integration test for that slice using an in-test in-memory store.
4. Define `MemoryRepositoryPort` as the next interaction boundary contract.
5. Add contract tests for `MemoryRepositoryPort`.
6. Extend interaction flow coverage toward AC-005 to AC-008 in small increments.

## Out of Scope for This Slice

- real database
- external services
- ROS2
- mobility
- complex distributed runtime
