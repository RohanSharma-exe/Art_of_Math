from pathlib import Path

from PIL import Image, ImageDraw


class Canvas:
    """Simple drawing canvas backed by Pillow."""

    def __init__(
        self,
        width: int,
        height: int,
        background: tuple[int, int, int] = (10, 10, 15),
    ) -> None:
        self.width = width
        self.height = height

        self.image = Image.new(
            "RGB",
            (width, height),
            background,
        )

        self.draw = ImageDraw.Draw(self.image)

    def line(
        self,
        points: list[tuple[float, float]],
        fill: tuple[int, int, int] = (240, 240, 240),
        width: int = 1,
    ) -> None:
        """Draw a connected line through a collection of points."""

        if len(points) < 2:
            return

        self.draw.line(
            points,
            fill=fill,
            width=width,
        )

    def save(self, path: Path) -> None:
        """Save the generated image to disk."""

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.image.save(path)
