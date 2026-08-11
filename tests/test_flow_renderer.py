from generative_art_engine.rendering.flow_renderer import (
    _clamp,
    _distance_from_center,
)


def test_clamp() -> None:
    assert _clamp(0.5, 0.0, 1.0) == 0.5
    assert _clamp(-1.0, 0.0, 1.0) == 0.0
    assert _clamp(2.0, 0.0, 1.0) == 1.0


def test_center_has_zero_distance() -> None:
    distance = _distance_from_center(
        x=50,
        y=50,
        width=101,
        height=101,
    )

    assert distance == 0.0


def test_corner_has_large_distance() -> None:
    distance = _distance_from_center(
        x=0,
        y=0,
        width=101,
        height=101,
    )

    assert distance > 0.9
