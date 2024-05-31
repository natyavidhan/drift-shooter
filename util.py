from math import radians, degrees, sqrt
from enum import Enum

def sqr(x: float) -> float:
    return x*x

class Color:
    """ Color class """
    red: int
    """ the amount of red in the color """
    green: int
    """ the amount of green in the color """
    blue: int
    """ the amount of blue in the color """

    def __init__(self, red=0, green=0, blue=0):
        self.red = red
        self.green = green
        self.blue = blue

    @staticmethod
    def from_hex(hex_string: str):
        """ Make a color from hex values """
        tup = tuple(int(hex_string.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))
        return Color(tup[0], tup[1], tup[2])

    def toRGB(self) -> tuple[int, int, int]:
        """ Turns RGB value """
        return self.red, self.green, self.blue

    def toBGR(self) -> tuple[int, int, int]:
        """ Turns BGR value """
        return self.blue, self.green, self.red

    def to_hex(self):
        return "{:X}{:X}{:X}".format(self.red, self.green, self.blue)


class Angle:
    """ Angle class """
    degree: float
    """ Angle in degrees unit """
    radian: float
    """ Angle in radian unit """

    def __init__(self, degree: float = None, radian: float = None):
        if degree is not None:  # <<<<<
            self.degree = degree
            self.radian = radians(degree)
        elif radian is not None:  # <<<<<
            self.radian = radian
            self.degree = degrees(radian)
        else:
            raise ValueError("Please specify either \"degree\" or \"radian\"")

    def offset(self, degree: float = None, radian: float = None):
        """ Offsets the value of angle """
        if degree is not None:  # <<<<<
            self.degree += degree
            self.radian = radians(self.degree)
        elif radian is not None:  # <<<<<
            self.radian += radian
            self.degree = degrees(self.radian)
        else:
            raise ValueError("Please specify either \"degree\" or \"radian\"")
        return self

    def offset_new(self, degree: float):
        """ Returns a new angle object with the offset """
        return Angle(degree=(self.degree + degree))


class Vec:
    """A vector class"""
    x: float
    y: float
    a: float
    b: float
    w: float
    h: float
    def __init__(self, *args):
        if len(args) == 1:
            x = args[0][0]
            y = args[0][1]
        else:
            x = args[0]
            y = args[1]
        self.x = x
        self.y = y

        self.a = x
        self.b = y

        self.w = x
        self.h = y
    
    def sep(self):
        return self.x, self.y

    def neg(self):
        self.x = -self.x
        self.y = -self.y
        return self
    
    def neg_new(self):
        return Vec(-self.x, -self.y)

    def mod(self):
        return sqrt(sqr(self.x) + sqr(self.y))
    
    def add(a, b):
        return Vec(a.x + b.x, a.y + b.y)

    def offset(self, *offset):
        """ Offsets the position """
        self.x += offset[0]
        self.y += offset[1]
        return self  # returning self to allow chaining

    def offset_new(self, *offset):
        """ Returns a new position object with the offset """
        return Vec(self.x + offset[0], self.y + offset[1])


class DisplayMode(Enum):
    CORNER = False
    """ Render objects from the corner """
    CENTER = True
    """ Render objects from the center """


class Side:
    """ A side of a custom polygon """
    position: Vec
    """ Position of the side (base point) """
    length: float
    """ Length of the side """
    angle: Angle
    """ Rotation of the side """

    def __init__(
            self,
            position: Vec = None,
            angle: Angle = None,
            length: float = 0
        ):
        if position is None:
            position = Vec(0, 0)
        if angle is None:
            angle = Angle(degree=0)
        self.position = position
        self.angle = angle
        self.length = length
