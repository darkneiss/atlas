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


class SpyOperationalStateStore(OperationalStateStorePort):
    def __init__(self, initial_state: RobotOperationalState) -> None:
        self.state = initial_state
        self.get_state_calls = 0
        self.set_state_calls = 0
        self.set_state_arguments: list[RobotOperationalState] = []

    def set_state(self, state: RobotOperationalState) -> None:
        self.set_state_calls += 1
        self.set_state_arguments.append(state)
        self.state = state

    def get_state(self) -> RobotOperationalState:
        self.get_state_calls += 1
        return self.state


def test_transition_operational_state_creates_and_returns_next_state() -> None:
    # Arrange
    state_store = SpyOperationalStateStore(initial_state=RobotOperationalState.BOOTING)
    use_case = TransitionOperationalState(state_store=state_store)

    # Act
    result = use_case.execute(next_state=RobotOperationalState.IDLE)

    # Assert
    assert result is RobotOperationalState.IDLE
    assert state_store.state is RobotOperationalState.IDLE
    assert state_store.set_state_arguments == [RobotOperationalState.IDLE]


def test_transition_operational_state_persists_state_through_store_port() -> None:
    # Arrange
    state_store = SpyOperationalStateStore(initial_state=RobotOperationalState.BOOTING)
    use_case = TransitionOperationalState(state_store=state_store)

    # Act
    use_case.execute(next_state=RobotOperationalState.IDLE)

    # Assert
    assert state_store.set_state_calls == 1
    assert state_store.set_state_arguments == [RobotOperationalState.IDLE]


def test_transition_operational_state_reads_current_state_from_store() -> None:
    # Arrange
    state_store = SpyOperationalStateStore(initial_state=RobotOperationalState.BOOTING)
    use_case = TransitionOperationalState(state_store=state_store)

    # Act
    use_case.execute(next_state=RobotOperationalState.IDLE)

    # Assert
    assert state_store.get_state_calls == 1
    assert state_store.set_state_calls == 1


@pytest.mark.parametrize(
    ("current_state", "next_state"),
    [
        pytest.param(
            RobotOperationalState.BOOTING,
            RobotOperationalState.IDLE,
            id="booting_to_idle",
        ),
        pytest.param(
            RobotOperationalState.IDLE,
            RobotOperationalState.LISTENING,
            id="idle_to_listening",
        ),
        pytest.param(
            RobotOperationalState.LISTENING,
            RobotOperationalState.THINKING,
            id="listening_to_thinking",
        ),
        pytest.param(
            RobotOperationalState.THINKING,
            RobotOperationalState.TALKING,
            id="thinking_to_talking",
        ),
        pytest.param(
            RobotOperationalState.TALKING,
            RobotOperationalState.IDLE,
            id="talking_to_idle",
        ),
        pytest.param(
            RobotOperationalState.LISTENING,
            RobotOperationalState.ERROR,
            id="listening_to_error",
        ),
        pytest.param(
            RobotOperationalState.THINKING,
            RobotOperationalState.ERROR,
            id="thinking_to_error",
        ),
        pytest.param(
            RobotOperationalState.TALKING,
            RobotOperationalState.ERROR,
            id="talking_to_error",
        ),
        pytest.param(
            RobotOperationalState.ERROR,
            RobotOperationalState.IDLE,
            id="error_to_idle",
        ),
    ],
)
def test_transition_operational_state_supports_phase1_valid_transitions(
    current_state: RobotOperationalState,
    next_state: RobotOperationalState,
) -> None:
    # Arrange
    state_store = SpyOperationalStateStore(initial_state=current_state)
    use_case = TransitionOperationalState(state_store=state_store)

    # Act
    result = use_case.execute(next_state=next_state)

    # Assert
    assert result is next_state
    assert state_store.state is next_state
    assert state_store.set_state_arguments[-1] is next_state


@pytest.mark.parametrize(
    ("current_state", "next_state"),
    [
        pytest.param(
            RobotOperationalState.BOOTING,
            RobotOperationalState.TALKING,
            id="booting_to_talking",
        ),
        pytest.param(
            RobotOperationalState.IDLE,
            RobotOperationalState.TALKING,
            id="idle_to_talking",
        ),
        pytest.param(
            RobotOperationalState.THINKING,
            RobotOperationalState.IDLE,
            id="thinking_to_idle",
        ),
        pytest.param(
            RobotOperationalState.ERROR,
            RobotOperationalState.TALKING,
            id="error_to_talking",
        ),
    ],
)
def test_transition_operational_state_propagates_invalid_transition_error(
    current_state: RobotOperationalState,
    next_state: RobotOperationalState,
) -> None:
    # Arrange
    state_store = SpyOperationalStateStore(initial_state=current_state)
    use_case = TransitionOperationalState(state_store=state_store)

    # Act / Assert
    with pytest.raises(InvalidStateTransitionError):
        use_case.execute(next_state=next_state)

    # Assert
    assert state_store.set_state_calls == 0
    assert state_store.state is current_state


def test_transition_operational_state_uses_persisted_state_across_multiple_executions() -> None:
    # Arrange
    state_store = SpyOperationalStateStore(initial_state=RobotOperationalState.BOOTING)
    use_case = TransitionOperationalState(state_store=state_store)

    # Act
    result_1 = use_case.execute(next_state=RobotOperationalState.IDLE)
    result_2 = use_case.execute(next_state=RobotOperationalState.LISTENING)
    result_3 = use_case.execute(next_state=RobotOperationalState.THINKING)
    result_4 = use_case.execute(next_state=RobotOperationalState.TALKING)
    result_5 = use_case.execute(next_state=RobotOperationalState.IDLE)

    # Assert
    assert result_1 is RobotOperationalState.IDLE
    assert result_2 is RobotOperationalState.LISTENING
    assert result_3 is RobotOperationalState.THINKING
    assert result_4 is RobotOperationalState.TALKING
    assert result_5 is RobotOperationalState.IDLE
    assert state_store.get_state_calls == 5
    assert state_store.set_state_calls == 5
    assert state_store.set_state_arguments == [
        RobotOperationalState.IDLE,
        RobotOperationalState.LISTENING,
        RobotOperationalState.THINKING,
        RobotOperationalState.TALKING,
        RobotOperationalState.IDLE,
    ]
    assert state_store.state is RobotOperationalState.IDLE


def test_transition_operational_state_uses_state_store_port_boundary() -> None:
    # Arrange
    spy_state_store = SpyOperationalStateStore(initial_state=RobotOperationalState.BOOTING)
    state_store_boundary: OperationalStateStorePort = spy_state_store
    use_case = TransitionOperationalState(state_store=state_store_boundary)

    # Act
    result = use_case.execute(next_state=RobotOperationalState.IDLE)

    # Assert
    assert result is RobotOperationalState.IDLE
    assert spy_state_store.get_state_calls == 1
    assert spy_state_store.set_state_calls == 1
    assert spy_state_store.set_state_arguments == [RobotOperationalState.IDLE]
