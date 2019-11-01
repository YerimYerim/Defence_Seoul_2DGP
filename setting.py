from pico2d import *

tmpR = None
class RECT:
    def __init__(self):
        self.left = 0
        self.bot = 0
        self.right = 0
        self.top = 0

    def set(self, left, bot, right, top):
        self.left = left
        self.right = right
        self.bot = bot
        self.top = top

def InterSectRECT(x, y, R1 ):

    if R1.left <= x <= R1.right and R1.bot >= y >= R1.top:
   #     print("충돌쓰")
        return True

    else:
        return False
def Crash_Circle_Rect(x, y , r, Rect):
    global tmpR
    tmpR = RECT()

    x = int()
    y = int()
    r = int()

    tmpR.left, tmpR.bot, tmpR.right, tmpR.top = Rect.left - r, Rect.bot - r,  Rect.right + r, Rect.top + r
 #   tmpR.set(Rect.left - r, Rect.bot - r ,  Rect.right + r , Rect.top + r)
    print(tmpR.left, tmpR.right)
    if InterSectRECT(x, y, tmpR):
        print(Rect.left , Rect.right)
        print (tmpR.left , tmpR.right)
        return True
    else:
        return False


IMG_HEIGHT = 701
IMG_WIDTH = 1648
BackWIDTH = 961
BackHIEGHT = 567
tower_IMG_SIZE = 140
Boat_IMG_SIZE = 50
Tile_SIZE = 57
x = 0
y = 0

SelectRect = [RECT() for i in range(5)]
for i in range(4):
    SelectRect[i].set(Tile_SIZE * i *2, Tile_SIZE * 10, Tile_SIZE * 2 * (i+1), Tile_SIZE * 8)
    print(i)


