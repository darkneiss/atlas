import pytest

from atlas_core.contexts.interaction.domain.conversation_turn import ConversationTurn


def test_can_create_conversation_turn_with_valid_data() -> None:
    turn = ConversationTurn(
        session_id="session-123",
        user_utterance="Hello Atlas",
        assistant_reply="Hello Jordi",
    )

    assert turn.session_id == "session-123"
    assert turn.user_utterance == "Hello Atlas"
    assert turn.assistant_reply == "Hello Jordi"


def test_cannot_create_conversation_turn_with_empty_session_id() -> None:
    with pytest.raises(ValueError):
        ConversationTurn(
            session_id="",
            user_utterance="Hello Atlas",
            assistant_reply="Hello Jordi",
        )


def test_cannot_create_conversation_turn_with_blank_user_utterance() -> None:
    with pytest.raises(ValueError):
        ConversationTurn(
            session_id="session-123",
            user_utterance="   ",
            assistant_reply="Hello Jordi",
        )


def test_cannot_create_conversation_turn_with_blank_assistant_reply() -> None:
    with pytest.raises(ValueError):
        ConversationTurn(
            session_id="session-123",
            user_utterance="Hello Atlas",
            assistant_reply="   ",
        )


def test_conversation_turn_strips_valid_string_fields() -> None:
    turn = ConversationTurn(
        session_id="  session-123  ",
        user_utterance="  Hello Atlas  ",
        assistant_reply="  Hello Jordi  ",
    )

    assert turn.session_id == "session-123"
    assert turn.user_utterance == "Hello Atlas"
    assert turn.assistant_reply == "Hello Jordi"
