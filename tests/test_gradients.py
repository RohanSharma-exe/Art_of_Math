from generative_art_engine.utils.gradients import (
    interpolate,
    palette_color,
)


def test_interpolate_start() -> None:
    assert interpolate(
        (0, 0, 0),
        (255, 255, 255),
        0.0,
    ) == (0, 0, 0)


def test_interpolate_end() -> None:
    assert interpolate(
        (0, 0, 0),
        (255, 255, 255),
        1.0,
    ) == (255, 255, 255)


def test_palette_color_interpolates() -> None:
    color = palette_color(
        (
            (0, 0, 0),
            (100, 100, 100),
        ),
        0.5,
    )

    assert color == (50, 50, 50)


def test_palette_position_is_clamped() -> None:
    colors = (
        (0, 0, 0),
        (255, 255, 255),
    )

    assert palette_color(colors, -1.0) == (0, 0, 0)
    assert palette_color(colors, 2.0) == (255, 255, 255)
