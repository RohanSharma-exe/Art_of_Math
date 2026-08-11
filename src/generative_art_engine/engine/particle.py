from dataclasses import dataclass

from generative_art_engine.algorithms.flow_field import FlowField

Point = tuple[float, float]


@dataclass
class Particle:
    """A particle moving through a flow field."""

    x: float
    y: float

    def follow(
        self,
        field: FlowField,
        step_size: float,
    ) -> Point:
        """Move the particle according to the flow field."""

        dx, dy = field.direction(
            self.x,
            self.y,
        )

        self.x += dx * step_size
        self.y += dy * step_size

        return self.x, self.y

    def is_inside(
        self,
        width: int,
        height: int,
    ) -> bool:
        """Return whether the particle remains inside the canvas."""

        return 0 <= self.x < width and 0 <= self.y < height
