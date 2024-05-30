class Car:
    def __init__(self, name, color:tuple) -> None:
        self.name = name
        self.color = color
        self.position = {
            "x": 100,
            "y": 800
        }
        self.size = {
            "w": 50,
            "h": 100
        }
        self.angle = 0
    
    def get_center_pos(self):
        x, y = self.position["x"], self.position["y"]
        w, h = self.size["w"], self.size["h"]
        return x - w/2, y - h/2

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