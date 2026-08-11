"""Generative Art Engine."""

from generative_art_engine.config import ArtConfig
from generative_art_engine.engine.art_engine import ArtEngine

__version__ = "0.5.0"


def main() -> None:
    """Generate colorful flow-field artwork."""

    print("🎨 Generative Art Engine")
    print(f"Version: {__version__}")
    print("Algorithm: Flow Field")

    config = ArtConfig(
        palette="midnight",
    )

    engine = ArtEngine(config)

    output_path = engine.generate_flow_field_art()

    print(f"Palette: {config.palette}")
    print(f"Artwork generated: {output_path}")
