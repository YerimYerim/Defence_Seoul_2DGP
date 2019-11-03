import framework
import pico2d
import State_main
from setting import *
from pico2d import *
import gameover_stage
import State_NextStage
from framework import *

class Boat:
    Img = None
    HP_font = None
    def __init__(self):
        self.frame_ = 0
        self.hp = 10
        self.speed = 2.0
        self.type = 1  # 일반 1  보스 2
        self.R = RECT()
        self.R.bot, self.R.left, self.R.right, self.R.top = 7 * Tile_SIZE, 0, Tile_SIZE, 8 * Tile_SIZE
        self.move_times = 0
        self.white_color = [0, 0, 0]
        self.Boat_frame = 0
        self.frame_dir = 'R'
        if self.Img is None:
            self.Img = load_image('Spritesheet\\boat.png')
        if self.HP_font is None :
            self.HP_font = load_font('font\\SeoulNamsanB.ttf', 13)
        self.state = 0 # 0 - 대기 1 - 시작 2 - dead

    def Is_dead(self):
        if self.move_times >= Tile_SIZE * 27:
            self.state = 3
        if self.hp < 0:
            self.state = 2
        else:
            pass

    def draw(self):
        if self.hp >= 1:
            s = str( int (self.hp))
            self.Img.clip_draw(3 + 61 * self.Boat_frame, 400 - 116 - Boat_IMG_SIZE, Boat_IMG_SIZE + 5, Boat_IMG_SIZE,
                            (self.R.left+self.R.right) / 2 - 5  , (self.R.top + self.R.bot) / 2 + 15, Tile_SIZE + 10, Tile_SIZE + 10 )

            self.HP_font.draw((self.R.left + self.R.right) / 2 + self.Boat_frame / 5 - 5 , (self.R.top + self.R.bot) / 2 + 25, s, self.white_color)

    def go_right(self):
        self.R.left += self.speed
        self.R.right += self.speed

    def go_up(self):
        self.R.top += self.speed
        self.R.bot += self.speed

    def go_down(self):
        self.R.top -= self.speed
        self.R.bot -= self.speed

    def do(self):
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
        else:
            self.Is_dead()
            print("hi im dead")

        self.move_times += self.speed






    def update(self):
        global stage
        if self.state < 2:
            if self.Boat_frame >= 8:
                self.frame_dir = 'L'

            elif self.Boat_frame == 1:
                self.frame_dir = 'R'

            if self.frame_dir == 'L':
                self.frame_ += 1
                if self.frame_ % 5 == 0:
                    self.Boat_frame -= 1

            elif self.frame_dir == 'R':
                self.frame_ += 1
                if self.frame_ % 5 == 0:
                    self.Boat_frame += 1

        self.Is_dead()
        if self.state is 1:
            self.do()
        if self.state is 3:
            stage = 1
            framework.push_state(gameover_stage)
            print("push")

        pass