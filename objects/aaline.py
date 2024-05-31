from pygame import Surface, draw
from .line import Line
from util import Color, DisplayMode, Vec


class AALine(Line):
    """ Pygame AALine """
    def __init__(
            self,
            position1: Vec,
            position2: Vec,
            color: Color,
            thickness: int = 1
        ):
        super().__init__(position1, position2, color, thickness)

    def display(self, screen: Surface, _: DisplayMode, camera_offset: Vec):
        pos1 = self.position1.offset_new(camera_offset)
        pos2 = self.position2.offset_new(camera_offset)
        draw.aaline(
            screen,
            self.color.toRGB(),
            pos1.sep(),
            pos2.sep(),
            self.thickness
        )
