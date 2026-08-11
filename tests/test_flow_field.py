import math

from generative_art_engine.algorithms.flow_field import FlowField


def test_flow_field_is_deterministic() -> None:
    first = FlowField(seed=42)
    second = FlowField(seed=42)

    assert first.angle(100, 200) == second.angle(100, 200)

    assert first.direction(100, 200) == second.direction(
        100,
        200,
    )


def test_direction_is_unit_length() -> None:
    field = FlowField(seed=42)

    dx, dy = field.direction(
        100,
        200,
    )

    magnitude = math.sqrt(
        dx**2 + dy**2,
    )

    assert math.isclose(
        magnitude,
        1.0,
        rel_tol=1e-9,
    )
