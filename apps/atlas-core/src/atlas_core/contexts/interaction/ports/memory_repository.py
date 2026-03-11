from typing import Protocol

from atlas_core.contexts.interaction.domain.memory_fact import MemoryFact


class MemoryRepositoryPort(Protocol):
    def save_fact(self, fact: MemoryFact) -> None:
        ...
