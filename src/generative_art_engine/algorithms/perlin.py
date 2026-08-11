import math
import random


class PerlinNoise:
    """Deterministic 2D improved Perlin noise generator."""

    def __init__(self, seed: int = 0) -> None:
        rng = random.Random(seed)

        permutation = list(range(256))
        rng.shuffle(permutation)

        self._permutation = permutation * 2

    def _fade(self, t: float) -> float:
        """Smooth interpolation curve."""

        return t * t * t * (t * (t * 6 - 15) + 10)

    def _lerp(self, a: float, b: float, t: float) -> float:
        """Linear interpolation."""

        return a + t * (b - a)

    def _gradient(
        self,
        hash_value: int,
        x: float,
        y: float,
    ) -> float:
        """Calculate the gradient contribution."""

        direction = hash_value & 3

        if direction == 0:
            return x + y

        if direction == 1:
            return -x + y

        if direction == 2:
            return x - y

        return -x - y

    def noise(self, x: float, y: float) -> float:
        """
        Return 2D Perlin noise in approximately the range [-1, 1].
        """

        x0 = math.floor(x)
        y0 = math.floor(y)

        local_x = x - x0
        local_y = y - y0

        xi = x0 & 255
        yi = y0 & 255

        u = self._fade(local_x)
        v = self._fade(local_y)

        permutation = self._permutation

        aa = permutation[permutation[xi] + yi]
        ab = permutation[permutation[xi] + yi + 1]
        ba = permutation[permutation[xi + 1] + yi]
        bb = permutation[permutation[xi + 1] + yi + 1]

        x1 = self._lerp(
            self._gradient(aa, local_x, local_y),
            self._gradient(ba, local_x - 1, local_y),
            u,
        )

        x2 = self._lerp(
            self._gradient(ab, local_x, local_y - 1),
            self._gradient(bb, local_x - 1, local_y - 1),
            u,
        )

        return self._lerp(x1, x2, v)
