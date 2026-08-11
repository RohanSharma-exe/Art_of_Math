import json

from generative_art_engine.metadata import (
    GenerationMetadata,
    save_metadata,
)


def test_save_metadata(tmp_path) -> None:
    output_path = tmp_path / "art.png"

    metadata = GenerationMetadata(
        algorithm="flow-field",
        seed=42,
        width=1024,
        height=1024,
        palette="ocean",
        particle_count=1500,
        particle_steps=150,
        particle_step_size=3.0,
        flow_scale=0.003,
        noise_scale=None,
    )

    metadata_path = save_metadata(
        metadata,
        output_path,
    )

    assert metadata_path.exists()

    data = json.loads(
        metadata_path.read_text(
            encoding="utf-8",
        )
    )

    assert data["algorithm"] == "flow-field"
    assert data["seed"] == 42
    assert data["palette"] == "ocean"
    assert data["particle_count"] == 1500
