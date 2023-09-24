import pygame
import sys


class MainMenu:
    def __init__(self):
        self.width = 400
        self.height = 300
        pygame.font.init()
        self.menu_screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Connect Four Main Menu")

        # Adjusted positions and sizes
        self.title_font = pygame.font.Font(None, 48)
        self.menu_font = pygame.font.Font(None, 36)
        self.title_text = self.title_font.render("Connect Four", True, (0, 0, 0))  # Text color is black
        self.title_rect = self.title_text.get_rect(center=(self.width // 2, self.height // 4))

        self.menu_options = {
            "2_PLAYER": pygame.Rect(self.width // 4, self.height // 2, self.width // 2, 50),
            "VS_AI": pygame.Rect(self.width // 4, self.height // 2 + 60, self.width // 2, 50),
            "QUIT": pygame.Rect(self.width // 4, self.height // 2 + 120, self.width // 2, 50),
        }

    def run_menu(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for option, rect in self.menu_options.items():
                        if rect.collidepoint(event.pos):
                            return option

            # Set background to white
            self.menu_screen.fill((255, 255, 255))

            # Blit the title text
            self.menu_screen.blit(self.title_text, self.title_rect)

            # Blit menu options
            for option, rect in self.menu_options.items():
                pygame.draw.rect(self.menu_screen, (0, 120, 200), rect)
                text = self.menu_font.render(option, True, (255, 255, 255))  # Text color is white
                text_rect = text.get_rect(center=rect.center)
                self.menu_screen.blit(text, text_rect)

            pygame.display.flip()
