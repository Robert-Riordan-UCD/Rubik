#! /usr/bin/env python3

"""
    Version:        1.0
    Date:           30.JUN.2019
    Author:         Robert Riordan
    Email:          robert.riordan@ucdconnect.ie
    
    Goal(s):        Output an unfolded ASCII template of Rubik's Cube with colour of each piece given scramble.
    
    Method:         1. Get an input scramble.
                    2. Set up position, orientation, and colour of corner, edge and center objects.
                    3. Deconstruct scramble into series of moves.
                    4. Perform the scramble on each piece.
                        4.1. Centers can be ignored.
                    5. Create array of colours based on the position and orientation of each piece.
                    6. Place each colour in the template.
    
    Dependncies:    sys
    
    Usage:          ./ascii_template.py "SCRAMBLE"
                    SCRAMBLE must be a single string of moves seperated by spaces.
"""

import sys

msg = "Only one scramble as a single string can be input"
assert(len(sys.argv) <= 2), msg

class Corner:
    p = 0
    o = 0
    c = 'wrg'
    def __init__(self, position, orientation, colour):
        self.p = position
        self.o = orientation
        self.c = colour
    
    def R(self):        
        if self.p == 1:
            self.p = 6
            self.o = (self.o + 2)%3
        elif self.p == 2:
            self.p = 1
            self.o = (self.o + 1)%3
        elif self.p == 5:
            self.p = 2
            self.o = (self.o + 2)%3
        elif self.p == 6:
            self.p = 5
            self.o = (self.o + 1)%3
    
    def R2(self):
        self.R()
        self.R()
    
    def Rp(self):
        self.R2()
        self.R()
    
    def L(self):
        if self.p == 0:
            self.p = 3
            self.o = (self.o + 1)%3
        elif self.p == 3:
            self.p = 4
            self.o = (self.o + 2)%3
        elif self.p == 4:
            self.p = 7
            self.o = (self.o + 1)%3
        elif self.p == 7:
            self.p = 0
            self.o = (self.o + 2)%3        
    
    def L2(self):
        self.L()
        self.L()
    
    def Lp(self):
        self.L2()
        self.L()
        
    def U(self):
        if self.p == 0:
            self.p = 1
        elif self.p == 1:
            self.p = 2
        elif self.p == 2:
            self.p = 3
        elif self.p == 3:
            self.p = 0
    
    def U2(self):
        self.U()
        self.U()
    
    def Up(self):
        self.U2()
        self.U()
    
    def D(self):
        if self.p == 4:
            self.p = 5
        elif self.p == 5:
            self.p = 6
        elif self.p == 6:
            self.p = 7
        elif self.p == 7:
            self.p = 4
    
    def D2(self):
        self.D()
        self.D()
    
    def Dp(self):
        self.D2()
        self.D()

    def F(self):
        if self.p == 2:
            self.p = 5
            self.o = (self.o + 2)%3
        elif self.p == 5:
            self.p = 4
            self.o = (self.o + 1)%3
        elif self.p == 4:
            self.p = 3
            self.o = (self.o + 2)%3
        elif self.p == 3:
            self.p = 2
            self.o = (self.o + 1)%3
    
    def F2(self):
        self.F()
        self.F()
    
    def Fp(self):
        self.F2()
        self.F()
    
    def B(self):
        if self.p == 0:
            self.p = 7
            self.o = (self.o + 2)%3
        elif self.p == 7:
            self.p = 6
            self.o = (self.o + 1)%3
        elif self.p == 6:
            self.p = 1
            self.o = (self.o + 2)%3
        elif self.p == 1:
            self.p = 0
            self.o = (self.o + 1)%3        
    
    def B2(self):
        self.B()
        self.B()
    
    def Bp(self):
        self.B2()
        self.B()

class Center:
    p = 0
    c = 'w'
    
    def __init__(self, position, colour):
        self.p = position
        self.c = colour

class Edge:
    p = 0
    o = 0
    c = 'wb'
    
    def __init__(self, position, orientation, colour):
        self.p = position
        self.o = orientation
        self.c = colour
        
    def R(self):
        if self.p == 1:
            self.p = 7
        elif self.p == 6:
            self.p = 1
        elif self.p == 9:
            self.p = 6
        elif self.p == 7:
            self.p = 9
    
    def R2(self):
        self.R()
        self.R()
        
    def Rp(self):
        self.R2()
        self.R()

    def L(self):
        if self.p == 3:
            self.p = 5
        elif self.p == 5:
            self.p = 11
        elif self.p == 11:
            self.p = 4
        elif self.p == 4:
            self.p = 3
    
    def L2(self):
        self.L()
        self.L()
        
    def Lp(self):
        self.L2()
        self.L()

    def U(self):
        if self.p == 0:
            self.p = 1
        elif self.p == 1:
            self.p = 2
        elif self.p == 2:
            self.p = 3
        elif self.p == 3:
            self.p = 0
    
    def U2(self):
        self.U()
        self.U()
        
    def Up(self):
        self.U2()
        self.U()

    def D(self):
        if self.p == 8:
            self.p = 9
        elif self.p == 9:
            self.p = 10
        elif self.p == 10:
            self.p = 11
        elif self.p == 11:
            self.p = 8
    
    def D2(self):
        self.D()
        self.D()
        
    def Dp(self):
        self.D2()
        self.D()
        
    def F(self):
        if self.p == 2:
            self.p = 6
            self.o = (self.o + 1)%2
        elif self.p == 6:
            self.p = 8
            self.o = (self.o + 1)%2
        elif self.p == 8:
            self.p = 5
            self.o = (self.o + 1)%2
        elif self.p == 5:
            self.p = 2
            self.o = (self.o + 1)%2
    
    def F2(self):
        self.F()
        self.F()
        
    def Fp(self):
        self.F2()
        self.F()

    def B(self):
        if self.p == 0:
            self.p = 4
            self.o = (self.o + 1)%2
        elif self.p == 4:
            self.p = 10
            self.o = (self.o + 1)%2
        elif self.p == 10:
            self.p = 7
            self.o = (self.o + 1)%2
        elif self.p == 7:
            self.p = 0
            self.o = (self.o + 1)%2
    
    def B2(self):
        self.B()
        self.B()
        
    def Bp(self):
        self.B2()
        self.B()

def scramble(scramble, Corners, Edges):
    scramble = scramble.split(' ')
    s = []
    for m in scramble:
        if not m == '':
            s.append(m)
    for corner in Corners:
        for move in s:
            if move.strip() == 'R':
                corner.R()
            elif move.strip() == 'R\'':
                corner.Rp()
            elif move.strip() == 'R2':
                corner.R2()
            elif move.strip() == 'L':
                corner.L()
            elif move.strip() == 'L\'':
                corner.Lp()
            elif move.strip() == 'L2':
                corner.L2()
            elif move.strip() == 'U':
                corner.U()
            elif move.strip() == 'U\'':
                corner.Up()
            elif move.strip() == 'U2':
                corner.U2()
            elif move.strip() == 'D':
                corner.D()
            elif move.strip() == 'D\'':
                corner.Dp()
            elif move.strip() == 'D2':
                corner.D2()
            elif move.strip() == 'F':
                corner.F()
            elif move.strip() == 'F\'':
                corner.Fp()
            elif move.strip() == 'F2':
                corner.F2()
            elif move.strip() == 'B':
                corner.B()
            elif move.strip() == 'B\'':
                corner.Bp()
            elif move.strip() == 'B2':
                corner.B2()
        
    for edge in Edges:
        for move in s:
            if move.strip() == 'R':
                edge.R()
            elif move.strip() == 'R\'':
                edge.Rp()
            elif move.strip() == 'R2':
                edge.R2()
            elif move.strip() == 'L':
                edge.L()
            elif move.strip() == 'L\'':
                edge.Lp()
            elif move.strip() == 'L2':
                edge.L2()
            elif move.strip() == 'U':
                edge.U()
            elif move.strip() == 'U\'':
                edge.Up()
            elif move.strip() == 'U2':
                edge.U2()
            elif move.strip() == 'D':
                edge.D()
            elif move.strip() == 'D\'':
                edge.Dp()
            elif move.strip() == 'D2':
                edge.D2()
            elif move.strip() == 'F':
                edge.F()
            elif move.strip() == 'F\'':
                edge.Fp()
            elif move.strip() == 'F2':
                edge.F2()
            elif move.strip() == 'B':
                edge.B()
            elif move.strip() == 'B\'':
                edge.Bp()
            elif move.strip() == 'B2':
                edge.B2()

    return (Corners, Edges)

def print_cube(c):
    print('              ___ ___ ___')
    print('             |   |   |   |')
    print('             |', c[0][0], '|', c[0][1], '|', c[0][2], '|')
    print('             |___|___|___|')
    print('             |   |   |   |')
    print('             |', c[1][0], '|', c[1][1], '|', c[1][2], '|')
    print('             |___|___|___|')
    print('             |   |   |   |')
    print('             |', c[2][0], '|', c[2][1], '|', c[2][2], '|')
    print('             |___|___|___|')
    print(' ___ ___ ___  ___ ___ ___  ___ ___ ___  ___ ___ ___')
    print('|   |   |   ||   |   |   ||   |   |   ||   |   |   |')
    print('|', c[3][0], '|', c[3][1], '|', c[3][2], '||', c[3][3], '|', c[3][4], '|', c[3][5], '||', c[3][6], '|', c[3][7], '|', c[3][8], '||', c[3][9], '|', c[3][10], '|', c[3][11], '|')
    print('|___|___|___||___|___|___||___|___|___||___|___|___|')
    print('|   |   |   ||   |   |   ||   |   |   ||   |   |   |')
    print('|', c[4][0], '|', c[4][1], '|', c[4][2], '||', c[4][3], '|', c[4][4], '|', c[4][5], '||', c[4][6], '|', c[4][7], '|', c[4][8], '||', c[4][9], '|', c[4][10], '|', c[4][11], '|')
    print('|___|___|___||___|___|___||___|___|___||___|___|___|')
    print('|   |   |   ||   |   |   ||   |   |   ||   |   |   |')
    print('|', c[5][0], '|', c[5][1], '|', c[5][2], '||', c[5][3], '|', c[5][4], '|', c[5][5], '||', c[5][6], '|', c[5][7], '|', c[5][8], '||', c[5][9], '|', c[5][10], '|', c[5][11], '|')
    print('|___|___|___||___|___|___||___|___|___||___|___|___|')
    print('              ___ ___ ___')
    print('             |   |   |   |')
    print('             |', c[6][0], '|', c[6][1], '|', c[6][2], '|')
    print('             |___|___|___|')
    print('             |   |   |   |')
    print('             |', c[7][0], '|', c[7][1], '|', c[7][2], '|')
    print('             |___|___|___|')
    print('             |   |   |   |')
    print('             |', c[8][0], '|', c[8][1], '|', c[8][2], '|')
    print('             |___|___|___|')


def make_layout(layout, Corners, Edges, Centers):
    c = [[],[],[],[],[],[],[],[]]
    e = [[],[],[],[],[],[],[],[],[],[],[],[]]
    for corner in Corners:
        if corner.o == 0:
            c[corner.p] = corner.c
        elif corner.o == 1:
            c[corner.p] = corner.c[1:] + corner.c[0]
        else:
            c[corner.p] = corner.c[2] + corner.c[:2]
    for edge in Edges:
        if edge.o == 0:
            e[edge.p] = edge.c
        else:
            e[edge.p] = edge.c[1] + edge.c[0]
    layout = [[c[7][2], e[10][1], c[6][1]], [e[4][0], Centers[4].c, e[7][0]], [c[0][1], e[0][1], c[1][2]], [c[7][1], e[4][1], c[0][2], c[0][0], e[0][0], c[1][0], c[1][1], e[7][1], c[6][2], c[6][0], e[10][0], c[7][0]], [e[11][1], Centers[1].c, e[3][1], e[3][0], Centers[0].c, e[1][0], e[1][1], Centers[3].c, e[9][1], e[9][0], Centers[5].c, e[11][0]], [c[4][2], e[5][1], c[3][1], c[3][0], e[2][0], c[2][0], c[2][2], e[6][1], c[5][1], c[5][0], e[8][0], c[4][0]], [c[3][2], e[2][1], c[2][1]], [e[5][0], Centers[2].c, e[6][0]], [c[4][1], e[8][1], c[5][2]]]
    
    
    return layout

corners = [Corner(0, 0, 'wbo'), Corner(1, 0, 'wrb'), Corner(2, 0, 'wgr'), Corner(3, 0, 'wog'), Corner(4, 0, 'ygo'), Corner(5, 0, 'yrg'), Corner(6, 0, 'ybr'), Corner(7, 0, 'yob')]
edges = [Edge(0, 0, 'wb'), Edge(1, 0, 'wr'), Edge(2, 0, 'wg'), Edge(3, 0, 'wo'), Edge(4, 0, 'bo'), Edge(5, 0, 'go'), Edge(6, 0, 'gr'), Edge(7, 0, 'br'), Edge(8, 0, 'yg'), Edge(9, 0, 'yr'), Edge(10, 0, 'yb'), Edge(11, 0, 'yo')]
centers = [Center(0, 'w'), Center(1, 'o'), Center(2, 'g'), Center(3, 'r'), Center(4, 'b'), Center(5, 'y')]

if len(sys.argv) == 1:
    layout = [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b'], ['o', 'o', 'o', 'w', 'w', 'w', 'r', 'r', 'r', 'y', 'y', 'y'], ['o', 'o', 'o', 'w', 'w', 'w', 'r', 'r', 'r', 'y', 'y', 'y'], ['o', 'o', 'o', 'w', 'w', 'w', 'r', 'r', 'r', 'y', 'y', 'y'], ['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']]
    print_cube(layout)
elif len(sys.argv) == 2:
    corners, edges = scramble(sys.argv[1], corners, edges)
    layout = [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b'], ['o', 'o', 'o', 'w', 'w', 'w', 'r', 'r', 'r', 'y', 'y', 'y'], ['o', 'o', 'o', 'w', 'w', 'w', 'r', 'r', 'r', 'y', 'y', 'y'], ['o', 'o', 'o', 'w', 'w', 'w', 'r', 'r', 'r', 'y', 'y', 'y'], ['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']]
    layout = make_layout(layout, corners, edges, centers)
    print_cube(layout)
        
    
