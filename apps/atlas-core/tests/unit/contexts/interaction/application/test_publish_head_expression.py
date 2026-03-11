import pytest

from atlas_core.contexts.interaction.application.publish_head_expression import (
    PublishHeadExpression,
)
from atlas_core.contexts.interaction.domain.expression import HeadExpression
from atlas_core.contexts.interaction.domain.operational_state import RobotOperationalState
from atlas_core.contexts.interaction.ports.head_expression_output import (
    HeadExpressionOutputPort,
)


class SpyHeadExpressionOutput(HeadExpressionOutputPort):
    def __init__(self) -> None:
        self.expressions: list[HeadExpression] = []
        self.show_expression_calls = 0

    def show_expression(self, expression: HeadExpression) -> None:
        self.show_expression_calls += 1
        self.expressions.append(expression)


class FailingHeadExpressionOutput(HeadExpressionOutputPort):
    def show_expression(self, expression: HeadExpression) -> None:
        raise RuntimeError("head device unavailable")


def test_publish_head_expression_returns_mapped_expression() -> None:
    # Arrange
    output = SpyHeadExpressionOutput()
    use_case = PublishHeadExpression(output=output)

    # Act
    result = use_case.execute(state=RobotOperationalState.THINKING)

    # Assert
    assert result is HeadExpression.THINKING


def test_publish_head_expression_sends_mapped_expression_to_output_port() -> None:
    # Arrange
    output = SpyHeadExpressionOutput()
    use_case = PublishHeadExpression(output=output)

    # Act
    result = use_case.execute(state=RobotOperationalState.TALKING)

    # Assert
    assert output.show_expression_calls == 1
    assert output.expressions == [HeadExpression.TALKING]
    assert output.expressions[0] is result


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
def test_publish_head_expression_supports_phase1_mapped_states(
    state: RobotOperationalState,
    expected_expression: HeadExpression,
) -> None:
    # Arrange
    output = SpyHeadExpressionOutput()
    use_case = PublishHeadExpression(output=output)

    # Act
    result = use_case.execute(state=state)

    # Assert
    assert result is expected_expression
    assert output.expressions[-1] is expected_expression


def test_publish_head_expression_rejects_unmapped_state_without_side_effects() -> None:
    # Arrange
    output = SpyHeadExpressionOutput()
    use_case = PublishHeadExpression(output=output)

    # Act / Assert
    with pytest.raises(ValueError):
        use_case.execute(state=RobotOperationalState.BOOTING)

    # Assert
    assert output.show_expression_calls == 0
    assert output.expressions == []


def test_publish_head_expression_uses_output_port_boundary() -> None:
    # Arrange
    spy_output = SpyHeadExpressionOutput()
    output_boundary: HeadExpressionOutputPort = spy_output
    use_case = PublishHeadExpression(output=output_boundary)

    # Act
    result = use_case.execute(state=RobotOperationalState.IDLE)

    # Assert
    assert result is HeadExpression.IDLE
    assert spy_output.show_expression_calls == 1
    assert spy_output.expressions == [HeadExpression.IDLE]


def test_publish_head_expression_propagates_output_port_errors() -> None:
    # Arrange
    output = FailingHeadExpressionOutput()
    use_case = PublishHeadExpression(output=output)

    # Act / Assert
    with pytest.raises(RuntimeError):
        use_case.execute(state=RobotOperationalState.IDLE)
