
# AGENTS.md

## Purpose

This repository contains **Atlas**, a modular embodied AI home robot platform.

Atlas combines:

- conversational interaction
- long-term memory
- physical embodiment
- modular hardware and software
- a phased architecture that starts with a conversational head and a Raspberry Pi core

This file defines the **operational guidelines** for AI coding assistants working in this repository.
`CODEX.md` contains the strict architectural rules.
`AGENTS.md` summarizes the most important constraints and working patterns.
`docs/AI_CONTEXT.md` defines the current project context and phase focus and should be reviewed before implementing changes.

---

# Source of truth and decision priority

When making decisions, use this priority order:

1. direct user instructions
2. accepted ADRs in `docs/adr/`
3. feature specs in `docs/specs/`
4. project context in `docs/AI_CONTEXT.md`
5. existing tests
6. architecture documentation in `docs/architecture/`
7. repository rules in `CODEX.md` and `rules/`
8. local code style and surrounding code
9. assistant judgment

If a higher-priority source conflicts with a lower-priority source, follow the higher-priority source.

---

# Architecture overview

Atlas follows these architectural principles:

- **Hexagonal Architecture**
- **DDD-lite (pragmatic Domain Driven Design)**
- **Test Driven Development**
- **Modular monolith in phase 1**

Assistants must preserve these principles.

Key rule:

Production code must respect **clear architectural layers**.


atlas_core/contexts/<context>/
    domain/
    application/
    ports/
    adapters/


---

# Layer responsibilities

### domain

Contains:

- entities
- value objects
- enums
- invariants
- domain exceptions
- domain behavior

Domain code must **not depend on**:

- frameworks
- databases
- infrastructure
- adapters

---

### application

Contains:

- use cases
- orchestration of domain logic
- coordination of ports

Application code may depend on:

- domain
- ports

Application code must **not depend on infrastructure implementations**.

---

### ports

Ports define **interfaces for external systems**.

Examples:

- repositories
- state stores
- external gateways

Ports contain **contracts only**, no logic.

---

### adapters

Adapters implement ports.

Examples:

- in-memory implementations
- persistence adapters
- external service integrations

Adapters depend on ports, **never the other way around**.

---

# Python project layout

Atlas uses the **src layout**.

All importable Python code must live under:


apps/atlas-core/src/atlas_core/


Example structure:


apps/
  atlas-core/
    src/
      atlas_core/
        contexts/


Do not place production code at the repository root.

Tests must import code through the package path, not via relative imports.

---

# Naming rules

There is a difference between **distribution names** and **Python package names**.

Distribution names may use hyphens:


atlas-core
atlas-head-android


Python packages must use underscores:


atlas_core


Never create Python modules containing hyphens.

---

# TDD workflow

Atlas uses **strict Test Driven Development**.

Standard workflow:

1. write or refine the specification
2. write a failing test
3. implement the minimal code required
4. refactor without changing behavior

Rules:

- never write production code before tests
- reproduce bugs with tests first
- keep tests small and explicit
- keep domain tests independent from infrastructure

---

# Test levels

Use the correct testing level:

- **unit tests** → domain and application logic
- **contract tests** → ports and message schemas
- **integration tests** → adapters and persistence
- **end-to-end tests** → full system flows

---

# Scope control

Atlas is built in phases.

Current phase: **Phase 1 — Conversational Head**

Scope includes:

- interaction state machine
- conversational turns
- memory interfaces
- head expressions
- core orchestration logic

Out of scope unless explicitly requested:

- mobility
- navigation
- ROS2 integration
- motor control
- advanced perception
- distributed runtime

If something touches future scope, implement **minimal phase‑appropriate behavior only**.

---

# Change discipline

Assistants must:

- make the smallest valid change
- avoid unrelated refactors
- avoid premature infrastructure
- avoid introducing heavy dependencies
- preserve existing architecture

If a requested change would modify architecture or domain boundaries:

- align with ADRs
- do not silently change conventions

---

# Documentation alignment

When changing behavior, keep documentation aligned.

Update when necessary:

- `docs/specs/`
- `docs/architecture/`
- `docs/adr/`
- `docs/AI_CONTEXT.md`
- `TESTING.md`
- `CODEX.md`

---

# Expected assistant behavior

Assistants should:

- respect the current phase
- preserve architectural boundaries
- work from specs and tests
- avoid inventing domain behavior
- keep code easy to review
- prefer explicitness over magic

If information is missing, **preserve constraints rather than improvising behavior**.
