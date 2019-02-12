"""
######################################################################################
#                                                                                    #
#                           --- EXPERIMENTAL SECTION ---                             #
#                                 !!HARD HATS ON!!                                   #
#                                                                                    #
######################################################################################

Course:             CS 2302 - Data Structures
Author:             Nguyen, Abram
Assignment:         Lab 1
Instructor:         Fuentes, Olac
T.A.:               Nath, Anindita 
Last modified:      2/6/19

Purpose of program: The purpose of this program is to demonstrate the use of recursion in 
                    drawing shapes and fractals.
"""

import matplotlib.pyplot as plt
import numpy as np
import math 
#---------------------------------------------------------------------------------
#PART 1: SQUARES ON CORNERS  -  EXPERIMENTAL
#---------------------------------------------------------------------------------
def draw_squares_rec(ax,x,y,size,n):
    #base case
    if n>0:
        
        ax.plot([x,x+size,x+size,x-size,x-size,x], 
                [y+size,y+size,y-size,y-size,y+size,y+size], color='k')
        #instead of placing the squares on corners, place them so that their sides/corners overlap...
        #...it created a GRID of squares! The height and width are (2^n)/2
        draw_squares_rec(ax,x+size/2,y+size/2,size/2,n-1)    
        draw_squares_rec(ax,x+size/2,y-size/2,size/2,n-1)    
        draw_squares_rec(ax,x-size/2,y-size/2,size/2,n-1)    
        draw_squares_rec(ax,x-size/2,y+size/2,size/2,n-1)   

fig, ax = plt.subplots()
draw_squares_rec(ax,0,0,100,3)
ax.axis('off')
ax.set_aspect(1.0)
plt.show()
    
fig, ax = plt.subplots()
draw_squares_rec(ax,0,0,100,5)
ax.axis('off')
ax.set_aspect(1.0)
plt.show()

#---------------------------------------------------------------------------------
#PART 2: CASCADING CIRCLES  -  EXPERIMENTAL
#---------------------------------------------------------------------------------
def circle(center,rad):  
    n = int(4*rad*math.pi)
    #I can change how much of the circle is made, it can be made into just a slice:
    #t = np.linspace(0,3,n) 
    t = np.linspace(0,6.3,n)
    x = center[1]+rad*np.sin(t)
    y = center[0]+rad*np.cos(t)
    return x,y

def draw_circles(ax,n,center,r,w): 
    if n>0:
        x,y = circle(center,r)  
        ax.plot(x,y,color='k')  
        
        #editing the third parameter allows me to change the pattern of circles
        #right-left-right-left... pattern
        if n%2 == 0:
            draw_circles(ax,n-1,[center[0],  center[1]-r*w+r],r*w,w) 
        else:
            draw_circles(ax,n-1,[center[0],  center[1]+r*w-r],r*w,w)

fig, ax = plt.subplots() 
draw_circles( ax, 100, [0,0],  100, .9) 
ax.set_aspect(1.0)
ax.axis('off')
plt.show()

fig, ax = plt.subplots() 
draw_circles( ax, 10, [0,0],  100, .7) 
ax.set_aspect(1.0)
ax.axis('off')
plt.show()

fig, ax = plt.subplots() 
draw_circles( ax, 4, [0,0],  100, .5) 
ax.set_aspect(1.0)
ax.axis('off')
plt.show()

def draw_circles2(ax,n,center,r,w): 
    if n>0:
        x,y = circle(center,r)  
        ax.plot(x,y,color='k')
        
        #recreates PART 4 figure
        draw_circles2(ax,n-1,[center[0],  center[1]],r*w,w)         
        draw_circles2(ax,n-1,[center[0]-r+r*w,  center[1]],r*w,w)
        draw_circles2(ax,n-1,[center[0],  center[1]-r+r*w],r*w,w) 
        draw_circles2(ax,n-1,[center[0]+r-r*w,  center[1]],r*w,w)
        draw_circles2(ax,n-1,[center[0],  center[1]+r-r*w],r*w,w)

fig, ax = plt.subplots() 
draw_circles2( ax, 3, [0,0],  100, 1/3) 
ax.set_aspect(1.0)
ax.axis('on')
plt.show()

fig, ax = plt.subplots() 
draw_circles2( ax, 4, [0,0],  100, 1/3) 
ax.set_aspect(1.0)
ax.axis('on')
plt.show()

fig, ax = plt.subplots() 
draw_circles2( ax, 5, [0,0],  100, 1/3) 
ax.set_aspect(1.0)
ax.axis('on')
plt.show()

#---------------------------------------------------------------------------------
#PART 3: BINARY TREE REPRESENTATION  -  EXPERIMENTAL
#---------------------------------------------------------------------------------
def draw_bin_tree(ax,x,y,n,size): #n = height of the tree
    #base case
    if n>0:
        #draw the initial shape (2 lines)
        ax.plot([x,x-(2**n),x,x+(2**n)],[y,y-size,y,y-size], color='k')
        #draw the next 2 shapes, originating from either leaf of the initial shape
        draw_bin_tree(ax,x-(2**n),y-size,n-1,size)
        draw_bin_tree(ax,x+(2**n),y-size,n-1,size)

fig, ax = plt.subplots()    
draw_bin_tree(ax,0,0,4,100)
ax.set_aspect(.2)
ax.axis('on')
plt.show()

fig, ax = plt.subplots()    
draw_bin_tree(ax,0,0,8,100)
ax.set_aspect(.2)
ax.axis('on')
plt.show()

#fig, ax = plt.subplots()    
#draw_bin_tree(ax,0,0,16,100)
#ax.set_aspect(.2)
#ax.axis('on')
#plt.show()

#---------------------------------------------------------------------------------
#PART 4: SIX CIRCLES IN ONE  -  EXPERIMENTAL
#---------------------------------------------------------------------------------
def draw_circles(ax,n,center,r):
    if n>0: 
        x,y = circle(center,r)
        ax.plot(x,y,color='k')

        r = r/3                 
        x,y = circle(center,r)  
    
        draw_circles(ax,n-1,center,r)
        ax.plot(x, y, color='k')        
        
        draw_circles(ax,n-1,[center[0]+r*2,  center[1]],r) 
        ax.plot(x, y+r*2, color='k')  
   
        draw_circles(ax,n-1,[center[0],      center[1]+r*2],r)
        ax.plot(x+r*2, y, color='k')
        
        draw_circles(ax,n-1,[center[0]-r*2,  center[1]],r)
        ax.plot(x, y-r*2, color='k')
     
        draw_circles(ax,n-1,[center[0],      center[1]-r*2],r) 
        ax.plot(x-r*2, y, color='k')
        
fig, ax = plt.subplots() 
draw_circles( ax, 4, [0,0],  100)   #keep raising 'n' to find the program's limit
ax.set_aspect(1.0)
ax.axis('off')

def draw_circles2(ax,n,center,r):
    if n>0: 
        r = r/4 #+1          
        x,y = circle(center,r)  

        draw_circles2(ax,n-1,[center[0],  center[1]-r*3],r)
        #                                             +1
        ax.plot(x-r*3, y, color='k') 
        #          +1
        
fig, ax = plt.subplots() 
draw_circles2( ax, 5, [0,0],  100)   
ax.set_aspect(1)
ax.axis('off')
