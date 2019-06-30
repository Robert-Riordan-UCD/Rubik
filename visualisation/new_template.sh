#! /usr/bin/env bash
<<Comment
    Version:        1.0
    Date:           30.JUN.2019
    Author:         Robert Riordan
    Email:          robert.riordan@ucdconnect.ie
    
    Goal(s):        Generate a new scramble for Rubik's Cube and display an unfolded ascii template.
    
    Dependncies:    ../scramble_generation/random_move.py
                    ./ascii_template.py
Comment


# Generate scramble
../scramble_generation/random_move.py > scramble.txt

# Display scramble
cat scramble.txt

# Generate and display template
./ascii_template.py