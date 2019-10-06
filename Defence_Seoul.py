from pico2d import *
IMG_HEIGHT = 701
IMG_WIDTH = 1648
BackWIDTH = 961
BackHIEGHT = 567
tower_IMG_SIZE = 140
Boat_IMG_SIZE = 50
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
    white_color = [0, 0, 0]
    Img = None
    Boat_frame = 0
    frame_dir = 'R'

    def draw(self):
        s = str(self.hp)

        if self.Boat_frame >= 7:
            self.frame_dir = 'L'

        if self.Boat_frame <= 0:
            self.frame_dir = 'R'

        if self.frame_dir == 'L':
            self.Boat_frame -= 1

        if self.frame_dir == 'R':
            self.Boat_frame += 2

        self.Img = load_image('boat.png')
        self.HP_font = load_font('font\\SeoulNamsanB.ttf', 15)
        self.Img.clip_draw(3 + 61 * self.Boat_frame, 400 - 116 - Boat_IMG_SIZE, Boat_IMG_SIZE+5, Boat_IMG_SIZE,
                        (self.R.left+self.R.right) / 2, (self.R.top + self.R.bot) / 2, Tile_SIZE - 10, Tile_SIZE - 10)
        self.HP_font.draw((self.R.left + self.R.right) /2 + self.Boat_frame / 5  - 2 , (self.R.top + self.R.bot) / 2 + 5, s, self.white_color)
        print(self.Boat_frame)
        print(self.frame_dir)




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
Wave = None
running = True
boat = Boat()
boat.Img = load_image('boat.png')


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

BackGround = load_image('resource.png')
Wave = load_image('wave_background.jpg')
B = Boat()
wave_x = 0

while running:
    clear_canvas()

    Wave.clip_draw(-x, 0, BackWIDTH, BackHIEGHT, BackWIDTH/2, BackHIEGHT/2)
    BackGround.clip_draw(666, 708-583, BackWIDTH, BackHIEGHT, BackWIDTH/2, BackHIEGHT/2)
    B.move()
    B.draw()
    update_canvas()
    handle_events()
    x+= 1
    delay(0.05)

close_canvas()

