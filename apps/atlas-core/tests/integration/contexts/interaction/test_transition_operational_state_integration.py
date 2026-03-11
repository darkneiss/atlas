import pytest

from atlas_core.contexts.interaction.application.transition_operational_state import (
    TransitionOperationalState,
)
from atlas_core.contexts.interaction.domain.operational_state import (
    InvalidStateTransitionError,
    RobotOperationalState,
)
from atlas_core.contexts.interaction.ports.operational_state_store import (
    OperationalStateStorePort,
)


class InMemoryOperationalStateStore(OperationalStateStorePort):
    def __init__(self, initial_state: RobotOperationalState) -> None:
        self.state = initial_state
        self.state_history: list[RobotOperationalState] = []

    def set_state(self, state: RobotOperationalState) -> None:
        self.state = state
        self.state_history.append(state)

    def get_state(self) -> RobotOperationalState:
        return self.state


def test_transition_operational_state_persists_updated_state() -> None:
    # Arrange
    state_store = InMemoryOperationalStateStore(initial_state=RobotOperationalState.BOOTING)
    use_case = TransitionOperationalState(state_store=state_store)

    # Act
    result = use_case.execute(next_state=RobotOperationalState.IDLE)

    # Assert
    assert result is RobotOperationalState.IDLE
    assert state_store.state is RobotOperationalState.IDLE
    assert state_store.state_history == [RobotOperationalState.IDLE]


def test_multiple_transitions_are_applied_in_sequence() -> None:
    # Arrange
    state_store = InMemoryOperationalStateStore(initial_state=RobotOperationalState.BOOTING)
    use_case = TransitionOperationalState(state_store=state_store)

    # Act
    use_case.execute(next_state=RobotOperationalState.IDLE)
    use_case.execute(next_state=RobotOperationalState.LISTENING)
    use_case.execute(next_state=RobotOperationalState.THINKING)
    use_case.execute(next_state=RobotOperationalState.TALKING)
    use_case.execute(next_state=RobotOperationalState.IDLE)

    # Assert
    assert state_store.state is RobotOperationalState.IDLE
    assert state_store.state_history == [
        RobotOperationalState.IDLE,
        RobotOperationalState.LISTENING,
        RobotOperationalState.THINKING,
        RobotOperationalState.TALKING,
        RobotOperationalState.IDLE,
    ]


def test_invalid_transition_does_not_mutate_stored_state() -> None:
    # Arrange
    state_store = InMemoryOperationalStateStore(initial_state=RobotOperationalState.BOOTING)
    use_case = TransitionOperationalState(state_store=state_store)

    # Act / Assert
    with pytest.raises(InvalidStateTransitionError):
        use_case.execute(next_state=RobotOperationalState.TALKING)

    # Assert
    assert state_store.state is RobotOperationalState.BOOTING
    assert state_store.state_history == []
