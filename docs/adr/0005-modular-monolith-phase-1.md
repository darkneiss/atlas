# ADR-0005: Modular Monolith for Phase 1

## Status
Accepted

## Context
Phase 1 targets a conversational head experience and Raspberry Pi core runtime. The system needs strong internal boundaries without distributed-system overhead during early product and architecture discovery.

## Decision
- Phase 1 backend will be implemented as a modular monolith.
- The Raspberry Pi/core runtime will start as one deployable backend.
- Internal modules must keep explicit boundaries aligned with bounded contexts.
- The Android head remains a separate application.
- Future extraction into services is permitted when justified by operational or scaling needs.
- Premature microservices adoption is explicitly avoided in phase 1.

## Consequences
### Positive
- Delivery is faster with lower operational complexity.
- Strong module boundaries can be enforced before distribution.
- Cross-module refactoring is simpler in early phases.

### Negative
- Without discipline, module boundaries can erode inside a single deployable.
- Independent scaling/deployment per module is limited.

### Neutral
- Service extraction remains a future option, not a current requirement.
