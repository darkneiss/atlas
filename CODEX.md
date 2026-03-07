# CODEX Guidelines

AI coding assistants working in this repository must follow these rules:

- Follow Hexagonal Architecture boundaries.
- Respect DDD bounded contexts and keep context ownership explicit.
- Keep framework and infrastructure code out of the domain layer.
- Enforce TDD workflow: write tests first, then implement, then refactor.
- Do not bypass ports/adapters for external dependencies.
- Update architecture and decision documentation when system structure changes.
