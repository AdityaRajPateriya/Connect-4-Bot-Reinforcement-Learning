import numpy as np
import pygame
import sys
import math

from Board import Board
from Player import Player


class ConnectFourGame:
    def __init__(self):
        self.ROW_COUNT = 6
        self.COLUMN_COUNT = 7
        self.board = Board(self.ROW_COUNT, self.COLUMN_COUNT)
        self.game_over = False
        self.turn = 0
        self.init_pygame()

    def init_pygame(self):
        pygame.init()
        self.SQUARESIZE = 100
        self.width = self.COLUMN_COUNT * self.SQUARESIZE
        self.height = (self.ROW_COUNT + 1) * self.SQUARESIZE
        self.size = (self.width, self.height)
        self.RADIUS = int(self.SQUARESIZE / 2 - 5)
        self.screen = pygame.display.set_mode(self.size)
        self.board.draw_board(self.screen)
        pygame.display.update()
        self.myfont = pygame.font.SysFont("monospace", 75)

    def run_game(self):
        while not self.game_over:
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
                            self.display_winner()
                            self.game_over = True
                        self.turn += 1
                        self.turn %= 2
                        self.board.draw_board(self.screen)
                        pygame.display.update()
                        if self.game_over:
                            pygame.time.wait(3000)

    def get_clicked_column(self, posx):
        return int(math.floor(posx / self.SQUARESIZE))

    def is_valid_location(self, col):
        return self.board.is_valid_location(col)

    def display_winner(self):
        if self.turn == 0:
            label = self.myfont.render("Player 1 wins!!", 1, (255, 0, 0))
        else:
            label = self.myfont.render("Player 2 wins!!", 1, (255, 255, 0))
        self.screen.blit(label, (40, 10))
        pygame.display.update()
