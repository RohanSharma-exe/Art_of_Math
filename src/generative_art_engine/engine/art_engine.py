from pathlib import Path

from generative_art_engine.algorithms.random_walk import generate_random_walk
from generative_art_engine.config import ArtConfig
from generative_art_engine.rendering.canvas import Canvas


class ArtEngine:
    """Coordinate algorithm generation and image rendering."""

    def __init__(self, config: ArtConfig) -> None:
        self.config = config

    def generate(self) -> Path:
        """Generate artwork and save it to disk."""

        canvas = Canvas(
            width=self.config.width,
            height=self.config.height,
        )

        points = generate_random_walk(
            width=self.config.width,
            height=self.config.height,
            steps=5000,
            seed=self.config.seed,
        )

        canvas.line(
            points,
            fill=(240, 240, 240),
            width=2,
        )

        output_path = self.config.output_dir / f"art_{self.config.seed}.png"

        canvas.save(output_path)

        return output_path
