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

### Application

- `store_conversation_turn.py` (`StoreConversationTurn`)

### Ports (contracts)

- `conversation_repository.py` (`ConversationRepositoryPort`)
- `operational_state_store.py` (`OperationalStateStorePort`)

## Test map (implemented)

### Unit tests

- domain: operational state, expression mapping, conversation turn, interaction session
- application: `StoreConversationTurn`

### Contract tests

- `ConversationRepositoryPort`
- `OperationalStateStorePort`

### Integration tests

- first interaction slice:
  - `StoreConversationTurn` + in-test in-memory repository

## Current slice status

Implemented slice:

- application receives input fields
- domain validates and creates `ConversationTurn`
- application persists via `ConversationRepositoryPort.save_turn(...)`

Next planned slice:

- operational-state application use case via `OperationalStateStorePort`
