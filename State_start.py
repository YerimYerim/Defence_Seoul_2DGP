import framework
import State_main
from setting import *
from pico2d import *

start_Img = None
name = "Start_state"
def enter():
    global start_Img
    start_Img = load_image('Map\\start.png')

def exit():
    global start_Img
    del start_Img

def pause():
    pass


def resume():
    pass

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            framework.change_state(State_main)
            print("메ㄴ인으로넘어감")
            pass

def update():
    pass
def draw():
    clear_canvas()
    start_Img.clip_draw(0, 0, BackWIDTH, BackHIEGHT, BackWIDTH/2, BackHIEGHT/2)
    update_canvas()