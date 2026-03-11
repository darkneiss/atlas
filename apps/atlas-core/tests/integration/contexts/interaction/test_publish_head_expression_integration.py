import pytest

from atlas_core.contexts.interaction.application.publish_head_expression import (
    PublishHeadExpression,
)
from atlas_core.contexts.interaction.domain.expression import HeadExpression
from atlas_core.contexts.interaction.domain.operational_state import RobotOperationalState
from atlas_core.contexts.interaction.ports.head_expression_output import (
    HeadExpressionOutputPort,
)


class InMemoryHeadExpressionOutput(HeadExpressionOutputPort):
    def __init__(self) -> None:
        self.expressions: list[HeadExpression] = []

    def show_expression(self, expression: HeadExpression) -> None:
        self.expressions.append(expression)


def test_publish_head_expression_writes_mapped_expression_to_output() -> None:
    # Arrange
    output = InMemoryHeadExpressionOutput()
    use_case = PublishHeadExpression(output=output)

    # Act
    result = use_case.execute(state=RobotOperationalState.LISTENING)

    # Assert
    assert result is HeadExpression.LISTENING
    assert output.expressions == [HeadExpression.LISTENING]


def test_publish_head_expression_writes_expressions_in_sequence() -> None:
    # Arrange
    output = InMemoryHeadExpressionOutput()
    use_case = PublishHeadExpression(output=output)

    # Act
    use_case.execute(state=RobotOperationalState.IDLE)
    use_case.execute(state=RobotOperationalState.THINKING)
    use_case.execute(state=RobotOperationalState.TALKING)

    # Assert
    assert output.expressions == [
        HeadExpression.IDLE,
        HeadExpression.THINKING,
        HeadExpression.TALKING,
    ]


def test_publish_head_expression_keeps_output_unchanged_for_unmapped_state() -> None:
    # Arrange
    output = InMemoryHeadExpressionOutput()
    use_case = PublishHeadExpression(output=output)

    # Act / Assert
    with pytest.raises(ValueError):
        use_case.execute(state=RobotOperationalState.BOOTING)

    # Assert
    assert output.expressions == []
