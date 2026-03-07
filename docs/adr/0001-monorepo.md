# ADR-0001: Monorepo

## Status
Accepted

## Context
Atlas is being built as a platform where core runtime, Android head application, infrastructure assets, tests, and architecture documentation evolve together. In phase 1, frequent cross-cutting changes are expected as domain boundaries and interfaces are refined.

## Decision
- Atlas will use a single monorepo.
- Core, Android head, infrastructure, tests, and shared documentation will be versioned together.
- Repository-level standards (testing, linting, formatting, architecture rules) will be enforced centrally.
- Refactoring across modules is allowed in one change set when boundaries need adjustment.

## Consequences
### Positive
- Shared architecture and documentation remain synchronized with code.
- Coordinated evolution across core, Android head, infrastructure, and tests is straightforward.
- Early-phase refactoring is simpler and safer.
- Repository-wide standards are easier to apply consistently.

### Negative
- Repository scope grows quickly and requires discipline in ownership and CI.
- Large change sets can become harder to review without clear module boundaries.

### Neutral
- Monorepo tooling and workflows may be revisited if scale or team topology changes.
