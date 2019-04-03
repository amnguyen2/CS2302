"""
Author:             Nguyen, Abram
Assignment:         Lab 5
Course:             CS 2302 - Data Structures
Instructor:         Fuentes, Olac
T.A.:               Nath, Anindita 
Last modified:      April 2, 2019

Purpose of program: The purpose of this program is to demonstrate the real life
                        applications of hash tables and compare the running times
                        of hash tables and binary search trees given the same
                        information. 
"""
import numpy as np
import math
import time
###############################################################################
# BST
class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.num_items = 0
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T == None:
        T = BST(newItem[0])
    elif T.item > newItem[0]:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    T.num_items += 1
    return T

def Delete(T,del_item):
    if T is not None:
        if del_item < T.item:
            T.left = Delete(T.left,del_item)
        elif del_item > T.item:
            T.right = Delete(T.right,del_item)
        else:  # del_item == T.item
            if T.left is None and T.right is None: # T is a leaf, just remove it
                T = None
            elif T.left is None: # T has one child, replace it by existing child
                T = T.right
            elif T.right is None:
                T = T.left    
            else: # T has two chldren. Replace T by its successor, delete successor
                m = Smallest(T.right)
                T.item = m.item
                T.right = Delete(T.right,m.item)
    T.num_items -= 1
    return T
         
def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item,end = ' ')
        InOrder(T.right)
  
def InOrderD(T,space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right,space+'   ')
        print(space,T.item)
        InOrderD(T.left,space+'   ')
  
def SmallestL(T):
    # Returns smallest item in BST. Returns None if T is None
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T   
 
def Smallest(T):
    # Returns smallest item in BST. Error if T is None
    if T.left is None:
        return T
    else:
        return Smallest(T.left)

def Largest(T):
    if T.right is None:
        return T
    else:
        return Largest(T.right)   

def Find(T,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item == k:
        return T
    if T.item<k:
        return Find(T.right,k)
    return Find(T.left,k)
    
def FindAndPrint(T,k):
    f = Find(T,k)
    if f is not None:
        print(f.item,'found')
    else:
        print(k,'not found')

###############################################################################   
# Implementation of hash tables with chaining using strings
        
class HashTableC(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size):  
        self.item = []
        self.num_items = 0
        for i in range(size):
            self.item.append([])
        
def InsertC(H,k,l):
    # Inserts k in appropriate bucket (list) 
    # Does nothing if k is already in the table
    b = h(k,len(H.item))
    H.num_items += 1
    H.item[b] == None
    H.item[b].append([k,l]) 
   
def FindC(H,k):
    # Returns bucket (b) and index (i) 
    # If k is not in table, i == -1
    b = h(k,len(H.item))
    for i in range(len(H.item[b])):
        if H.item[b][i][0] == k:
            return H.item[b][i][1]
    return None
 
#r = (r*k + ord(c))% n
def h(s,n):
    r = 0
    for c in s:
        #r = (r*k + ord(c))% n
        r = (r*4 + ord(c))% n
    return r  

"""
################################
################################
################################
"""
###############################################################################

def HashTableBST(T, filename): 
    f = open(filename, encoding="utf-8") 
    #for each line in the file:
    for line in f:
        str(line)
        #create array of items including 'words' and values
        temp = line.split(" ")
        #ignore all non 'words'
        if temp[0].isalpha():
            #create array of numbers from array of items
            nums = np.array([])
            nums = np.append(nums, temp[1:]).astype(float)
            #insert word and embedding into binary search tree
            Insert(T, [temp[0], nums])
    #InOrder(T)
    #InOrder(T, '')
    
# Find the similarity between two words, return running time in ms
def SimilaritiesBST(T):
    print("Reading word file to determine similarities...\n")
    file = open('pairs.txt')
    c = 0
    start = time.time()
    for line in file: #per line:
        temp = line.split()
        e0 = FindC(T,temp[0]) #embedding of first word
        e1 = FindC(H,temp[1]) #embedding of second word
        dot = np.sum(e0*e1,dtype=float) #compute dot product of e0 and e1
        mag = math.sqrt(np.sum(e0*e0,dtype=float))*math.sqrt(np.sum(e1*e1,dtype=float))
        print("Similarity",temp,"→",round(dot/mag, 5))
        c+=1
    end = time.time()
    print("\nTime to compare", c, "pair(s) of words →", round((end-start)*1000, 5), "ms")

# Return the number of nodes in tree 'T'
def Count(T):
    c = 1
    if T.left != None:
        c += Count(T.left)
    if T.right != None:
        c += Count(T.right)
    return c

# Return the height of tree 'T'
def Height(T):
    if T == None:
        return 0
    L = Height(T.left) #left height
    R = Height(T.right) #right height
    if L < R:
        return R+1
    else:
        return L+1
###############################################################################

def HashTableChaining(H, filename):
    #f = open('glove.6B.50d.txt', encoding="utf-8")
    f = open(filename, encoding="utf-8") 
    #for each line in the file:
    for line in f:
        str(line)
        #create array of items including 'words' and values
        temp = line.split(" ")
        #ignore all non 'words'
        if temp[0].isalpha():
            #create array of numbers from array of items
            nums = np.array([])
            nums = np.append(nums, temp[1:]).astype(float)
            #insert word and embedding into hash table
            InsertC(H, temp[0], nums)
            
# Compute the load factor of hash table 'H'
def LoadFactorChain(H):
    #number of items / length of table
    return float(H.num_items/len(H.item))

# Compute the percentage of empty lists in hash table 'H'
def EmptyPercent(H):
    c = 0
    for i in range(len(H.item)):
        #count number of empty lists
        if len(H.item[i]) == 0:
            c += 1
    #compute percentage of empty lists in hash table 'H'
    return c/len(H.item)*100 

# Compute the standard deviation of the lengths of the lists in hash table 'H'
def HashSD(H):
    lengths = []
    for i in range(len(H.item)):
        #record every list's length
        lengths.append(len(H.item[i]))
    #compute using numpy.std
    return np.std(lengths)

# Find the similarity between two words, return running time in ms     
def SimilaritiesHash(H):
    print("Reading word file to determine similarities...\n")
    print("\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ ")
    file = open('pairs.txt')
    c = 0
    start = time.time()
    for line in file: #per line:
        temp = line.split()
        e0 = FindC(H,temp[0]) #embedding of first word
        e1 = FindC(H,temp[1]) #embedding of second word
        dot = np.sum(e0*e1,dtype=float) #compute dot product of e0 and e1
        mag = math.sqrt(np.sum(e0*e0,dtype=float))*math.sqrt(np.sum(e1*e1,dtype=float))
        print("Similarity",temp,"→",round(dot/mag, 5))
        c+=1
    end = time.time()
    print("\nTime to compare", c, "pair(s) of words →", round((end-start)*1000, 5), "ms")


"""
################################
######### METHOD CALLS #########
################################
"""

p = input("Please choose preferred implementation (enter number):\n[1]  Binary search tree\n[2]  Hash table w/ chaining\nChoice: ")
print()
filename = 'glove.6B.50d.txt'

if p == '1': #store values into BST
    T = BST("")
    print("Building binary search tree...\n")
    start = time.time()
    HashTableBST(T, filename)
    end = time.time()
    print("    ~~~  Binary Search Tree Stats  ~~~ ")
    print("  Number of nodes →       ", Count(T))
    print("      Height →            ", Height(T))
    print("Running time for BST construction →", round(end-start, 2), "sec")
    #SimilaritiesBST(T) DOESN'T WORK CORRECTLY
    
if p == '2': #store values into hash table w/ chaining
    start = time.time()
    #initialize hash table
    H = HashTableC(49999)
    print("Building hash table with chaining...\n")
    print("    ~~~  Hash Table Stats  ~~~ ")
    print("Initial table size →       ", len(H.item))
    #fill hash table
    HashTableChaining(H, filename)
    while LoadFactorChain(H) >= 1:
        H = HashTableC(2*len(H.item) + 1)
        HashTableChaining(H, filename)
    end = time.time()    
    print(" Final table size →        ", len(H.item))
    print("   Load factor →           ", round(LoadFactorChain(H), 5))
    print(" % of empty lists →        ", round(EmptyPercent(H), 2), "%")
    print("Standard deviation of the length of the lists →", round(HashSD(H), 5))
    print("Running time for Hash Table construction →", round(end-start, 2), "sec\n")
    SimilaritiesHash(H)
###############################################################################
# End of program