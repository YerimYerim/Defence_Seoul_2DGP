from pico2d import *
from setting import *
import Class_Boat
from Class_Bullet import*


class Tower:
    HP_font = None
    Img = None
    def __init__(self):
        self.speed = 15.0
        self.Rectangle = RECT()
        self.Rectangle.bot, self.Rectangle.left, self.Rectangle.right, self.Rectangle.top = 0, 0, 100, 100
        self.angle = 0
        self.Boat_frame = 0
        self.range = Tile_SIZE * 3
        self.type = -1       # 0- 불 1 - 냉기  2 - 전기 3 - 강등
        self.bullet = Bullet(self)
#        self.bullet = Bullet()
        if Tower.Img is None:
            Tower.Img = load_image('Spritesheet\\resource.png')
            Tower.HP_font = load_font('font\\SeoulNamsanB.ttf', 13)

    def draw(self):
        self.bullet.draw()
        self.Img.clip_composite_draw(12 + 16 * self.type + 142 * self.type, IMG_HEIGHT - 144 - 10, 144, 144, self.angle, ' ', self.Rectangle.left + Tile_SIZE / 2, BackHIEGHT - self.Rectangle.bot + Tile_SIZE / 2, Tile_SIZE, Tile_SIZE)
    #     print("타워그림")

    def update(self):
        self.bullet.update()
        self.angle += 0.01
        pass