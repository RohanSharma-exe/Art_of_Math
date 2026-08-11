from pathlib import Path

from PIL import Image

from generative_art_engine.algorithms.random_walk import generate_random_walk
from generative_art_engine.config import ArtConfig
from generative_art_engine.rendering.canvas import Canvas
from generative_art_engine.rendering.flow_renderer import (
    generate_flow_field_image,
)
from generative_art_engine.rendering.noise_renderer import generate_noise_image


class ArtEngine:
    """Coordinate algorithm generation and image rendering."""

    def __init__(self, config: ArtConfig) -> None:
        self.config = config

    def generate_random_walk_art(self) -> Path:
        """Generate random-walk artwork."""

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

        output_path = (
            self.config.output_dir / f"art_random_walk_s{self.config.seed}.png"
        )

        canvas.save(output_path)

        return output_path

    def generate_noise_art(self) -> Path:
        """Generate Perlin noise artwork."""

        preview_size = 256

        image = generate_noise_image(
            width=preview_size,
            height=preview_size,
            seed=self.config.seed,
            scale=self.config.noise_scale,
        )

        image = image.resize(
            (self.config.width, self.config.height),
            Image.Resampling.BICUBIC,
        )

        output_path = self.config.output_dir / f"art_noise_s{self.config.seed}.png"

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        image.save(output_path)

        return output_path

    def generate_flow_field_art(self) -> Path:
        """Generate colorful particle-based flow-field artwork."""

        image = generate_flow_field_image(
            width=self.config.width,
            height=self.config.height,
            seed=self.config.seed,
            particle_count=self.config.particle_count,
            steps=self.config.particle_steps,
            step_size=self.config.particle_step_size,
            noise_scale=self.config.flow_scale,
            palette_name=self.config.palette,
        )

        filename = (
            f"art_flow_field_"
            f"{self.config.palette}_"
            f"s{self.config.seed}_"
            f"p{self.config.particle_count}_"
            f"n{self.config.particle_steps}.png"
        )

        output_path = self.config.output_dir / filename

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        image.save(output_path)

        return output_path
