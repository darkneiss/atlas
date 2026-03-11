# Architecture Map

## Purpose

Provide a quick, up-to-date map of Atlas architecture for implementation and review work.

This document is a living snapshot and should be updated when bounded contexts, layer responsibilities, or implemented slices change.

## Phase and style

- Phase: 1 (Conversational Head)
- Architecture: Hexagonal
- Modeling approach: DDD-lite
- Delivery approach: strict TDD
- Deployment shape: modular monolith (phase 1)

## Layer dependency rules

- `domain` depends on nothing external (no frameworks, no persistence, no adapters)
- `application` depends on `domain` and `ports`
- `ports` define contracts only
- `adapters` implement ports and depend inward

Allowed direction:

`adapters -> ports <- application -> domain`

## Bounded context map (current)

Active context:

- `interaction`

Context layout:

```text
apps/atlas-core/src/atlas_core/contexts/interaction/
  domain/
  application/
  ports/
  adapters/   (reserved for future concrete implementations)
```

## Interaction context map (implemented)

### Domain

- `operational_state.py` (phase-1 conversational transitions + error/recovery path)
- `expression.py`
- `conversation_turn.py`
- `interaction_session.py`
- `memory_fact.py`

### Application

- `store_conversation_turn.py` (`StoreConversationTurn`)
- `transition_operational_state.py` (`TransitionOperationalState`)
- `publish_head_expression.py` (`PublishHeadExpression`)

### Ports (contracts)

- `conversation_repository.py` (`ConversationRepositoryPort`)
- `operational_state_store.py` (`OperationalStateStorePort`)
- `head_expression_output.py` (`HeadExpressionOutputPort`)
- `memory_repository.py` (`MemoryRepositoryPort`)

## Test map (implemented)

### Unit tests

- domain: operational state, expression mapping, conversation turn, interaction session, memory fact
- application: `StoreConversationTurn`, `TransitionOperationalState`, `PublishHeadExpression`

### Contract tests

- `ConversationRepositoryPort`
- `OperationalStateStorePort`
- `HeadExpressionOutputPort`
- `MemoryRepositoryPort`

### Integration tests

- conversation persistence slice:
  - `StoreConversationTurn` + in-test in-memory repository
- operational-state slice:
  - `TransitionOperationalState` + in-test in-memory state store
- head-expression output slice:
  - `PublishHeadExpression` + in-test output port

## Current slice status

Implemented slices:

- application receives input fields
- domain validates and creates `ConversationTurn`
- application persists via `ConversationRepositoryPort.save_turn(...)`
- application reads/persists operational state through `OperationalStateStorePort`
- domain validates state transitions through `OperationalStateMachine`
- application maps operational state to head expression and emits through `HeadExpressionOutputPort`

Next planned slice:

- first interaction orchestration use case combining conversation, state transition, and head-expression publication
