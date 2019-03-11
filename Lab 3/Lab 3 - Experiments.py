"""
Author:             Nguyen, Abram
Assignment:         Lab 3
Course:             CS 2302 - Data Structures
Instructor:         Fuentes, Olac
T.A.:               Nath, Anindita 
Last modified:      March 7, 2019
Purpose of program: The purpose of this program is to demonstrate the use and
                        versatility of binary search trees as well as this 
                        data structure's method of organization of information.
"""
import matplotlib.pyplot as plt
import numpy as np
import math 

# Code to implement a binary search tree 
# Programmed by Olac Fuentes
# Last modified February 27, 2019

class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

        
"""
###############################################################################
# Programmed by Abram Nguyen ##################################################
# Last modified March 7, 2019 #################################################
###############################################################################        
"""
     
###############################################################################    
# Display the binary tree as a figure #########################################
###############################################################################  
def drawTree(ax,x,y,n,size,T):
    if T != None:
        drawCircle(ax,[x,y],1.5)    #draw a circle
        ax.text(x-.5, y-.5, T.item, size=8, weight='bold') #include node's value
        #if T has a left child:
        if T.left != None:
            #plot the left branch and draw the rest of the tree
            ax.plot([x,x-(2**n)],[y-1.5,y-size], color='k')  
            drawTree(ax,x-(2**n),y-size-1.5,n-1,size,T.left)
        if T.right != None:
            #plot the right branch and draw the rest of the tree
            ax.plot([x,x+(2**n)],[y-1.5,y-size], color='k')
            drawTree(ax,x+(2**n),y-size-1.5,n-1,size,T.right)   
            
# Draws a circle of radius 'r' at center point [x,y]
def drawCircle(ax,center,r): 
    x,y = circle(center,r)  
    ax.plot(x,y,color='k')  
    
# Creates a circle given a center and radius
def circle(center,radius): 
    n = int(4*radius*math.pi)
    t = np.linspace(0,6.3,n)
    y = center[1]+radius*np.sin(t)
    x = center[0]+radius*np.cos(t)
    return x,y

###############################################################################      
# Iterative version of the search operation. ##################################
###############################################################################  
def search(T,k):
    while T != None:
        if k == T.item:
            return T
        #if k is still smaller, traverse left
        elif k < T.item:
            T = T.left
        #if k is still larger, traverse right
        elif k > T.item:
            T = T.right
    return T

###############################################################################            
# Building a balanced binary search tree given a sorted list as input. ########
### Note: this should not use the insert operation, ###########################
### the tree must be built directly from the list in O(n) time. ###############
###############################################################################  
def balance(L):      
    if L: 
        # median(middle) of list will be the top node to keep the tree balanced
        med = len(L) // 2
        T = BST(L[med])
        #insert right sub-tree
        T.right = balance(L[med+1:])
        #insert left sub-tree
        T.left = balance(L[:med])
        return T

###############################################################################  
# Extracting the elements in a binary search tree into a sorted list. #########
### As above, this should be done in O(n) time. ###############################
###############################################################################      
def extract(T, L):
    if T != None:
        #traverse through every node in the tree
        extract(T.left, L)
        L += [T.item] #append every item to L, a native python list
        extract(T.right, L)

###############################################################################  
# Printing the elements in a binary tree ordered by depth. ####################
### The root has depth 0, the root’s children have depth one, #################
### and so on. ################################################################
###############################################################################  
def depthPrint(T, k):
    if T != None:
        if k == 0:
            #print the current node(s) data
            print(T.item, end=" ")
        else:
            #traverse to every node at level k
            depthPrint(T.left, k-1)
            depthPrint(T.right, k-1)
 
"""
# Code to test the functions above ############################################
"""         
T = None
#A = [10, 9, 8, 7, 4, 5, 3, 1, 3.5, 4.5, 5.5, 2, 3.6, 4.75, 5.25, 5.75, 3.25, 4.25, 0]
A = [70, 50, 90, 130, 150, 40, 10, 30, 100, 60, 80, 45, 55, 75]
for a in A:
    T = Insert(T,a)

print("ANALYZING TREE 'T'...")
print("======================\n")

# 1) DRAW BINARY TREE
fig, ax = plt.subplots()    
drawTree(ax,0,0,4,10,T) 
#drawTree(ax,x,y,n,size) 
ax.set_aspect(1.0)
ax.axis('off')
plt.show()


# 2) ITERATIVE SEARCH
print("Searching for 70:", search(T,70).item)
print("Searching for 70, trying to print node:", search(T,70))
print("Searching for 10:", search(T,10).item)
print("Searching for 30:", search(T,30).item)
print("Searching for 150:", search(T,150).item)
print("Searching for -1:", search(T,-1))
print("Searching for 500:", search(T,500))
print()

# 3) BALANCE A TREE
B = [10, 20, 30, 35, 50, 75]
C = balance(B)
fig, ax = plt.subplots()    
drawTree(ax,0,0,4,10,C) 
ax.set_aspect(1.0)
ax.axis('off')
plt.show()

D = [0,0,0,0,0,0,0]
E = balance(D)
fig, ax = plt.subplots()    
drawTree(ax,0,0,4,10,E) 
ax.set_aspect(1.0)
ax.axis('off')
plt.show()


# 4) EXTRACT TREE INTO LIST
Z = None
test1 = []
extract(Z, test1)

fig, ax = plt.subplots()    
drawTree(ax,0,0,4,10,Z) 
#drawTree(ax,x,y,n,size) 
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
print("Sorted list of test1's elements:", test1)
print()


Y = None
y = [50, 40, 30, 20, 10]
for j in y:
    Y = Insert(Y,j)
test2 = []
extract(Y, test2)

fig, ax = plt.subplots()    
drawTree(ax,0,0,4,10,Y) 
#drawTree(ax,x,y,n,size) 
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
print("Sorted list of test2's elements:", test2)
print()


# 5) PRINT ELEMENTS AT GIVEN DEPTH
print("FIRST TREE DEPTHS:")
print("Keys at depth -1:", end=" ")
depthPrint(T,-1)
print()
print("Keys at depth 0:", end=" ")
depthPrint(T,0)
print()
print("Keys at depth 1:", end=" ")
depthPrint(T,1)
print()
print("Keys at depth 2:", end=" ")
depthPrint(T,2)
print()
print("Keys at depth 3:", end=" ")
depthPrint(T,3)
print()
print("Keys at depth 4:", end=" ")
depthPrint(T,4)
print()
print("Keys at depth 5:", end=" ")
depthPrint(T,5)
print("\n")

print("EMPTY TREE DEPTHS:")
Empty = None
print("Keys at depth -1:", end=" ")
depthPrint(Empty,-1)
print()
print("Keys at depth 0:", end=" ")
depthPrint(Empty,0)
print()
print("Keys at depth 1:", end=" ")
depthPrint(Empty,1)
print()



###############################################################################

#End of program