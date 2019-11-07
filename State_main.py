
from Class_Boat import *
from map import *

BackGround = None
running = True
speedy = 0.02
font = None
name = "MainState"
boat = None
map = None
HpSum  = None
main_bgm = None
boat_move_bgm = None
volume = 0
def enter():
    global boat, BackGround, map, tower , HpSum , main_bgm , boat_move_bgm
    map = Map()
    boat = [ Boat() for i in range(map.stage)]
    for i in range(map.stage):
        boat[i].Hp = map.stage * 10
        boat[i].Speed += map.stage / 5
    BackGround = load_image('Spritesheet\\resource.png')
    HpSum = 0
    main_bgm = load_music('sound\\테란브금.mp3')
    main_bgm.set_volume(64)
    main_bgm.repeat_play()
    boat_move_bgm = load_music('sound\\낙찰.mp3')

def exit():
    global boat , map , main_bgm , boat_move_bgm
    del map , main_bgm , boat_move_bgm
    del boat


def pause():
    pass


def resume():
    pass


def handle_events():
    global running,speedy , gold , volume
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_MOUSEMOTION:
            map.select(event.x, event.y)
        if event.type == SDL_MOUSEBUTTONDOWN:
            if map.tower[map.towerCnt].type >= 0 and map.gold > 0 and \
                    map.select(event.x , event.y) is not False and Tile_SIZE * 8 > event.y:
                for i in range(map.towerCnt):
                    if map.select(event.x , event.y).left is map.tower[i].Rectangle.left and \
                            map.select(event.x, event.y).bot is map.tower[i].Rectangle.bot:
                        return
                map.tower[map.towerCnt].Rectangle.set(map.select(event.x, event.y).left,
                                                      map.select(event.x, event.y).bot,
                                                      map.select(event.x, event.y).right,
                                                      map.select(event.x, event.y).top)

                map.tower[map.towerCnt].bullet.type = map.tower[map.towerCnt].type
                map.tower[map.towerCnt].bullet.From = map.tower[map.towerCnt]
                map.tower[map.towerCnt].bullet.x = (map.tower[map.towerCnt].Rectangle.right + map.tower[map.towerCnt].Rectangle.left)/2
                map.tower[map.towerCnt].bullet.y = BackHIEGHT - (map.tower[map.towerCnt].Rectangle.bot + map.tower[map.towerCnt].Rectangle.top)/2

                map.towerCnt += 1
                map.gold -= 1
            elif map.select(event.x, event.y) is False:
                map.tower[map.towerCnt].type = -1
            else:
                for i in range(4):
                    if InterSectRECT(event.x, event.y, Select_Tower_Rect[i]):
                        map.tower[map.towerCnt].type = i
        #     print (event.x , event.y)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            boat_move_bgm.set_volume(volume)
            boat_move_bgm.repeat_play()
            for i in range(map.Move_Boat):
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
    global boat, map, BackHIEGHT, tmpR , HpSum, boat_move_bgm , volume
    HpSum = 0
    for i in range(map.stage):
        boat[i].update()
        if boat[i].state is 0 and boat[i-1].Move_Times > Tile_SIZE * 2 - 2:
            boat[i].state = 1

    for i in range(map.towerCnt):
        for z in range(map.stage):
            tmpR = RECT()
            tmpR.left, tmpR.bot, tmpR.right, tmpR.top = boat[z].Rectangle.left - Tile_SIZE * 3, \
                                                        BackHIEGHT - boat[z].Rectangle.bot + Tile_SIZE*3, \
                                                        boat[z].Rectangle.right + Tile_SIZE*3, \
                                                        BackHIEGHT - boat[z].Rectangle.top - Tile_SIZE*3
            if boat[z].state is 1 and InterSectRECT((map.tower[i].Rectangle.left + map.tower[i].Rectangle.right) / 2,
                                                    (map.tower[i].Rectangle.bot + map.tower[i].Rectangle.top) / 2, tmpR):
                if map.tower[i].bullet.To is None and boat[z].Hp > 0:
                        map.tower[i].bullet.To = boat[z]


    for i in range(map.stage):
        HpSum += boat[i].Hp

    if HpSum <= 0:
        map.stage += 1
        boat = [Boat() for i in range(map.stage)]
        map.gold += map.stage - 1
        for i in range(map.stage):
            boat[i].Speed += map.stage / 5
            boat[i].Hp = map.stage * 10
        main_bgm.repeat_play()
        for i in range(map.towerCnt):
            map.tower[i].bullet.__init__(map.tower[i])
            map.tower[i].bullet.Comeback()
        framework.push_state(State_NextStage)

    boat_move_bgm.set_volume(volume)
    if volume < 100:
        volume += 1

    for i in range(map.towerCnt): #포탄과 배 충돌쳌흐
        if map.tower[i].bullet.To is not None:
            if ( map.tower[i].bullet.crashCheck() and map.tower[i].bullet.type is Light):
                if random.randint(0, 100) <= Light_Level:
                    for i in range(map.stage):
                        boat[i].Hp -= 1
                        print(i , " - 연쇄피해")


    map.update()
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






