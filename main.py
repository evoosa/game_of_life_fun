from components.board import Board

if __name__ == '__main__':
    dimensions = (7, 7)
    initial_living_cell_coordinates = (3, 4)
    board = Board(dimensions, initial_living_cell_coordinates)
    board.calculate_next_state()
    board.update_current_state()
