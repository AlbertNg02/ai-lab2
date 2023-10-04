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

    rows = int(input("Enter rows: "))
    columns = int(input("Enter columns: "))
    win_length = int(input("Enter number in a row to win: "))
    # debug = bool(input("Debug: True or False: "))

    board = Board(rows, columns, win_length)
    table = TranspositionTable()

    if part == "A":
        st = time.time()
        partA.minimax_search(board, table)
        et = time.time()
        elapsed_time = et - st
        print('Search completed in:', elapsed_time, 'seconds')
        print("Transposition table has {} states".format(len(table.table.keys())))
        table.unhashedtable = sorted(table.unhashedtable, key=lambda x: [state.moves_made_so_far for state in table.unhashedtable.keys()])
        for t in reversed(table.unhashedtable):
            print(t)
    elif part == "B":
        st = time.time()
        info = partB.alpha_beta_search(board, -math.inf, math.inf, table)
        print("PRUNING VALIABLE IS PRUNING:", partB.pruning)
        et = time.time()
        elapsed_time = et - st
        print('Search completed in:', elapsed_time, 'seconds')
        print("Transposition table has {} states".format(len(table.table.keys())))
        # table.unhashedtable = sorted(table.unhashedtable, key=lambda x: [state.moves_made_so_far for state in table.unhashedtable.keys()])
        # for t in reversed(table.unhashedtable):
        #     print(t)
    elif part == "C":
        board = partC.game(board, -math.inf, math.inf, table)
    else:
        print("Invalid Response")

    while (part != "C") and (board.get_game_state().value == gamestate.GameState.IN_PROGRESS.value):
        print(board.to_2d_string(), "\n")
        best_move = table.lookup(board).best_move
        board = board.make_move(best_move)


    print("Final State: \n", board.to_2d_string())
    print("Game Over. State of the game:", board.get_game_state())



main()
