import pygame
import socket, sys

from window import Window, Scene
from objects import Rectangle, Image
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
car_img = pygame.image.load("assets\Cars\car_red_1.png").convert()

def main():
    car.event()
    window.camera = car.position
    
    client.send(str.encode("get:all"))
    cars = client.recv(2048).decode()
    print(cars)
    for car_ in cars.split("||")[1:]:
        v = [i.split(":")[1] for i in car_.split("|")]
        # print(v)
        Image(Vec(float(v[2]), float(v[3])), Vec(25, 50), car_img, float(v[4]))
    return True


window.display(main)
