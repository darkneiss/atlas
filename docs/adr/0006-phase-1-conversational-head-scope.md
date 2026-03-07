# ADR-0006: Phase 1 Conversational Head Scope

## Status
Accepted

## Context
Atlas is a long-term robotics project with multiple future capabilities, including embodiment, mobility, memory, automation, and physical interaction.

Without a clearly bounded first phase, the project risks early over-expansion, excessive architectural complexity, and delayed feedback.

A first phase is needed that is small enough to complete, but representative enough to validate the core direction of the project.

## Decision
Phase 1 of Atlas will focus on a conversational head architecture.

This phase will include:
- a Raspberry Pi based Atlas Core
- an Android-based Atlas Head device
- conversational interaction
- operational state management
- head expression rendering
- basic identity and personality configuration
- persistent conversation and memory foundations

This phase will not include:
- body mobility
- motor control
- ROS 2 integration
- navigation
- external automation tools
- scheduled autonomous behaviour
- advanced multimodal perception
- distributed multi-node execution as a required feature

Phase 1 will be treated as the foundation for later phases, but it must remain independently valuable and testable.

## Consequences

### Positive
- Reduces scope and delivery risk
- Enables early validation of interaction, identity, and memory
- Supports TDD with clear boundaries
- Keeps the system useful before robotics complexity is introduced
- Preserves future extensibility without committing to premature infrastructure

### Negative
- Atlas will not yet behave like a full embodied home robot
- Some future architectural decisions will remain deferred
- Certain integrations will need to be revisited in later phases

### Neutral
- This decision does not prevent future mobility, ROS 2, automation, or distributed execution
- The Android head remains a separate application even though phase 1 is otherwise a modular monolith
