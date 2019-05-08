import math

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

###############################################################################
# Given an integer array with no duplicates. A maximum tree building on this array is defined as
# follow:
#  1. The root is the maximum number in the array.
#  2. The left subtree is the maximum tree constructed from left part subarray divided by the
#      maximum number.
#  3. The right subtree is the maximum tree constructed from right part subarray divided by the
#      maximum number.
def constructMaximumBinaryTree(nums): # leetcode solution
    if not nums: # simplest problem (base case)
        return None
    i = nums.index(max(nums)) # find the index of the max value in the list
    T = BST(nums[i]) # create a node containing the max value
    
    T.left = constructMaximumBinaryTree(nums[:i]) # list left of max = left subtree
    T.right = constructMaximumBinaryTree(nums[i + 1:]) # list right of max = right subtree
    
    return T

###############################################################################
# Print a binary tree in an m*n 2D string array following these rules:
#   1. The row number m should be equal to the height of the given binary tree.
#   2. The column number n should always be an odd number.
#   3. The root node's value (in string format) should be put in the exactly middle of the first
#       row it can be put. The column and the row where the root node belongs will separate the
#       rest space into two parts (left-bottom part and right-bottom part). You should print the
#       left subtree in the left-bottom part and print the right subtree in the right-bottom part. The
#       left-bottom part and the right-bottom part should have the same size. Even if one subtree
#       is none while the other is not, you don't need to print anything for the none subtree but
#       still need to leave the space as large as that for the other subtree. However, if two
#       subtrees are none, then you don't need to leave space for both of them.
#   4. Each unused space should contain an empty string "".
#   5. Print the subtrees following the same rules.

def printTree(root): #leetcode solution
    def get_height(node): # height function within printTree function
        return 0 if not node else 1 + max(get_height(node.left), get_height(node.right))
    
    def update_output(node, row, left, right): # update_output function within printTree function
        if not node:
            return
        mid = round((left + right) / 2) # calculate the middle of the current row
        output[row][mid] = str(node.item) # place root value into middle of row
        update_output(node.left, row + 1 , left, mid - 1) # next row, LEFT half
        update_output(node.right, row + 1 , mid + 1, right) # next row, RIGHT half
        
    height = get_height(root) # compute the height of the tree (m)
    width = 2 ** height - 1 # compute the width of the tree, based on height (n)
    output = [[''] * width for i in range(height)]
    update_output(node=root, row=0, left=0, right=width - 1)
    
    # print result line by line (level by level)
    for level in output:
        print(level)
    
"""
def printTree(T):
    m = height(T)
    n = (2**height(T))-1
    print("rows:", m)
    print("columns:", n)
    
    tree = [[""] * n for i in range(m)]
    for level in tree:
        print(level)
        
def height(T):
    if T == None:
        return 0

    Lh = height(T.left)
    Rh = height(T.right)
    
    if Lh < Rh:
        return Rh+1
    else:
        return Lh+1
"""  


###############################################################################
# Given a binary tree, return the inorder traversal of its nodes' values.
def inorder(T):
    if T is None:
        return []
    return inorder(T.left) + [T.item] + inorder(T.right)

###############################################################################
    



###############################################################################
    



"""
###############################################################################
###############################################################################
###############################################################################
""" 
# Problem 654. Maximum Binary Tree
nums = [3,2,1,6,0,5]
T = constructMaximumBinaryTree(nums)

# Problem: 655 Print Binary Tree
printTree(T)

# Problem 94. Binary Tree Inorder Traversal
#print("in-order traversal:", inorder(T))
print()    

# Problem 814. Binary Tree Pruning


# Problem 662. Maximum Width of Binary Tree
    









