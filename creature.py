from food import *
import random
import settings

class Creature():
    def __init__(self, sight):
        self.sight = sight

        self.row = 0
        self.col = 0
        self.prev_row = 0
        self.prev_col = 0
        self.hungry = True
        self.sees_food = False
        self.direction = None
        self.move_count = 0

    def sim(self):
        while(self.hungry):
            self.move()
        print("Food found in " + str(self.move_count) + " moves!")

    def move(self):
        if(self.sees_food):
            self.prev_row = self.row
            self.prev_col = self.col
            if(self.direction == 'N'): self.row += -1
            elif(self.direction == 'E'): self.col += 1
            elif(self.direction == 'S'): self.row += 1
            else: self.col += -1
        else:
            next_pos = random.choice(self.valid_moves())
            self.prev_row = self.row
            self.prev_col = self.col
            self.row = next_pos[0]
            self.col = next_pos[1]
            self.set_direction()
            if(self.sight): self.look_for_food()
            if(self.sees_food): print("Food in sight!")
        
        self.move_count += 1
        if(self.row == settings.food.row and self.col == settings.food.col): self.hungry = False
        print("Food: " + str(settings.food.row) + " " + str(settings.food.col))
        print("Creature: " + str(self.row) + " " + str(self.col))
        print(self.direction)
        

    def valid_moves(self):
        list = []

        if(self.row-1 >= 0): 
            if(self.row-1 != self.prev_row): list.append([self.row-1, self.col])
        if(self.col+1 <= len(settings.map[0])-1): 
            if(self.col+1 != self.prev_col): list.append([self.row, self.col+1])
        if(self.row+1 <= len(settings.map)-1):
            if(self.row+1 != self.prev_row): list.append([self.row+1, self.col])
        if(self.col-1 >= 0):
            if(self.col-1 != self.prev_col): list.append([self.row, self.col-1])
        return list

    def set_direction(self):
        if(self.row < self.prev_row): self.direction = 'N'
        elif(self.col > self.prev_col): self.direction = 'E'
        elif(self.row > self.prev_row): self.direction = 'S'
        else: self.direction = 'W'

    def look_for_food(self):
        if(self.direction == 'N'):
            if(self.col == settings.food.col and self.row > settings.food.row): self.sees_food = True
        elif(self.direction == 'E'):
            if(self.row == settings.food.row and self.col < settings.food.col): self.sees_food = True
        elif(self.direction == 'S'):
            if(self.col == settings.food.col and self.row < settings.food.row): self.sees_food = True
        else:
            if(self.row == settings.food.row and self.col > settings.food.col): self.sees_food = True