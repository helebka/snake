from typing import Optional

from pygame import sprite, Surface
from random import randint

from config import WINDOW_HEIGHT, WINDOW_WIDTH


class Apple(sprite.Sprite):
    
    def __init__(self, crate_coords: Optional[list] = None) -> None:
        super().__init__()
        
        self.image = Surface((15, 15))
        self.rect = self.image.get_rect()
        
        self.rect.x = randint(20, WINDOW_WIDTH - 20)
        self.rect.y = randint(20, WINDOW_HEIGHT - 20)

        if crate_coords is not None and (self.rect.x, self.rect.y) in crate_coords:
            while (self.rect.x, self.rect.y) in crate_coords:
                self.rect.x = randint(20, WINDOW_WIDTH - 20)
                self.rect.y = randint(20, WINDOW_HEIGHT - 20)
