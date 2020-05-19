import random
import pyglet


class GameOfLife:

    def __init__(self, window_width, window_height, cell_size, percent_fill):
        self.grid_width = int(window_width / cell_size)
        self.grid_height = int(window_height / cell_size)
        self.cell_size = cell_size
        self.percent_fill = percent_fill
        self.cells = []
        self.generate_cells()

    def generate_cells(self):
        for row in range(0, self.grid_height):
            self.cells.append([])
            for col in range(0, self.grid_width):
                if random.random() < self.percent_fill:
                    self.cells[row].append(1)
                else:
                    self.cells[row].append(0)

    def draw(self):
        for row in range(0, self.grid_height):
            for col in range(0, self.grid_width):
                if self.cells[row][col] == 1:
                    # (0, 0), (0, 20), (20, 0), (20, 20)
                    square_coords = (row * self.cell_size,                  col * self.cell_size,
                                     row * self.cell_size,                  col * self.cell_size + self.cell_size,
                                     row * self.cell_size + self.cell_size, col * self.cell_size,
                                     row * self.cell_size + self.cell_size, col * self.cell_size + self.cell_size)
                    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                                 [0, 1, 2, 1, 2, 3],
                                                 ('v2i', square_coords))

    def run_rules(self):
        # if you apply the rules to a cell in the original grid, it will mess with the cells that come after
        # use a copy
        temp = []
        for row in range(0, self.grid_height):
            temp.append([])
            for col in range(0, self.grid_width):
                cell_sum = sum([self.get_cell_value(row - 1, col - 1),
                                self.get_cell_value(row - 1, col),
                                self.get_cell_value(row - 1, col + 1),
                                self.get_cell_value(row,     col - 1),
                                self.get_cell_value(row,     col + 1),
                                self.get_cell_value(row + 1, col - 1),
                                self.get_cell_value(row + 1, col),
                                self.get_cell_value(row + 1, col + 1)])

                """ ---------- Conway's Rules ---------- """
                # if a cell is dead and it has three neighbors, it comes alive
                if self.cells[row][col] == 0 and cell_sum == 3:
                    temp[row].append(1)
                # if a cell is alive and has 2 or 3 neighbors, it stays alive
                elif self.cells[row][col] == 1 and ( cell_sum == 3 or cell_sum == 2):
                    temp[row].append(1)
                # in all other cases, the cell dies
                else:
                    temp[row].append(0)

        self.cells = temp


    def get_cell_value(self, row, col):
        if 0 <= row < self.grid_height and 0 <= col < self.grid_width:
            return self.cells[row][col]
        return 0
