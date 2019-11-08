import random
import Class_Boat
from Class_Bullet import *
import setting
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
        bullet.To.Hp -= random.randint(1, Fire_Level * 2)
        print ("passive fire")


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