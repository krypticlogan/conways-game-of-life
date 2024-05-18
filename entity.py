import pygame
import const as const
from const import *


class Entity:
    
    PADDING = .2

    def __init__(self, row, col, size, color):
        self.row = row
        self.col = col
        self.size = size
        self.color = color
        self.alive = False
        self.x = 0
        self.y = 0
        self.calc_coords()
        # self.index = self.row * ROWS + self.col


    def draw(self, screen):
        length = self.size - self.PADDING
        rect = pygame.Rect(self.x+5, self.y+5, length, length)
        if self.alive:
            self.color = BLACK
        else: self.color = WHITE
        pygame.draw.rect(screen, self.color, rect)

    def calc_coords(self):
        self.x = self.col * self.size
        self.y = self.row * self.size

    # def findF(self):
    #     if self.start:
    #         self.f = 0
    #     else:
    #         self.f = self.h + self.g


    def toggle(self):
        if self.alive == False:
            self.color = BLUE
            # self.enroute = True
            self.alive = True
            const.num_selected+=1
        else: 
            self.color = WHITE
            self.enroute = False
            self.alive = False
            const.num_selected-=1
    
        
    def __repr__(self):
        # if self.start:
        #     return str('S')
        # if self.end:
        #     return str('E')
        if self.alive:
            return str('Y')
        else: 
            return str('N')


    # def __repr__(self):
    #     return str(self.index)