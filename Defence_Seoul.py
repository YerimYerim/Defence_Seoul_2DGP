from pico2d import *
from Boat_class import *
from setting import *
from Tower import *
from map import *
open_canvas(BackWIDTH, BackHIEGHT)

BackGround = None
running = True
boat = Boat_class()
boat.Img = load_image('Spritesheet\\boat.png')
BackGround = load_image('Spritesheet\\resource.png')
font = None
B = Boat_class()
tower = Tower()
map = Map()

def handle_events():
    global running
    global dir
    events = get_events()
    for event in events:

        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
        elif event.type == SDL_MOUSEBUTTONDOWN:
            pass
    pass




while running:
    clear_canvas()
    BackGround.clip_draw(666, 708-583, BackWIDTH, BackHIEGHT, BackWIDTH/2, BackHIEGHT/2)
    B.do()
    B.draw()
    tower.draw()
    update_canvas()
    handle_events()
    x += 1
    delay(0.05)

close_canvas()

