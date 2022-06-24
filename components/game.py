import sys
from time import sleep

import pygame

from .board import Board

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
CYBER_GREEN = (0, 200, 0)
GREY = (150, 150, 150)
LIVING_CELL_COLOR = CYBER_GREEN
DEAD_CELL_COLOR = BLACK

MAX_WINDOW_HEIGHT = 800
MAX_WINDOW_WIDTH = 800
FRAME_IDLE_TIME_SECONDS = 0.01


class Game:
    def __init__(self, board: Board):
        self.board = board
        self.block_side_len = int(min(MAX_WINDOW_WIDTH / self.board.width, MAX_WINDOW_HEIGHT / self.board.height))
        self.block_border_width = 1
        self.window_width = self.block_side_len * self.board.width
        self.window_height = self.block_side_len * self.board.height
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((self.window_width, self.window_height))

    def start_game(self):
        """ start the game of life """
        pygame.init()
        self.clock = pygame.time.Clock()
        self.display.fill(DEAD_CELL_COLOR)

        while True:
            self.board.calculate_board_next_state()
            self.board.update_board_current_state()
            self.draw_grid()
            sleep(FRAME_IDLE_TIME_SECONDS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def draw_grid(self):
        """ draw the grid on the screen """
        x_counter = 0
        for x in range(0, self.window_width, self.block_side_len):
            y_counter = 0
            if x_counter == self.board.width: break
            for y in range(0, self.window_height, self.block_side_len):
                if y_counter == self.board.height: break
                current_cell_state = self.board.cells_matrix[y_counter][x_counter].current_state
                current_cell_color = LIVING_CELL_COLOR if current_cell_state == 1 else DEAD_CELL_COLOR
                rect = pygame.Rect(x - self.block_border_width,
                                   y - self.block_border_width,
                                   self.block_side_len - self.block_border_width,
                                   self.block_side_len - self.block_border_width)
                pygame.draw.rect(self.display, current_cell_color, rect)
                y_counter += 1
            x_counter += 1
