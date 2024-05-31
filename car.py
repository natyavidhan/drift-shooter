import pygame
from math import sin, cos

from objects import Rectangle
from util import Color, Vec
from consts import ACCELERATION, FRICTION, TERMINAL_VELOCITY, TURNING_ANGLE, WINDOW_DIMENSION

def sgn(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

class Car(Rectangle):
    def __init__(self, name, color: Color) -> None:
        self.name = name
        self.vel = Vec(0, 0)
        self.acc = Vec(0, 0)
        self.accelerating = False
        super().__init__(Vec(WINDOW_DIMENSION.w//2, WINDOW_DIMENSION.h//2), Vec(5, 10), color)
    
    def assign_acc(self, amplitude):
        self.acc.x = amplitude * sin(-self.rotation.radian)
        self.acc.y = amplitude * cos(-self.rotation.radian)
    
    def tick(self):
        # friction
        if not self.accelerating:
            self.acc.x = -sgn(self.vel.x)*min(FRICTION, abs(self.vel.x))
            self.acc.y = -sgn(self.vel.y)*min(FRICTION, abs(self.vel.y))

        self.vel = Vec.add(self.vel, self.acc)

        self.vel.x = sgn(self.vel.x)*min(TERMINAL_VELOCITY, abs(self.vel.x))
        self.vel.y = sgn(self.vel.y)*min(TERMINAL_VELOCITY, abs(self.vel.y))

        self.center = Vec.add(self.center, self.vel)
        self.accelerating = False

    def event(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.accelerating = True
            self.assign_acc(-ACCELERATION + FRICTION)
        if keys[pygame.K_s]:
            self.accelerating = True
            self.assign_acc(ACCELERATION - FRICTION)

        if keys[pygame.K_a]:
            self.rotation.offset(-TURNING_ANGLE)
        elif keys[pygame.K_d]:
            self.rotation.offset(TURNING_ANGLE)