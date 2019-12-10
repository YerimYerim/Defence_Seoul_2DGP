
from Class_Boat import *
from map import *


BackGround = None
running = True
speedy = 0.02
font = None
name = "MainState"
boat = None
map = None
HpSum = None
main_bgm = None
boat_move_bgm = None
volume = 10

crash_font = None

def enter():
    global boat, BackGround, map, tower , HpSum , main_bgm , boat_move_bgm , Fire_Level, Ice_Level , Light_Level, DownGrade_Level
    global crash_font
    map = Map()
    boat = [ Boat() for i in range(map.stage)]
    for i in range(map.stage):
        boat[i].Hp = map.stage * 10
        boat[i].Speed += map.stage / 5
    if BackGround is None:
        BackGround = load_image('Spritesheet\\resource.png')
    HpSum = 0
    if main_bgm is None:
        main_bgm = load_music('sound\\테란브금.mp3')
    main_bgm.set_volume(volume)
    main_bgm.repeat_play()
    boat_move_bgm = load_music('sound\\낙찰.mp3')
    Fire_Level = 1
    Ice_Level = 1
    Light_Level = 1
    DownGrade_Level = 1
    if crash_font is None:
        crash_font = load_font('font\\SeoulNamsanB.ttf', 13)


def exit():
    global boat , map , main_bgm , boat_move_bgm
    del map , main_bgm , boat_move_bgm
    del boat


def pause():
    pass


def resume():
    pass


def handle_events():
    global running,speedy , volume , Fire_Level , DownGrade_Level , Ice_Level , Light_Level
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            framework.change_state(State_start)
        if event.type == SDL_MOUSEMOTION:
            map.select(event.x, event.y)
        if event.type == SDL_MOUSEBUTTONDOWN:
            if map.tower[map.towerCnt].type >= 0 and map.gold > 0 and map.select(event.x , event.y) is not False and Tile_SIZE * 8 > event.y:
                for i in range(map.towerCnt):
                    if map.select(event.x , event.y).left is map.tower[i].Rectangle.left and map.select(event.x, event.y).bot is map.tower[i].Rectangle.bot:
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
                        if i is Fire:
                            if map.gold - Fire_Level >= 0:
                                map.gold -= Fire_Level
                                Fire_Level += 1

                        if i is Ice:
                            if map.gold - Ice_Level >= 0:
                                map.gold -= Ice_Level
                                Ice_Level += 1

                        if i is Light:
                            if map.gold - Light_Level >= 0:
                                map.gold -= Light_Level
                                Light_Level += 1
                        if i is DownGrade:
                            if map.gold - DownGrade_Level >= 0:
                                map.gold -= DownGrade_Level
                                DownGrade_Level += 1


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
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            volume  = volume + 10
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            volume = volume - 10


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


    for i in range(map.towerCnt): #포탄과 배 충돌
        if map.tower[i].bullet.To is not None:
            if ( map.tower[i].bullet.crashCheck() and map.tower[i].bullet.type is Light):
                if random.randint(0, 100) <= Light_Level * 10:
                    for i in range(map.stage):
                        boat[i].Hp -= 1
                        boat[i].state_down = False
                        boat[i].state_fire = False
                        boat[i].state_Light = True


    map.update()



def draw():
    global BackWIDTH, BackHIEGHT, BackWIDTH, BackHIEGHT
    clear_canvas()
    BackGround.clip_draw(666, 708-583, BackWIDTH, BackHIEGHT, BackWIDTH/2, BackHIEGHT/2)
    for i in range(map.stage):
        if boat[i].state is not 2:
            boat[i].draw()
    map.draw()
    draw_Level(Fire_Level, Ice_Level, Light_Level, DownGrade_Level)
    update_canvas()






