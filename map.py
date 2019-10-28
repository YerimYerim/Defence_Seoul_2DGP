from pico2d import *
from Boat import *
from setting import *
from Tower import *

class map:
    def __init__(self):
        self.Tiles = [[0] * 17 for i in range(10)]
        self.Img = load_image('Spritesheet\\resource.png')
        self.Light = RECT()
        self.Light.set()