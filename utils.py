import os
import sys
import pygame

from config import get_data, write_data
from objects.snake import Snake
from objects.apple import Apple


def load_image(name, colorkey=None):
    fullname = os.path.join('data/images', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class DrawSprites:
    @staticmethod
    def draw_snake(screen: pygame.Surface, snake: Snake):
        snake_images = [
            load_image("snake_body.png") for _ in range(len(snake.body) - 2)
        ]
        snake_images.insert(0, load_image("snake_head.png"))
        snake_images.append(load_image("snake_tail.png"))

        for i in range(len(snake.body)):
            screen.blit(snake_images[i], snake.body[i])

    @staticmethod
    def draw_apple(screen: pygame.Surface, apple: Apple):
        screen.blit(load_image("apple.png"), apple.rect)

    @staticmethod
    def draw_crates(screen: pygame.Surface, crates: pygame.sprite.Group):
        for crate in crates:
            screen.blit(load_image("crate.png"), crate.rect)

    @staticmethod
    def draw_score(screen: pygame.Surface, snake: Snake):
        # Update score
        data = get_data()
        data["max_score"] = max(snake.score, data["max_score"])
        write_data(data)

        # Display score
        score = "Score: " + str(snake.score)
        max_score = "Max score: " + str(data["max_score"])

        score_text = pygame.font.Font("data/font/MainFont.ttf", 30).render(
            score, True, (255, 255, 255)
        )
        max_score_text = pygame.font.Font("data/font/MainFont.ttf", 20).render(
            max_score, True, (255, 255, 255)
        )
        
        screen.blit(score_text, (300, 40))
        screen.blit(max_score_text, (300, 70))
        