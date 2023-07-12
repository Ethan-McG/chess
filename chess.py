# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 10:15:56 2023

@author: ethan
"""

from defs import *


def init_board():
    board = [["□" for _ in range(board_dim)] for _ in range(board_dim)]
    #white pieces:
    board[7][0] = White_Rook  
    board[7][1] = White_Horse
    board[7][2] = White_Bishop
    board[7][3] = White_Queen
    board[7][4] = White_King
    board[7][5] = White_Bishop
    board[7][6] = White_Horse
    board[7][7] = White_Rook 
    
    for i in range(8):
        board[6][i] = White_Pawn
           
        
    #Black pieces
    board[0][0] = Black_Rook  
    board[0][1] = Black_Horse
    board[0][2] = Black_Bishop
    board[0][3] = Black_Queen
    board[0][4] = Black_King
    board[0][5] = Black_Bishop
    board[0][6] = Black_Horse
    board[0][7] = Black_Rook 
    
    for i in range(8):
        board[1][i] = Black_Pawn
        
    
    
    board[7][1] = White_King
    return board



#label the edges of the board
def print_board(board):
    print("  ", end= "")
    for i in range(len(board)):
        print(chr(ord("a")+i), end = " ")
    print()
    for i in range(len(board)):
        print(8-i, end = " ")
        for j in range(len(board[i])):
            print(board[i][j], end = " ")
        print()
        
        
board = init_board() 
print_board(board)
#players_turn = "White's"
players_turn = "Black's"

def main():
    print("Welcome to Chess!\n")
    players_turn = "White's"
    board = init_board()

#checks for blank squares
def Blank_is_valid(i_square,players_turn):
    if board[8-int(i_square[1])][int(to_number(i_square[0]))] == "□": 
        return True  
    
# Checks the inputs are different squares    
def not_same_square(i_square, m_square,players_turn):
    if board[8-int(m_square[1])][int(to_number(m_square[0]))] == board[8-int(i_square[1])][int(to_number(i_square[0]))] :
        return True
    
#checks that the piece matches the player
def piece_matches_colour(i_square,players_turn):
    return (( players_turn == "White's" and board[8-int(i_square[1])][int(to_number(i_square[0]))].isupper())
    or (players_turn == "Black's" and board[8-int(i_square[1])][int(to_number(i_square[0]))].islower()) )


#pawn movement is valid only if; 
# in the same column, onyl moves forward 1 square, or 2 if beginning from row 2.
#

def white_pawn_is_valid(i_square,m_square,players_turn):
    if board[8-int(i_square[1])][int(to_number(i_square[0]))] == White_Pawn :
        if i_square[0] == m_square[0]:
            if int(i_square[1]) == 2  and ((int(i_square[1])+1 == int(m_square[1])) or (int(i_square[1])+2 == int(m_square[1]))):
                return True
            elif int(i_square[1])+1 == int(m_square[1]) :
                return True

def black_pawn_is_valid(i_square,m_square,players_turn):
    if board[8-int(i_square[1])][int(to_number(i_square[0]))] == Black_Pawn :
        if i_square[0] == m_square[0]:
            if int(i_square[1]) == 7  and ((int(i_square[1])-1 == int(m_square[1])) or (int(i_square[1])-2 == int(m_square[1]))):
                return True
            elif int(i_square[1])-1 == int(m_square[1]) :
                return True
            
def rook_is_valid(i_square,m_square,players_turn):
    if board[8-int(i_square[1])][int(to_number(i_square[0]))] == White_rook or Black_Rook :
        if i_square[0] == m_square[0] :
            if int(i_square[1]) == 7  and ((int(i_square[1])-1 == int(m_square[1])) or (int(i_square[1])-2 == int(m_square[1]))):
                return True
            elif int(i_square[1])-1 == int(m_square[1]) :
                return True
    
        

 
def check_for_movement(): 
    while True:
        print(f"{players_turn} turn")
        print("Enter the current square of piece: ", end = '')
        i_square = input()
        print("What is the target square: ", end ='')
        m_square = input()
        if Blank_is_valid(i_square, players_turn):
           print("Blank square, pick again ")
           print()
           continue
        elif  not_same_square(i_square, m_square,players_turn): 
            print("Same square for both values, try again ")
            print()
        elif not piece_matches_colour(i_square,players_turn):
            print("Not your piece, try again ")
            print()
            continue
        elif not white_pawn_is_valid(i_square,m_square,players_turn) and players_turn == "White's" :
            print("Invalid Pawn move, try again ")
            print()
            continue
        elif not black_pawn_is_valid(i_square,m_square,players_turn) and players_turn == "Black's" :
            print("Invalid Pawn move, try again ")
            print()
            continue
        
        print(movement_of_piece(i_square, m_square,players_turn))
        break
        

           
          
    
    
    
    
    #moves the chess piece to the choosen squares.  
def movement_of_piece(i_square, m_square,players_turn):   
    board[8-int(m_square[1])][int(to_number(m_square[0]))] = board[8-int(i_square[1])][int(to_number(i_square[0]))] 
    board[8-int(i_square[1])][int(to_number(i_square[0]))] = "□"
    print_board(board)  
    if players_turn == "White's":
        players_turn = "Black's"
    else:
        players_turn = "White's"
    print(check_for_movement())
        
   
print(check_for_movement())



        