import random
import Class_Boat
from Class_Bullet import *

Fire = 0
Ice = 1
Light = 2
DownGrade = 3

Fire_Level = 1
Ice_Level = 1
Light_Level = 1
DownGrade_Level = 1


def Firing(bullet):
    if random.randint(0, 100) <= Fire_Level:
        bullet.To.Hp -= random.randint(5, 10)
        print ("passive fire")


def Icing(bullet):
    if random.randint(0,100) <= Ice_Level * 10:
        bullet.To.Speed = bullet.To.Speed * 0.95


def Lightning(bullet):

    if random.randint(0,100) <= Light_Level:
        pass

def DownGrading(bullet):

    if random.randint(0, 100) <= DownGrade_Level:
        bullet.To.Hp -= bullet.To.Hp / 100 * 5