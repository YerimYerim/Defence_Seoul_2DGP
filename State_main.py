
from Class_Boat import *
from map import *

BackGround = None
running = True
speedy = 0.02
font = None
name = "MainState"
boat = None
map = None
hpsum  = None

def enter():
    global boat, BackGround, map, tower , hpsum
    map = Map()
    boat = [ Boat() for i in range(map.stage)]
    for i in range(map.stage):
        boat[i].hp = map.stage * 10
        boat[i].speed += map.stage / 5
    BackGround = load_image('Spritesheet\\resource.png')
    hpsum = 0

def exit():
    global boat , map
    del map
    del boat


def pause():
    pass


def resume():
    pass


def handle_events():
    global running,speedy , gold
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_MOUSEMOTION:
            map.select(event.x, event.y)
        if event.type == SDL_MOUSEBUTTONDOWN:
            if (map.tower[map.towerCnt].type >= 0 and map.gold > 0 and map.select(event.x , event.y) is not False and  Tile_SIZE * 8 > event.y ) :
                for i in range(map.towerCnt):
                    print(map.tower[i].R.left , map.tower[i].R.bot , map.select(event.x , event.y).left ,map.select(event.x , event.y).bot )
                    if map.select(event.x , event.y).left is map.tower[i].R.left and map.select(event.x , event.y).bot is map.tower[i].R.bot:
                        return
                map.tower[map.towerCnt].R.set (map.select(event.x, event.y).left, map.select(event.x, event.y).bot , map.select(event.x, event.y).right ,map.select(event.x, event.y).top)
                map.towerCnt += 1
                map.gold -= 1
            elif map.select(event.x, event.y) is False :
                map.tower[map.towerCnt].type = -1
            else:
                for i in range(4):
                    if InterSectRECT(event.x, event.y, SelectRect[i]):
                        map.tower[map.towerCnt].type = i
                        print(i)
        #     print (event.x , event.y)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            for i in range(map.moveboat):
                if boat[i] is not 2:
                    boat[i].state = 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            speedy -= 0.002
            pass
        elif (event.type, event.key) == (SDL_KEYDOWN , SDLK_q):
            map.tower[map.towerCnt].type  = 0
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_w):
            map.tower[map.towerCnt].type = 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_e):
            map.tower[map.towerCnt].type = 2
        elif (event.type, event.key) == (SDL_KEYDOWN , SDLK_r):
            map.tower[map.towerCnt].type  = 3


def update():
    global boat, map, BackHIEGHT , tmpR , hpsum
    print("메인")
    hpsum = 0
    for i in range(map.stage):
        boat[i].update()
        if boat[i].state is 0 and boat[i-1].move_times > Tile_SIZE * 2 - 2:
            boat[i].state = 1
    map.update()
    for i in range(map.towerCnt):
        for z in range(map.stage):
            tmpR = RECT()
            tmpR.left, tmpR.bot, tmpR.right, tmpR.top = boat[z].R.left - Tile_SIZE* 3 , BackHIEGHT - boat[z].R.bot + Tile_SIZE*3, boat[z].R.right + Tile_SIZE*3, BackHIEGHT - boat[z].R.top - Tile_SIZE*3
            if boat[z].state is 1 and InterSectRECT((map.tower[i].R.left + map.tower[i].R.right) / 2, (map.tower[i].R.bot + map.tower[i].R.top) / 2 , tmpR):
                boat[z].hp -= 0.01
                pass
     #       print_fps

    for i in range(map.stage):
        hpsum += boat[i].hp

    if hpsum <= 0:
        map.stage += 1
        boat = [Boat() for i in range(map.stage)]
        map.gold += map.stage - 1
        for i in range(map.stage):
            boat[i].hp = map.stage * 10
            boat[i].speed += map.stage / 5
            boat[i].hp = map.stage * 10
        framework.push_state(State_NextStage)
    delay(speedy)


def draw():
    global BackWIDTH, BackHIEGHT, BackWIDTH, BackHIEGHT
    clear_canvas()
    BackGround.clip_draw(666, 708-583, BackWIDTH, BackHIEGHT, BackWIDTH/2, BackHIEGHT/2)
    for i in range(map.stage):
        if boat[i].state is not 2:
            boat[i].draw()
    map.draw()
    update_canvas()






