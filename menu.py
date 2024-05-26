import sys
import pygame

from config import get_data, write_data


class MainMenu:
    screen: pygame.Surface
    font: pygame.font.Font

    def load_properties(self, screen: pygame.Surface):
        self.screen = screen
        self.font = pygame.font.Font("data/font/MainFont.ttf", 30)

    def display_menu(self) -> None:
        self.screen.fill((0, 0, 0))

        play_button = pygame.Rect(300, 300, 200, 60)
        play_button_text = self.font.render("Play", True, (0, 0, 0))

        self.display_button(
            play_button,
            play_button_text,
            play_button.x,
            play_button.y,
            "Play"
        )

        difficulty_button = pygame.Rect(300, 400, 200, 60)
        difficulty_button_text = self.font.render(
            "Difficulty", True, (0, 0, 0))

        self.display_button(
            difficulty_button,
            difficulty_button_text,
            difficulty_button.x,
            difficulty_button.y,
            "Difficulty"
        )
        
        self.draw_text(
            "Your difficulty is: " + get_data()["selected_difficulty"],
            190, 
            500
        )

        pygame.display.update()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.collidepoint(event.pos):
                        running = False
                    elif difficulty_button.collidepoint(event.pos):
                        data = get_data()
                        difficulty = "hard" if data["selected_difficulty"] == "easy" else "easy"
                        data["selected_difficulty"] = difficulty
                        write_data(data)

                        # Reset screen
                        self.screen.fill((0, 0, 0))

                        self.display_button(
                            play_button,
                            play_button_text,
                            play_button.x,
                            play_button.y,
                            "Play"
                        )

                        self.display_button(
                            difficulty_button,
                            difficulty_button_text,
                            difficulty_button.x,
                            difficulty_button.y,
                            "Difficulty"
                        )
                        
                        self.draw_text(
                            "Your difficulty is: " + difficulty, 
                            190, 
                            500
                        )
                        
                        pygame.display.update()

    def draw_text(self, text: str, x: int, y: int):
        text = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(text, (x, y))

    def display_button(
        self,
        button_rect: pygame.Rect,
        button_text: pygame.Surface,
        button_x_pos: int,
        button_y_pos: int,
        text: str
    ):
        pygame.draw.rect(self.screen, (255, 255, 255), button_rect)
        if len(text) <= 5:
            self.screen.blit(
                button_text, (button_x_pos + 60, button_y_pos + 8))
        else:
            self.screen.blit(
                button_text, (button_x_pos + 15, button_y_pos + 8))
