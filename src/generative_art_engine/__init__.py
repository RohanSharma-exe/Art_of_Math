"""Generative Art Engine."""

from generative_art_engine.config import ArtConfig
from generative_art_engine.engine.art_engine import ArtEngine

__version__ = "0.4.0"


def main() -> None:
    """Generate flow-field artwork using the default configuration."""

    print("🎨 Generative Art Engine")
    print(f"Version: {__version__}")
    print("Algorithm: Flow Field")

    config = ArtConfig()

    engine = ArtEngine(config)

    output_path = engine.generate_flow_field_art()

    print(f"Artwork generated: {output_path}")
