import pygame, math

from vec import Vec

FRICTION = 0.25
ACCELERATION = 0.4

def sgn(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

class Car(Vec):
    def __init__(self, name, color: tuple) -> None:
        self.name = name
        self.color = color
        super().__init__(100, 800)
        self.vel = Vec(0, 0)
        self.acc = Vec(0, 0)
        self.size = Vec(50, 100)
        self.angle = 0
        self.accelerating = False
    
    def get_center_pos(self):
        x, y = self.sep()
        w, h = self.size.sep()
        return x - w/2, y - h/2
    
    def assign_acc(self, amplitude):
        self.acc.x = amplitude * math.sin(self.angle)
        self.acc.y = amplitude * math.cos(self.angle)
    
    def tick(self):
        # friction
        if not self.accelerating:
            self.acc.x = -sgn(self.vel.x)*min(FRICTION, abs(self.vel.x))
            self.acc.y = -sgn(self.vel.y)*min(FRICTION, abs(self.vel.y))

        self.vel = Vec.add(self.vel, self.acc)
        self.x, self.y = Vec.add(self, self.vel).sep()

    def event(self):
        keys = pygame.key.get_pressed()
        self.accelerating = False
        if keys[pygame.K_w]:
            self.assign_acc(-ACCELERATION + FRICTION)
            self.accelerating = True
        if keys[pygame.K_s]:
            self.assign_acc(ACCELERATION - FRICTION)
            self.accelerating = True

        if keys[pygame.K_a]:
            self.angle += math.pi / 24
        elif keys[pygame.K_d]:
            self.angle -= math.pi / 24