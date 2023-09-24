import numpy as np
import pygame


class Board:
    def __init__(self, row_count, column_count):
        self.ROW_COUNT = row_count
        self.COLUMN_COUNT = column_count
        self.board = np.zeros((self.ROW_COUNT, self.COLUMN_COUNT))
        self.SQUARESIZE = 100
        self.RADIUS = int(self.SQUARESIZE / 2 - 5)
        self.width = self.COLUMN_COUNT * self.SQUARESIZE
        self.height = (self.ROW_COUNT + 1) * self.SQUARESIZE
        self.size = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.size)

    def create_board(self):
        self.board = np.zeros((self.ROW_COUNT, self.COLUMN_COUNT))

    def drop_piece(self, row, col, piece):
        self.board[row][col] = piece

    def is_valid_location(self, col):
        return self.board[self.ROW_COUNT - 1][col] == 0

    def get_next_open_row(self, col):
        for r in range(self.ROW_COUNT):
            if self.board[r][col] == 0:
                return r

    def printBoard(board):
        print(np.flip(board, 0))

    def winning_move(self, piece):
        # Check horizontal locations for win
        for c in range(self.COLUMN_COUNT - 3):
            for r in range(self.ROW_COUNT):
                if (
                        self.board[r][c] == piece
                        and self.board[r][c + 1] == piece
                        and self.board[r][c + 2] == piece
                        and self.board[r][c + 3] == piece
                ):
                    return True

        # Check vertical locations for win
        for c in range(self.COLUMN_COUNT):
            for r in range(self.ROW_COUNT - 3):
                if (
                        self.board[r][c] == piece
                        and self.board[r + 1][c] == piece
                        and self.board[r + 2][c] == piece
                        and self.board[r + 3][c] == piece
                ):
                    return True

        # Check positively sloped diagonals
        for c in range(self.COLUMN_COUNT - 3):
            for r in range(self.ROW_COUNT - 3):
                if (
                        self.board[r][c] == piece
                        and self.board[r + 1][c + 1] == piece
                        and self.board[r + 2][c + 2] == piece
                        and self.board[r + 3][c + 3] == piece
                ):
                    return True

        # Check negatively sloped diagonals
        for c in range(self.COLUMN_COUNT - 3):
            for r in range(3, self.ROW_COUNT):
                if (
                        self.board[r][c] == piece
                        and self.board[r - 1][c + 1] == piece
                        and self.board[r - 2][c + 2] == piece
                        and self.board[r - 3][c + 3] == piece
                ):
                    return True

    def draw_board(self, screen):
        for c in range(self.COLUMN_COUNT):
            for r in range(self.ROW_COUNT):
                pygame.draw.rect(
                    screen,
                    (0, 0, 255),
                    (c * self.SQUARESIZE, r * self.SQUARESIZE + self.SQUARESIZE, self.SQUARESIZE, self.SQUARESIZE),
                )
                pygame.draw.circle(
                    screen,
                    (0, 0, 0),
                    (
                        int(c * self.SQUARESIZE + self.SQUARESIZE / 2),
                        int(r * self.SQUARESIZE + self.SQUARESIZE + self.SQUARESIZE / 2),
                    ),
                    self.RADIUS,
                )

        for c in range(self.COLUMN_COUNT):
            for r in range(self.ROW_COUNT):
                if self.board[r][c] == 1:
                    pygame.draw.circle(
                        screen,
                        (255, 0, 0),
                        (
                            int(c * self.SQUARESIZE + self.SQUARESIZE / 2),
                            self.height - int(r * self.SQUARESIZE + self.SQUARESIZE / 2),
                        ),
                        self.RADIUS,
                    )
                elif self.board[r][c] == 2:
                    pygame.draw.circle(
                        screen,
                        (255, 255, 0),
                        (
                            int(c * self.SQUARESIZE + self.SQUARESIZE / 2),
                            self.height - int(r * self.SQUARESIZE + self.SQUARESIZE / 2),
                        ),
                        self.RADIUS,
                    )

    def update_hover_circle(self, turn, posx):
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, self.width, self.SQUARESIZE))
        if turn == 0:
            pygame.draw.circle(self.screen, (255, 0, 0), (posx, int(self.SQUARESIZE / 2)), self.RADIUS)
        else:
            pygame.draw.circle(self.screen, (255, 255, 0), (posx, int(self.SQUARESIZE / 2)), self.RADIUS)

    def get_height(self):
        return self.height
