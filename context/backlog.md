# Backlog

## Phase 1 Prioritized Backlog

### Done

- Repository and architecture foundation completed.
- Core ADRs accepted for monorepo, hexagonal architecture, DDD-lite, TDD, and modular monolith phase 1.
- Interaction domain implemented for operational state model and head expression mapping.
- Operational-state domain transitions expanded for AC-003/AC-007/AC-008 at unit-test level.
- Interaction domain implemented for conversation turn model.
- Interaction domain implemented for interaction session model.
- `StoreConversationTurn` application use case implemented.
- `ConversationRepositoryPort` contract and tests implemented.
- `OperationalStateStorePort` contract and tests implemented.
- First integration slice implemented for storing conversation turns.
- Unit, contract, and current integration tests are green for implemented slices.

### In Progress / Next

- Implement first operational-state application use case through `OperationalStateStorePort`.
- Add unit tests for that operational-state use case.
- Add integration test for the operational-state slice with in-test in-memory store.
- Define `MemoryRepositoryPort` and its contract tests.

### Later in Phase 1

- Expand interaction flow coverage toward AC-005/AC-006 and application-level handling of AC-007/AC-008.
- Add additional integration slices for interaction orchestration.
- Add phase-1 end-to-end conversational flow tests with mocked external boundaries.
