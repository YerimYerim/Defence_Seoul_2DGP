import random
import json
import os

from pico2d import *
import game_framework
from pico2d import *
from Boat import *
from setting import *
from Tower import *
from map import *
BackGround = None
running = True

font = None
name = "MainState"

tower = None
boat = None
map = None



def enter():
    global tower, boat, map, BackGround
    boat = Boat()
    map = Map()
    boat.Img = load_image('Spritesheet\\boat.png')
    BackGround = load_image('Spritesheet\\resource.png')

def exit():
    global tower, boat, Map
    del tower
    del boat
    del Map


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



def update():
    boat.do()
    delay(0.07)

def draw():
    global  BackWIDTH, BackHIEGHT, BackWIDTH, BackHIEGHT
    clear_canvas()
    BackGround.clip_draw(666, 708-583, BackWIDTH, BackHIEGHT, BackWIDTH/2, BackHIEGHT/2)
    boat.draw()
#    map.draw()
    update_canvas()






