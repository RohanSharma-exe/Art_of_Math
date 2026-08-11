import pytest

from generative_art_engine.utils.colors import PALETTES, get_palette


def test_all_palettes_are_valid() -> None:
    assert len(PALETTES) >= 5

    for palette in PALETTES.values():
        assert palette.name
        assert palette.background
        assert len(palette.colors) >= 2


def test_get_palette() -> None:
    palette = get_palette("ocean")

    assert palette.name == "ocean"


def test_unknown_palette_raises_error() -> None:
    with pytest.raises(ValueError):
        get_palette("does-not-exist")
