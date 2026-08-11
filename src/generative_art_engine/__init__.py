"""Generative Art Engine."""

from generative_art_engine.config import ArtConfig
from generative_art_engine.engine.art_engine import ArtEngine

__version__ = "0.3.0"


def main() -> None:
    """Generate artwork using the default configuration."""

    print("🎨 Generative Art Engine")
    print(f"Version: {__version__}")

    config = ArtConfig()

    engine = ArtEngine(config)

    output_path = engine.generate_noise_art()

    print(f"Artwork generated: {output_path}")
