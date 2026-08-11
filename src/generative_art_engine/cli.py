import argparse

from generative_art_engine.config import ArtConfig
from generative_art_engine.engine.art_engine import ArtEngine
from generative_art_engine.utils.colors import PALETTES

ALGORITHMS = (
    "flow-field",
    "noise",
    "random-walk",
)


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line argument parser."""

    parser = argparse.ArgumentParser(
        prog="generative-art-engine",
        description="Generate procedural mathematical artwork.",
    )

    parser.add_argument(
        "--algorithm",
        choices=ALGORITHMS,
        default="flow-field",
        help="Generative algorithm to use.",
    )

    parser.add_argument(
        "--palette",
        choices=sorted(PALETTES),
        default="midnight",
        help="Color palette for flow-field artwork.",
    )

    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed controlling the artwork.",
    )

    parser.add_argument(
        "--particles",
        type=int,
        default=1500,
        help="Number of particles for flow-field artwork.",
    )

    parser.add_argument(
        "--steps",
        type=int,
        default=150,
        help="Maximum number of steps per particle.",
    )

    parser.add_argument(
        "--step-size",
        type=float,
        default=3.0,
        help="Distance each particle moves per step.",
    )

    parser.add_argument(
        "--flow-scale",
        type=float,
        default=0.003,
        help="Scale of the flow-field noise.",
    )

    parser.add_argument(
        "--noise-scale",
        type=float,
        default=0.02,
        help="Scale of Perlin noise artwork.",
    )

    return parser


def main() -> None:
    """Parse arguments and generate artwork."""

    parser = build_parser()
    args = parser.parse_args()

    if args.particles <= 0:
        parser.error("--particles must be greater than 0")

    if args.steps <= 0:
        parser.error("--steps must be greater than 0")

    if args.step_size <= 0:
        parser.error("--step-size must be greater than 0")

    if args.flow_scale <= 0:
        parser.error("--flow-scale must be greater than 0")

    if args.noise_scale <= 0:
        parser.error("--noise-scale must be greater than 0")

    config = ArtConfig(
        seed=args.seed,
        palette=args.palette,
        particle_count=args.particles,
        particle_steps=args.steps,
        particle_step_size=args.step_size,
        flow_scale=args.flow_scale,
        noise_scale=args.noise_scale,
    )

    print("🎨 Generative Art Engine")
    print("Version: 0.9.0")
    print()
    print(f"Algorithm:  {args.algorithm}")
    print(f"Seed:       {config.seed}")

    if args.algorithm == "flow-field":
        print(f"Palette:    {config.palette}")
        print(f"Particles:  {config.particle_count}")
        print(f"Steps:      {config.particle_steps}")
        print(f"Step size:  {config.particle_step_size}")
        print(f"Flow scale: {config.flow_scale}")

    elif args.algorithm == "noise":
        print(f"Noise scale: {config.noise_scale}")

    print()

    engine = ArtEngine(config)

    if args.algorithm == "flow-field":
        output_path = engine.generate_flow_field_art()

    elif args.algorithm == "noise":
        output_path = engine.generate_noise_art()

    else:
        output_path = engine.generate_random_walk_art()

    print(f"Artwork generated: {output_path}")
