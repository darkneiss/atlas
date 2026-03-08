import pytest

from atlas_core.contexts.interaction.domain.interaction_session import InteractionSession


def test_can_create_interaction_session_with_valid_data() -> None:
    session = InteractionSession(session_id="session-123", status="ACTIVE")

    assert session.session_id == "session-123"
    assert session.status == "ACTIVE"


def test_cannot_create_interaction_session_with_empty_session_id() -> None:
    with pytest.raises(ValueError):
        InteractionSession(session_id="", status="ACTIVE")


def test_cannot_create_interaction_session_with_blank_status() -> None:
    with pytest.raises(ValueError):
        InteractionSession(session_id="session-123", status="   ")


def test_interaction_session_strips_valid_string_fields() -> None:
    session = InteractionSession(session_id="  session-123  ", status="  ACTIVE  ")

    assert session.session_id == "session-123"
    assert session.status == "ACTIVE"


def test_interaction_session_accepts_different_valid_status_values() -> None:
    active_session = InteractionSession(session_id="session-123", status="ACTIVE")
    completed_session = InteractionSession(session_id="session-456", status="COMPLETED")

    assert active_session.status == "ACTIVE"
    assert completed_session.status == "COMPLETED"
