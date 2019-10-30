from pico2d import *
from setting import *

class Tower:
    HP_font = None
    Img = None
    def __init__(self):
        self.speed = 15.0
        self.R = RECT()
        self.R.bot, self.R.left, self.R.right, self.R.top = 0, 0, 100, 100
        self.angle = 0
        self.Boat_frame = 0
        if Tower.Img is None:
            Tower.Img = load_image('Spritesheet\\resource.png')
            Tower.HP_font = load_font('font\\SeoulNamsanB.ttf', 13)
            print(" 그림 업로드")

    def draw(self):
        self.Img.clip_composite_draw(13, 678  - 140, 142, 142, self.angle, ' ', 500, 100, Tile_SIZE, Tile_SIZE)
        print("타워그림")
    def istall(self , x, y):

        pass

    def update(self):
        self.angle += 0.1
        pass