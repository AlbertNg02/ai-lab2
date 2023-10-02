from utils.board import Board
from utils.table import TranspositionTable
from utils.minimax import MinimaxInfo
from utils import gamestate
from parts import partA
import time


def main():
    print("Welcome to Connect 4!")

    # part = input("What part do you want to run (A, B, C): ")
    # rows = int(input("Enter rows: "))
    rows = 3
    # columns = int(input("Enter columns: "))
    columns = 4
    # win_length = int(input("Enter number in a row to win: "))
    win_length = 3
    # debug = bool(input("Debug: True or False: "))

    # print("Here is the board:")
    # print(board.to_2d_string())
    # print(str(info))
    board = Board(rows, columns, win_length)
    table = TranspositionTable()
    st = time.time()
    partA.minimaxSearch(board, table)
    et = time.time()
    print(len(table.table.keys()))
    # get the execution time
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')

    while board.get_game_state().value == gamestate.GameState.IN_PROGRESS.value:
        print(board.to_2d_string(), "\n")
        best_move = table.lookup(board).best_move
        board = board.make_move(best_move)


    # print(board.game_state)

    print("Game Over. State of the game:", board.get_game_state())

main()