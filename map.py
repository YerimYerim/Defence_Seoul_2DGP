
from Tower import *

tempRC = RECT()
TileRect = RECT()
class Map:
    def __init__(self):
        self.Tiles = [[0] * 17 for i in range(10)]
        self.type = 0
        self.TileRow = [i * Tile_SIZE for i in range(19)]
        self.TileCol = [i * Tile_SIZE for i in range(12)]


    def select(self, x, y, type):
        global tempRC, TileRect
        tempRC = set(x, y, x+1, y+1)
        for i in range(11):
            for j in range(18):
                TileRect = RECT().set(self.TileRow[j], self.TileCol[i], self.TileRow[j+1], self.TileCol[i+1])
                if InterSectRECT(tempRC, TileRect):
                    self.Tiles[i][j] = type
        pass
#map = Map()
#for i in range(0,10):
#    for j in range(0,17):
#        TileRect = RECT()
#        TileRect.set(map.TileRow[j], map.TileCol[i], map.TileRow[j + 1], map.TileCol[i + 1])
#        print(TileRect.left , TileRect.right)
