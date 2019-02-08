"""
Course:             CS 2302 - Data Structures
Author:             Nguyen, Abram
Assignment:         Lab 1
Instructor:         Fuentes, Olac
T.A.:               Nath, Anindita 
Last modified:      2/7/19

Purpose of program: The purpose of this program is to demonstrate and practice 
                    the use of recursion in drawing shapes and fractals.
"""

import matplotlib.pyplot as plt
import numpy as np
import math 

"""
#---------------------------------------------------------------------------------
#   PART 1: SQUARES ON CORNERS
#---------------------------------------------------------------------------------
"""
#Draws a square around a center point, then 1 smaller square centered on each corner
#   of the initial square (+4 squares). The 4 added squares are all half the size of 
#   the initial square.
def draw_squares_rec(ax,x,y,size,n):
    #base case
    if n>0:
        #draw the initial square around a center point
        ax.plot([x,x+size,x+size,x-size,x-size,x], 
                [y+size,y+size,y-size,y-size,y+size,y+size], color='k')
        #draw 4 more squares, one per corner of the initial square
        draw_squares_rec(ax,x+size,y+size,size/2,n-1)    #top-right corner
        draw_squares_rec(ax,x+size,y-size,size/2,n-1)    #bottom-right corner
        draw_squares_rec(ax,x-size,y-size,size/2,n-1)    #bottom-left corner
        draw_squares_rec(ax,x-size,y+size,size/2,n-1)    #top-left corner

#Figures
fig, ax = plt.subplots()    
draw_squares_rec(ax,0,0,100,2) #fig 1a
#draw_squares_rec(ax,x,y,size,n)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()

fig, ax = plt.subplots()    
draw_squares_rec(ax,0,0,100,3) #fig 1b
ax.axis('off')
ax.set_aspect(1.0)
plt.show()


fig, ax = plt.subplots()
draw_squares_rec(ax,0,0,100,4) #fig 1c
ax.axis('off')
ax.set_aspect(1.0)
plt.show()


"""
#---------------------------------------------------------------------------------
#   PART 2: CASCADING CIRCLES
#---------------------------------------------------------------------------------
"""
#create each circle using 'center' and 'rad' variables (defined for both PART 2 and PART 4)
def circle(center,radius): 
    n = int(4*radius*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[1]+radius*np.sin(t)
    y = center[0]+radius*np.cos(t)
    return x,y

#Draws 'n' number of circles, but every following circle's radius will be multiplied 
#   by decimal variable 'w' and will be pushed to the side, keeping completely within 
#   the outer circle's range.
def draw_circles(ax,n,center,r,w): 
    if n>0:
        x,y = circle(center,r)  
        ax.plot(x,y,color='k')  #draw a circle
        #move the new circle to the left, staying within the outer circle
        draw_circles(ax,n-1,[center[0],  center[1]+r*w-r],r*w,w) #new center = (r*w - r, 0)
        
#Figures
fig, ax = plt.subplots() 
draw_circles( ax, 10, [0,0],  100,   .6) #fig 2a
#draw_circles(ax, n, center, r, w)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()

fig, ax = plt.subplots() 
draw_circles( ax, 50, [0,0],  100,   .9) #fig 2b
ax.set_aspect(1.0)
ax.axis('off')
plt.show()

fig, ax = plt.subplots() 
draw_circles( ax, 100, [0,0],  100,   .95) #fig 2c
ax.set_aspect(1.0)
ax.axis('off')
plt.show()


"""
#---------------------------------------------------------------------------------
#   PART 3: BINARY TREE REPRESENTATION
#---------------------------------------------------------------------------------
"""
#Draw an initial tree, which is like a triangle without a bottom. This shape is a 
#   small binary tree with a head and 2 leaf nodes. 2 recursive calls (1 per leaf) 
#   will draw another small binary tree, like the initial tree, starting from each
#   leaf. The number of leaves in relation to the depth of the tree is 2^n.  
#   Note: n = DEPTH (counting edges).
def draw_bin_tree(ax,x,y,n,size): 
    #base case
    if n>0:
        #draw the initial shape (2 branches/lines)
        ax.plot([x,x-(2**n),x,x+(2**n)],[y,y-size,y,y-size], color='k')
        #draw 2 more branches growing from each previous branch
        draw_bin_tree(ax,x-(2**n),y-size,n-1,size)
        draw_bin_tree(ax,x+(2**n),y-size,n-1,size)

#Figures
fig, ax = plt.subplots()    
draw_bin_tree(ax,0,0,3,10) #fig 3a
#draw_bin_tree(ax,x,y,n,size) 
ax.set_aspect(1.0)
ax.axis('off')
plt.show()

fig, ax = plt.subplots()    
draw_bin_tree(ax,0,0,4,15) #fig 3b
ax.set_aspect(1.0)
ax.axis('off')
plt.show()

fig, ax = plt.subplots()    
draw_bin_tree(ax,0,0,6,45) #fig 3c
ax.set_aspect(1.0)
ax.axis('off')
plt.show()


"""
#---------------------------------------------------------------------------------
#   PART 4: SIX CIRCLES IN ONE
#---------------------------------------------------------------------------------
"""
#Draw an initial circle, then 5 circles within it in a fixed pattern. There will be
#   3 circles side-by-side, from edge-to-edge of the outer circle, horizontally and
#   vertically. This results in 5 circles within 1 larger circle, 6 total. Because
#   there are 5 inner circles for every circle, I wrote in 5 recursive calls.
def draw_circles(ax,n,center,r):
    if n>0: 
        #outer circle
        x,y = circle(center,r)
        ax.plot(x,y,color='k')

        r = r/3                 #the 5 circles inside each have 1/3 the radius of the outer circle
        x,y = circle(center,r)  #create a circle based on the new, smaller radius
        
        #center circle
        draw_circles(ax,n-1,center,r)
        ax.plot(x, y, color='k')        
        
        #new center point: ABOVE (+x coord.) the original center
        draw_circles(ax,n-1,[center[0]+r*2,  center[1]],r) 
        ax.plot(x, y+r*2, color='k')  
        #      'x, y+r*2' : move the origin for a new circle based on the radius of the outer circle 
        
        #new center point: RIGHT (+y coord.) of the original center
        draw_circles(ax,n-1,[center[0],      center[1]+r*2],r)
        ax.plot(x+r*2, y, color='k')
        
        #new center point: BELOW (-x coord.) the original center
        draw_circles(ax,n-1,[center[0]-r*2,  center[1]],r)
        ax.plot(x, y-r*2, color='k')
        
        #new center point: LEFT (-y coord.) of the original center
        draw_circles(ax,n-1,[center[0],      center[1]-r*2],r) 
        ax.plot(x-r*2, y, color='k')
        
#Figures
fig, ax = plt.subplots() 
draw_circles( ax, 2, [0,0],  100)   #fig 4a
#draw_circles(ax,n,center,r)
ax.set_aspect(1.0)
ax.axis('off')

fig, ax = plt.subplots() 
draw_circles( ax, 3, [0,0],  100)   #fig 4b
ax.set_aspect(1.0)
ax.axis('off')

fig, ax = plt.subplots() 
draw_circles( ax, 4, [0,0],  100)   #fig 4c
ax.set_aspect(1.0)
ax.axis('off')

#END OF PROGRAM
