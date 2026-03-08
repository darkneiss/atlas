import pytest

from atlas_core.contexts.interaction.application.store_conversation_turn import (
    StoreConversationTurn,
)
from atlas_core.contexts.interaction.domain.conversation_turn import ConversationTurn
from atlas_core.contexts.interaction.ports.conversation_repository import (
    ConversationRepositoryPort,
)


VALID_SESSION_ID = "session-123"
VALID_USER_UTTERANCE = "Hello Atlas"
VALID_ASSISTANT_REPLY = "Hello Jordi"


class SpyConversationRepository(ConversationRepositoryPort):
    """Simple spy to observe application-layer interaction with the port boundary."""

    def __init__(self) -> None:
        self.saved_turns: list[ConversationTurn] = []
        self.save_turn_calls: int = 0

    def save_turn(self, turn: ConversationTurn) -> None:
        self.save_turn_calls += 1
        self.saved_turns.append(turn)


def test_store_conversation_turn_creates_and_returns_conversation_turn() -> None:
    # Arrange
    repository = SpyConversationRepository()
    use_case = StoreConversationTurn(repository=repository)

    # Act
    result = use_case.execute(
        session_id=VALID_SESSION_ID,
        user_utterance=VALID_USER_UTTERANCE,
        assistant_reply=VALID_ASSISTANT_REPLY,
    )

    # Assert
    assert isinstance(result, ConversationTurn)
    assert repository.save_turn_calls == 1
    assert len(repository.saved_turns) == 1
    assert repository.saved_turns[0] is result
    assert result.session_id == VALID_SESSION_ID
    assert result.user_utterance == VALID_USER_UTTERANCE
    assert result.assistant_reply == VALID_ASSISTANT_REPLY


def test_store_conversation_turn_persists_created_turn() -> None:
    # Arrange
    repository = SpyConversationRepository()
    use_case = StoreConversationTurn(repository=repository)

    # Act
    result = use_case.execute(
        session_id=VALID_SESSION_ID,
        user_utterance=VALID_USER_UTTERANCE,
        assistant_reply=VALID_ASSISTANT_REPLY,
    )

    # Assert
    assert repository.save_turn_calls == 1
    assert len(repository.saved_turns) == 1
    saved_turn = repository.saved_turns[0]
    assert saved_turn is result


def test_store_conversation_turn_strips_input_before_persisting() -> None:
    # Arrange
    repository = SpyConversationRepository()
    use_case = StoreConversationTurn(repository=repository)

    # Act
    use_case.execute(
        session_id="  session-123  ",
        user_utterance="  Hello Atlas  ",
        assistant_reply="  Hello Jordi  ",
    )

    # Assert
    assert repository.save_turn_calls == 1
    assert len(repository.saved_turns) == 1
    saved_turn = repository.saved_turns[0]
    assert saved_turn.session_id == VALID_SESSION_ID
    assert saved_turn.user_utterance == VALID_USER_UTTERANCE
    assert saved_turn.assistant_reply == VALID_ASSISTANT_REPLY


def test_store_conversation_turn_propagates_validation_error_from_domain() -> None:
    # Arrange
    repository = SpyConversationRepository()
    use_case = StoreConversationTurn(repository=repository)

    # Act / Assert
    with pytest.raises(ValueError):
        use_case.execute(
            session_id=VALID_SESSION_ID,
            user_utterance=VALID_USER_UTTERANCE,
            assistant_reply="   ",
        )

    # Assert
    assert repository.save_turn_calls == 0
    assert repository.saved_turns == []


def test_store_conversation_turn_uses_repository_port_boundary() -> None:
    # Arrange
    spy_repository = SpyConversationRepository()
    repository_boundary: ConversationRepositoryPort = spy_repository
    use_case = StoreConversationTurn(repository=repository_boundary)

    # Act
    result = use_case.execute(
        session_id=VALID_SESSION_ID,
        user_utterance=VALID_USER_UTTERANCE,
        assistant_reply=VALID_ASSISTANT_REPLY,
    )

    # Assert
    assert spy_repository.save_turn_calls == 1
    assert len(spy_repository.saved_turns) == 1
    assert spy_repository.saved_turns[0] is result
