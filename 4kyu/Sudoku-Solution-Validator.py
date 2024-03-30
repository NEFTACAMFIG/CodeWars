#DESCRIPTION:

#Sudoku Background

#Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9, so that each column, 
#each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9.
#(More info at: http://en.wikipedia.org/wiki/Sudoku)

#Sudoku Solution Validator
#Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, and returns true if 
#it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. 
#Boards containing one or more zeroes are considered to be invalid solutions.

#The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.

#Examples

#validSolution([
 # [5, 3, 4, 6, 7, 8, 9, 1, 2],
 # [6, 7, 2, 1, 9, 5, 3, 4, 8],
 # [1, 9, 8, 3, 4, 2, 5, 6, 7],
 # [8, 5, 9, 7, 6, 1, 4, 2, 3],
 # [4, 2, 6, 8, 5, 3, 7, 9, 1],
 # [7, 1, 3, 9, 2, 4, 8, 5, 6],
 # [9, 6, 1, 5, 3, 7, 2, 8, 4],
 # [2, 8, 7, 4, 1, 9, 6, 3, 5],
 # [3, 4, 5, 2, 8, 6, 1, 7, 9]
#]); // => true

#validSolution([
 # [5, 3, 4, 6, 7, 8, 9, 1, 2], 
 # [6, 7, 2, 1, 9, 0, 3, 4, 8],
 # [1, 0, 0, 3, 4, 2, 5, 6, 0],
 # [8, 5, 9, 7, 6, 1, 0, 2, 0],
 # [4, 2, 6, 8, 5, 3, 7, 9, 1],
 # [7, 1, 3, 9, 2, 4, 8, 5, 6],
 # [9, 0, 1, 5, 3, 7, 2, 1, 4],
 # [2, 8, 7, 4, 1, 9, 6, 3, 5],
 # [3, 0, 0, 4, 8, 1, 1, 7, 9]
#]); // => false


#MY SOLUTION

import numpy as np
def valid_solution(board):
    board2 = np.array(board)
    bT = board2.T
    bT = bT.tolist()

    for j in range(len(board)):
        dup = [x for i,x in enumerate(board[j]) if i != board[j].index(x)]
        if len(dup) > 0:
            y = True
            break
        else:
            y = False

    for k in range(len(bT)):
        dup = [t for l,t in enumerate(bT[k]) if l != bT[k].index(t)]
        if len(dup) > 0:
            a = True
            break
        else:
            a = False

    for i in range(9):
        square = [
            board[i][j:j + 3] + board[i + 1][j:j + 3] + board[i + 2][j:j + 3]
                for i in range(0, 9, 3)
                for j in range(0, 9, 3)]
        
        if list(set(square[i]))!=sorted(square[i]):
            b = True
            break
        else:
            b = False
    
    if y == False and a == False and b == False:
        return True
    else:
        return False
