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

---

## Source of truth and decision priority

When making decisions, use this priority order:

1. direct user instructions
2. accepted ADRs in `docs/adr/`
3. feature specs in `docs/specs/`
4. existing tests
5. architecture documentation in `docs/architecture/`
6. repository rules in `CODEX.md` and `rules/`
7. local code style and surrounding code
8. assistant judgment

If a higher-priority source conflicts with a lower-priority source, follow the higher-priority source.

---

## Architecture principles

Atlas follows these architectural principles:

- **Hexagonal Architecture**
- **DDD-lite (pragmatic Domain Driven Design)**
- **Test Driven Development**
- **Modular monolith in phase 1**

Assistants must preserve these principles.

### Mandatory rules

- Keep **domain**, **application**, and **infrastructure/adapters** clearly separated.
- Do not place framework-specific code inside `domain/`.
- Do not bypass ports/adapters to access infrastructure directly from domain or application code.
- Do not collapse architectural boundaries for convenience.
- Prefer small, explicit, local changes over broad refactors.

---

## Domain protection rules

The domain model is protected and must not be changed casually.

### Do not invent domain behavior

Do **not** introduce any of the following unless they are explicitly defined by the user, specs, ADRs, or tests:

- new states
- new transitions
- new invariants
- new domain properties
- new domain methods
- new workflows
- new side effects

If something is missing, do not silently invent it.

### Preserve agreed APIs

If the requested API is explicit, preserve it exactly.

Examples of forbidden changes unless explicitly requested:

- replacing a factory method with a constructor
- replacing a mutable API with an immutable one
- replacing an immutable API with a mutable one
- renaming domain concepts
- moving logic across bounded contexts without reason

---

## DDD-lite rules

Atlas uses **pragmatic DDD**, not ceremony-heavy DDD.

### Required

- use bounded contexts
- use ubiquitous language from docs/specs/ADR
- model behavior in the domain where appropriate
- keep names aligned with the domain language
- keep aggregates/entities/value objects simple and explicit

### Avoid

- unnecessary abstraction
- speculative patterns
- event sourcing unless explicitly decided
- CQRS unless explicitly decided
- artificial domain services without a real need
- over-modeling for future possibilities

---

## TDD rules

Atlas is built with **strict TDD** for production code.

### Required workflow

For any production behavior:

1. write or refine the spec if needed
2. write a failing test
3. implement the minimum production code required to pass
4. refactor without changing behavior

### Mandatory test rules

- Do not write production code before failing tests exist.
- Bugs should first be reproduced with a failing test.
- Tests must validate one behavior/rule at a time, except for simple parametrized mappings.
- Domain tests must not depend on infrastructure.
- Adapter behavior must be verified with integration and/or contract tests.

### Test levels

Use the appropriate level:

- **unit tests** for domain and application logic
- **contract tests** for ports and message schemas
- **integration tests** for adapters and persistence
- **end-to-end tests** for system flows

### Allowed exception

Spikes and experiments may exist in `experiments/`, but they must not be treated as production-ready code.

---

## Scope control rules

Atlas is developed in phases.

For **phase 1**, the scope is the conversational head and core interaction flow.

Do not silently broaden scope.

### Out of scope unless explicitly requested

- mobility
- navigation
- ROS2 integration
- hardware motor control
- autonomous tool execution
- scheduled autonomy
- advanced multimodal perception
- distributed multi-node runtime as a required feature

If a requested change touches future scope, keep the implementation minimal and phase-appropriate.

---

## Test design rules

### Preferred organization

- one test file per concept/module/responsibility
- multiple focused tests inside that file

### Avoid

- one file per single tiny test
- giant tests that validate many unrelated behaviors
- hidden setup that obscures intent

### Style

- keep tests small and explicit
- use clear arrange / act / assert structure
- prefer readability over cleverness
- use parametrization for mapping tables and equivalence sets

---

## Change discipline

### Smallest valid change

Assistants should make the smallest valid change that satisfies the request.

### Do not overreach

Do not:

- refactor unrelated code
- rename things without need
- add dependencies without clear justification
- introduce infrastructure early
- optimize prematurely

### If architecture would change

If a change would alter architecture, domain boundaries, or repository conventions:

- do not silently apply it
- align with existing ADRs/specs
- if needed, propose or require a new ADR/spec update first

---

## Documentation obligations

When changing behavior, keep documentation aligned.

Update the relevant files when necessary:

- `docs/specs/`
- `docs/architecture/`
- `docs/adr/`
- `docs/AI_CONTEXT.md`
- `TESTING.md`
- `CODEX.md`

Do not leave architecture-relevant changes undocumented.

---

## Forbidden moves

The following are forbidden unless explicitly requested:

- inventing domain states or transitions
- adding unapproved behavior
- bypassing ports/adapters
- placing infrastructure code in domain
- writing production code before tests
- silently broadening phase scope
- replacing requested APIs with “better” alternatives
- introducing heavy dependencies for small problems
- turning the modular monolith into microservices prematurely

---

## Expected assistant behavior

When modifying this repository, assistants should:

- respect the current phase
- preserve architectural boundaries
- work from specs and tests
- prefer explicitness over magic
- keep code easy to review
- keep the domain model coherent
- avoid hidden design decisions

If information is missing, prefer **preserving constraints** over improvising behavior.
