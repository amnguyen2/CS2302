"""
Student ID: 0994

Automata 3350, MW 12-1:20 PM
Homework 21
Due: Nov. 6, 2019
"""

"""
    Write a method that emulates a general Turing machine. The input to this method should include:
        - The number N of states q0,...,qN-1; 
            q0 is the start state, qN-2 is the accept state, qN-1 is the reject state
        - The number M of symbols s0,...,sM-1;
            s0 is the blank symbol '#'
            
        - int array state[n][m]
            state[n][m] = what state to go to when in the state q_n and you see the symbol s_m
        - int array symbol[n][m]
            symbol[n][m] = what symbol to write while in state q_n and you see the symbol s_m (may be the same as before)
        - char array lr[n][m]
            lr[n][m] = for each state q_n and each symbol s_m, go left (L), right (R), or stays in place ('')
        - int array tape[any significantly large size]
            tape[len] = contents of the original input tape
    The program must keep track of the current head's position on the tape, which is initially 0.
"""

# decide what state to go to when in the state q_n and you see the symbol s_m
def make_state(n, m):
    state = [[0 for x in range(m)] for y in range(n)]  # state[n][m]
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("You'll now construct the state machine used to simulate the Turing machine.")
    print("Remember that states = {0,...," + str(n-1) + "}")
    
    for i in range(n):
        print("\n> You're in state " + str(i) +" :")
        for j in range(m):
            state[i][j] = int(input("If you see symbol " + str(j) + ", what state do you move to?\n $ "))
    
    return state


# decide what symbol to write when in the state q_n and you see the symbol s_m
def make_symbol(n, m):
    symbol = [[0 for x in range(m)] for y in range(n)] # symbol[n][m]
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("You'll now decide when to write certain symbols on the tape of the Turing machine.")
    print("Remember that symbols = {'0',...,'" + str(m-1) + "', '#', ''}")
    
    for i in range(n):
        print("\n> You're in state " + str(i) +" :")
        for j in range(m):
            symbol[i][j] = str(input("If you see symbol " + str(j) + ", what symbol do you write?\n $ "))

    return symbol


def make_lr(n, m):
    lr = [[0 for x in range(m)] for y in range(n)] # lr[n][m]
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("You'll now decide when you should move in a certain direction or not at all.")
    print("Remember that directions = {'L', 'R', ''}")
    
    for i in range(n):
        print("\n> You're in state " + str(i) +" :")
        for j in range(m):
            lr[i][j] = str(input("If you see symbol " + str(j) + ", which direction do you move?\n $ "))

    return lr
    
# the user inputs the initial contents of the tape from left to right
def make_tape(m):
    tape = ['#'] 
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("You'll now fill the tape as it is initially.")
    print("Remember that symbols = {'0',...,'" + str(m-1) + "', '#'}")
    print("Input nothing (empty string) to finish writing.")
    
    i = 1
    write = str(input("What is written on the tape in position " + str(1) + "?\n $ "))
    while (write != ''):
        tape.append(write) # write = #, 0, 1, ...
        i += 1 # keep track of the last symbol in tape
        write = str(input("What is written on the tape in position " + str(i) + "?\n $ ")) # write what next?
    tape.append('#')
                
    print("The tape now reads:\n >> " + str(tape[0:i+1]))
    return tape


# simulate the turing machine
def turing_machine(n, m, state, symbol, lr, tape):
    h_pos = 0 # head's current position on the tape
    cur_state = 0
    
    while (cur_state < n-2):
        cur_sym     = tape[h_pos]
        new_sym     = symbol[cur_state][cur_sym]
        new_state   = state[cur_state][cur_sym]
        move        = lr[cur_state][cur_sym]
        
        cur_state = new_state
        tape[h_pos] = new_sym
        
        if (move == 'L'):
            h_pos -= 1
        elif (move == 'R'):
            h_pos += 1
    
    return n


def main():
    # construct turing machine
    n = int(input("How many states will the Turing machine have?\n $ "))
    m = int(input("How many symbols will the Turing machine have?\n $ "))
    
    state    = make_state(n, m)
    symbol  = make_symbol(n, m)
    lr      = make_lr(n, m)
    tape    = make_tape(m)
    
    # run turing machine
    turing_machine(n, m, state, symbol, lr, tape)
    
    
if __name__ == '__main__':
    main()
