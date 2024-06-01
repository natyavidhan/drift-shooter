import pygame
from math import sin, cos
import socket

from objects import Image
from util import Angle, Vec
from consts import ACCELERATION, FRICTION, TERMINAL_VELOCITY, TURNING_ANGLE, WINDOW_DIMENSION

def sgn(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

class Car(Image):
    def __init__(self, ID: int, name: str, client:socket.socket) -> None:
        self.name = name
        self.ID = ID
        self.client = client
        super().__init__(Vec(0, 0), Vec(25, 50), "assets\Cars\car_black_1.png")
    
    def send(self, command:str) -> str:
        self.client.send(str.encode(command))
        return self.client.recv(2048).decode()

    def event(self):
        keys = pygame.key.get_pressed()
        comm = "keypress:"
        if keys[pygame.K_w]:
            comm+="w"
        if keys[pygame.K_s]:
            comm+=",s"
        if keys[pygame.K_a]:
            comm+=",a"
        if keys[pygame.K_d]:
            comm+=",d"
        pos = self.send(comm)
        print(pos)
        values = [float(i.split(":")[1]) for i in pos.split("|")]
        self.position.x = values[0]
        self.position.y = values[1]
        self.rotation = Angle(values[2])
