from inspect import signature
from typing import get_type_hints

from atlas_core.contexts.interaction.domain.conversation_turn import ConversationTurn
from atlas_core.contexts.interaction.ports.conversation_repository import (
    ConversationRepositoryPort,
)


def test_conversation_repository_port_exposes_save_turn_operation() -> None:
    assert hasattr(ConversationRepositoryPort, "save_turn")


def test_save_turn_accepts_conversation_turn_argument() -> None:
    turn = ConversationTurn(
        session_id="session-123",
        user_utterance="Hello Atlas",
        assistant_reply="Hello Jordi",
    )

    save_turn_signature = signature(ConversationRepositoryPort.save_turn)
    parameters = list(save_turn_signature.parameters.values())

    assert len(parameters) == 2
    assert parameters[1].name == "turn"
    save_turn_signature.bind(object(), turn)


def test_save_turn_returns_none() -> None:
    save_turn_hints = get_type_hints(ConversationRepositoryPort.save_turn)

    assert save_turn_hints["return"] is type(None)


def test_save_turn_requires_conversation_turn_instance() -> None:
    save_turn_hints = get_type_hints(ConversationRepositoryPort.save_turn)

    assert save_turn_hints["turn"] is ConversationTurn


def test_conversation_repository_port_is_a_protocol_like_boundary() -> None:
    public_operations = [
        name
        for name, value in vars(ConversationRepositoryPort).items()
        if callable(value) and not name.startswith("_")
    ]

    assert public_operations == ["save_turn"]
