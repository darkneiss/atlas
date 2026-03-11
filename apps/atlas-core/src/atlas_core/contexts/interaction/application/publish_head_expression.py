from atlas_core.contexts.interaction.domain.expression import HeadExpression
from atlas_core.contexts.interaction.domain.operational_state import RobotOperationalState
from atlas_core.contexts.interaction.ports.head_expression_output import (
    HeadExpressionOutputPort,
)


class PublishHeadExpression:
    def __init__(self, output: HeadExpressionOutputPort) -> None:
        self._output = output

    def execute(self, state: RobotOperationalState) -> HeadExpression:
        try:
            expression = HeadExpression.from_operational_state(state)
        except KeyError as error:
            raise ValueError(f"No head expression mapping for state: {state!r}") from error

        self._output.show_expression(expression)
        return expression
