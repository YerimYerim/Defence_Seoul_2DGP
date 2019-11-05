import framework
import State_main
from setting import *
from pico2d import *

start_Img = None
start_Sound = None
button_sound = None
name = "Start_state"
def enter():
    global start_Img , start_Sound , button_sound
    start_Img = load_image('Map\\start.png')
    start_Sound = load_music('sound\\대기.mp3')
    start_Sound.set_volume(128)
#    button_sound = load_wav('sound\\button.wav')
#    button_sound.set_volume(50)
    print("재생")
    start_Sound.repeat_play()


def exit():
    global start_Img, start_Sound
    del start_Img , start_Sound


def pause():
    pass


def resume():
    pass

def handle_events():
    global button_sound , events
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            framework.change_state(State_main)
            print("메ㄴ인으로넘어감")


def update():
    delay(0.1)
    pass


def draw():
    clear_canvas()
    start_Img.clip_draw(0, 0, BackWIDTH, BackHIEGHT, BackWIDTH/2, BackHIEGHT/2)
    update_canvas()