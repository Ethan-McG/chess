#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 20:43:11 2023

@author: Ethan
"""

#defines the dimension of the board
board_dim = 8


#Chess Pieces
White_King = "K"
White_Queen = "Q"
White_Bishop = "B"
White_Horse = "H"
White_Rook = "R"
White_Pawn = "P"

Black_King = "k"
Black_Queen = "q"
Black_Bishop = "b"
Black_Horse = "h"
Black_Rook = "r"
Black_Pawn = "p"



def to_number(i): 
    return ord(i) - ord("a")
    