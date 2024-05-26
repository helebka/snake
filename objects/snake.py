from pygame import sprite, Surface
from config import WINDOW_HEIGHT, WINDOW_WIDTH


class Snake(sprite.Sprite):

    def __init__(self, x: int, y: int) -> None:
        super().__init__()

        self.image = Surface((15, 15))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.position = [x, y]

        self.body = [
            [x, y],
            [x - 15, y],
            [x - 30, y],
            [x - 45, y],
        ]
        self.score = len(self.body) * 10

        self.direction = "right"

    def update(self, event: str) -> bool:
        if event == "left":
            self.position[0] -= 15
            self.rect.x -= 15
        if event == "right":
            self.position[0] += 15
            self.rect.x += 15
        if event == "up":
            self.position[1] -= 15
            self.rect.y -= 15
        if event == "down":
            self.position[1] += 15
            self.rect.y += 15

        # COLLIDE WITH ITSELF
        if self.position in self.body[1:]:
            return True

        # COLLIDE WITH WALLS
        if self.position[0] < 0 or self.position[0] > WINDOW_WIDTH \
                or self.position[1] < 0 or self.position[1] > WINDOW_HEIGHT:
            return True

        self.body.insert(0, list(self.position))

        self.body.pop()
        
        return False

    def extend(self) -> None:
        self.body.insert(0, list(self.position))
        self.score = len(self.body) * 10
