from math import tau
from util import Vec

WINDOW_DIMENSION = Vec(1600, 900)

FRICTION = 0.05
ACCELERATION = 0.07
TERMINAL_VELOCITY = 5
TURNING_ANGLE = tau/(720 * TERMINAL_VELOCITY)