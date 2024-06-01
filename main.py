import pygame, socket
from sys import argv

from window import Window, Scene
from objects import Rectangle
from util import Color, DisplayMode, Vec, Angle
from car import PlayableCar, NonPlayableCar
from consts import WINDOW_DIMENSION, MAP_SIZE, MAP_COLOR

window = Window("Window", DisplayMode.CENTER, WINDOW_DIMENSION, 420)
scene = Scene("Main", Color.from_hex("#202020"))
window.add_scene(scene)
window.set_active_scene("Main")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try: name = argv[1]
except: raise Exception("""Please specify a name
example: py main.py username ip_address port""")

try: client.connect((argv[2], int(argv[3])))
except: raise Exception("""Please specify a ip_address and port
example: py main.py username ip_address port""")

client.send(str.encode(name))
ID = client.recv(2048).decode()

level = Rectangle(Vec(0, 0), MAP_SIZE, MAP_COLOR)
player = PlayableCar(name, ID, client)

scene.add_objs([level, player])

def escape_close(event):
    if event.key == pygame.K_ESCAPE:
        window.running = False

window.add_event_handler(pygame.KEYDOWN, escape_close)

frame = 0

def main():
    player.event()
    window.camera = player.position
    
    client.send(str.encode("get:all"))
    cars = client.recv(2048).decode()
    car_objects = []
    for car in cars.split("||")[1:]:
        v = [j.split(":")[1] for j in car.split("|")]
        car_objects.append(NonPlayableCar(
            v[0],
            v[1],
            Vec(float(v[2]), float(v[3])),
            Angle(degree=float(v[4]))
        ))
    scene.objs[2:] = car_objects
    return True


window.display(main)
