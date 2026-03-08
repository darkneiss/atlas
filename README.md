# Atlas

Atlas is a modular embodied AI home robot platform combining conversational intelligence, long-term memory, and physical interaction.

## Overview

Atlas is designed as a long-lived robotics platform that can evolve from a modular monolith into a distributed system as hardware and software capabilities grow.

## Architecture principles

- Hexagonal Architecture
- Domain-Driven Design (DDD) with bounded contexts
- Modular monolith in early phases
- Clear ports/adapters boundaries for external integrations

## Development approach

- Test Driven Development (TDD)
- Monorepo organization for coordinated delivery
- Documentation-first architecture decisions through ADRs
- Incremental robotics integration (ROS2, hardware, sensors)

## Repository structure

Key areas:

- `apps/`: deployable applications and device-specific runtimes
- `docs/`: architecture, ADRs, and feature specifications
- `rules/`: engineering and AI assistant operating rules
- `context/`: project state, backlog, and hardware context
- `infrastructure/`, `tools/`, `experiments/`, `tests/`: platform support and validation areas

## Documentation entry points

- `docs/AI_CONTEXT.md`: current project context and phase focus
- `docs/architecture/ARCHITECTURE_MAP.md`: architecture map and implemented slices
- `docs/specs/phase-01/conversational-head.md`: active phase-1 functional specification
- `docs/adr/README.md`: architecture decision records index
- `context/current-sprint.md`: current iteration priorities
