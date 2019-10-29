import game_framework
import pico2d
import main_state
import Start_stage
import gameover_stage
from setting import *

pico2d.open_canvas(BackWIDTH, BackHIEGHT)
game_framework.run(Start_stage)
pico2d.close_canvas(BackWIDTH, BackHIEGHT)