
from Boat import *
from map import *

BackGround = None
running = True

font = None
name = "MainState"

#tower = None
boat = None
#map = None

def enter():
    global boat, BackGround, stage
    print(stage)
    boat = Boat()
    boat.hp = stage * 10
    boat.speed += stage / 5
#    map = Map()
    boat.Img = load_image('Spritesheet\\boat.png')
    BackGround = load_image('Spritesheet\\resource.png')

def exit():
    global boat
    del boat


def pause():
    pass


def resume():
    pass


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            pass
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            boat.hp -= 1
            pass



def update():
    boat.update()
    delay(0.03)

def draw():
    global BackWIDTH, BackHIEGHT, BackWIDTH, BackHIEGHT
    clear_canvas()
    BackGround.clip_draw(666, 708-583, BackWIDTH, BackHIEGHT, BackWIDTH/2, BackHIEGHT/2)
    boat.draw()
#    map.draw()
    update_canvas()






