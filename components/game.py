import sys

import pygame

from board import Board

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
BLOCKSIZE = 20  # size of the grid block


class Game:
    def __init__(self, board: Board):
        # self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        # self.clock = pygame.time.Clock()
        self.board_width = board.width
        self.board_height = board.height
        self.block_side_len = self._get_block_dimensions()

    def _get_block_dimensions(self) -> int:
        block_width = int(WINDOW_WIDTH / self.board_width)
        block_height = int(WINDOW_HEIGHT / self.board_height)
        return min(block_height, block_width)

    # def main(self):
    #     # global self.screen, self.clock
    #     pygame.init()
    #     self.clock = pygame.time.Clock()
    #     self.screen.fill(BLACK)
    #
    #     while True:
    #         self.drawGrid()
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 pygame.quit()
    #                 sys.exit()
    #
    #         pygame.display.update()

    # def drawGrid():
    #     # for x in range(0, WINDOW_WIDTH, BLOCKSIZE):
    #     #     for y in range(0, WINDOW_HEIGHT, BLOCKSIZE):
    #     #         rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
    #     #         pygame.draw.rect(self.screen, WHITE, rect, 1)
    #     for y in range(height):
    #         for x in range(width):
    #             rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
    #             pygame.draw.rect(window, color, rect)
    #

if __name__ == '__main__':
    dimensions = (10, 7)
    initial_living_cell_coordinates = (1, 1) # FIXME
    board = Board(dimensions, initial_living_cell_coordinates)
    board.calculate_next_state()
    board.update_current_state()
    g = Game(board)
    print(g.block_side_len)
    # main()
