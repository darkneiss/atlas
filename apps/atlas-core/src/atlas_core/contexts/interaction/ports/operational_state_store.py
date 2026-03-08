from typing import Protocol

from atlas_core.contexts.interaction.domain.operational_state import RobotOperationalState


class OperationalStateStorePort(Protocol):
    def set_state(self, state: RobotOperationalState) -> None:
        ...

    def get_state(self) -> RobotOperationalState:
        ...
