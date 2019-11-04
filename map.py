
from Class_Tower import *

class Map:
    font = None
    def __init__(self):
        self.Tiles = [[0] * 17 for i in range(10)]
        self.type = 0
        self.TileRow = [i * Tile_SIZE for i in range(19)]
        self.TileCol = [i * Tile_SIZE for i in range(12)]
        self.tower = [Tower() for i in range(200)]
        self.TileRect = RECT()
        self.towerCnt = 0
        self.NoCnt = 38
        self.gold = 10
        self.stage = 1
        self.Move_Boat = 1
        
        self.No = (
        (2, 0), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (4, 4), (5, 4), (5, 5), (5, 6), (4, 6), (4, 7), (3, 7), (3, 7),
        (3, 8), (3, 9), (4, 9), (4, 10), (4, 11), (5, 11), (5, 12), (5, 13), (4, 13), (4, 14), (3, 14), (3, 15),
        (2, 15), (2, 16), (6, 0), (7, 0), (7, 1), (7, 2,), (7, 7), (7, 8), (7, 9), (7, 16), (0, 0), (0, 15), (0, 16))

        if self.font is None:
            self.font = load_font('font\\PressStart2P.ttf', 20)


    def select(self, x, y):

        for i in range(11):
            for j in range(18):
                self.TileRect.set(self.TileRow[j], self.TileCol[i+1], self.TileRow[j+1], self.TileCol[i])
                if InterSectRECT(x, y, self.TileRect) is True:
                    for n in range(38):
                        if i is self.No[n][0] and j is self.No[n][1]:
                            self.TileRect.left, self.TileRect.bot, self.TileRect.right, self.TileRect.top = 0,0,0,0
                            return False
                    return self.TileRect


    def draw(self):
        if BackHIEGHT-self.TileRect.bot >= Tile_SIZE:
            draw_rectangle(self.TileRect.left,  BackHIEGHT- self.TileRect.bot + 2 , self.TileRect.right, BackHIEGHT - self.TileRect.top)
        for i in range(self.towerCnt):
            if self.tower[i].type >= 0:
                self.tower[i].draw()
        s = str (self.gold)
        self.font.draw(Tile_SIZE * 10,Tile_SIZE * 1, s, ( 0,0,0))
        s =  "stage"
        self.font.draw(Tile_SIZE * 13.3,Tile_SIZE * 1.5, s, ( 0,0,0))
        s = str(self.stage)
        self.font.draw(Tile_SIZE * 14,Tile_SIZE * 0.7, s, ( 0,0,0))


    def update(self):
        for i in range(self.towerCnt):
            if self.tower[i].type >= 0:
                self.tower[i].update()