import pygame, math

WINDOW_DIMENSION = (1600, 900)

class Car:
    def __init__(self, name, color:tuple) -> None:
        self.name = name
        self.color = color
        self.x = 100
        self.y = 800
        self.w = 50
        self.h = 100
        self.angle = 0
        self.dir = 0
    
    def get_center_pos(self):
        return (self.x-(self.w/2), self.y-(self.h/2))

    def event(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y-=1
        if keys[pygame.K_s]:
            self.y+=1

        if keys[pygame.K_a]:
            self.angle = math.pi / 4
        elif keys[pygame.K_s]:
            self.angle = - math.pi / 4
        else:
            self.angle = 0
        
        return False
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(WINDOW_DIMENSION)
        self.running = True
        self.clock = pygame.time.Clock()
        self.w = self.screen.get_width()
        self.h = self.screen.get_height()

        self.map = pygame.Surface((self.w, self.h))

        self.player = Car("Player1", (255, 0, 0))
    
    def draw_player(self):
        pygame.draw.rect(self.screen, self.player.color, ((self.w//2)-(self.player.w//2), (self.h//2)-(self.player.h//2), self.player.w, self.player.h), border_radius=10)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.running = False

            pygame.display.set_caption(f"FPS: {self.clock.get_fps()}")

            self.screen.fill((0, 0, 0))

            self.map.fill((255, 255, 255))

            x, y = self.player.get_center_pos()
            self.screen.blit(self.map, ((self.w//2)-x, (self.h//2)-y))

            self.draw_player()
            self.player.event()

            pygame.display.update()
            self.clock.tick(240)

if __name__ == "__main__":
    game = Game()
    game.run()