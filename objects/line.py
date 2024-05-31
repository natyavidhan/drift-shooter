from pygame import Surface, draw
from util import Color, DisplayMode, Vec


class Line:
    """ Pygame Line """
    position1: Vec
    """ Starting position of the line """
    position2: Vec
    """ Ending position of the line """
    color: Color
    """ Color of the line """
    thickness: int
    """ Thickness of the line """

    def __init__(
            self,
            position1: Vec,
            position2: Vec,
            color: Color,
            thickness: int = 1
        ):
        self.position1 = position1
        self.position2 = position2
        self.color = color
        self.thickness = thickness

    def display(self, screen: Surface, _: DisplayMode, camera_offset: Vec):
        pos1 = self.position1.offset_new(camera_offset)
        pos2 = self.position2.offset_new(camera_offset)
        draw.line(
            screen,
            self.color.toRGB(),
            pos1.sep(),
            pos2.sep(),
            self.thickness
        )
