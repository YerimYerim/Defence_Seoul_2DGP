IMG_HEIGHT = 701
IMG_WIDTH = 1648
BackWIDTH = 961
BackHIEGHT = 567
tower_IMG_SIZE = 140
Boat_IMG_SIZE = 50
Tile_SIZE = 57
x = 0
y = 0
stage = 1

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

def InterSectRECT(R1, R2):
    if R1.left < R2.left < R1.right or R1.left < R2.right < R1.right:
        if R1.bot < R2.bot < R1.top or R1.top < R2.top < R1.top:
            return True
        else:
            return False
    else:
        return False







