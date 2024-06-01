import pygame
import socket

from objects import Image
from util import Angle, Vec
from consts import SELF_CAR, OTHER_CAR, CAR_SIZE

def sgn(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

class NonPlayableCar(Image):
    def __init__(self, ID: int, name: str, position: Vec, rotation: Angle) -> None:
        self.name = name
        self.ID = ID
        super().__init__(position, CAR_SIZE, OTHER_CAR, rotation)

class PlayableCar(Image):
    def __init__(self, ID: int, name: str, client: socket.socket) -> None:
        self.name = name
        self.ID = ID
        self.client = client
        super().__init__(Vec(0, 0), CAR_SIZE, SELF_CAR)
    
    def send(self, command: str) -> str:
        self.client.send(str.encode(command))
        return self.client.recv(2048).decode()

    def event(self):
        keys = pygame.key.get_pressed()
        comm = "keypress:"
        if keys[pygame.K_w]:
            comm+="w"
        if keys[pygame.K_s]:
            comm+="s"
        if keys[pygame.K_a]:
            comm+="a"
        if keys[pygame.K_d]:
            comm+="d"

        try: pos = self.send(comm)
        except: raise Exception("Failed to send a message to the server")

        values = [float(i.split(":")[1]) for i in pos.split("|")]
        self.position= Vec(values[:2])
        self.rotation = Angle(values[2])
