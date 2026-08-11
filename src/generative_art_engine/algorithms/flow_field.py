import math

from generative_art_engine.algorithms.perlin import PerlinNoise


class FlowField:
    """Generate smooth directions from a Perlin noise field."""

    def __init__(
        self,
        seed: int,
        scale: float = 0.003,
        strength: float = math.tau,
    ) -> None:
        self.noise = PerlinNoise(seed)
        self.scale = scale
        self.strength = strength

    def angle(self, x: float, y: float) -> float:
        """Return the flow direction at a position."""

        value = self.noise.noise(
            x * self.scale,
            y * self.scale,
        )

        normalized = (value + 1.0) / 2.0

        return normalized * self.strength

    def direction(self, x: float, y: float) -> tuple[float, float]:
        """Return a unit direction vector at a position."""

        angle = self.angle(x, y)

        return math.cos(angle), math.sin(angle)
