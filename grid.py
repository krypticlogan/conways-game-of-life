from const import *
import numpy as np
from entity import Entity
import pygame
import math

class Grid:
    def __init__(self, size : tuple):
        self.ROWS = size[0]
        self.COLS = size[1]
        self.sqsize = WIDTH // self.ROWS
        self.grid =np.array([[Entity(row,col,self.sqsize,WHITE) for col in range(self.COLS)] for row in range(self.ROWS)])
        self.start =  None
        self.end = None


    def drawSquares(self, surface):
        for row in range(self.ROWS):
            for col in range(self.COLS):
                rect = (col * self.sqsize, row * self.sqsize, self.sqsize*.1, self.sqsize*.1)
                pygame.draw.rect(surface, GRAY, rect)

    def draw(self, screen):
        # self.drawSquares(screen)
        for row in range(self.ROWS):
            for col in range(self.COLS):
                city = self.grid[row][col]
                city.draw(screen)


    def changeGrid(self):
        for row in range(self.ROWS):
            for col in range(self.COLS):
                value = self.grid[row,col]

                surrounding = self.findParents(value)

                # ruleset(self.grid)
                if value.alive == True:   
                    if surrounding > 3:
                        self.grid[row,col].alive = False
                    elif surrounding < 2:
                        self.grid[row,col].alive = False
                if value.alive == False and surrounding == 3:
                    self.grid[row,col].alive = True
                
                

    def getCity(self,row,col):
        city = self.grid[row,col]
        return city
    
    def findParents(self,city):
        row = city.row
        col = city.col

        if(row == 0 or col == 0 or col == self.COLS-1 or row == self.ROWS-1):
            if(row == 0):
                startRow = row
                endRow = row + 2
            elif(row == self.ROWS-1):
                startRow = row - 1
                endRow = row+1
            else:
                startRow = row - 1
                endRow = row +2
            
            if(col == 0):
                startCol = col
                endCol = col + 2
            elif(col == self.COLS -1):
                endCol = col+1
                startCol = col-1
            else:
                startCol = col -1
                endCol = col + 2


            parents = np.array(self.grid[startRow : endRow, startCol : endCol])
            parents = np.array(parents).flatten()
        else:
            parents = self.grid[row-1: row+2, col-1: col+2]
            np.array(parents).flatten()
            parents = np.delete(parents, 4)
        count = 0

        for parent in parents:
            if parent.alive:
                count+=1
        # if count > 0: print(count)

        return count
    



        

# g = Grid()
# grid = g.grid

# start = grid[0,19]
# start.toggle()
# g.find_start()

# print(grid)
# print(g.findParents(start))
