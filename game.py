import numpy as np
    # for gui
import pygame
    # for exiting the gui
import sys
    # for calulations, for exampel with infinity
import math
    # for delaying execution of certain events
from threading import Timer
    # for generating random values, for example for 1st turn
import random

def the_game():
    ROWS = 6
    COLS = 7

    # turns
    AI_TURN2 = 0
    AI_TURN = 1

    # pieces represented as numbers
    AI_PIECE2 = 1
    AI_PIECE = 2

    # colors for GUI
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)


    # various functions used by the game
    # -------------------------------

    # using numpy, create an empty matrix of 6 rows and 7 columns
    def create_board():
        board = np.zeros((ROWS, COLS))
        return board


    # add a piece to a given location, i.e., set a position in the matrix as 1 or 2
    def drop_piece(board, row, col, piece):
        board[row][col] = piece


    # checking that the top row of the selected column is still not filled
    # i.e., that there is still space in the current column
    # note that indexing starts at 0
    def is_valid_location(board, col):
        return board[0][col] == 0

    # get all columns where a piece can be
    def get_valid_locations(board):
        valid_locations = []
        
        for column in range(COLS):
            if is_valid_location(board, column):
                valid_locations.append(column)

        return valid_locations

    # checking if the given turn or in other words node in the minimax tree is terminal
    # a terminal node is player winning, AI winning or board being filled up
    def is_terminal_node(board):
        return winning_move(board, AI_PIECE2) or winning_move(board, AI_PIECE) or len(get_valid_locations(board)) == 0
    
    # checking where the piece will fall in the current column
    # i.e., finding the first zero row in the given column
    def get_next_open_row(board, col):
        for r in range(ROWS-1, -1, -1):
            if board[r][col] == 0:
                return r

    def print_board(board):
        print(np.flip(board, 1))
        
   import numpy as np
    # for gui
import pygame
    # for exiting the gui
import sys
    # for calulations, for exampel with infinity
import math
    # for delaying execution of certain events
from threading import Timer
    # for generating random values, for example for 1st turn
import random

def the_game():
    ROWS = 6
    COLS = 7

    # turns
    AI_TURN2 = 0
    AI_TURN = 1

    # pieces represented as numbers
    AI_PIECE2 = 1
    AI_PIECE = 2

    # colors for GUI
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)


    # various functions used by the game
    # -------------------------------

    # using numpy, create an empty matrix of 6 rows and 7 columns
    def create_board():
        board = np.zeros((ROWS, COLS))
        return board


    # add a piece to a given location, i.e., set a position in the matrix as 1 or 2
    def drop_piece(board, row, col, piece):
        board[row][col] = piece


    # checking that the top row of the selected column is still not filled
    # i.e., that there is still space in the current column
    # note that indexing starts at 0
    def is_valid_location(board, col):
        return board[0][col] == 0

    # get all columns where a piece can be
    def get_valid_locations(board):
        valid_locations = []
        
        for column in range(COLS):
            if is_valid_location(board, column):
                valid_locations.append(column)

        return valid_locations

    # checking if the given turn or in other words node in the minimax tree is terminal
    # a terminal node is player winning, AI winning or board being filled up
    def is_terminal_node(board):
        return winning_move(board, AI_PIECE2) or winning_move(board, AI_PIECE) or len(get_valid_locations(board)) == 0
    
    # checking where the piece will fall in the current column
    # i.e., finding the first zero row in the given column
    def get_next_open_row(board, col):
        for r in range(ROWS-1, -1, -1):
            if board[r][col] == 0:
                return r

    def print_board(board):
        print(np.flip(board, 1))
    
    # calculating if the current state of the board for player or AI is a win
    def winning_move(board, piece):
        # checking horizontal 'windows' of 4 for win
        for c in range(COLS-3):
            for r in range(ROWS):
                if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                    return True

        # checking vertical 'windows' of 4 for win
        for c in range(COLS):
            for r in range(ROWS-3):
                if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                    return True

        # checking positively sloped diagonals for win
        for c in range(COLS-3):
            for r in range(3, ROWS):
                if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                    return True

        # checking negatively sloped diagonals for win
        for c in range(3,COLS):
            for r in range(3, ROWS):
                if board[r][c] == piece and board[r-1][c-1] == piece and board[r-2][c-2] == piece and board[r-3][c-3] == piece:
                    return True


    # visually representing the board using pygame
    # for each position in the matrix the board is either filled with an empty black circle, or a palyer/AI red/yellow circle
    def draw_board(board):
        for c in range(COLS):
            for r in range(ROWS):
                pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE ))
                if board[r][c] == 0:
                    pygame.draw.circle(screen, BLACK, (int(c * SQUARESIZE + SQUARESIZE/2), int(r* SQUARESIZE + SQUARESIZE + SQUARESIZE/2)), circle_radius)
                elif board[r][c] == 1:
                    pygame.draw.circle(screen, RED, (int(c * SQUARESIZE + SQUARESIZE/2), int(r* SQUARESIZE + SQUARESIZE + SQUARESIZE/2)), circle_radius)
                else :
                    pygame.draw.circle(screen, YELLOW, (int(c * SQUARESIZE + SQUARESIZE/2), int(r* SQUARESIZE + SQUARESIZE + SQUARESIZE/2)), circle_radius)

        pygame.display.update()


    # evaluate a 'window' of 4 locations in a row based on what pieces it contains
    # the values used can be experimented with
    def evaluate_window(window, piece):
        # by default the oponent is the player
        opponent_piece = AI_PIECE2

        # if we are checking from the player's perspective, then the oponent is AI
        if piece == AI_PIECE2:
            opponent_piece = AI_PIECE

        # initial score of a window is 0
        score = 0

        # based on how many friendly pieces there are in the window, we increase the score
        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(0) == 1:
            score += 5
        elif window.count(piece) == 2 and window.count(0) == 2:
            score += 2

        # or decrese it if the oponent has 3 in a row
        if window.count(opponent_piece) == 3 and window.count(0) == 1:
            score -= 4 

        return score    


    # scoring the overall attractiveness of a board after a piece has been droppped
    def score_position(board, piece):

        score = 0

        # score center column --> we are prioritizing the central column because it provides more potential winning windows
        center_array = [int(i) for i in list(board[:,COLS//2])]
        center_count = center_array.count(piece)
        score += center_count * 6

        # below we go over every single window in different directions and adding up their values to the score
        # score horizontal
        for r in range(ROWS):
            row_array = [int(i) for i in list(board[r,:])]
            for c in range(COLS - 3):
                window = row_array[c:c + 4]
                score += evaluate_window(window, piece)

        # score vertical
        for c in range(COLS):
            col_array = [int(i) for i in list(board[:,c])]
            for r in range(ROWS-3):
                window = col_array[r:r+4]
                score += evaluate_window(window, piece)

        # score positively sloped diagonals
        for r in range(3,ROWS):
            for c in range(COLS - 3):
                window = [board[r-i][c+i] for i in range(4)]
                score += evaluate_window(window, piece)

        # score negatively sloped diagonals
        for r in range(3,ROWS):
            for c in range(3,COLS):
                window = [board[r-i][c-i] for i in range(4)]
                score += evaluate_window(window, piece)

        return score
