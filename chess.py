# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 10:15:56 2023

@author: ethan
"""

from defs import *


# set up the chess board, and all the pieces

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
        
    

def main():
    print("Welcome to Chess!\n")
    players_turn = "White's"
    board = init_board()
    print_board(board)
    check_for_movement(players_turn,board)
    
    
    # checks is the inputted sqaure is within the chess board:
        
def inside_square(i_square,m_square,players_turn,board): 
    
    if (ord(i_square[0]) <= ord("h") and ord(i_square[0]) >= ord("a")) and ((int(i_square[1:]) <= 8) and (int(i_square[1:]) >= 1)) and (ord(m_square[0]) <= ord("h") and ord(m_square[0]) >= ord("a")) and (int(m_square[1:]) <= 8 and int(m_square[1:]) >= 1):
        return True
    else:
        return False
   
        

#checks for blank squares
def Blank_is_valid(i_square,players_turn,board):
    if board[8-int(i_square[1])][int(to_number(i_square[0]))] == "□": 
        return True  
    
# Checks the inputs are different squares    
def not_same_square(i_square, m_square,players_turn,board):
    if m_square == i_square :
        return True
    
#checks that the piece matches the player
def piece_matches_colour(i_square,players_turn,board):
    return (( players_turn == "White's" and board[8-int(i_square[1])][int(to_number(i_square[0]))].isupper())
    or (players_turn == "Black's" and board[8-int(i_square[1])][int(to_number(i_square[0]))].islower()) )


# pawn movement is valid only if; 
# in the same column, onyl moves forward 1 square, or 2 if beginning from row 2.

def white_pawn_is_valid(i_square,m_square,players_turn,board):
    if i_square[0] == m_square[0]:
        if int(i_square[1]) == 2  and ((int(i_square[1])+1 == int(m_square[1])) or (int(i_square[1])+2 == int(m_square[1]))):
            return True
        elif int(i_square[1])+1 == int(m_square[1]) :
            return True


#same code as above but for black's pawns 

def black_pawn_is_valid(i_square,m_square,players_turn,board):
    if board[8-int(i_square[1])][int(to_number(i_square[0]))] == Black_Pawn :
        if i_square[0] == m_square[0]:
            if int(i_square[1]) == 7  and ((int(i_square[1])-1 == int(m_square[1])) or (int(i_square[1])-2 == int(m_square[1]))):
                return True
            elif int(i_square[1])-1 == int(m_square[1]) :
                return True
            

# checks if the rook move is valid, so only in the same column or row as initial value           
def rook_is_valid(i_square,m_square,players_turn,board):
    if i_square[0] == m_square[0] :
        return True
    elif i_square[1] == m_square[1]  :
        return True
    

def horse_is_valid(i_square,m_square,players_turn,board):
    if ord(i_square[0]) + 1 == ord(m_square[0]) and ((int(i_square[1])-2 == int(m_square[1])) or (int(i_square[1])+2 == int(m_square[1]))) :
        return True
    elif ord(i_square[0]) - 1 == ord(m_square[0]) and ((int(i_square[1])-2 == int(m_square[1])) or (int(i_square[1])+2 == int(m_square[1]))) :
        return True
    elif int(i_square[1]) + 1 == int(m_square[1]) and ((ord(i_square[0]) - 2 == ord(i_square[0])) or (ord(i_square[0]) + 2 == ord(i_square[0]))) :
        return True
    elif int(i_square[1]) - 1 == int(m_square[1]) and ((ord(i_square[0]) - 2 == ord(i_square[0])) or (ord(i_square[0]) + 2 == ord(i_square[0]))) :
        return True
    
    
    
    
    pass
    
    
# checks if a Bishop Move is Valid 

def Bishop_is_valid(i_square,m_square,players_turn,board):
    for i in range(8) :
        if ord(i_square[0]) + i == ord(m_square[0]) and int(i_square[1]) + i == int(m_square[1] ):
            if ord(str(m_square[0])) <=  ord("h") and   int(m_square[1]) <= 8:
                return True
        elif ord(i_square[0]) - i == ord(m_square[0]) and int(i_square[1]) - i == int(m_square[1] ):
            if ord(str(m_square[0])) >=  ord("a") and   int(m_square[1]) >= 1:
                return True
        elif ord(i_square[0]) + i == ord(m_square[0]) and int(i_square[1]) - i == int(m_square[1] ):
            if ord(str(m_square[0])) <=  ord("h") and   int(m_square[1]) >= 1:
                return True
        elif ord(i_square[0]) - i == ord(m_square[0]) and int(i_square[1]) + i == int(m_square[1] ):
            if ord(str(m_square[0])) >=  ord("a") and   int(m_square[1]) <= 8:
                return True
                
        # check if a vald king move, can only be 1 move in any direction 
def King_is_valid(i_square,m_square,players_turn,board):
        if ord(i_square[0]) + 1 == ord(m_square[0]) and int(i_square[1]) + 1 == int(m_square[1] ):
            if ord(str(m_square[0])) <=  ord("h") and   int(m_square[1]) <= 8:
                return True
        elif ord(i_square[0]) - 1 == ord(m_square[0]) and int(i_square[1]) - 1 == int(m_square[1] ):
            if ord(str(m_square[0])) >=  ord("a") and   int(m_square[1]) >= 1:
                return True
        elif ord(i_square[0]) + 1 == ord(m_square[0]) and int(i_square[1]) - 1 == int(m_square[1] ):
            if ord(str(m_square[0])) <=  ord("h") and   int(m_square[1]) >= 1:
                return True
        elif ord(i_square[0]) - 1 == ord(m_square[0]) and int(i_square[1]) + 1 == int(m_square[1] ):
            if ord(str(m_square[0])) >=  ord("a") and   int(m_square[1]) <= 8:
                return True      
        
        
        
        
        
        
        
        
    
        
 
def check_for_movement(players_turn,board): 
    while True:
        print()
        print(f"{players_turn} turn")
        print("Enter the current square of piece: ", end = '')
        i_square = input()
        print("What is the target square: ", end ='')
        m_square = input()
        
        if not inside_square(i_square,m_square,players_turn,board):
            print("Not a valid Chess square, try again ")
            print()
            continue
        elif Blank_is_valid(i_square, players_turn, board):
           print("Blank square, pick again ")
           print()
           continue
        elif  not_same_square(i_square, m_square,players_turn, board): 
            print("Same square for both values, try again ")
            print()
            continue
        elif not piece_matches_colour(i_square,players_turn,board):
            print("Not your piece, try again ")
            print()
            continue
        
        # check for each piece
        
        if board[8-int(i_square[1])][int(to_number(i_square[0]))] == White_Pawn:
            
            # is the pawn move valid 
            
            if not white_pawn_is_valid(i_square,m_square,players_turn,board) and players_turn == "White's" :
                print("Invalid White Pawn move, try again ")
                print()
                continue
            elif not black_pawn_is_valid(i_square,m_square,players_turn,board) and players_turn == "Black's" :
                print("Invalid Pawn move, try again ")
                print()
                continue
        
        # is the piece a rook, and is the move valid 
        elif board[8-int(i_square[1])][int(to_number(i_square[0]))] == (White_Rook or Black_Rook) :
        
            if not rook_is_valid(i_square,m_square,players_turn,board):
                print("Invalid Rook move, try again ")
                print()
                continue
            
        # is the piece a horse, and is the move valid 
        elif board[8-int(i_square[1])][int(to_number(i_square[0]))] == (White_Horse or Black_Horse) :
        
            if not horse_is_valid(i_square,m_square,players_turn,board):
                print("Invalid horse move, try again ")
                print()
                continue
            
        
        # checks for a Bishop an then a valid move    
        elif board[8-int(i_square[1])][int(to_number(i_square[0]))] == (White_Bishop or Black_Bishop) :
         
             if not Bishop_is_valid(i_square,m_square,players_turn,board):
                 print("Invalid Bishop move, try again ")
                 print()
                 continue
             
        
        # checks for a Queen, and then if its a valid move
        elif board[8-int(i_square[1])][int(to_number(i_square[0]))] == (White_Queen or Black_Queen) :
 
            if not Bishop_is_valid(i_square,m_square,players_turn,board) and not rook_is_valid(i_square,m_square,players_turn,board):
                print("Invalid Queen move, try again ")
                print()
                continue      
     
        # checks for a Queen, and then if its a valid move
        elif board[8-int(i_square[1])][int(to_number(i_square[0]))] == (White_King or Black_King) :

            if not King_is_valid(i_square,m_square,players_turn,board):
                print("Invalid King move, try again ")
                print()
                continue         
     
        
     
        print(movement_of_piece(i_square, m_square,players_turn,board))
        break
        

           
          
    
    
    
    
    #moves the chess piece to the choosen squares.  
def movement_of_piece(i_square, m_square,players_turn,board):   
    board[8-int(m_square[1])][int(to_number(m_square[0]))] = board[8-int(i_square[1])][int(to_number(i_square[0]))] 
    board[8-int(i_square[1])][int(to_number(i_square[0]))] = "□"
    print_board(board)  
    
    if players_turn == "White's":
        players_turn = "Black's"
    else:
        players_turn = "White's"
   
    print(check_for_movement(players_turn,board))
        



main()



        