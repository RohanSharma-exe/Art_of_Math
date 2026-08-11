import random
from pathlib import Path

from PIL import Image, ImageDraw

from generative_art_engine.algorithms.flow_field import FlowField
from generative_art_engine.engine.particle import Particle
from generative_art_engine.utils.colors import get_palette
from generative_art_engine.utils.gradients import palette_color


def _clamp(value: float, minimum: float, maximum: float) -> float:
    """Clamp a value to a range."""

    return max(minimum, min(maximum, value))


def _distance_from_center(
    x: float,
    y: float,
    width: int,
    height: int,
) -> float:
    """Return normalized distance from the canvas center."""

    center_x = (width - 1) / 2
    center_y = (height - 1) / 2

    dx = (x - center_x) / max(center_x, 1)
    dy = (y - center_y) / max(center_y, 1)

    distance = (dx * dx + dy * dy) ** 0.5

    return _clamp(distance, 0.0, 1.0)


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
    """Generate visually composed flow-field artwork."""

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
        start_x = rng.uniform(0, width - 1)
        start_y = rng.uniform(0, height - 1)

        particle = Particle(
            x=start_x,
            y=start_y,
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

        if len(points) < 2:
            continue

        # Combine horizontal position and local noise
        # to create a continuous 2D color mapping.
        x_position = start_x / max(width - 1, 1)
        y_position = start_y / max(height - 1, 1)

        noise_value = field.noise.noise(
            start_x * noise_scale,
            start_y * noise_scale,
        )

        noise_position = (noise_value + 1.0) / 2.0

        color_position = x_position * 0.45 + y_position * 0.20 + noise_position * 0.35

        color = palette_color(
            colors,
            color_position,
        )

        # Keep the center visually stronger and the edges lighter.
        edge_distance = _distance_from_center(
            start_x,
            start_y,
            width,
            height,
        )

        alpha = int(75 - edge_distance * 35 + rng.uniform(-8, 8))

        alpha = int(
            _clamp(
                alpha,
                20,
                85,
            )
        )

        # Slight deterministic variation in line width.
        line_width = 1

        if rng.random() < 0.08:
            line_width = 2

        draw.line(
            points,
            fill=(*color, alpha),
            width=line_width,
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
