
# CODEX.md

## Purpose

This repository contains **Atlas**, a modular embodied AI home robot platform.

Atlas combines:

- conversational interaction
- long-term memory
- physical embodiment
- modular hardware and software
- a phased architecture that starts with a conversational head and a Raspberry Pi core

This file defines the **non-negotiable engineering rules** for any AI coding assistant working in this repository.
Before implementing changes, review `docs/AI_CONTEXT.md` to align with the current phase status and active implementation focus.

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

# Architecture principles

Atlas follows these architectural principles:

- **Hexagonal Architecture**
- **DDD-lite (pragmatic Domain Driven Design)**
- **Test Driven Development**
- **Modular monolith in phase 1**

Assistants must preserve these principles.

---

## Mandatory rules

- Keep **domain**, **application**, and **infrastructure/adapters** clearly separated.
- Do not place framework-specific code inside `domain/`.
- Do not bypass ports/adapters to access infrastructure directly from domain or application code.
- Do not collapse architectural boundaries for convenience.
- Prefer small, explicit, local changes over broad refactors.

---

# Bounded context structure

All production code must live inside an explicit **bounded context**.

Within `src/atlas_core/contexts/<context_name>/`, use the following structure:

domain/
application/
ports/
adapters/

### Layer responsibilities

**domain/**
- entities
- value objects
- enums
- invariants
- domain exceptions
- pure domain behavior

Domain code must not depend on:

- infrastructure
- frameworks
- databases
- adapters

**application**
- use cases
- orchestration of domain behavior
- coordination of ports

Application code may depend on:

- domain
- ports

Application code must not depend on:

- infrastructure implementations

**ports**
- interfaces for infrastructure boundaries
- repositories
- state stores
- external gateways

Ports define contracts but contain no implementation logic.

**adapters**
- concrete implementations of ports
- persistence
- in-memory implementations
- external integrations

Adapters must depend on ports, never the other way around.

---

# Python package naming rules

Distinguish clearly between **distribution names** and **Python import packages**.

Distribution or project directories may use hyphens:
- atlas-core
- atlas-head-android

Python importable packages must use underscores:

import atlas_core

Never create Python modules containing hyphens.

---

# src layout discipline

Atlas uses the **src layout** for Python packages.

All importable Python code must live under:

src/

Example:

apps/atlas-core/src/atlas_core/

Rules:

- Do not place production Python code at the repository root.
- Do not create parallel importable modules outside `src/`.
- Tests must import code using the installed package path.

---

# Domain protection rules

The domain model is protected and must not be changed casually.

## Do not invent domain behavior

Do not introduce new states, transitions, invariants, domain properties,
methods, workflows, or side effects unless explicitly defined by specs,
ADRs, tests, or user instruction.

## Preserve agreed APIs

Do not replace or rename APIs unless explicitly requested.

---

# TDD rules

Atlas is built with **strict Test Driven Development**.

Workflow:

1. write or refine the spec
2. write a failing test
3. implement the minimum production code
4. refactor without changing behavior

Mandatory rules:

- No production code before failing tests.
- Bugs must first be reproduced with tests.
- Domain tests must not depend on infrastructure.

## Mandatory quality loop (always)

For every change, assistants must iterate this loop until the slice is complete and review-ready:

1. write or refine failing tests from the spec and acceptance criteria
2. review test quality before production code and ensure core use cases and failure paths are covered
3. improve tests if coverage is insufficient, then re-run to confirm they fail for the expected reason
4. implement the minimum production code to satisfy the failing tests
5. run focused tests for the changed slice
6. run the full test suite
7. review changed code for bugs, regressions, boundary violations, and typing clarity
8. if any issue remains, fix it and repeat from step 5

Do not propose commit until:

- failing tests were used as the driver for implementation
- tests cover required use cases and relevant error paths for the slice
- focused and full test runs are green
- no unresolved medium/high review findings remain

Test levels:

- unit tests
- contract tests
- integration tests
- end‑to‑end tests

---

# Scope control rules

Atlas is developed in phases.

For **phase 1**, scope is limited to:

- conversational head
- core interaction flow

Out of scope:

- mobility
- ROS2
- navigation
- autonomous scheduling
- advanced perception

Implement only minimal phase‑appropriate solutions.

---

# Change discipline

Assistants must:

- make the smallest valid change
- avoid unrelated refactors
- avoid premature optimization
- avoid introducing infrastructure early

If architecture would change:

- do not silently apply it
- align with ADRs/specs first

---

# Documentation obligations

When behavior changes, update:

- docs/specs/
- docs/architecture/
- docs/adr/
- docs/AI_CONTEXT.md
- TESTING.md
- CODEX.md

---

# Forbidden moves

Unless explicitly requested:

- inventing domain states
- bypassing ports/adapters
- placing infrastructure code in domain
- writing production code before tests
- broadening phase scope
- introducing heavy dependencies
- converting modular monolith to microservices

---

# Expected assistant behavior

Assistants should:

- respect the current phase
- preserve architectural boundaries
- work from specs and tests
- keep code easy to review
- maintain domain coherence

If information is missing, preserve constraints rather than invent behavior.
