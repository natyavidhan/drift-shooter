from pygame import Surface, draw, Rect
from objects import Base
from util import Color, DisplayMode, Vec


class Ellipse(Base):
    """ Pygame Ellipse """
    dimension: Vec
    """ Dimensions of the ellipse """
    thickness: int
    """ Thickness of the ellipse """

    def __init__(
            self,
            position: Vec,
            dimension: Vec,
            color: Color,
            thickness: int = 0
        ):
        super().__init__(position, color)

        self.dimension = dimension
        self.thickness = thickness

    def display(
            self,
            screen: Surface,
            display_mode: DisplayMode,
            camera_offset: Vec
        ):
        pos = self.position.offset_new(camera_offset)
        draw.ellipse(
            screen,
            self.color.toRGB(),
            Rect(
                pos.x - (self.dimension.w/2
                        if display_mode == DisplayMode.CENTER
                        else 0),
                pos.y - (self.dimension.h/2
                        if display_mode == DisplayMode.CENTER
                        else 0),
                self.dimension.w,
                self.dimension.h
            ),
            self.thickness
        )
