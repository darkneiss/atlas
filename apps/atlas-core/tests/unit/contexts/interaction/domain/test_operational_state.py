import pytest

from atlas_core.contexts.interaction.domain.expression import HeadExpression
from atlas_core.contexts.interaction.domain.operational_state import (
    InvalidStateTransitionError,
    OperationalStateMachine,
    RobotOperationalState,
)


def test_initial_state_is_booting() -> None:
    machine = OperationalStateMachine.initial()

    assert machine.current_state is RobotOperationalState.BOOTING


def test_state_machine_cannot_be_created_directly_with_non_booting_state() -> None:
    with pytest.raises(ValueError):
        OperationalStateMachine(RobotOperationalState.IDLE)


def test_state_machine_can_be_rehydrated_from_existing_state() -> None:
    machine = OperationalStateMachine.rehydrate(RobotOperationalState.THINKING)

    assert machine.current_state is RobotOperationalState.THINKING


def test_state_machine_can_be_rehydrated_from_valid_serialized_state() -> None:
    machine = OperationalStateMachine.rehydrate("THINKING")

    assert machine.current_state is RobotOperationalState.THINKING


def test_rehydrate_rejects_invalid_serialized_state() -> None:
    with pytest.raises(ValueError):
        OperationalStateMachine.rehydrate("UNKNOWN")


def test_rehydrated_state_machine_keeps_transition_rules() -> None:
    machine = OperationalStateMachine.rehydrate(RobotOperationalState.THINKING)

    machine.transition_to(RobotOperationalState.TALKING)

    assert machine.current_state is RobotOperationalState.TALKING


def test_can_transition_from_booting_to_idle() -> None:
    machine = OperationalStateMachine.initial()

    machine.transition_to(RobotOperationalState.IDLE)

    assert machine.current_state is RobotOperationalState.IDLE


def test_cannot_transition_from_idle_to_talking_without_reply_ready() -> None:
    machine = OperationalStateMachine.initial()
    machine.transition_to(RobotOperationalState.IDLE)

    with pytest.raises(InvalidStateTransitionError):
        machine.transition_to(RobotOperationalState.TALKING)

    assert machine.current_state is RobotOperationalState.IDLE


def test_transition_to_rejects_non_operational_state_value() -> None:
    machine = OperationalStateMachine.initial()

    with pytest.raises(ValueError):
        machine.transition_to("IDLE")  # type: ignore[arg-type]

    assert machine.current_state is RobotOperationalState.BOOTING


def test_can_transition_from_listening_to_thinking() -> None:
    machine = OperationalStateMachine.initial()
    machine.transition_to(RobotOperationalState.IDLE)
    machine.transition_to(RobotOperationalState.LISTENING)

    machine.transition_to(RobotOperationalState.THINKING)

    assert machine.current_state is RobotOperationalState.THINKING


def test_can_transition_from_thinking_to_talking() -> None:
    machine = OperationalStateMachine.initial()
    machine.transition_to(RobotOperationalState.IDLE)
    machine.transition_to(RobotOperationalState.LISTENING)
    machine.transition_to(RobotOperationalState.THINKING)

    machine.transition_to(RobotOperationalState.TALKING)

    assert machine.current_state is RobotOperationalState.TALKING


def test_can_transition_from_talking_to_idle() -> None:
    machine = OperationalStateMachine.initial()
    machine.transition_to(RobotOperationalState.IDLE)
    machine.transition_to(RobotOperationalState.LISTENING)
    machine.transition_to(RobotOperationalState.THINKING)
    machine.transition_to(RobotOperationalState.TALKING)

    machine.transition_to(RobotOperationalState.IDLE)

    assert machine.current_state is RobotOperationalState.IDLE


@pytest.mark.parametrize(
    "transition_sequence",
    [
        pytest.param(
            (
                RobotOperationalState.IDLE,
                RobotOperationalState.LISTENING,
                RobotOperationalState.ERROR,
            ),
            id="from_listening",
        ),
        pytest.param(
            (
                RobotOperationalState.IDLE,
                RobotOperationalState.LISTENING,
                RobotOperationalState.THINKING,
                RobotOperationalState.ERROR,
            ),
            id="from_thinking",
        ),
        pytest.param(
            (
                RobotOperationalState.IDLE,
                RobotOperationalState.LISTENING,
                RobotOperationalState.THINKING,
                RobotOperationalState.TALKING,
                RobotOperationalState.ERROR,
            ),
            id="from_talking",
        ),
    ],
)
def test_can_transition_to_error_from_any_active_state(
    transition_sequence: tuple[RobotOperationalState, ...],
) -> None:
    machine = OperationalStateMachine.initial()

    for state in transition_sequence:
        machine.transition_to(state)

    assert machine.current_state is RobotOperationalState.ERROR


def test_can_recover_from_error_to_idle() -> None:
    machine = OperationalStateMachine.initial()
    machine.transition_to(RobotOperationalState.IDLE)
    machine.transition_to(RobotOperationalState.LISTENING)
    machine.transition_to(RobotOperationalState.ERROR)

    machine.transition_to(RobotOperationalState.IDLE)

    assert machine.current_state is RobotOperationalState.IDLE


@pytest.mark.parametrize(
    ("state", "expected_expression"),
    [
        (RobotOperationalState.IDLE, HeadExpression.IDLE),
        (RobotOperationalState.LISTENING, HeadExpression.LISTENING),
        (RobotOperationalState.THINKING, HeadExpression.THINKING),
        (RobotOperationalState.TALKING, HeadExpression.TALKING),
        (RobotOperationalState.SLEEPING, HeadExpression.SLEEPING),
        (RobotOperationalState.ERROR, HeadExpression.ERROR),
    ],
)
def test_operational_state_maps_to_matching_head_expression(
    state: RobotOperationalState,
    expected_expression: HeadExpression,
) -> None:
    expression = HeadExpression.from_operational_state(state)

    assert expression is expected_expression
