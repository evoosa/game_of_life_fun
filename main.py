from components.board import Board
from components.game import Game

if __name__ == '__main__':
    board_dimensions = (50, 50)
    static_cells_step = 5
    initial_living_cells_coordinates = [
        (2, 5),
        (3, 5),
        (4, 5),
        (3, 6),
    ]
    static_cells_coordinates = []
    # calculate the static cells coordinates dynamically
    for i in range(0, board_dimensions[0], static_cells_step):
        for j in range(0, board_dimensions[1], static_cells_step):
            static_cells_coordinates.append((i, j))

    board = Board(board_dimensions, initial_living_cells_coordinates, static_cells_coordinates)
    game = Game(board)
    game.start_game()
