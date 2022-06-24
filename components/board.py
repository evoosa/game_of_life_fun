from cell import Cell


class Board:
    def __init__(self, dimensions: tuple, initial_living_cell_coordinates: tuple):
        self.width = dimensions[0]
        self.height = dimensions[1]
        self.matrix = [[Cell() for j in range(self.width)] for i in range(self.height)]
        self.matrix[initial_living_cell_coordinates[1]][initial_living_cell_coordinates[0]].current_state = 1

    def get_neighbour_cells_current_state(self, cell_x, cell_y):
        neighbours_cells_states = []
        xs = [i for i in [cell_x - 1, cell_x, cell_x + 1] if not ((i == self.width + 1) or (i == -1))]
        ys = [j for j in [cell_y - 1, cell_y, cell_y + 1] if not ((j == self.height + 1) or (j == -1))]
        for _y in ys:
            for _x in xs:
                if not ((_x == cell_x) and (_y == cell_y)):
                    neighbours_cells_states.append(self.matrix[_y - 1][_x - 1].current_state)
        return neighbours_cells_states

    def calculate_next_state(self, ):
        for y in range(self.height):
            for x in range(self.width):
                self.get_neighbour_cells_current_state(x, y)
                self.matrix[y][x].calculate_next_state(self.get_neighbour_cells_current_state(x, y))

    def update_current_state(self):
        for y in range(self.height):
            for x in range(self.width):
                self.matrix[y][x].update_current_state()
