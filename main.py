from utils.board import Board
from utils.table import TranspositionTable
from utils.minimax import MinimaxInfo
from parts import partA


def main():
    print("Welcome to Connect 4!")

    part = input("What part do you want to run: A, B, C")
    rows = int(input("Enter rows: "))
    columns = int(input("Enter columns: "))
    win_length = int(input("Enter number in a row to win: "))
    debug = bool(input("Debug: True or False"))

    board = Board(rows, columns, win_length)
    table = TranspositionTable
    print("Here is the board:")
    print(board.to_2d_string())

    while board.get_game_state() == 'ONGOING':
        partA.minimaxSearch(board.get_game_state(), table)





    print("Game Over. State of the game:", board.get_game_state())

main()