from inspect import signature
from typing import get_type_hints

from atlas_core.contexts.interaction.domain.memory_fact import MemoryFact
from atlas_core.contexts.interaction.ports.memory_repository import MemoryRepositoryPort


def test_memory_repository_port_exposes_save_fact_operation() -> None:
    assert hasattr(MemoryRepositoryPort, "save_fact")


def test_save_fact_accepts_memory_fact_argument() -> None:
    fact = MemoryFact(source="user", confidence=0.9)

    save_fact_signature = signature(MemoryRepositoryPort.save_fact)
    parameters = list(save_fact_signature.parameters.values())

    assert len(parameters) == 2
    assert parameters[1].name == "fact"
    save_fact_signature.bind(object(), fact)


def test_save_fact_returns_none() -> None:
    save_fact_hints = get_type_hints(MemoryRepositoryPort.save_fact)

    assert save_fact_hints["return"] is type(None)


def test_save_fact_requires_memory_fact_instance() -> None:
    save_fact_hints = get_type_hints(MemoryRepositoryPort.save_fact)

    assert save_fact_hints["fact"] is MemoryFact


def test_memory_repository_port_exposes_only_expected_public_operation() -> None:
    public_operations = [
        name
        for name, value in vars(MemoryRepositoryPort).items()
        if callable(value) and not name.startswith("_")
    ]

    assert public_operations == ["save_fact"]
