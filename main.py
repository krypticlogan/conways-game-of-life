import pygame, sys
import numpy as np
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
from const import *
from grid import Grid





class Main:
    
    def __init__(self): 
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Pathfinder')
        self.Grid = Grid()
        self.clock = pygame.time.Clock()

    def getRowCol(self, pos):
        x , y = pos
        row = y // SQSIZE
        col = x // SQSIZE
        return row, col
    
    def mainLoop(self):
        self.clock.tick()
        running = self.running = True
        screen = self.screen


        while running:
            screen.fill(WHITE)
            self.Grid.draw(screen)
        
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    # Was it the Escape key? If so, stop the loop.
                    if event.key == K_ESCAPE:
                        running = False
                        sys.exit()
                elif event.type == QUIT:
                    running = False
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = self.getRowCol(pos)
                    city = self.Grid.grid[row,col]
                    city.toggle()

            pygame.display.update()

main = Main()
main.mainLoop()

