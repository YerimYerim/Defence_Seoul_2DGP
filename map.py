
from Tower import *

class Map:
    def __init__(self):
        self.Tiles = [[0] * 17 for i in range(10)]
        self.type = 0
        self.TileRow = [i * Tile_SIZE for i in range(19)]
        self.TileCol = [i * Tile_SIZE for i in range(12)]

    def select(self, x, y):

        for i in range(11):
            for j in range(18):
                TileRect = RECT()
                TileRect.set(self.TileRow[j], self.TileCol[i+1], self.TileRow[j+1], self.TileCol[i])
                print(TileRect.left, TileRect.right, TileRect.bot, TileRect.top)
                if InterSectRECT(x, y, TileRect) is True:
                    print(TileRect.left, TileRect.right)
                    print(x, y)
                    print(i, j)
                    return i, j
                del TileRect

        pass

