import pygame

from objects import Rectangle
from window import Window, Scene
from util import Color, DisplayMode, Vec
from car import Car
from consts import WINDOW_DIMENSION

window = Window("Window", DisplayMode.CENTER, Vec(1600, 800), 420)
scene = Scene("Main", Color.from_hex("#202020"))
window.add_scene(scene)
window.set_active_scene("Main")
car = Car("Player1", Color.from_hex("#ff0000"))
scene.add_obj(car)

def escape_close(event):
    if event.key == pygame.K_ESCAPE:
        window.running = False

window.add_event_handler(pygame.KEYDOWN, escape_close)

def main():
    car.event()
    car.tick()
    return True


window.display(main)
