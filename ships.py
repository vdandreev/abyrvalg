import json

class ship():
    def __init__(self, x, y, direction, length):
        self.tiles = []
        while len(self.tiles) < length:
            tile_x = x
            tile_y = y

            if direction == "right":
                tile_x = x + len(self.tiles)
            elif direction == "down":
                tile_y = y + len(self.tiles)

            ship_tile = {
                "alive": True,
                "coodrd_x": tile_x,
                "coodrd_y": tile_y
            }
            self.tiles.append(ship_tile)
    
    def get_ship(self):
        print json.dumps(self.tiles, indent=4, sort_keys=True)
            
    

battleship = ship(2,3,"right", 4)

battleship.get_ship()

