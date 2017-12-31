from __future__ import print_function

class Tile():
    def __init__(self):
        self.coord_x = 0
        self.coord_y = 0
        self.tile_contents = "water"
        self.is_hit = False

    def __repr__(self):
        if self.tile_contents == "ship":
            if self.is_hit:
                return "[*]"
            else:
                return "[ ]"
        if self.tile_contents == "water":
            if self.is_hit:
                return " * "   
            else:
                return " . "

    def do_hit(self):
        self.is_hit = True
        return self.tile_contents
        
    def set_type(self, tile_type):
        self.tile_contents = tile_type
        
    

class Field():
    def __init__(self, rows = 10, cols = 10):
        local_grid = []

        while len(local_grid) < rows:
            local_col = []
            while len(local_col) < cols:
                local_col.append(Tile())
            
            local_grid.append(local_col)

        self.grid = local_grid

    def draw(self):
        for i in self.grid:
            for j in i:
                print (j,end = '')
            print ('')
            
            
        



field = Field()

field.grid[2][4].set_type("ship")
field.grid[2][5].set_type("ship")
field.grid[2][6].set_type("ship")


field.grid[2][5].do_hit()
field.grid[3][5].do_hit()

field.draw()
