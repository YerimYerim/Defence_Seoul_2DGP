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


def Firing(bullet = Bullet()):
    if random.randint(0, 100) <= Fire_Level:
        bullet.To.hp -= random.random(0,5)


def Icing(bullet = Bullet()):
    if random.randint(0,100) <= Ice_Level:
        bullet.To.Speed = bullet.To.Speed * 0.95


def Lightning(bullet= Bullet()):
    if random.randint(0,100) <= Light_Level:
        pass

def DownGrading(bullet = Bullet()):
    if random.randint(0, 100) <= DownGrade_Level:
        bullet.To.hp -= bullet.To.hp / 100 * 5