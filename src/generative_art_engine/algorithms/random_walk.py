import math
import random

Point = tuple[float, float]


def generate_random_walk(
    width: int,
    height: int,
    steps: int,
    seed: int,
) -> list[Point]:
    """Generate a deterministic random walk."""

    rng = random.Random(seed)

    x = width / 2
    y = height / 2

    points: list[Point] = [(x, y)]

    for _ in range(steps):
        angle = rng.uniform(0, 2 * math.pi)
        distance = rng.uniform(2.0, 8.0)

        x += math.cos(angle) * distance
        y += math.sin(angle) * distance

        x = max(0, min(width - 1, x))
        y = max(0, min(height - 1, y))

        points.append((x, y))

    return points
