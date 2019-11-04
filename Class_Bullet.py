import framework
import pico2d
import State_main
import State_start
import gameover_stage
from Class_Tower import *
from Class_Boat import *
class Bullet :
    From = Tower()
    To = Boat()
    def __init__(self , FROM , TO ):
        self.From = FROM
        self.To = TO
        self.Frame = 0
        self.Type = -1
        self.Image = load_image()
        pass
    def draw(self):
        pass
    def update(self):
        pass