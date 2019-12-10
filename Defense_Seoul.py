import framework
import pico2d
import State_main
import State_start
import gameover_stage
from setting import *

pico2d.open_canvas(BackWIDTH, BackHIEGHT,True )
framework.run(State_start)
pico2d.close_canvas(BackWIDTH, BackHIEGHT)