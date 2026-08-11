from pathlib import Path

import numpy as np
from PIL import Image

from generative_art_engine.algorithms.perlin import PerlinNoise


def generate_noise_image(
    width: int,
    height: int,
    seed: int,
    scale: float = 0.015,
) -> Image.Image:
    """Generate a grayscale image from 2D Perlin noise."""

    noise = PerlinNoise(seed)

    image = np.zeros(
        (height, width),
        dtype=np.uint8,
    )

    for y in range(height):
        for x in range(width):
            value = noise.noise(
                x * scale,
                y * scale,
            )

            normalized = (value + 1.0) / 2.0
            pixel = int(normalized * 255)

            image[y, x] = max(0, min(255, pixel))

    return Image.fromarray(image, mode="L")


def save_noise_image(
    width: int,
    height: int,
    seed: int,
    output_path: Path,
    scale: float = 0.015,
) -> None:
    """Generate and save a Perlin noise image."""

    image = generate_noise_image(
        width=width,
        height=height,
        seed=seed,
        scale=scale,
    )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    image.save(output_path)
