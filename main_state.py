
from Boat import *
from map import *

BackGround = None
running = True
speedy = 0.03
font = None
name = "MainState"

#tower = None
boat = None
map = None


def enter():
    global boat, BackGround, stage , map, tower
    stage += stage
    print(stage)
    boat = Boat()
    boat.hp = stage * 10
    boat.speed += stage / 5
    map = Map()
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
    global running,speedy
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_MOUSEMOTION:
            map.select(event.x, event.y)
        if event.type == SDL_MOUSEBUTTONDOWN:
            if map.tower[map.towerCnt].type >= 0:
                map.tower[map.towerCnt].R.set (map.select(event.x, event.y).left, map.select(event.x, event.y).bot , map.select(event.x, event.y).right ,map.select(event.x, event.y).top)
                print ("install", map.towerCnt ,"타입 " ,map.tower[map.towerCnt].type , " 땅 " , map.select(event.x, event.y).left)
                print ("타워 구역", map.tower[map.towerCnt].R.left)
                map.towerCnt += 1
            else:
                for i in range(4):
                    if InterSectRECT(event.x, event.y, SelectRect[i]):
                        map.tower[map.towerCnt].type = i
                        print(i)
        #     print (event.x , event.y)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            boat.hp -= 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            boat.state = 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            speedy  -= 0.002
            pass


def update():
    boat.update()
    map.update()
    delay(speedy)


def draw():
    global BackWIDTH, BackHIEGHT, BackWIDTH, BackHIEGHT
    clear_canvas()
    BackGround.clip_draw(666, 708-583, BackWIDTH, BackHIEGHT, BackWIDTH/2, BackHIEGHT/2)
    boat.draw()
    map.draw()
    update_canvas()






