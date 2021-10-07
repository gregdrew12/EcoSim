from creature import Creature
from food import Food
import random

def init():
    global map 
    map = [[None] * 20 for i in range(20)]

    global creature
    creature = Creature(True)

    global food
    food = Food(random.randint(1, len(map)-1), random.randint(1, len(map[0])-1))

    map[0][0] = creature
    map[food.row][food.col] = food