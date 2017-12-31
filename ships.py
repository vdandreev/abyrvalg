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
                "coord_x": tile_x,
                "coord_y": tile_y
            }
            self.tiles.append(ship_tile)
    
    def get_ship(self):
        print json.dumps(self.tiles, indent=4, sort_keys=True)
    def tile_in_ship(self,def_x,def_y):
     for  i in range(len(self.tiles)):
         if (def_x == self.tiles[i]["coord_x"]) &  (def_y == self.tiles[i]["coord_y"]):print('True')
         else:print('False')
    

battleship = ship(2,3,"right", 4)

battleship.get_ship()
battleship.tile_in_ship(2,3)
