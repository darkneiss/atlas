import pytest

from atlas_core.contexts.interaction.application.store_conversation_turn import (
    StoreConversationTurn,
)
from atlas_core.contexts.interaction.domain.conversation_turn import ConversationTurn
from atlas_core.contexts.interaction.ports.conversation_repository import (
    ConversationRepositoryPort,
)


class InMemoryConversationRepository(ConversationRepositoryPort):
    def __init__(self) -> None:
        self.turns: list[ConversationTurn] = []

    def save_turn(self, turn: ConversationTurn) -> None:
        self.turns.append(turn)


def test_store_conversation_turn_persists_turn_in_repository() -> None:
    # Arrange
    repository = InMemoryConversationRepository()
    use_case = StoreConversationTurn(repository=repository)

    # Act
    use_case.execute(
        session_id="session-123",
        user_utterance="Hello Atlas",
        assistant_reply="Hello Jordi",
    )

    # Assert
    assert len(repository.turns) == 1
    stored_turn = repository.turns[0]
    assert stored_turn.session_id == "session-123"
    assert stored_turn.user_utterance == "Hello Atlas"
    assert stored_turn.assistant_reply == "Hello Jordi"


def test_multiple_turns_are_stored_in_sequence() -> None:
    # Arrange
    repository = InMemoryConversationRepository()
    use_case = StoreConversationTurn(repository=repository)

    # Act
    use_case.execute(
        session_id="session-123",
        user_utterance="Hello Atlas",
        assistant_reply="Hello Jordi",
    )
    use_case.execute(
        session_id="session-123",
        user_utterance="How are you?",
        assistant_reply="I am operational.",
    )

    # Assert
    assert len(repository.turns) == 2
    assert repository.turns[0].user_utterance == "Hello Atlas"
    assert repository.turns[1].user_utterance == "How are you?"


def test_integration_preserves_domain_validation_rules() -> None:
    # Arrange
    repository = InMemoryConversationRepository()
    use_case = StoreConversationTurn(repository=repository)

    # Act / Assert
    with pytest.raises(ValueError):
        use_case.execute(
            session_id="session-123",
            user_utterance="Hello Atlas",
            assistant_reply="   ",
        )

    # Assert
    assert repository.turns == []
