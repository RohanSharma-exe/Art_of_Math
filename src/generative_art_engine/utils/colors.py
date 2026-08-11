from dataclasses import dataclass

RGB = tuple[int, int, int]


@dataclass(frozen=True)
class ColorPalette:
    """A color palette used by the art renderer."""

    name: str
    background: RGB
    colors: tuple[RGB, ...]


PALETTES: dict[str, ColorPalette] = {
    "midnight": ColorPalette(
        name="midnight",
        background=(5, 7, 15),
        colors=(
            (80, 120, 255),
            (120, 170, 255),
            (180, 210, 255),
            (230, 240, 255),
        ),
    ),
    "ocean": ColorPalette(
        name="ocean",
        background=(3, 12, 20),
        colors=(
            (0, 110, 180),
            (0, 170, 210),
            (40, 220, 190),
            (180, 255, 230),
        ),
    ),
    "sunset": ColorPalette(
        name="sunset",
        background=(20, 5, 12),
        colors=(
            (180, 50, 80),
            (240, 80, 100),
            (255, 150, 70),
            (255, 220, 130),
        ),
    ),
    "forest": ColorPalette(
        name="forest",
        background=(3, 12, 8),
        colors=(
            (30, 100, 70),
            (50, 160, 100),
            (120, 210, 130),
            (210, 245, 180),
        ),
    ),
    "fire": ColorPalette(
        name="fire",
        background=(15, 4, 2),
        colors=(
            (150, 25, 10),
            (220, 60, 10),
            (255, 130, 20),
            (255, 220, 100),
        ),
    ),
}


def get_palette(name: str) -> ColorPalette:
    """Return a palette by name."""

    try:
        return PALETTES[name]
    except KeyError as exc:
        available = ", ".join(sorted(PALETTES))
        raise ValueError(
            f"Unknown palette '{name}'. Available palettes: {available}"
        ) from exc
