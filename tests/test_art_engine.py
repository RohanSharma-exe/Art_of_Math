import json

from generative_art_engine.config import ArtConfig
from generative_art_engine.engine.art_engine import ArtEngine


def test_flow_field_creates_metadata(tmp_path) -> None:
    config = ArtConfig(
        width=64,
        height=64,
        seed=42,
        output_dir=tmp_path,
        particle_count=10,
        particle_steps=5,
    )

    engine = ArtEngine(config)

    output_path = engine.generate_flow_field_art()

    metadata_path = output_path.with_suffix(".json")

    assert output_path.exists()
    assert metadata_path.exists()

    metadata = json.loads(
        metadata_path.read_text(
            encoding="utf-8",
        )
    )

    assert metadata["algorithm"] == "flow-field"
    assert metadata["seed"] == 42
    assert metadata["width"] == 64
    assert metadata["height"] == 64
    assert metadata["particle_count"] == 10
