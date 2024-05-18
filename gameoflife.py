import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import pygame

from grid import Grid

def getRowCol(pos, sqsize):
        x , y = pos
        row = y // sqsize
        col = x // sqsize
        return row, col


def animate(world : np.array, ruleset, iterations, fps=60) -> None:
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()
    grid = Grid((len(world), len(world)))
    running = True
    gen = 0
    entered = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = getRowCol(pos, grid.sqsize)
                    entity = grid.grid[row,col]
                    entity.toggle()

            if event.type == pygame.KEYDOWN:
                entered = True
                print(event.key)
                # while gen < iterations:
                #     gen+=1
                #     grid.changeGrid()
                    # grid.draw(screen)


        screen.fill("white")

        


        # RENDER YOUR GAME HERE
        # world = Grid((len(world),len(world)))
        # print(entered)
        grid.draw(screen)
        
        if entered == True: 
            grid.changeGrid()
            gen+=1

        # gen+=1
        # world = conways_game_of_life(world)
        # img.set_data(world)
        pygame.display.set_caption(f'Generation {gen}')
        if gen == iterations: break
        pygame.display.flip()

        clock.tick(fps)  # limits FPS to 60

    pygame.quit()

def init_world(size : int, randomize = False, high_chance = .55) -> np.array:
    if randomize:
        # return np.random.choice([0, 0, 0 , 1], size=(size, size))
        return np.rint(np.random.uniform(low=0, high=high_chance, size=(size,size)))
        # zeros = np.zeros(shape=(size,size))
        # base = np.empty(shape=(size,size), dtype=object)
        # for i in range(size):
        #     for j in range(size):
        #         base[i][j] = entity(coordinates = (i, j), state=randoms[i][j])
        # return base
        # return 0
    base = np.zeros(shape=(size,size))

    return base
# world = init_world(100)
# print(world)
def count_surrounding(grid : np.array, coordinates : tuple) -> int:

    top = None
    left = None
    bottom = None
    right = None
    # ltcorner
    # lbcorner
    # rtcorner
    # rbcorner
    y = coordinates[0]
    x = coordinates[1]
    neighbors = []
    # print(f"coordinates : {coordinates}")

    # van Nuemann neighbors
    #top and bottom values
    if y != 0:
        neighbors.append(grid[y-1][x])
        top = True
    if y < len(grid)-1:
        neighbors.append(grid[y+1][x])
        bottom = True

    #left and right values
    if x != 0:
        neighbors.append(grid[y][x-1])
        left = True
    if x < len(grid)-1:
        neighbors.append(grid[y][x+1])
        right = True

    # Diagnols : Moore's 
    if bottom:
        if left:
            neighbors.append(grid[y+1][x-1])
        if right:
            neighbors.append(grid[y+1][x+1])
    if top:
        if left:
            neighbors.append(grid[y-1][x-1])
        if right:
            neighbors.append(grid[y-1][x+1])
    
    count = 0
    for neighbor in neighbors:
        if neighbor == 1:
            count+=1
    # print(f"Values : {neighbors}")
    # print(count)

    return count

def conways_game_of_life(world : np.array) -> None:
    world_copy = world.copy()
    
    for i in range(len(world)):
        for j in range (len(world[0])):
            value = world_copy[i][j]
            surrounding : int = count_surrounding(world, (i , j))
            if value == 1:   
                if surrounding > 3:
                    world_copy[i][j] = 0
                elif surrounding < 2:
                    world_copy[i][j] = 0
            if value == 0 and surrounding == 3:
                world_copy[i][j] = 1
    return world_copy


def mazelike(world : np.array) -> None:
    world_copy = world.copy()
    
    for i in range(len(world)):
        for j in range (len(world[0])):
            value = world_copy[i][j]
            surrounding : int = count_surrounding(world, (i , j))
            if value == 1:   
                if surrounding > 4:
                    world_copy[i][j] = 0
                elif surrounding < 2:
                    world_copy[i][j] = 0
            if value == 0 and surrounding == 3:
                world_copy[i][j] = 1
    return world_copy

def chaos(world : np.array) -> None:
    world_copy = world.copy()
    
    for i in range(len(world)):
        for j in range (len(world[0])):
            value = world_copy[i][j]
            surrounding : int = count_surrounding(world, (i , j))
            if value == 1:   
                if surrounding > 5:
                    world_copy[i][j] = 0
                elif surrounding < 3:
                    world_copy[i][j] = 0
            if value == 0 and surrounding == 2:
                world_copy[i][j] = 1
    return world_copy

def idkyet(world : np.array) -> None:
    world_copy = world.copy()
    
    for i in range(len(world)):
        for j in range (len(world[0])):
            value = world_copy[i][j]
            # surrounding : int = count_surrounding(world, (i , j))
            
    return world_copy 
# print(update_world(randomWorld))
def run_animation(world, iterations, interval):
    gen = 0
    fig, ax = plt.subplots()
    img = ax.imshow(world, cmap='binary')

    def update(frame):
        nonlocal world
        nonlocal gen
        gen += 1
        world = conways_game_of_life(world)
        img.set_data(world)
        plt.title(f'Generation {gen}')
        return img,
    
    ani = animation.FuncAnimation(fig, update, frames=iterations, interval = interval, repeat = False)
    plt.show()

world = init_world(100, randomize=True, high_chance=.55) # game of life high population
# mazelike = init_world(150, randomize=True, high_chance=.6)
# run_animation(world, 300, 100)

animate(world, ruleset=conways_game_of_life, iterations = 2000, fps = 15)