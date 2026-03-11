from atlas_core.contexts.interaction.domain.operational_state import (
    OperationalStateMachine,
    RobotOperationalState,
)
from atlas_core.contexts.interaction.ports.operational_state_store import (
    OperationalStateStorePort,
)


class TransitionOperationalState:
    def __init__(self, state_store: OperationalStateStorePort) -> None:
        self._state_store = state_store

    def execute(self, next_state: RobotOperationalState) -> RobotOperationalState:
        current_state = self._state_store.get_state()
        machine = OperationalStateMachine.rehydrate(current_state=current_state)
        machine.transition_to(next_state)
        self._state_store.set_state(machine.current_state)
        return machine.current_state
