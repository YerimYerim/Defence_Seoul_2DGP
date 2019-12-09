
import framework
import pico2d
import State_main
import State_start
import gameover_stage

from Class_Boat import *
from Tower_Type_Passive import *
import random
import math
from Class_Tower import *
class Bullet:
    From = None
    To = None
    crash_sound  = None
    def __init__(self , FROM):
        self.From = FROM
        self.x, self.y = (self.From.Rectangle.left + self.From.Rectangle.right) / 2, (self.From.Rectangle.top + self.From.Rectangle.bot) / 2
        self.To = None
        self.type = FROM.type
        self.Image = load_image('Spritesheet\\bullet.png')
        if self.crash_sound is None:
            self.crash_sound = load_wav('sound\\crash.ogg')
            self.crash_sound.set_volume(5)

    def draw(self):
        if self.type >= 0:
            self.Image.clip_draw(65 * self.type, 0, 44, 44, self.x, self.y, 20, 20 )


        pass

    def Comeback(self):
        self.x = (self.From.Rectangle.left + self.From.Rectangle.right) / 2
        self.y = BackHIEGHT - (self.From.Rectangle.top + self.From.Rectangle.bot) / 2

    def crashCheck(self):
            tmpR = RECT()
            tmpR.left, tmpR.bot, tmpR.right, tmpR.top = self.To.Rectangle.left,  BackHIEGHT - self.To.Rectangle.bot, \
                                                        self.To.Rectangle.right,  BackHIEGHT - self.To.Rectangle.top

            if InterSectRECT(self.x, BackHIEGHT - self.y, tmpR):
                if self.To.Hp <= 0:
                    self.__init__(self.From)
                    self.Comeback()
                    return False
                self.crash_sound.play()
                self.To.Hp = self.To.Hp - 1
                if self.type is Fire:
                    Firing(self)
                    self.To.state_fire = True
                    self.To.state_down = False
                    self.To.state_Light = False
                elif self.type is Ice:
                    Icing(self)

                    self.To.state_Ice = True
                elif self.type is Light:
                    Lightning(self)
                    self.To.state_Light = True
                elif self.type is DownGrade:
                    DownGrading(self)
                    self.To.state_down = True
                    self.To.state_fire = False
                    self.To.state_Light = False
                self.__init__(self.From)
                self.Comeback()
                return True



    def update(self):
        if self.To is not None and InterSectRECT(self.x, self.y, self.To.Rectangle):
            self.x, self.y = (self.From.Rectangle.left + self.From.Rectangle.right) / 2, \
                             (self.From.Rectangle.top + self.From.Rectangle.bot) / 2

        elif self.To is not None:
            distance = math.sqrt(((self.To.Rectangle.left + self.To.Rectangle.right) / 2 - self.x) ** 2
                                 + ((self.To.Rectangle.top + self.To.Rectangle.bot) / 2 - self.y) ** 2)
            self.y += (((self.To.Rectangle.top + self.To.Rectangle.bot + 2) / 2 - self.y)/distance) * 4
            self.x += (((self.To.Rectangle.right + self.To.Rectangle.left + 2) / 2 - self.x)/distance) * 4


