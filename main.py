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
    debug = bool(int(input("Debug: 0(False) or 1(True): ")))

    board = Board(rows, columns, win_length)
    table = TranspositionTable()

    if part == "A":
        board = partA.game(board, table, debug)
    elif part == "B":
        board = partB.game(board, -math.inf, math.inf, table, debug)
    elif part == "C":
        board = partC.game(board, -math.inf, math.inf, table, debug)
    else:
        print("Invalid Response")

    while (part != "C") and (board.get_game_state().value == gamestate.GameState.IN_PROGRESS.value):
        print(board.to_2d_string(), "\n")
        best_move = table.lookup(board).best_move
        board = board.make_move(best_move)


    print("Final State:")
    print(board.to_2d_string())
    print("Game Over. State of the game:", board.get_game_state())



main()
