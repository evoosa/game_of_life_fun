class Cell:
    def __init__(self):
        self.current_state = 0
        self.new_state = 0

    def calculate_next_state(self, neighbour_cell_states: list):
        living_neighbour_cells_count = sum(neighbour_cell_states)
        if self.current_state == 1:  # if cell is alive
            if (living_neighbour_cells_count < 2) or (living_neighbour_cells_count > 3):
                self.new_state = 0
            if (living_neighbour_cells_count == 2) or (living_neighbour_cells_count == 3):
                self.new_state = 1
        elif self.current_state == 0:  # if cell is dead
            if living_neighbour_cells_count == 3:
                self.new_state = 1

    def update_current_state(self):
        self.current_state = self.new_state
