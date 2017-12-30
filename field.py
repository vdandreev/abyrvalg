from __future__ import print_function



class Field():
    def __init__(self, rows = 10, cols = 10):
        local_grid = []

        while len(local_grid) < rows:
            local_col = []
            while len(local_col) < cols:
                local_col.append(".")
            
            local_grid.append(local_col)

        self.grid = local_grid

    def draw(self):
        for i in self.grid:
            for j in i:
                print (j+" ",end = '')
            print ('')
            
            
        



field = Field()

field.grid[2][4] = "!"

field.draw()
