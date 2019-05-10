"""
Author:             Nguyen, Abram
Assignment:         Lab 8
Course:             CS 2302 - Data Structures
Instructor:         Fuentes, Olac
T.A.:               Nath, Anindita 
Last modified:      

Purpose of program: The purpose of this program is to practice and demonstrate the
                        uses of randomized and backtracking algorithms, two of several
                        algorithm design techniques. I use randomization and
                        backtracking to come up with a solution to 2 given problems.
"""
import numpy as np
import random
import math
from mpmath import *
import time

# Write a program to ”discover” trigonometric identities. Your program should
# test all combinations of the trigonometric expressions shown below and use a 
# randomized algorithm to detect the equalities. For your equality testing, 
# generate random numbers in the −π to π range.
def equal(trig, tries=1000, tolerance=0.0000000000000001): # i've modified the method so that it's as accurate as possible
    identities = []
    for i in range(len(trig)): # compare each expression...
        t = random.uniform(-math.pi, math.pi) # test expression using a number between -pi and pi
        y1 = eval(trig[i])
        
        for j in range(i, len(trig), 1): # ...to every other expression in the list
            if i != j:
                y2 = eval(trig[j])
                
                for k in range(j, tries):
                    if np.abs(y1-y2)<=tolerance: # if two expressions are equal...
                        identities.append(f"{trig[i]} = {trig[j]}") # an identity has been found! record it
                        break
    return identities


# Split a list of values into 2 subsets such that the sum of the numbers in
# subset 1 is equal to the sum of the numbers in subset 2. S1 and S2 must contain
# different numbers, the original set must be divided.
# Ex: {2, 4, 5, 9, 12} can be partitioned into S1 = {2, 5, 9} and S2 = {4, 12}.
# Indicate whether or not a valid partition exists.
def partition(S, last, goal): 
    if goal == 0: # if we reached our goal exactly, partition has been found so
        return True, []
    if goal < 0 or last < 0: # if we've gone over our goal, no partition has been found so far
        return False, []
    result, subset1 = partition(S, last-1, goal-S[last]) # Take S[last]
    if result: # if we're still on track with our goal, add the last checked value to the current subset
        subset1.append(S[last])
        return True, subset1 # return True and the current subset we've made
    else:
        return partition(S, last-1, goal) # Don't take S[last]

# create a subset of values that are in 'S' but are not in 's1'
def set2(S, s1): 
    s2 = []
    for s in S:
        if s not in s1: 
            s2.append(s)
    return s2
    
    
"""
###############################################################################
###############################################################################
###############################################################################
"""
trig = ['sin(t)', 'cos(t)' , 'tan(t)', 'sec(t)', '-sin(t)', '-cos(t)', '-tan(t)', 
        'sin(-t)', 'cos(-t)', 'tan(-t)', 'sin(t)/cos(t)', '2*sin(t/2)*cos(t/2)',
        'sin(t)**2', '1-cos(t)**2', '(1-cos(2*t))/2', '1/cos(t)']

start = time.time()
identities = equal(trig)
end = time.time()

print(f"List of trigonometric identities among given expressions:\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for i in identities:
    print(i)
print()
print(f"Time spent finding trigonometric identities: {round((end-start)*1000, 8)} ms")
###############################################################################

S = [2, 4, 5, 9, 12, 8, 16, 30, 32, 50, 18, 60, 80, 20]
#S = [2, 4, 5, 9, 13]
#S = []
#S = [3, 5]
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print(f"Searching for an equal partition of S = {S}")

contains, s1 = partition(S, len(S)-1, goal=sum(S)/2)
print(contains)
if contains:
    s2 = set2(S, s1)
    print(f"S1 = {s1}\nS2 = {s2}")
else:
    print("No partition could be found!")