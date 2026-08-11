from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ArtConfig:
    """Configuration for generative artwork."""

    width: int = 1024
    height: int = 1024

    seed: int = 42

    output_dir: Path = Path("output")

    noise_scale: float = 0.02
