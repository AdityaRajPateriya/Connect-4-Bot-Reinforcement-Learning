import math
import sys
import pygame
from Board import Board
from MainMenu import MainMenu

class ConnectFourGame:
    def __init__(self):
        self.ROW_COUNT = 6
        self.COLUMN_COUNT = 7
        self.board = Board(self.ROW_COUNT, self.COLUMN_COUNT)
        self.game_over = False
        self.turn = 0
        self.main_menu = MainMenu()
        self.init_pygame()
        self.current_state = "MAIN_MENU"  # Initial state is the main menu

    def init_pygame(self):
        pygame.init()
        self.SQUARESIZE = 100
        self.width = self.COLUMN_COUNT * self.SQUARESIZE
        self.height = (self.ROW_COUNT + 1) * self.SQUARESIZE
        self.size = (self.width, self.height)
        self.RADIUS = int(self.SQUARESIZE / 2 - 5)
        self.screen = pygame.display.set_mode(self.size)
        self.myfont = pygame.font.SysFont("monospace", 75)

    def run_game(self):
        while True:
            if self.current_state == "MAIN_MENU":
                self.handle_main_menu()
            elif self.current_state == "2_PLAYER_GAME":
                self.handle_2_player_game()
            elif self.current_state == "VS_AI_GAME":
                self.handle_vs_ai_game()
            elif self.current_state == "GAME_OVER":
                self.handle_game_over()

    def handle_main_menu(self):
        menu_choice = self.main_menu.run_menu()
        if menu_choice == "2_PLAYER":
            self.current_state = "2_PLAYER_GAME"
            self.reset_game()
        elif menu_choice == "VS_AI":
            self.current_state = "VS_AI_GAME"
            self.reset_game()
        elif menu_choice == "QUIT":
            sys.exit()

    def handle_2_player_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                self.board.update_hover_circle(self.turn, event.pos[0])
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                col = self.get_clicked_column(event.pos[0])
                if self.is_valid_location(col):
                    row = self.board.get_next_open_row(col)
                    self.board.drop_piece(row, col, self.turn + 1)
                    if self.board.winning_move(self.turn + 1):
                        self.display_winner(self.turn + 1)
                        self.current_state = "GAME_OVER"
                    elif self.board.is_full():  # Check for a tie
                        self.current_state = "GAME_OVER"
                    self.turn += 1
                    self.turn %= 2
                    self.board.draw_board(self.screen)
                    pygame.display.update()

    def handle_vs_ai_game(self):
        # Implement game logic for playing against AI here
        pass

    def handle_game_over(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.current_state = "MAIN_MENU"

    def reset_game(self):
        self.board.create_board()
        self.game_over = False
        self.turn = 0
        self.board.draw_board(self.screen)

    def get_clicked_column(self, posx):
        return int(math.floor(posx / self.SQUARESIZE))

    def is_valid_location(self, col):
        return self.board.is_valid_location(col)

    def display_winner(self, player):
        if player == 1:
            label = self.myfont.render("Player 1 wins!!", 1, (255, 0, 0))
        else:
            label = self.myfont.render("Player 2 wins!!", 1, (255, 255, 0))
        self.screen.blit(label, (40, 10))
        pygame.display.update()
