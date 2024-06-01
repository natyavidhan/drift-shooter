from math import tau
from util import Vec, Color

WINDOW_DIMENSION = Vec(1600, 900)

FRICTION = 0.05
ACCELERATION = 0.07
TERMINAL_VELOCITY = 3
TURNING_ANGLE = tau/(720 * TERMINAL_VELOCITY)
PORT = 5050

SELF_CAR = "assets\Cars\car_black_1.png"
OTHER_CAR = "assets\Cars\car_red_1.png"
CAR_SIZE = Vec(25, 50)

MAP_SIZE = Vec(1000, 1000)
MAP_COLOR = Color.from_hex("#505050")