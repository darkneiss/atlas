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


def test_can_transition_from_listening_to_thinking() -> None:
    machine = OperationalStateMachine.initial()
    machine.transition_to(RobotOperationalState.IDLE)
    machine.transition_to(RobotOperationalState.LISTENING)

    machine.transition_to(RobotOperationalState.THINKING)

    assert machine.current_state is RobotOperationalState.THINKING


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
