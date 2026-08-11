import random
from pathlib import Path

from PIL import Image, ImageDraw

from generative_art_engine.algorithms.flow_field import FlowField
from generative_art_engine.engine.particle import Particle
from generative_art_engine.utils.colors import get_palette


def generate_flow_field_image(
    width: int,
    height: int,
    seed: int,
    particle_count: int = 1500,
    steps: int = 150,
    step_size: float = 3.0,
    noise_scale: float = 0.003,
    palette_name: str = "midnight",
) -> Image.Image:
    """Generate colorful artwork from particles following a flow field."""

    rng = random.Random(seed)

    palette = get_palette(palette_name)

    image = Image.new(
        "RGBA",
        (width, height),
        (*palette.background, 255),
    )

    draw = ImageDraw.Draw(
        image,
        "RGBA",
    )

    field = FlowField(
        seed=seed,
        scale=noise_scale,
    )

    colors = palette.colors

    for _ in range(particle_count):
        particle = Particle(
            x=rng.uniform(0, width - 1),
            y=rng.uniform(0, height - 1),
        )

        points: list[tuple[float, float]] = [
            (particle.x, particle.y),
        ]

        for _ in range(steps):
            point = particle.follow(
                field,
                step_size,
            )

            if not particle.is_inside(
                width,
                height,
            ):
                break

            points.append(point)

        if len(points) >= 2:
            color = rng.choice(colors)

            draw.line(
                points,
                fill=(*color, 55),
                width=1,
            )

    return image


def save_flow_field_image(
    width: int,
    height: int,
    seed: int,
    output_path: Path,
    particle_count: int = 1500,
    steps: int = 150,
    step_size: float = 3.0,
    noise_scale: float = 0.003,
    palette_name: str = "midnight",
) -> None:
    """Generate and save flow-field artwork."""

    image = generate_flow_field_image(
        width=width,
        height=height,
        seed=seed,
        particle_count=particle_count,
        steps=steps,
        step_size=step_size,
        noise_scale=noise_scale,
        palette_name=palette_name,
    )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    image.save(output_path)
