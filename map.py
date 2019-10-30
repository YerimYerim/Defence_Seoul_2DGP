
from Tower import *

class Map:
    def __init__(self):
        self.Tiles = [[0] * 17 for i in range(10)]
        self.type = 0
        self.TileRow = [i * Tile_SIZE for i in range(19)]
        self.TileCol = [i * Tile_SIZE for i in range(12)]
        self.tower = [ Tower() for i in range(200)]
        self.TileRect = RECT()
        self.towerCnt = 0
    def select(self, x, y):
        for i in range(11):
            for j in range(18):
                self.TileRect.set(self.TileRow[j], self.TileCol[i+1], self.TileRow[j+1], self.TileCol[i])
                if InterSectRECT(x, y, self.TileRect) is True:
                    return self.TileRect


        pass

    def draw(self):
        if BackHIEGHT-self.TileRect.bot >= Tile_SIZE:
            draw_rectangle(self.TileRect.left,  BackHIEGHT- self.TileRect.bot + 2 , self.TileRect.right, BackHIEGHT - self.TileRect.top)
        for i in range(self.towerCnt):
            self.tower[i].draw()
        pass
    def update(self):
        pass