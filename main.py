import pygame

from window import Window, Scene
from objects import Rectangle
from util import Color, DisplayMode, Vec
from car import Car
from consts import WINDOW_DIMENSION

window = Window("Window", DisplayMode.CENTER, WINDOW_DIMENSION, 420)
scene = Scene("Main", Color.from_hex("#202020"))
window.add_scene(scene)
window.set_active_scene("Main")

level = Rectangle(Vec(0, 0), Vec(1000, 1000), Color.from_hex("#505050"))
car = Car("Player1", Color.from_hex("#ff0000"))

scene.add_objs([level, car])

def escape_close(event):
    if event.key == pygame.K_ESCAPE:
        window.running = False

window.add_event_handler(pygame.KEYDOWN, escape_close)

frame = 0
def main():
    global frame
    car.event()
    if frame % 2 == 0:
        car.tick()
    window.camera = car.position
    frame += 1
    return True


window.display(main)
