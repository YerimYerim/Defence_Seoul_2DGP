from pico2d import *
from setting import *

class Tower:
    def __init__(self):
        self.speed = 15.0
        self.R = RECT()
        self.R.bot, self.R.left, self.R.right, self.R.top = 0, 0, 100,100
        self.angle = 0
        self.HP_font = None
        self.Img = None
        self.Boat_frame = 0
        self.Img = load_image('Spritesheet\\resource.png')
        self.HP_font = load_font('font\\SeoulNamsanB.ttf', 13)

    def draw(self):
        self.Img.clip_composite_draw(0, 0, 100, 100, 1, ' ', 0, 0, 500, 500)
