"""
Student ID: 0994

Automata 3350, MW 12-1:20 PM
Homework 15
Due: Oct. 16, 2019
"""

"""
    Given an arithmetic expression,
        - transform it into postfix form, then
        - compute its value
    using the stack-based algorithms went over in class.

    Assume that all numbers are one-digit.
    
    Submit a printout of the code, and a printout of an example 
    of what this program generates on each step
"""

# transform arithmetic expression 's' --> postfix expression (using stack-based algorithm)
#   and return the resulting postfix expression 'p'
def topostfix(s):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("TRANSFORMING ARITHMETIC EXPRESSION TO POSTFIX FORM")
    
    operator = ['+', '-', '*', '/']
    p = ""
    stack = []
    
    for i in range(len(s)):
        # if s[i] is a number, concatenate it to 'p'
        if s[i].isdigit():
            p += s[i]
            print("postfix --> ", p) # show the current expression being built
            # if +-*/ is on top of the stack
            if stack:
                if stack[-1] in operator: 
                    p += stack.pop() # concatenate the operator to 'p'
                    print("postfix --> ", p) # show the current expression being built
                
        elif s[i] == '(': # will later be popped from stack
            stack.append('(')
            
        elif s[i] == ')': # at this point, everything within the parentheses is done
            stack.append(')') # appended here only to show that it was pushed and popped from the stack 
            print("# stack --> ", stack) # show the contents of stack
            stack.pop() # pop the recent ')' (only for show))
            stack.pop() # this pop of '(' actually matters
            # after parentheses are removed, there should be an operand
            if stack:
                if stack[-1] in operator:
                    p += stack.pop()
                    print("postfix --> ", p) # show the current expression being built
        
        elif s[i] in operator:
            stack.append(s[i])
        
        print("# stack --> ", stack) # show the contents of stack
    
    return p


# compute a postfix expression 'p' (using stack-based algorithm) 
#   and return its result 'n' 
def computepostfix(p):
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("EVALUATING POSTFIX EXPRESSION")
    
    operator = ['+', '-', '*', '/']
    stack = []
    n = 0 # resulting value
    r = 0 # register, save a value for later
    
    for i in range(len(p)):
        # if character is a number
        if p[i].isdigit and p[i] not in operator:
            stack.append(p[i])
        
        # if character is an operator
        else: 
            print("operate --> ", p[i]) # show the operator about to be used to compute 'n'
            if p[i] == '+':
                n = int(stack.pop()) + int(stack.pop())
                
            elif p[i] == '-':
                r = int(stack.pop()) # pop top of stack to get to the item below it
                n = int(stack.pop()) - r
                
            elif p[i] == '*':
                n = int(stack.pop()) * int(stack.pop())
                    
            elif p[i] == '/':
                r = int(stack.pop()) # pop top of stack to get to the item below it
                n = int(stack.pop()) / r
            
            stack.append(n) # push the temporary result onto the stack
        print("# stack --> ", stack) # show the contents of stack
        
    return stack.pop() # should be the resulting value

def main():
    print("Input an arithmetic expression.\nUse only numbers 0-9 and choose from the following symbols: + - * / ( )")
    s = input("> ")
    
    p = topostfix(s) # transform arithmetic expression 's' to postfix form
    print("\nThe resulting postfix expression is... ", p)
    
    n = computepostfix(p) # compute postfix expression 'p' 
    print("\n===================================================")
    print("Th resulting equation is...")
    print(s, "=", n)
    
if __name__ == '__main__':
    main()
