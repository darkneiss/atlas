import pytest

from atlas_core.contexts.interaction.domain.memory_fact import MemoryFact


def test_can_create_memory_fact_with_valid_data() -> None:
    fact = MemoryFact(source="user", confidence=0.8)

    assert fact.source == "user"
    assert fact.confidence == 0.8


def test_memory_fact_strips_source() -> None:
    fact = MemoryFact(source="  user  ", confidence=0.5)

    assert fact.source == "user"


def test_cannot_create_memory_fact_with_blank_source() -> None:
    with pytest.raises(ValueError):
        MemoryFact(source="   ", confidence=0.7)


def test_cannot_create_memory_fact_with_non_string_source() -> None:
    with pytest.raises(ValueError):
        MemoryFact(source=None, confidence=0.7)  # type: ignore[arg-type]


def test_cannot_create_memory_fact_with_confidence_below_zero() -> None:
    with pytest.raises(ValueError):
        MemoryFact(source="user", confidence=-0.01)


def test_cannot_create_memory_fact_with_confidence_above_one() -> None:
    with pytest.raises(ValueError):
        MemoryFact(source="user", confidence=1.01)


@pytest.mark.parametrize("confidence", [0.0, 1.0])
def test_can_create_memory_fact_with_confidence_boundaries(confidence: float) -> None:
    fact = MemoryFact(source="system", confidence=confidence)

    assert fact.confidence == confidence


def test_cannot_create_memory_fact_with_nan_confidence() -> None:
    with pytest.raises(ValueError):
        MemoryFact(source="user", confidence=float("nan"))


@pytest.mark.parametrize("confidence", ["0.8", True])
def test_cannot_create_memory_fact_with_non_numeric_confidence(
    confidence: object,
) -> None:
    with pytest.raises(ValueError):
        MemoryFact(source="user", confidence=confidence)  # type: ignore[arg-type]
