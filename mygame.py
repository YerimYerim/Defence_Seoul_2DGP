import game_framework
import pico2d
import main_state
from setting import *

pico2d.open_canvas(BackWIDTH, BackHIEGHT)
game_framework.run(main_state)
pico2d.close_canvas(BackWIDTH, BackHIEGHT)