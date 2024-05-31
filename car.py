import pygame
from math import sin, cos

from objects import Image
from util import Angle, Color, Vec
from consts import ACCELERATION, FRICTION, TERMINAL_VELOCITY, TURNING_ANGLE, WINDOW_DIMENSION

def sgn(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

class ServerCar:
    def __init__(self, id: int, name: str) -> None:
        self.name = name
        self.id = id
        self.center = Vec(0, 0)
        self.vel = Vec(0, 0)
        self.acc = Vec(0, 0)
        self.accelerating = False
        self.rotation = Angle(degree=0)

    def assign_acc(self, amplitude):
        self.acc.x = amplitude * sin(-self.rotation.radian)
        self.acc.y = amplitude * cos(-self.rotation.radian)

    def tick(self):
        # friction
        if not self.accelerating:
            self.acc.x = -sgn(self.vel.x)*min(FRICTION * 0.65, abs(self.vel.x))
            self.acc.y = -sgn(self.vel.y)*min(FRICTION * 0.65, abs(self.vel.y))

        self.vel = Vec.add(self.vel, self.acc)
        self.id = id

        velocity = self.vel.mod()
        if velocity > TERMINAL_VELOCITY:
            self.vel.y = self.vel.y * TERMINAL_VELOCITY / velocity
            self.vel.x = self.vel.x * TERMINAL_VELOCITY / velocity
        
        self.position = Vec.add(self.position, self.vel)
        self.accelerating = False
    
    def event_w(self):
        self.accelerating = True
        self.assign_acc(-ACCELERATION + FRICTION)
    
    def event_s(self):
        self.accelerating = True
        self.assign_acc(ACCELERATION - FRICTION)
    
    def event_a(self):
        vel = self.vel.mod()
        if vel == 0:
            return
        self.rotation.offset(radian=-TURNING_ANGLE * vel)
    
    def event_d(self):
        vel = self.vel.mod()
        if vel == 0:
            return
        self.rotation.offset(radian=TURNING_ANGLE * vel)
    
    def update_client(self):
        pass
        # send position
        # send color

class Car(Image):
    def __init__(self, id: int, name: str) -> None:
        self.name = name
        self.id = id
        super().__init__(Vec(0, 0), Vec(25, 50), "assets\Cars\car_black_1.png")
    
    def event(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.event_w()
            pass
            # socket event_w
        if keys[pygame.K_s]:
            self.event_s()
            pass
            # socket event_s

        if keys[pygame.K_a]:
            self.event_a()
            pass
            # socket event_a
        elif keys[pygame.K_d]:
            self.event_d()
            pass
            # socket event_d