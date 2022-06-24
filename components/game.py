import sys
from time import sleep

import pygame

from board import Board

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREY = (150, 150, 150)
MAX_WINDOW_HEIGHT = 800
MAX_WINDOW_WIDTH = 800


class Game:
    def __init__(self, board: Board):
        self.board = board
        self.block_side_len = int(min(MAX_WINDOW_WIDTH / self.board.width, MAX_WINDOW_HEIGHT / self.board.height))
        self.block_border_width = 1
        self.window_width = self.block_side_len * self.board.width
        self.window_height = self.block_side_len * self.board.height
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((self.window_width, self.window_height))

    def main(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.display.fill(GREY)

        while True:
            self.board.calculate_next_state()
            self.board.update_current_state()
            self.draw_grid()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def draw_grid(self):
        sleep(0.1)
        x_counter = 0
        for x in range(0, self.window_width, self.block_side_len):
            y_counter = 0
            if x_counter == (self.board.width): break
            for y in range(0, self.window_height, self.block_side_len):
                if y_counter == (self.board.height): break
                current_cell_state = self.board.matrix[y_counter][x_counter].current_state
                current_cell_color = BLACK if current_cell_state == 1 else WHITE
                rect = pygame.Rect(x - self.block_border_width,
                                   y - self.block_border_width,
                                   self.block_side_len - self.block_border_width,
                                   self.block_side_len - self.block_border_width)
                pygame.draw.rect(self.display, current_cell_color, rect)
                y_counter += 1
            x_counter += 1


if __name__ == '__main__':
    dimensions = (100, 100)
    initial_living_cells_coordinates = [
        (2, 5),
        (3, 5),
        (4, 5),
        (3, 6),
        (4, 6),
        (2, 7),
        (3, 8),
        (4, 7),
        (3, 7),
        (4, 7)
    ]  # FIXME
    # static_cells_coordinates = [
    #
    # ]
    board = Board(dimensions, initial_living_cells_coordinates)
    g = Game(board)
    g.main()
    # main()
