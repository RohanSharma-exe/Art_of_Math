from generative_art_engine.algorithms.flow_field import FlowField
from generative_art_engine.engine.particle import Particle


def test_particle_moves() -> None:
    field = FlowField(seed=42)

    particle = Particle(
        x=100,
        y=100,
    )

    original = (
        particle.x,
        particle.y,
    )

    particle.follow(
        field,
        step_size=5,
    )

    updated = (
        particle.x,
        particle.y,
    )

    assert updated != original


def test_particle_inside_canvas() -> None:
    particle = Particle(
        x=50,
        y=50,
    )

    assert particle.is_inside(
        width=100,
        height=100,
    )


def test_particle_outside_canvas() -> None:
    particle = Particle(
        x=150,
        y=50,
    )

    assert not particle.is_inside(
        width=100,
        height=100,
    )
