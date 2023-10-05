from utils.gamestate import GameState
from utils.table import TranspositionTable
from utils.minimax import MinimaxInfo
from utils.board import Board
from utils.player import Player
from utils.stateUtils import is_terminal, utility_val, actions, result, debug_log, winner_log
import math


def minimax_search(state: Board, table: TranspositionTable) -> MinimaxInfo:
    hashed_state = hash(state)
    if hashed_state in table.table.keys():
        return table.lookup(state)
    elif is_terminal(state):
        util = utility_val(state)
        info = MinimaxInfo(util, None)
        table.store(state, info)
        return info
    elif state.player_to_move == Player.MAX:
        v = -math.inf
        best_move = None
        for action in actions(state):
            child_state = result(state, action)
            child_info = minimax_search(child_state, table)
            v2 = child_info.value
            if v2 > v:
                v = v2
                best_move = action
        info = MinimaxInfo(v, best_move)
        table.store(state, info)
        return info
    else:
        v = math.inf
        best_move = None
        for action in actions(state):
            child_state = result(state, action)
            child_info = minimax_search(child_state, table)
            v2 = child_info.value
            if v2 < v:
                v = v2
                best_move = action
        info = MinimaxInfo(v, best_move)
        table.store(state, info)
        return info


def game(state: Board, table: TranspositionTable, debug: bool) -> Board:
    info = minimax_search(state, table=table)
    winner_log(info)
    print("Transposition table has {} states".format(len(table.table.keys())))
    player = int(input("Who plays first? 1=human, 2=computer: "))

    if debug == True:
        debug_log(table)

    while state.get_game_state().value == GameState.IN_PROGRESS.value:
        best = table.lookup(state)
        best_move = best.best_move
        minimax_value = best.value

        print(state.to_2d_string())
        if player == 1:
            print("It is {}'s turn".format(state.player_to_move))
            print("Minimax value for this state: {} and The best move is: {}".format(minimax_value, best_move))
            player_move = int(input("Enter move: "))
            state = state.make_move(player_move)
        else:
            print("It is {}'s turn".format(state.player_to_move))
            print("Computer choose move: {}".format(best_move))
            state = state.make_move(best_move)

        player = 3 - player
    return state

