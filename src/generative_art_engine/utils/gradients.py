from collections.abc import Sequence

from generative_art_engine.utils.colors import RGB


def interpolate(
    first: RGB,
    second: RGB,
    amount: float,
) -> RGB:
    """Interpolate between two RGB colors."""

    amount = max(0.0, min(1.0, amount))

    return tuple(
        round(first[index] + (second[index] - first[index]) * amount)
        for index in range(3)
    )


def palette_color(
    colors: Sequence[RGB],
    position: float,
) -> RGB:
    """
    Return a smoothly interpolated color from a palette.

    Position is expected to be in the range [0, 1].
    """

    if not colors:
        raise ValueError("Palette must contain at least one color.")

    if len(colors) == 1:
        return colors[0]

    position = max(0.0, min(1.0, position))

    scaled = position * (len(colors) - 1)

    index = min(
        int(scaled),
        len(colors) - 2,
    )

    local_position = scaled - index

    return interpolate(
        colors[index],
        colors[index + 1],
        local_position,
    )
