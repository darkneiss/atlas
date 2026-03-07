# ADR-0002: Hexagonal Architecture

## Status
Accepted

## Context
Atlas integrates multiple external technologies (LLM services, speech systems, storage engines, real-time transports, and hardware interfaces). The platform needs stable core behavior while these integrations evolve.

## Decision
- Atlas core will follow Hexagonal Architecture.
- Domain and application layers must remain isolated from infrastructure details.
- Ports and adapters are mandatory for all external interactions.
- Framework, transport, and vendor-specific code must not leak into the domain model.
- External integrations such as LLM, speech, storage, WebSocket, and hardware gateways are implemented as adapters.

## Consequences
### Positive
- Core behavior stays testable and stable despite infrastructure changes.
- Integrations can be replaced with limited impact on domain logic.
- Architectural boundaries are explicit and enforceable.

### Negative
- Additional interface design and adapter code increase initial development overhead.
- Teams must actively prevent boundary erosion over time.

### Neutral
- Specific frameworks and protocols can change without altering the architectural decision.
