# Project Context

Atlas is in phase-1 conversational-head development.

Current implemented baseline in `atlas-core`:

- interaction domain models: operational state, head expression mapping, conversation turn, interaction session
- interaction application use case: `StoreConversationTurn`
- interaction port contracts: conversation repository and operational state store
- unit/contract tests plus first integration slice for conversation persistence behavior

Execution constraints:

- keep strict hexagonal boundaries (`domain`, `application`, `ports`, `adapters`)
- keep DDD-lite bounded context ownership
- keep incremental TDD slices
