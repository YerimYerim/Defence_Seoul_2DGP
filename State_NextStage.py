import framework
import State_main
from setting import *
from pico2d import *


name = "NextStage_state"
Img = None

def enter():
    global Img
    Img = load_image('Spritesheet\\NextStage.png')

def exit():
    pass

def pause():
    pass


def resume():
    pass


def handle_events():
    global running,stage , boat
    events = get_events()
    for event in events:
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            framework.pop_state()

def update():
    delay(0.03)
    pass

def draw():
    clear_canvas()
#   self, left, bottom, width, height, x, y, w = None, h = None)
    State_main.draw()
    Img.clip_draw(0, 0, 1362, 345, BackWIDTH / 2, BackHIEGHT / 2, BackWIDTH, BackHIEGHT / 2)

    update_canvas()