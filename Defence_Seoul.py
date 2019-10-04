from pico2d import *
IMG_HEIGHT = 701
IMG_WIDTH = 1648
BackWIDTH = 961
BackHIEGHT = 567
tower_IMG_SIZE = 140
Boat_IMG_SIZE = 135
Tile_SIZE = 57
x = 0
y = 0


class RECT:
    left = 0
    bot = 0
    right = 0
    top = 0


class Tower:
    Type = -1   # 0 -fire 1 - Ice 2 -lighting 3 - downGrade
    Level = 1
    R = RECT()

font = None

class Boat:
    hp = 10
    speed = 1.0
    type = 1    # 일반 1  보스 2
    R = RECT()
    R.bot = 7 * Tile_SIZE
    R.left = 0
    R.right = Tile_SIZE
    R.top = 8 * Tile_SIZE
    move_times = 0
    HP_font = None
    white_color = [255, 255, 255]

    def draw(self):
        s = str(self.hp)
        self.HP_font = load_font('font\\SeoulNamsanB.ttf', 20)
        BackGround.clip_draw(32, 6, Boat_IMG_SIZE, Boat_IMG_SIZE,
                             (self.R.left+self.R.right) / 2, (self.R.top + self.R.bot) / 2, Tile_SIZE, Tile_SIZE)
        self.HP_font.draw((self.R.left + self.R.right) /2 - 10, (self.R.top + self.R.bot) / 2, s, self.white_color)


    def go_right(self):
        self.R.left += self.speed
        self.R.right += self.speed

    def go_up(self):
        self.R.top += self.speed
        self.R.bot += self.speed

    def go_down(self):
        self.R.top -= self.speed
        self.R.bot -= self.speed

    def move(self):
        if self.move_times < Tile_SIZE * 2 - 2:
            self.go_right()
            self.move_times += self.speed

        elif self. move_times < Tile_SIZE * 3:
            self.go_down()

        elif self.move_times < Tile_SIZE * 5 - 1:
            self.go_right()

        elif self.move_times < Tile_SIZE * 6:
            self.go_down()

        elif self.move_times < Tile_SIZE * 7 - 1:
            self.go_right()

        elif self.move_times < Tile_SIZE * 8:
            self.go_down()

        elif self.move_times < Tile_SIZE * 10 - 1:
            self.go_right()

        elif self.move_times < Tile_SIZE * 11:
            self.go_up()

        elif self.move_times < Tile_SIZE * 12 - 1:
            self.go_right()

        elif self.move_times < Tile_SIZE * 13:
            self.go_up()

        elif self.move_times < Tile_SIZE * 15 - 1:
            self.go_right()

        elif self.move_times < Tile_SIZE * 16:
            self.go_down()

        elif self.move_times < Tile_SIZE * 18 - 1:
            self.go_right()

        elif self.move_times < Tile_SIZE * 19:
            self.go_down()

        elif self.move_times < Tile_SIZE * 21 - 1:
            self.go_right()

        elif self.move_times < Tile_SIZE * 22:
            self.go_up()

        elif self.move_times < Tile_SIZE * 23 - 1:
            self.go_right()

        elif self.move_times < Tile_SIZE * 24:
            self.go_up()

        elif self.move_times < Tile_SIZE * 25 - 1:
            self.go_right()

        elif self.move_times < Tile_SIZE * 26:
            self.go_up()

        elif self.move_times < Tile_SIZE * 27:
            self.go_right()
       # elif self.move_times == Tile_SIZE * 27:

        self.move_times += self.speed

open_canvas(BackWIDTH, BackHIEGHT)

BackGround = None
running = True
boat = Boat()



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
    pass

BackGround = load_image('resources.png')
B = Boat()


while running:
    clear_canvas()
    BackGround.clip_draw(666, 708-583, BackWIDTH, BackHIEGHT, BackWIDTH/2, BackHIEGHT/2)
    B.move()
    B.draw()
    update_canvas()
    handle_events()
    delay(0.01)

close_canvas()

