#! /usr/bin/env bash
<<Comment
    Version:        1.0
    Date:           05.JUL.2019
    Author:         Robert Riordan
    Email:          robert.riordan@ucdconnect.ie
    
    Goal(s):        Interact with a 2D ASCII Rubik's Cube through the command line.
    
    Dependncies:    ../scramble_generation/random_move.py
                    ../visualisation/ascii_template.py
    
    To Do:          Check if cube is solved and exit
Comment


# Generate scramble
../scramble_generation/random_move.py > scramble.txt

# Generate and display template
../visualisation/ascii_template.py

# Get move from the user
# Concatinate with scramble
# Create new template with new scramble and display
while :
do
    read -p 'Move(s): ' Move
    scramble=$(<scramble.txt)
    new_scramble="$scramble $Move"
    echo "$new_scramble" > scramble.txt
    ../visualisation/ascii_template.py
done
