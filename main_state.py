
from Boat_class import *
from map import *

BackGround = None
running = True
speedy = 0.03
font = None
name = "MainState"
damage = 0


#tower = None
boat = None
map = None


def enter():
    global boat, BackGround, stage, map, tower
    stage = 1
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
            speedy -= 0.002
            pass


def update():
    global boat, map, BackHIEGHT , tmpR , damage , stage
    boat.update()
    map.update()
    for i in range(map.towerCnt):
        tmpR = RECT()
        tmpR.left, tmpR.bot, tmpR.right, tmpR.top = boat.R.left - Tile_SIZE* 3 , BackHIEGHT -boat.R.bot + Tile_SIZE*3, boat.R.right + Tile_SIZE*3, BackHIEGHT - boat.R.top - Tile_SIZE*3
        if boat.state is not 0 and InterSectRECT((map.tower[i].R.left + map.tower[i].R.right) / 2 , (map.tower[i].R.bot + map.tower[i].R.top) / 2 , tmpR):
            damage += speedy
            if damage > 1:
                boat.hp -= 1
                damage = 0

            pass

     #       print_fps(0,0)
    if boat.hp <= 0:
        boat.__init__()
        stage += 1
        boat.hp = stage * 10
        game_framework.push_state(NextStage)
    delay(speedy)


def draw():
    global BackWIDTH, BackHIEGHT, BackWIDTH, BackHIEGHT
    clear_canvas()
    BackGround.clip_draw(666, 708-583, BackWIDTH, BackHIEGHT, BackWIDTH/2, BackHIEGHT/2)
    boat.draw()
    map.draw()
    update_canvas()






