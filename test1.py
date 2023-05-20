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