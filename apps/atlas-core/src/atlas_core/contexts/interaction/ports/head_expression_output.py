from typing import Protocol

from atlas_core.contexts.interaction.domain.expression import HeadExpression


class HeadExpressionOutputPort(Protocol):
    def show_expression(self, expression: HeadExpression) -> None:
        ...
