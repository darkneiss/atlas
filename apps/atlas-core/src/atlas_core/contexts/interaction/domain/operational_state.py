from enum import Enum


class RobotOperationalState(str, Enum):
    BOOTING = "BOOTING"
    IDLE = "IDLE"
    LISTENING = "LISTENING"
    THINKING = "THINKING"
    TALKING = "TALKING"
    SLEEPING = "SLEEPING"
    ERROR = "ERROR"


class InvalidStateTransitionError(ValueError):
    """Raised when an operational state transition is not allowed."""


class OperationalStateMachine:
    def __init__(self, current_state: RobotOperationalState) -> None:
        if current_state is not RobotOperationalState.BOOTING:
            raise ValueError("OperationalStateMachine must be created in BOOTING state")

        self._current_state = current_state

    @classmethod
    def initial(cls) -> "OperationalStateMachine":
        return cls(current_state=RobotOperationalState.BOOTING)

    @property
    def current_state(self) -> RobotOperationalState:
        return self._current_state

    def transition_to(self, next_state: RobotOperationalState) -> None:
        allowed_transitions: dict[RobotOperationalState, set[RobotOperationalState]] = {
            RobotOperationalState.BOOTING: {RobotOperationalState.IDLE},
            RobotOperationalState.IDLE: {RobotOperationalState.LISTENING},
            RobotOperationalState.LISTENING: {
                RobotOperationalState.THINKING,
                RobotOperationalState.ERROR,
            },
            RobotOperationalState.THINKING: {
                RobotOperationalState.TALKING,
                RobotOperationalState.ERROR,
            },
            RobotOperationalState.TALKING: {
                RobotOperationalState.IDLE,
                RobotOperationalState.ERROR,
            },
            RobotOperationalState.ERROR: {RobotOperationalState.IDLE},
        }

        if next_state not in allowed_transitions.get(self._current_state, set()):
            raise InvalidStateTransitionError(
                f"Invalid transition: {self._current_state.value} -> {next_state.value}"
            )

        self._current_state = next_state
