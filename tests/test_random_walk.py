from generative_art_engine.algorithms.random_walk import generate_random_walk


def test_random_walk_is_deterministic() -> None:
    first = generate_random_walk(
        width=100,
        height=100,
        steps=100,
        seed=42,
    )

    second = generate_random_walk(
        width=100,
        height=100,
        steps=100,
        seed=42,
    )

    assert first == second


def test_random_walk_stays_inside_canvas() -> None:
    points = generate_random_walk(
        width=100,
        height=100,
        steps=100,
        seed=42,
    )

    for x, y in points:
        assert 0 <= x < 100
        assert 0 <= y < 100
