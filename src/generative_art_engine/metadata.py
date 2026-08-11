import json
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class GenerationMetadata:
    """Metadata describing a generated artwork."""

    algorithm: str
    seed: int

    width: int
    height: int

    palette: str | None

    particle_count: int | None
    particle_steps: int | None
    particle_step_size: float | None

    flow_scale: float | None
    noise_scale: float | None


def save_metadata(
    metadata: GenerationMetadata,
    output_path: Path,
) -> Path:
    """Save generation metadata beside the artwork."""

    metadata_path = output_path.with_suffix(".json")

    metadata_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    metadata_path.write_text(
        json.dumps(
            asdict(metadata),
            indent=2,
        ),
        encoding="utf-8",
    )

    return metadata_path
