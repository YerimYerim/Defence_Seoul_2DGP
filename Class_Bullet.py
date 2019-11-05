import framework
import pico2d
import State_main
import State_start
import gameover_stage
from Class_Tower import *
from Class_Boat import *
import math

class Bullet :
    From = None
    To = None
    def __init__(self , FROM):
        self.From = FROM
        print (self.From.Rectangle.left)
        self.x, self.y = (self.From.Rectangle.left + self.From.Rectangle.right) / 2 , (self.From.Rectangle.top + self.From.Rectangle.bot) / 2
        self.To = None
        self.type = FROM.type
        self.Image = load_image('Spritesheet\\bullet.png')
        pass
    def draw(self):
        if self.type >= 0:
            self.Image.clip_draw(65 * self.type, 0, 44, 44, self.x, self.y, 20, 20 )
        pass

    def Comeback(self):
        self.x = (self.From.Rectangle.left + self.From.Rectangle.right) / 2
        self.y = BackHIEGHT - (self.From.Rectangle.top + self.From.Rectangle.bot) / 2

    def crashCheck(self , boat):
        tmpR = RECT()
        tmpR.left, tmpR.bot, tmpR.right, tmpR.top = boat.Rectangle.left , \
                                                    BackHIEGHT - boat.Rectangle.bot , \
                                                    boat.Rectangle.right, \
                                                    BackHIEGHT - boat.Rectangle.top
        if InterSectRECT(self.x, self.y, tmpR):
            boat.Hp -= 1
            self.x = (self.From.Rectangle.left + self.From.Rectangle.right) / 2
            self.y = BackHIEGHT - (self.From.Rectangle.top + self.From.Rectangle.bot) / 2


    def update(self):
        if self.To is not None and InterSectRECT(self.x, self.y, self.To.Rectangle):
            self.x, self.y = (self.From.Rectangle.left + self.From.Rectangle.right) / 2, \
                             (self.From.Rectangle.top + self.From.Rectangle.bot) / 2

        elif self.To is not None:
            distance = math.sqrt(((self.To.Rectangle.left + self.To.Rectangle.right) / 2 - self.x) ** 2
                                 + ((self.To.Rectangle.top + self.To.Rectangle.bot) / 2 - self.y) ** 2)
            self.y += (((self.To.Rectangle.top + self.To.Rectangle.bot + 2) / 2 - self.y)/distance) * 5
            self.x += (((self.To.Rectangle.right + self.To.Rectangle.left + 2) / 2 - self.x)/distance) * 5


