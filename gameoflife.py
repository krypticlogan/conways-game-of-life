import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def init_world(size : int, randomize = False, high_chance = .55) -> np.array:
    if randomize:
        # return np.random.choice([0, 0, 0 , 1], size=(size, size))
        return np.rint(np.random.uniform(low=0, high=high_chance, size=(size,size)))
        # return 0
    return np.zeros(shape=(size,size))
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

def update_world(world : np.array) -> None:
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
# print(update_world(randomWorld))
def run_animation(world, iterations, interval):
    gen = 0
    fig, ax = plt.subplots()
    img = ax.imshow(world, cmap='binary')

    def update(frame):
        nonlocal world
        nonlocal gen
        gen += 1
        world = update_world(world)
        img.set_data(world)
        plt.title(f'Generation {gen}')
        return img,
    
    ani = animation.FuncAnimation(fig, update, frames=iterations, interval = interval, repeat = False)
    plt.show()

world = init_world(150, randomize=True, high_chance=.60)
print(world)
run_animation(world, 200, 75)