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
        self.x, self.y = (self.From.Rectangle.left + self.From.Rectangle.right) / 2 , (self.From.Rectangle.top + self.From.Rectangle.bot) / 2
        self.To = [self.x, self.y]
        self.type = self.From.type
        self.Image = load_image('Spritesheet\\bullet.png')
        pass
    def draw(self):
        if self.type >= 0:
            self.Image.clip_draw(65 * self.type, 0, 44, 44, self.x, self.y, 20, 20 )
        pass
    def update(self):
        if self.To[0] is self.x:
            if self.To[1] is self.y:
                self.x , self.y = (self.From.Rectangle.left + self.From.Rectangle.right) / 2 , (self.From.Rectangle.top + self.From.Rectangle.bot) / 2
        else:
            distance = math.sqrt((self.To[0] - self.x )*(self.To[0] - self.x ) + (self.To[1] - self.y)*(self.To[1] - self.y))
            self.x += (self.To[0] - self.x)/distance
            self.y += (self.To[1] - self.y)/distance

