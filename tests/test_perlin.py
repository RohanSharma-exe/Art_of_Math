from generative_art_engine.algorithms.perlin import PerlinNoise


def test_perlin_is_deterministic() -> None:
    first = PerlinNoise(seed=42)
    second = PerlinNoise(seed=42)

    points = [
        (0.1, 0.2),
        (1.5, 2.7),
        (10.25, 4.75),
        (25.5, 30.5),
    ]

    for x, y in points:
        assert first.noise(x, y) == second.noise(x, y)


def test_different_seeds_produce_different_noise() -> None:
    first = PerlinNoise(seed=42)
    second = PerlinNoise(seed=123)

    assert first.noise(1.5, 2.5) != second.noise(1.5, 2.5)


def test_noise_is_reasonably_bounded() -> None:
    noise = PerlinNoise(seed=42)

    for x in range(10):
        for y in range(10):
            value = noise.noise(
                x * 0.25,
                y * 0.25,
            )

            assert -1.0 <= value <= 1.0
