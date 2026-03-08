from inspect import signature
from typing import get_type_hints

from atlas_core.contexts.interaction.domain.operational_state import RobotOperationalState
from atlas_core.contexts.interaction.ports.operational_state_store import (
    OperationalStateStorePort,
)


def test_operational_state_store_port_exposes_set_state_operation() -> None:
    assert hasattr(OperationalStateStorePort, "set_state")


def test_operational_state_store_port_exposes_get_state_operation() -> None:
    assert hasattr(OperationalStateStorePort, "get_state")


def test_set_state_accepts_robot_operational_state_argument() -> None:
    set_state_signature = signature(OperationalStateStorePort.set_state)
    set_state_hints = get_type_hints(OperationalStateStorePort.set_state)

    set_state_signature.bind(object(), RobotOperationalState.IDLE)
    assert set_state_hints["state"] is RobotOperationalState


def test_get_state_returns_robot_operational_state() -> None:
    get_state_hints = get_type_hints(OperationalStateStorePort.get_state)

    assert get_state_hints["return"] is RobotOperationalState


def test_operational_state_store_port_exposes_only_the_expected_public_operations() -> None:
    public_operations = [
        name
        for name, value in vars(OperationalStateStorePort).items()
        if callable(value) and not name.startswith("_")
    ]

    assert sorted(public_operations) == ["get_state", "set_state"]
