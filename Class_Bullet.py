import framework
import pico2d
import State_main
import State_start
import gameover_stage
from Class_Tower import *
from Class_Boat import *


class Bullet :
    From = None
    To = None
    def __init__(self , FROM = Tower(), x, y):
        self.From = FROM
        self.x, self.y = (self.From.Rectangle.left + self.From.Rectangle.right) / 2 , (self.From.Rectangle.top + self.From.Rectangle.bot) / 2
        self.To = (x, y)
        self.Type = -1
        self.Image = load_image('Spritesheet\\bullet.png')
        pass
    def draw(self):
        if self.type is 0:
            self.Image.clip_draw(0,0,44,44, self.x , self.y , 20, 20 )
            pass
        if self.type is 1:
            self.Image.clip_draw(0,0,44,44, self.x , self.y , 20, 20 )
            pass
        if self.type is 2:
            self.Image.clip_draw( )
            pass
        if self.type is 3:
            self.Image.clip_draw( )
            pass


        pass
    def update(self):




        pass