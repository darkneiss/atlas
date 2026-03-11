from inspect import signature
from typing import get_type_hints

from atlas_core.contexts.interaction.domain.expression import HeadExpression
from atlas_core.contexts.interaction.ports.head_expression_output import (
    HeadExpressionOutputPort,
)


def test_head_expression_output_port_exposes_show_expression_operation() -> None:
    assert hasattr(HeadExpressionOutputPort, "show_expression")


def test_show_expression_accepts_head_expression_argument() -> None:
    show_expression_signature = signature(HeadExpressionOutputPort.show_expression)
    show_expression_hints = get_type_hints(HeadExpressionOutputPort.show_expression)

    show_expression_signature.bind(object(), HeadExpression.IDLE)
    assert show_expression_hints["expression"] is HeadExpression


def test_show_expression_returns_none() -> None:
    show_expression_hints = get_type_hints(HeadExpressionOutputPort.show_expression)

    assert show_expression_hints["return"] is type(None)


def test_show_expression_uses_expected_parameter_name() -> None:
    show_expression_signature = signature(HeadExpressionOutputPort.show_expression)

    assert list(show_expression_signature.parameters) == ["self", "expression"]


def test_head_expression_output_port_exposes_only_expected_public_operation() -> None:
    public_operations = [
        name
        for name, value in vars(HeadExpressionOutputPort).items()
        if callable(value) and not name.startswith("_")
    ]

    assert sorted(public_operations) == ["show_expression"]
