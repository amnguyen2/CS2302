# Starting point for program to build and draw a maze
# Modify program using disjoint set forest to ensure there is exactly one
# simple path joining any two cells
# Programmed by Olac Fuentes
# Last modified March 28, 2019

import matplotlib.pyplot as plt
import numpy as np
import random
import time

def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1

def find(S,i):
    # Returns root of tree that i belongs to
    if S[i]<0:
        return i
    return find(S,S[i])

def union(S,i,j):
    # Joins i's tree and j's tree, if they are different
    ri = find(S,i) 
    rj = find(S,j) 
    if ri!=rj: # Do nothing if i and j belong to the same set 
        S[rj] = ri  # Make j's root point to i's root

def find_c(S,i):
    if S[i]<0:
        return i
    r = find_c(S,S[i])
    S[i] = r
    return S[i]
    
def union_by_size(S, i, j):
    ri = find_c(S, i)
    rj = find_c(S, j)
    if ri != rj:
        if S[ri] > S[rj]:
            S[rj] += S[ri]
            S[ri] = rj
        else:
            S[ri] += S[rj]
            S[rj] = ri

def wall_list(maze_rows, maze_cols):
    w = []
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w

def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0  
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols   
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off') 
    ax.set_aspect(1.0)

###############################################################################

# normal union and find functions
def make_maze(size, walls):
    #Assign each cell to a different set in a disjoint set forest S
    S = DisjointSetForest(size*size)
    sets = 2
    #While S has more than 1 set:
    while sets > 1:
        #check number of sets
        sets = 0
        for i in range(len(S)):
            if S[i] < 0:
                sets+=1
        #Select a random wall w =[c1,c2]
        w = random.randint(0, len(walls)-1)
        #If cells c1 and c2 belong to different sets,
        if find(S, walls[w][1]) != find(S, walls[w][0]):
            #remove w and join c1’s set and c2’s set
            union(S, walls[w][0], walls[w][1])
            walls.pop(w)
    return walls


# using union by size and find path compression functions
def make_mazeUBS(size, walls):
    #Assign each cell to a different set in a disjoint set forest S
    S = DisjointSetForest(size*size)
    sets = 2
    #While S has more than 1 set:
    while sets > 1:
        #check number of sets
        sets = 0
        for i in range(len(S)):
            if S[i] < 0:
                sets+=1
        #Select a random wall w =[c1,c2]
        w = random.randint(0, len(walls)-1)
        #If cells c1 and c2 belong to different sets,
        if find_c(S, walls[w][1]) != find_c(S, walls[w][0]):
            #remove w and join c1’s set and c2’s set
            union_by_size(S, walls[w][0], walls[w][1])
            walls.pop(w)
    return walls

"""
###############################################################################
###############################################################################
###############################################################################
"""

plt.close("all") 
maze_size = [5, 10, 20, 30, 40] # more than 40 might crash my program

#normal union and find function
print("Making mazes using normal union and find functions...")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for s in maze_size: #for each sized maze,
    sum = 0
    for r in range(5): #collect an average maze creation time
        walls = wall_list(s, s)
        start = time.time() # start time
        maze = make_maze(s, walls) # timing make_maze() function (normal)
        end = time.time() # end time
        sum += end-start
    print("Average time making",s,"*",s,"maze →", round((sum*1000)/5, 8), "ms")
    

# union by size w/ path compression function
print("\nMaking mazes using union by size w/ path compression...")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for s in maze_size: #for each sized maze,
    sum = 0
    for r in range(5): #collect an average maze creation time
        wallsUBS = wall_list(s, s)
        start = time.time() # start time
        mazeUBS = make_mazeUBS(s, wallsUBS) # timing maze_mazeUBS() function (union by size w/compression)
        end = time.time() # end time
        sum += end-start
    print("Average time making",s,"*",s,"maze →", round((sum*1000)/5, 8), "ms")
    # 5 maze drawings using union by size w/ path compression
    draw_maze(mazeUBS, s, s, cell_nums=False) 
