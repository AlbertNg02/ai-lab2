from utils.board import Board
from utils.table import TranspositionTable
from utils.minimax import MinimaxInfo
from utils import gamestate
from parts import partA, partB, partC
import math
import time


def main():
    print("Welcome to Connect 4!")

    part = input("What part do you want to run (A, B, C): ")
    if part == "C":
        depth = int(input("Number of moves to look ahead"))
        player = int(input("Who plays first? 1=human, 2=computer"))

    # rows = int(input("Enter rows: "))
    # columns = int(input("Enter columns: "))
    # win_length = int(input("Enter number in a row to win: "))
    rows = 4
    columns = 4
    win_length = 3
    # debug = bool(input("Debug: True or False: "))

    board = Board(rows, columns, win_length)
    table = TranspositionTable()

    if part == "A":
        st = time.time()
        partA.minimaxSearch(board, table)
        et = time.time()
        elapsed_time = et - st
        print('Search completed in:', elapsed_time, 'seconds')
        print("Transposition table has {} states".format(len(table.table.keys())))
    elif part == "B":
        st = time.time()
        partB.alphaBetaSearch(board, -math.inf, math.inf, table)
        et = time.time()
        elapsed_time = et - st
        print('Search completed in:', elapsed_time, 'seconds')
        print("Transposition table has {} states".format(len(table.table.keys())))
    elif part == "C":
        print("")
    else:
        print("Invalid Response")

    while board.get_game_state().value == gamestate.GameState.IN_PROGRESS.value:
        print(board.to_2d_string(), "\n")
        best_move = table.lookup(board).best_move
        board = board.make_move(best_move)

    # print(board.game_state)

    print("Game Over. State of the game:", board.get_game_state())


main()
