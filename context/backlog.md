# Backlog

## Phase 1 Prioritized Backlog

### Done

- Repository and architecture foundation completed.
- Core ADRs accepted for monorepo, hexagonal architecture, DDD-lite, TDD, and modular monolith phase 1.
- Interaction domain implemented for operational state model and head expression mapping.
- Interaction domain implemented for conversation turn model.
- Unit tests are green for the implemented interaction domain models.

### In Progress / Next

- Model `InteractionSession` in the interaction domain.
- Add unit tests for `InteractionSession`.
- Define `ConversationRepositoryPort`.
- Add contract tests for `ConversationRepositoryPort`.
- Implement first interaction use case.
- Add integration tests using in-memory adapters for the first interaction slice.

### Later in Phase 1

- Define memory persistence port and contract tests.
- Expand interaction flow coverage toward AC-005 to AC-008.
- Add phase-1 end-to-end conversational flow tests with mocked external boundaries.
