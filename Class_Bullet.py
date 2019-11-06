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
        self.x, self.y = (self.From.Rectangle.left + self.From.Rectangle.right) / 2, (self.From.Rectangle.top + self.From.Rectangle.bot) / 2
        self.To = None
        self.type = FROM.type
        self.Image = load_image('Spritesheet\\bullet.png')


    def draw(self):
        if self.type >= 0:
            self.Image.clip_draw(65 * self.type, 0, 44, 44, self.x, self.y, 20, 20 )
        pass

    def Comeback(self):
        self.x = (self.From.Rectangle.left + self.From.Rectangle.right) / 2
        self.y = BackHIEGHT - (self.From.Rectangle.top + self.From.Rectangle.bot) / 2

    def crashCheck(self):
        if self.To is not None:
            tmpR = RECT()
            tmpR.left, tmpR.bot, tmpR.right, tmpR.top = self.To.Rectangle.left, \
                                                        BackHIEGHT - self.To.Rectangle.bot, \
                                                        self.To.Rectangle.right, \
                                                        BackHIEGHT - self.To.Rectangle.top
            if InterSectRECT(self.x, BackHIEGHT - self.y, tmpR):
                if self.To.Hp <= 0:
                    self.__init__(self.From)
                    self.Comeback()
                    return

                self.To.Hp = self.To.Hp - 1
                self.__init__(self.From)
                self.Comeback()


    def update(self):
        if self.To is not None and InterSectRECT(self.x, self.y, self.To.Rectangle):
            self.x, self.y = (self.From.Rectangle.left + self.From.Rectangle.right) / 2, \
                             (self.From.Rectangle.top + self.From.Rectangle.bot) / 2

        elif self.To is not None:
            distance = math.sqrt(((self.To.Rectangle.left + self.To.Rectangle.right) / 2 - self.x) ** 2
                                 + ((self.To.Rectangle.top + self.To.Rectangle.bot) / 2 - self.y) ** 2)
            self.y += (((self.To.Rectangle.top + self.To.Rectangle.bot + 2) / 2 - self.y)/distance) * 4
            self.x += (((self.To.Rectangle.right + self.To.Rectangle.left + 2) / 2 - self.x)/distance) * 4


