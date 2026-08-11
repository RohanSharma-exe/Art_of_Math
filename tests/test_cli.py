from generative_art_engine.cli import ALGORITHMS, build_parser


def test_default_arguments() -> None:
    parser = build_parser()

    args = parser.parse_args([])

    assert args.algorithm == "flow-field"
    assert args.palette == "midnight"
    assert args.seed == 42
    assert args.particles == 1500
    assert args.steps == 150
    assert args.step_size == 3.0
    assert args.flow_scale == 0.003
    assert args.noise_scale == 0.02


def test_custom_arguments() -> None:
    parser = build_parser()

    args = parser.parse_args(
        [
            "--algorithm",
            "noise",
            "--palette",
            "ocean",
            "--seed",
            "1234",
            "--particles",
            "3000",
            "--steps",
            "200",
            "--step-size",
            "2.5",
            "--flow-scale",
            "0.005",
            "--noise-scale",
            "0.01",
        ]
    )

    assert args.algorithm == "noise"
    assert args.palette == "ocean"
    assert args.seed == 1234
    assert args.particles == 3000
    assert args.steps == 200
    assert args.step_size == 2.5
    assert args.flow_scale == 0.005
    assert args.noise_scale == 0.01


def test_all_algorithms_are_registered() -> None:
    assert "flow-field" in ALGORITHMS
    assert "noise" in ALGORITHMS
    assert "random-walk" in ALGORITHMS
