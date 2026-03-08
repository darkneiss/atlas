from enum import Enum

from atlas_core.contexts.interaction.domain.operational_state import RobotOperationalState


class HeadExpression(str, Enum):
    IDLE = "IDLE"
    LISTENING = "LISTENING"
    THINKING = "THINKING"
    TALKING = "TALKING"
    SLEEPING = "SLEEPING"
    ERROR = "ERROR"

    @classmethod
    def from_operational_state(
        cls, state: RobotOperationalState
    ) -> "HeadExpression":
        mapping: dict[RobotOperationalState, HeadExpression] = {
            RobotOperationalState.IDLE: cls.IDLE,
            RobotOperationalState.LISTENING: cls.LISTENING,
            RobotOperationalState.THINKING: cls.THINKING,
            RobotOperationalState.TALKING: cls.TALKING,
            RobotOperationalState.SLEEPING: cls.SLEEPING,
            RobotOperationalState.ERROR: cls.ERROR,
        }

        return mapping[state]
