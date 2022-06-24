import sys

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
        self.window_width = self.block_side_len * self.board.width
        self.window_height = self.block_side_len * self.board.height
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))

    def main(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen.fill(WHITE)

        while True:
            self.draw_grid()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def draw_grid(self):
        for x in range(0, MAX_WINDOW_WIDTH, self.block_side_len):
            if x > self.window_width: break
            for y in range(0, MAX_WINDOW_HEIGHT, self.block_side_len):
                if y > self.window_height: break
                # current_cell = self.board.matrix[y][x]
                rect = pygame.Rect(x, y, self.block_side_len, self.block_side_len)
                pygame.draw.rect(self.screen, GREY, rect, 1)

    #     for y in range(height):
    #         for x in range(width):
    #             rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
    #             pygame.draw.rect(window, color, rect)
    #


if __name__ == '__main__':
    dimensions = (10, 10)
    initial_living_cell_coordinates = (1, 1)  # FIXME
    board = Board(dimensions, initial_living_cell_coordinates)
    board.calculate_next_state()
    board.update_current_state()
    g = Game(board)
    g.main()
    # main()
