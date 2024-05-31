from math import atan, sqrt, cos, sin
from pygame import Surface

from objects import Polygon
from util import Color, Angle, DisplayMode, Vec, sqr



class Rectangle(Polygon):
    """ Rectangle """
    center: Vec
    """ Position of the rectangle [TOP LEFT VERTEX IN DisplayMode.CORNER] """
    dimension: Vec
    """ Dimensions of the rectangle """
    rotation: Angle
    """ Rotation of the rectangle """
    positions: list[Vec]
    """ Position of each point """

    diagonal_angle: Angle
    diagonal_length: float

    vertex1: Vec
    vertex2: Vec
    vertex3: Vec
    vertex4: Vec

    def __init__(
            self,
            position: Vec,
            dimension: Vec,
            color: Color,
            rotation: Angle = None
    ):
        if rotation is None:
            rotation = Angle(degree=0)
        self.center = position
        self.dimension = dimension
        self.rotation = rotation
        self.positions = []
        self.draw()
        super().__init__(self.positions, color)

    def draw(self):
        self.diagonal_angle = Angle(
            radian=atan(self.dimension.h / self.dimension.w)
        )
        self.diagonal_length = sqrt(
            sqr(self.dimension.h) +
            sqr(self.dimension.w)
        )

        def vertex_calculator(angle: Angle):
            return Vec(
                (self.diagonal_length / 2) * cos(angle.radian),
                (self.diagonal_length / 2) * sin(angle.radian)
            )

        angle1 = self.rotation.offset_new(self.diagonal_angle.degree)
        angle2 = self.rotation.offset_new(180 - self.diagonal_angle.degree)
        angle3 = self.rotation.offset_new(180 + self.diagonal_angle.degree)
        angle4 = self.rotation.offset_new(-self.diagonal_angle.degree)

        self.vertex1 = self.center.offset_new(*vertex_calculator(angle1).sep())
        self.vertex2 = self.center.offset_new(*vertex_calculator(angle2).sep())
        self.vertex3 = self.center.offset_new(*vertex_calculator(angle3).sep())
        self.vertex4 = self.center.offset_new(*vertex_calculator(angle4).sep())

    def display(
            self,
            screen: Surface,
            display_mode: DisplayMode,
            camera_offset: Vec
        ):
        if display_mode == DisplayMode.CORNER:
            self.vertex1.offset(self.dimension.w/2, self.dimension.h/2)
            self.vertex2.offset(self.dimension.w/2, self.dimension.h/2)
            self.vertex3.offset(self.dimension.w/2, self.dimension.h/2)
            self.vertex4.offset(self.dimension.w/2, self.dimension.h/2)

        self.positions = [
            self.vertex1,
            self.vertex2,
            self.vertex3,
            self.vertex4
        ]
        super().display(screen, display_mode, camera_offset)
