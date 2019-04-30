"""
Author:             Nguyen, Abram
Assignment:         Lab 7
Course:             CS 2302 - Data Structures
Instructor:         Fuentes, Olac
T.A.:               Nath, Anindita 
Last modified:      

Purpose of program: The purpose of this program is to demonstrate different 
                        path finding algorithms by solving a maze created using
                        a disjoint set forest. The algorithms implemented are
                        breadth first search, depth first search using stacks,
                        and depth first search using recursion.
"""
import matplotlib.pyplot as plt
import numpy as np
import random
import queue
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

def numSets(S):
    c = 0
    for n in S:
        if n < 0:
            c += 1
    return c

def make_maze(size, walls):
    m = size*size-1 # always result in a unique path, for experiment
    n = size*size
    S = DisjointSetForest(n)
    # print(f"\nThere are {n} cells and {len(walls)} walls total, {m} walls will be removed.")
    if m > n-1:
        sets = numSets(S)
        # print("There is at least one path from source to destination.\n")
        if m > len(walls): # if all walls are going to be removed
            return []
        # remove walls...
        while m > 0:
            #Select a random wall w =[c1,c2]
            w = random.randint(0, len(walls)-1)
            #If cells c1 and c2 belong to different sets...
            if find_c(S, walls[w][0]) != find_c(S, walls[w][1]):
                #remove w and join c1’s set and c2’s set
                union_by_size(S, walls[w][0], walls[w][1])
                walls.pop(w)
                m -= 1
                sets -= 1
            if sets == 1: # avoid infinite loop
                walls.pop(w)
                m -= 1
        return walls
    # Experiment is set up so that a unique path always exists
    """
    elif m < n-1:
        print("A path from source to destination is not guaranteed to exist.\n")
    elif m == n-1:
        print("There is a unique path from source to destination.\n")
    """
    while m > 0:
        #Select a random wall w =[c1,c2]
        w = random.randint(0, len(walls)-1)
        #If cells c1 and c2 belong to different sets...
        if find_c(S, walls[w][0]) != find_c(S, walls[w][1]):
            #remove w and join c1’s set and c2’s set
            union_by_size(S, walls[w][0], walls[w][1])
            walls.pop(w)
            m -= 1
    return walls
                
def walls_to_adj_list(walls, size, walls_og):
    G = []
    for g in range(size*size):
        G.append([])
    for w in walls_og:
        if w not in walls: # if there is a wall, cells aren't adjacent
            G[w[0]].append(w[1]) # insert adjacency
            G[w[1]].append(w[0]) # in undirected graph
    return G

# referenced from given graph search pseudocode
def BFS(G, v):
    visited = [False]*len(G)
    visited[v] = True
    prev = [-1]*len(G)
    Q = queue.Queue() # https://docs.python.org/2/library/queue.html#queue-objects
    Q.put(v) # enqueue v
    while not Q.empty():
        u = Q.get() # dequeue
        for t in G[u]:
            if not visited[t]:
                visited[t] = True
                prev[t] = u
                Q.put(t) # enqueue t
    return prev

# referenced from given graph search pseudocode
def DFS_stack(G, v):
    visited = [False]*len(G)
    visited[v] = True
    prev = [-1]*len(G)
    S = []
    S.append(v) # add v to stack
    while len(S) > 0:
        u = S.pop() # take from top of stack
        for t in G[u]:
            if not visited[t]:
                visited[t] = True
                prev[t] = u
                S.append(t) # add t to stack
    return prev    

# referenced from given graph search pseudocode
def DFS_rec(G, v):
    visited[v] = True
    for t in G[v]:
        if visited[t] is False:
            prev[t] = v
            DFS_rec(G, t)
    return prev

# referenced from given graph search pseudocode
def printPath(prev, v):
    if prev[v] != -1:
        printPath(prev, prev[v])
        print("→", end="")
    print(v, end="")
    
# draw a line that leads from cell 0 to the last cell in a maze
# https://matplotlib.org/2.0.2/api/_as_gen/matplotlib.axes.Axes.plot.html
def draw_path(walls, maze_rows, maze_cols, G, cell_nums=False):
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

    B = BFS(G, 0)
    i = len(B)-1
    while B[i] != -1:
        if i - B[i] == 1: # draw horizontal line
            x0 = i%maze_cols + .5
            x1 = x0 - 1
            y0 = B[i]//maze_rows + .5
            y1 = y0
        else: # draw vertical line
            x0 = i%maze_cols + .5
            x1 = x0
            y0 = B[i]//maze_rows + .5
            y1 = y0 - 1
        # print("FROM", x0, y0, "TO", x1, y1)
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='r')
        i = B[i]

    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols   
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
                
    ax.axis('on') 
    ax.set_aspect(1.0)
    
"""
###############################################################################
###############################################################################
###############################################################################
"""

plt.close("all")
# different maze sizes, num of cells = size*size
sizes = [20, 30, 40, 50, 60, 70, 80]
global visited
global prev

# For each maze size, record the average time it takes to solve a randomly
# constructed maze using breadth first search, depth first search using stacks,
# and depth first search using recursion.
print(f"Average Running Times\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for size in sizes: 
    sums = [0, 0, 0]
    for i in range(5):
        # form walls
        walls_original = wall_list(size, size)
        walls = wall_list(size, size)
        # construct a maze
        maze = make_maze(size, walls)
        # create adj list representation of maze
        G = walls_to_adj_list(walls, size, walls_original)
        
        # record BFS time
        start = time.time()
        B = BFS(G, 0)
        end = time.time()
        sums[0] += end-start
        
        # record DFS_stack time
        start = time.time()
        D = DFS_stack(G, 0)
        end = time.time()
        sums[1] += end-start
        
        
        visited = [False]*len(G)
        prev = [-1]*len(G)
        # record DFS_rec time
        start = time.time()
        R = DFS_rec(G, 0)
        end = time.time()
        sums[2] += end-start
        """
        print("→ Breadth First Search: ", end="")
        printPath(B, size*size-1)
        print()
        
        print("→ Depth First Search (Stack): ", end="")
        printPath(D, size*size-1)
        print()
        
        print("→ Depth First Search (Recursion): ", end="")
        printPath(R, size*size-1)
        print()
        """
        
    # calculate and display average time for size of maze
    sums = [round(s*1000/5, 7) for s in sums]
    print(f"For {size}x{size} maze:", end=" ")
    print(f"\nBreadth First Search →            {sums[0]} ms", end = " ")
    print(f"\nDepth First Search (Stack) →      {sums[1]} ms", end = " ")
    print(f"\nDepth First Search (Recursion) →  {sums[2]} ms", end = " ")
    print(f"\n")
    # draw maze
    draw_maze(maze, size, size, cell_nums=False)
    # draw_path(walls, size, size, G)

###############################################################################
# End of program