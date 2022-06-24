from .cell import Cell


class Board:
    def __init__(self, dimensions: tuple, initial_living_cell_coordinates: list, static_cells_coordinates: list):
        self.width = dimensions[0]
        self.height = dimensions[1]
        self.cells_matrix = [[Cell() for j in range(self.width)] for i in range(self.height)]
        self.static_cells = {hash(cell_coordinates): self.cells_matrix[cell_coordinates[1]][cell_coordinates[0]] for
                             cell_coordinates in static_cells_coordinates}

        # set initial living cells to be alive
        for coordinates in initial_living_cell_coordinates:
            self.cells_matrix[coordinates[1] - 1][coordinates[0] - 1].current_state = 1

        # set static living cells to be alive
        for cell in self.static_cells.values():
            cell.current_state = 1

    def _get_neighbour_cells_current_state(self, cell_x, cell_y):
        """ get the  """
        neighbours_cells_states = []
        neighbour_cells_xs = [i for i in [cell_x - 1, cell_x, cell_x + 1] if not ((i == self.width + 1) or (i == -1))]
        neighbour_cells_ys = [j for j in [cell_y - 1, cell_y, cell_y + 1] if not ((j == self.height + 1) or (j == -1))]
        for y in neighbour_cells_ys:
            for x in neighbour_cells_xs:
                if not ((x == cell_x) and (y == cell_y)):
                    neighbours_cells_states.append(self.cells_matrix[y - 1][x - 1].current_state)
        return neighbours_cells_states

    def calculate_board_next_state(self):
        for y in range(self.height):
            for x in range(self.width):
                self._get_neighbour_cells_current_state(x, y)
                self.cells_matrix[y][x].calculate_next_state(self._get_neighbour_cells_current_state(x, y))

    def update_board_current_state(self):
        for y in range(self.height):
            for x in range(self.width):
                if hash((x, y)) not in self.static_cells.keys():  # don't change the static living cells state
                    self.cells_matrix[y][x].update_current_state()
