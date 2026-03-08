# AI Context

## Purpose

This document is a living summary of Atlas project context.

Update it when phase focus, implemented capabilities, or architectural boundaries change.

## Project vision

Atlas is a modular embodied AI home robot platform combining conversational intelligence, long-term memory, and physical interaction.

## Current phase

Phase 1: Conversational Head (Raspberry Pi core + Android head).

Repository and architecture foundation are complete, and early interaction slice implementation is in progress.

## Architecture baseline

- Hexagonal Architecture
- DDD-lite with bounded contexts
- Strict TDD
- Modular monolith for phase 1
- Monorepo organization

## Implemented interaction slice (current)

### Domain

- Operational state model (`RobotOperationalState`, `OperationalStateMachine`)
- Head expression mapping (`HeadExpression.from_operational_state(...)`)
- Conversation turn model (`ConversationTurn`)
- Interaction session model (`InteractionSession`)

### Application

- `StoreConversationTurn` use case

### Ports (contracts)

- `ConversationRepositoryPort` (`save_turn(...)`)
- `OperationalStateStorePort` (`set_state(...)`, `get_state()`)

### Tests available

- Unit tests for domain and first application use case
- Contract tests for interaction ports
- First integration test for conversation store slice (application -> domain -> port)

## Current focus

- Keep expanding phase-1 interaction flow in small vertical slices
- Preserve strict domain/application/ports boundaries
- Add contracts and integration tests before introducing concrete adapters

## Out of scope in current phase

- ROS2 integration
- Mobility and motor control
- Navigation
- Advanced multimodal perception
- Distributed runtime as a required capability

## Hardware context

- Raspberry Pi 4: core runtime target
- Android phone: conversational head device
