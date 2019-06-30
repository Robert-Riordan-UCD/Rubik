#! /usr/bin/env python3

"""
    Version:        1.0
    Date:           30.JUN.2019
    Author:         Robert Riordan
    Email:          robert.riordan@ucdconnect.ie
    
    Goal(s):        Output a valid Rubik's Cube scramble
                    Scramble will be random move, not random state
    
    Method:         1. Pick random move
                    2. Confirm move is not repeating
                        2.1. If repeating discard move, return to 1.
                    3. Add a random modifier
                    4. Output the scramble
    
    Dependncies:    random
"""

# Define constants
SCRAMBLE_LENGTH = 20

# Modules
import random as r

# Legal moves and extentions
moves = ['U', 'L', 'F', 'R', 'B', 'D']
modifier = [' ', '2', '\'']

# Initialise scramble array
scramble = []

# Generate scramble
move = SCRAMBLE_LENGTH
while move > 0:
    next_move = r.choice(moves)
    # Prevent pointless moves
    if len(scramble) == 1:
        if scramble[0][0] == next_move:
            continue
    elif len(scramble) == 2:
        if scramble[0][0] == next_move or scramble[1][0] == next_move:
            continue
    elif len(scramble) > 2:
        if scramble[-2][0] == next_move or scramble[-1][0] == next_move:
            continue
    
    scramble.append(next_move + r.choice(modifier))
    move -= 1
    
# Convert scramble to string
scram = ""
for n in range(len(scramble)):
    scram += scramble[n] + ' '

# Output
print(scram)
