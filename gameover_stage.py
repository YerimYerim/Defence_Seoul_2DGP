import framework
import State_main
from setting import *
from pico2d import *
import State_start

name = "Gameover_state"
Img = None


def enter():
    global Img
    if Img is None:
        Img = load_image('Spritesheet\\GameOver.png')


def exit():
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    global running
    events = get_events()
    for event in events:
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            framework.change_state(State_start)


def update():

    pass


def draw():
    clear_canvas()
    State_main.BackGround.clip_draw(666, 708-583, BackWIDTH, BackHIEGHT, BackWIDTH/2, BackHIEGHT/2)
    for i in range(State_main.map.stage):
        if State_main.boat[i].state is not 2:
            State_main.boat[i].draw()
    State_main.map.draw()
    State_main.draw_Level(State_main.Fire_Level, State_main.Ice_Level, State_main.Light_Level,State_main.State_main.DownGrade_Level)
    State_main.map.draw()
    Img.clip_draw(0, 0, 1362, 345, BackWIDTH / 2, BackHIEGHT / 2, BackWIDTH, BackHIEGHT / 2)
    update_canvas()



