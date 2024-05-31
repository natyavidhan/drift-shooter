import pygame
import socket, sys

from window import Window, Scene
from objects import Rectangle
from util import Color, DisplayMode, Vec
from car import Car
from consts import WINDOW_DIMENSION

window = Window("Window", DisplayMode.CENTER, WINDOW_DIMENSION, 420)
scene = Scene("Main", Color.from_hex("#202020"))
window.add_scene(scene)
window.set_active_scene("Main")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

name = sys.argv[1]

client.connect(("localhost", 5050))
client.send(str.encode(name))
ID = client.recv(2048).decode()

level = Rectangle(Vec(0, 0), Vec(1000, 1000), Color.from_hex("#505050"))
car = Car(name, ID, client)

scene.add_objs([level, car])

def escape_close(event):
    if event.key == pygame.K_ESCAPE:
        window.running = False

window.add_event_handler(pygame.KEYDOWN, escape_close)

frame = 0
def main():
    global frame
    car.event()
    window.camera = car.position
    frame += 1
    return True


window.display(main)
