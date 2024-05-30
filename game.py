import pygame

from car import Car
from consts import WINDOW_DIMENSION

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(WINDOW_DIMENSION)
        self.running = True
        self.clock = pygame.time.Clock()
        self.map = pygame.Surface(WINDOW_DIMENSION)

        self.player = Car("Player1", (255, 0, 0))
    
    def draw_player(self):
        pygame.draw.rect(
            self.screen,
            self.player.color,
            (
                WINDOW_DIMENSION[0]//2 - self.player.size.w//2 ,
                WINDOW_DIMENSION[1]//2 - self.player.size.h//2,
                self.player.size.w,
                self.player.size.h
            ),
            border_radius=1
        )

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.running = False

            pygame.display.set_caption(f"FPS: {self.clock.get_fps()}")

            self.screen.fill((0, 0, 0))

            self.map.fill((255, 255, 255))

            x, y = self.player.get_center_pos()
            self.screen.blit(self.map, (self.w//2 - x, self.h//2 - y))

            self.draw_player()
            self.player.event()

            pygame.display.update()
            self.clock.tick(240)