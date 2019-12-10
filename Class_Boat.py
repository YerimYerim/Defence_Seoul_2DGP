
import framework
import pico2d
import State_main
from setting import *
from pico2d import *
import gameover_stage
import random
import State_NextStage
from framework import *
Fire = 0
Ice = 1
Light = 2
DownGrade = 3


Fire_Level = 1
Ice_Level = 1
Light_Level = 1
DownGrade_Level = 1

font_level = None


def Firing(bullet):
#    if random.randint(0, 100) <= Fire_Level:
        global fire_damage
        fire_damage = random.randint(1 + Fire_Level, ( 1 + Fire_Level) * 2)
        bullet.To.Hp -= fire_damage


def Icing(bullet):
#    if random.randint(0,100) <= Ice_Level * 10:
        bullet.To.Speed = bullet.To.Speed * (0.99 **Ice_Level)


def Lightning(bullet):
    pass


def DownGrading(bullet):
    if random.randint(0, 100) <= DownGrade_Level:
        bullet.To.Hp -= bullet.To.Hp / 100 * 10

def draw_Level(Fire_Level , Ice_Level , Light_Level, DownGrade_Level):
    global font_level
    if font_level is None:
        font_level = load_font('font\\PressStart2P.ttf', 12)
    s = "Lv." + str(Fire_Level)
    font_level.draw(Tile_SIZE * 0.5, Tile_SIZE * 0.3, s, (0, 0, 0))
    s = "Lv." + str(Ice_Level)
    font_level.draw(Tile_SIZE * 2.5, Tile_SIZE * 0.3, s, (0, 0, 0))
    s = "Lv." + str(Light_Level)
    font_level.draw(Tile_SIZE * 4.5, Tile_SIZE * 0.3, s, (0, 0, 0))
    s = "Lv." + str(DownGrade_Level)
    font_level.draw(Tile_SIZE * 6.5, Tile_SIZE * 0.3, s, (0, 0, 0))

class Boat:
    Img = None
    HP_font = None
    crash_font = None
    def __init__(self):
        self.Frame = 0
        self.Hp = 10
        self.Speed = 2.0
        self.Type = 1  # 일반 1  보스 2
        self.Rectangle = RECT()
        self.Rectangle.bot, self.Rectangle.left, self.Rectangle.right, self.Rectangle.top = 7 * Tile_SIZE, 0, Tile_SIZE, 8 * Tile_SIZE
        self.Move_Times = 0
        self.White_color = [0, 0, 0]
        self.Boat_frame = 0
        self.Frame_Dir = 'R'
        self.state = -1
        self.state_fire = False
        self.state_Light = False
        self.state_Ice  = False
        self.state_down = False
        if self.Img is None:
            self.Img = load_image('Spritesheet\\boat.png')
        if self.HP_font is None :
            self.HP_font = load_font('font\\SeoulNamsanB.ttf', 13)
        self.state = 0  # 0 - 대기 1 - 시작 2 - dead
        if self.crash_font is None:
            self.crash_font = load_font('font\\SeoulNamsanB.ttf', 13)

    def Is_dead(self):
        if self.Move_Times >= Tile_SIZE * 28:
            self.state = 3
        if self.Hp <= 0:
            self.state = 2
        else:
            pass

    def draw(self):
        global fire_damage
        if self.state_fire is True and self.state_down is False and self.state_Light is False:
            self.crash_font.draw(self.Rectangle.left, self.Rectangle.bot, "-" + str(fire_damage+1), (255, 0, 0))
        if self.state_Light is True and self.state_down is False and self.state_fire is False:
            self.crash_font.draw(self.Rectangle.left, self.Rectangle.top, "LIGHT", (255, 255, 0))
        if self.state_Ice is True :
            self.crash_font.draw(self.Rectangle.right,self.Rectangle.top, "ICE", (0, 0, 255))
        if self.state_down is True and self.state_fire is False and self.state_Light is False:
            self.crash_font.draw(self.Rectangle.right,self.Rectangle.bot, "Down", (0, 255, 0))
            pass
        if self.Hp >= 0:
            s = str(int (self.Hp))
            self.Img.clip_draw(3 + 61 * self.Boat_frame, 400 - 116 - Boat_IMG_SIZE, Boat_IMG_SIZE + 5, Boat_IMG_SIZE,
                               (self.Rectangle.left + self.Rectangle.right) / 2, (self.Rectangle.top + self.Rectangle.bot) / 2 + 10, Tile_SIZE , Tile_SIZE )

            self.HP_font.draw((self.Rectangle.left + self.Rectangle.right) / 2 + self.Boat_frame / 5 - 5, (self.Rectangle.top + self.Rectangle.bot) / 2 + 10, s, self.White_color)

    def go_right(self):
        self.Rectangle.left += self.Speed
        self.Rectangle.right += self.Speed

    def go_up(self):
        self.Rectangle.top += self.Speed
        self.Rectangle.bot += self.Speed

    def go_down(self):
        self.Rectangle.top -= self.Speed
        self.Rectangle.bot -= self.Speed

    def do(self):
        if self.Move_Times < Tile_SIZE * 2 - 2:
            self.go_right()
            self.Move_Times += self.Speed

        elif self. Move_Times < Tile_SIZE * 3:
            self.go_down()

        elif self.Move_Times < Tile_SIZE * 5 - 1:
            self.go_right()

        elif self.Move_Times < Tile_SIZE * 6:
            self.go_down()

        elif self.Move_Times < Tile_SIZE * 7 - 1:
            self.go_right()

        elif self.Move_Times < Tile_SIZE * 8:
            self.go_down()

        elif self.Move_Times < Tile_SIZE * 10 - 1:
            self.go_right()

        elif self.Move_Times < Tile_SIZE * 11:
            self.go_up()

        elif self.Move_Times < Tile_SIZE * 12 - 1:
            self.go_right()

        elif self.Move_Times < Tile_SIZE * 13:
            self.go_up()

        elif self.Move_Times < Tile_SIZE * 15 - 1:
            self.go_right()

        elif self.Move_Times < Tile_SIZE * 16:
            self.go_down()

        elif self.Move_Times < Tile_SIZE * 18 - 1:
            self.go_right()

        elif self.Move_Times < Tile_SIZE * 19:
            self.go_down()

        elif self.Move_Times < Tile_SIZE * 21 - 1:
            self.go_right()

        elif self.Move_Times < Tile_SIZE * 22:
            self.go_up()

        elif self.Move_Times < Tile_SIZE * 23 - 1:
            self.go_right()

        elif self.Move_Times < Tile_SIZE * 24:
            self.go_up()

        elif self.Move_Times < Tile_SIZE * 25 - 1:
            self.go_right()

        elif self.Move_Times < Tile_SIZE * 26:
            self.go_up()

        elif self.Move_Times < Tile_SIZE * 27:
            self.go_right()
        else:
            self.Is_dead()

        self.Move_Times += self.Speed


    def update(self):
        if self.state < 2:
            if self.Boat_frame >= 8:
                self.Frame_Dir = 'L'

            elif self.Boat_frame == 1:
                self.Frame_Dir = 'R'

            if self.Frame_Dir == 'L':
                self.Frame += 1
                if self.Frame % 5 == 0:
                    self.Boat_frame -= 1

            elif self.Frame_Dir == 'R':
                self.Frame += 1
                if self.Frame % 5 == 0:
                    self.Boat_frame += 1

        self.Is_dead()
        if self.state is 1:
            self.do()
        if self.state is 3:
            self.state = 1
            framework.push_state(gameover_stage)

        pass