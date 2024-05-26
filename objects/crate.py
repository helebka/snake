from pygame import sprite, Surface
from random import randint

from config import WINDOW_HEIGHT, WINDOW_WIDTH


class Crate(sprite.Sprite):
    
    def __init__(self, x: int, y: int) -> None:
        super().__init__()
        
        self.image = Surface((15, 15))
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
