import game_framework
import main_state
from setting import *
from pico2d import *
import Start_stage

name = "Gameover_state"
Img = None

def enter():
    global Img, stage
    stage = 1
    Img = load_image('Spritesheet\\GameOver.png')

def exit():
    global Img , stage
    stage = 1
    del Img

def pause():
    pass


def resume():
    pass


def handle_events():
    global running
    events = get_events()
    for event in events:
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(Start_stage)

def update():
    delay(0.03)
    pass

def draw():
    clear_canvas()
#   self, left, bottom, width, height, x, y, w = None, h = None)
    main_state.draw()
    Img.clip_draw(0, 0, 1362, 345, BackWIDTH / 2, BackHIEGHT / 2, BackWIDTH, BackHIEGHT / 2)
    update_canvas()