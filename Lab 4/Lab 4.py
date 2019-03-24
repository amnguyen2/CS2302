"""
Author:             Nguyen, Abram
Assignment:         Lab 4
Course:             CS 2302 - Data Structures
Instructor:         Fuentes, Olac
T.A.:               Nath, Anindita 
Last modified:      March 24, 2019

Purpose of program: The purpose of this program is to demonstrate the attributes
                        and uses of B-Trees as a data structure. This program
                        handles B-Trees in different ways to showcase its use.
"""
import math

# Code to implement a B-tree 
# Programmed by Olac Fuentes
# Last modified February 28, 2019

class BTree(object):
    # Constructor
    def __init__(self,item=[],child=[],isLeaf=True,max_items=5):  
        self.item = item
        self.child = child 
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree    
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid]) 
        rightChild = BTree(T.item[mid+1:]) 
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf) 
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf) 
    return T.item[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.item.append(i)  
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
                  
def Print(T):
    # Prints items in tree in ascending order
    if T.isLeaf:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i],end=' ')
        Print(T.child[len(T.item)])    
 
def PrintD(T,space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')  
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')
        
"""
###############################################################################
# Programmed by Abram Nguyen ##################################################
# Last modified March 24, 2019 ################################################
###############################################################################        
"""     
# Compute the height of the tree ##############################################
def Height(T):
    if T.isLeaf:
        return 0
    return 1 + Height(T.child[-1]) #add 1 and iterate to next child

# Extract the items in the B-tree into a sorted list. #########################
def Extract(T, L):
    if T.isLeaf:
        for t in T.item:
            L += [t] #append items of leaf to list
    else:
        for i in range(len(T.item)):
            Extract(T.child[i], L) #traverse children recursively
            L += [T.item[i]] #append items to list
        Extract(T.child[len(T.item)], L) #last child

# Return the minimum element in the tree at a given depth d. ##################
def SmallestAtDepthD(T,d):
    if not T.item: #check if root is empty first
        return math.inf
    if d == 0: #reached depth 'd'
        return T.item[0]
    if T.isLeaf or d < 0: #if tree has no depth 'd'
        return math.inf
    return SmallestAtDepthD(T.child[0],d-1) #traverse to 'd', left most child

# Return the maximum element in the tree at a given depth d. ##################
def LargestAtDepthD(T,d):
    if not T.item: #check if root is empty first
        return -math.inf
    if d == 0: #reached depth 'd'
        return T.item[-1]
    if T.isLeaf or d < 0: #if tree has no depth 'd'
        return -math.inf
    return LargestAtDepthD(T.child[-1],d-1) #traverse to 'd', right most child

# Return the number of nodes in the tree at a given depth d. 
def NodesAtDepth(T, d):
    if not T.item: #check if root is empty first
        return 0
    if d == 0: #reached depth 'd'
        return 1
    if T.isLeaf or d < 0: #if tree has no depth 'd'
        return 0
    count = 0
    for i in range(len(T.child)): #for every child:
        count += NodesAtDepth(T.child[i],d-1) #count each child/node
    return count

# Print all the items in the tree at a given depth d. #########################
def PrintAtDepth(T,d):
    if d == 0: #reached depth 'd'
        for i in range(len(T.item)): #print every element of item
                print(T.item[i], end = " ")
    else:
        for j in range(len(T.child)): #traverse to every child
            PrintAtDepth(T.child[j],d-1)

# Return the number of nodes in the tree that are full.
def FullNodes(T):    
    if len(T.item) >= T.max_items: #if full node is found
        return 1
    if T.isLeaf: #full node not found here
        return 0
    count = 0
    for i in range(len(T.child)):
        count += FullNodes(T.child[i]) #traverse through every child, keep count
    return count 

# Return the number of leaves in the tree that are full.
def FullLeaves(T):
    if len(T.item) >= T.max_items: #if full node is found and...
        if T.isLeaf: #...full node is a leaf
            return 1
    count = 0
    for i in range(len(T.child)):
        count += FullLeaves(T.child[i]) #traverse through every child, keep count
    return count
    

# Given a key k, return the depth at which it is found in the tree, ###########
#   or -1 if k is not in the tree.        
def SearchDepth(T, k):
    i = 0
    #search a node for k w/ iterator, add 1 to i until/while...
    while i < len(T.item) and T.item[i] < k: 
        i += 1
        
    if len(T.item) == i or T.item[i] > k: #k not found in node and...
        if T.isLeaf: #...k not found in tree
            return -1
        else: #k not found in node but IS found in tree:
            depth = SearchDepth(T.child[i], k)          
            if depth >= 0: #if depth is valid (not negative)
                return depth+1 #i of element 1 is 0, so adjust depth by 1
            return -1
    return 0

"""
###############################################################################
################################ METHOD CALLS #################################
###############################################################################
"""
#L = []
#L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5, 105, 115, 200, 2, 45, 6]
L = [6, 3, 16, 11, 7, 17, 14, 8, 5, 19, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12, 21, 22, 0, -1, -2]
T = BTree()    
for i in L:
    print('Inserting',i)
    Insert(T,i)
    PrintD(T,'') 
    #Print(T)
    print('\n####################################')

# CALCULATE HEIGHT OF B-TREE --------------------------------------------------
print("Height of the B-Tree:", Height(T), "\n")

# EXTRACT INTO SORTED ARRAY ---------------------------------------------------
A = []
Extract(T, A)
print("Extracted array of numbers:", A, "\n")

# SMALLEST AT DEPTH -----------------------------------------------------------
for i in range(4):
    print("Smallest at depth", i, ":", SmallestAtDepthD(T,i))         
print()

# LARGEST AT DEPTH ------------------------------------------------------------
for i in range(4):
    print("Largest at depth", i, ":", LargestAtDepthD(T,i))         
print()

# COUNT NODES AT EVERY DEPTH --------------------------------------------------
for i in range(4):
    print("# of nodes at depth:", i, ":", NodesAtDepth(T, i))
print()

# PRINT ITEMS AT DEPTH --------------------------------------------------------
for i in range(4):
    print("Items at depth", i, ":", end=" ")
    PrintAtDepth(T,i)
    print()
print()

# COUNT FULL NODES ------------------------------------------------------------
print("# of full nodes:", FullNodes(T), "\n")     

# COUNT FULL LEAVES -----------------------------------------------------------
print("# of full leaves:", FullLeaves(T), "\n")

# DEPTHS OF VARIOUS VALUES ----------------------------------------------------
print("Depth of -999:", SearchDepth(T, -999))
print("Depth of 2:", SearchDepth(T, 2))
print("Depth of 3:", SearchDepth(T, 3))
print("Depth of 10:", SearchDepth(T, 10))
print("Depth of 14:", SearchDepth(T, 14))
print("Depth of 19:", SearchDepth(T, 19))
###############################################################################

#End of program