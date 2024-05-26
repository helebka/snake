import pygame

from random import randint

from objects.snake import Snake
from objects.apple import Apple
from objects.crate import Crate

from groups import crate_group

from config import WINDOW_SIZE, FPS, get_data

from menu import MainMenu

from utils import DrawSprites


def main():
    pygame.init()
    
    screen = pygame.display.set_mode(WINDOW_SIZE)
    
    # Initialize menu
    main_menu = MainMenu()
    main_menu.load_properties(screen)
    main_menu.display_menu()
    
    data = get_data()
    
    snake = Snake(100, 50)
    
    if data["selected_difficulty"] == "hard":
        crate_coords = []
        for _ in range(6):
            x, y = randint(10, WINDOW_SIZE[0] - 10), randint(10, WINDOW_SIZE[1] - 10)
            crate_coords.append((x, y))
            crate_group.add(Crate(x, y))
    
    apple = Apple(crate_coords if data["selected_difficulty"] == "hard" else None)
    
    clock = pygame.time.Clock()

    running = True
    while running:
        
        screen.fill((0, 0, 0))
        DrawSprites.draw_snake(screen, snake)
        DrawSprites.draw_apple(screen, apple)
        if data["selected_difficulty"] == "hard":
            DrawSprites.draw_crates(screen, crate_group)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if snake.direction != "up":
                        snake.direction = "down"
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    if snake.direction != "down":
                        snake.direction = "up"
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if snake.direction != "right":
                        snake.direction = "left"
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if snake.direction != "left":
                        snake.direction = "right"
        
        is_dead = snake.update(snake.direction)
        if is_dead:
            running = False
        
        if pygame.sprite.collide_rect(snake, apple):
            snake.extend()
            apple.kill()
            apple = Apple(crate_coords=crate_coords if data["selected_difficulty"] == "hard" else None)
        
        if data["selected_difficulty"] == "hard":
            if pygame.sprite.spritecollide(snake, crate_group, False):
                running = False

        pygame.display.update()

        clock.tick(FPS)
    
    DrawSprites.draw_score(screen, snake)
    pygame.display.update()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    pygame.display.quit()


if __name__ == "__main__":
    main()
