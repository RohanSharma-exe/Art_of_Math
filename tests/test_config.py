from generative_art_engine.config import ArtConfig


def test_default_art_config() -> None:
    config = ArtConfig()

    assert config.width == 1024
    assert config.height == 1024
    assert config.seed == 42
    assert config.output_dir.name == "output"
