import framework
import pico2d
import State_main
import State_start
import gameover_stage
from Class_Tower import *
from Class_Boat import *
class Bullet :
    def __init__(self , type):
        self.From = Tower()
        self.To = Boat()
        self.frame = 0
        self.Type = -1
        self.image = Image()
        pass
    def draw(self):
        pass
    def update(self):
        pass