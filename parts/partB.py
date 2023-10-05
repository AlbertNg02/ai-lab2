from utils.gamestate import GameState
from utils.table import TranspositionTable
from utils.minimax import MinimaxInfo
from utils.board import Board
from utils.player import Player
from utils.stateUtils import is_terminal, utility_val, actions, result, debug_log, winner_log
import math
import time

pruning = 0


def alpha_beta_search(state: Board, alpha: int, beta: int, table: TranspositionTable) -> MinimaxInfo:
    global pruning

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
            child_info = alpha_beta_search(child_state, alpha, beta, table)
            v2 = child_info.value
            if v2 > v:
                v = v2
                best_move = action
                alpha = max(alpha, v)
            if v >= beta:
                pruning += 1
                return MinimaxInfo(v, best_move)
        info = MinimaxInfo(v, best_move)
        table.store(state, info)
        return info
    else:
        v = math.inf
        best_move = None
        for action in actions(state):
            child_state = result(state, action)
            child_info = alpha_beta_search(child_state, alpha, beta, table)
            v2 = child_info.value
            if v2 < v:
                v = v2
                best_move = action
                beta = min(beta, v)
            if v <= alpha:
                pruning += 1
                return MinimaxInfo(v, best_move)

        info = MinimaxInfo(v, best_move)
        table.store(state, info)
        return info


def game(state: Board, alpha: int, beta: int, table: TranspositionTable, debug: bool) -> Board:
    global pruning
    info = alpha_beta_search(state, alpha, beta, table=table)
    winner_log(info)
    print("The tree was pruned {} times".format(pruning))
    print("Transposition table has {} states".format(len(table.table.keys())))
    player = int(input("Who plays first? 1=human, 2=computer: "))

    if debug == True:
        debug_log(table)

    while state.get_game_state().value == GameState.IN_PROGRESS.value:
        if table.lookup(state) != None:
            best = table.lookup(state)
            best_move = best.best_move
            minimax_value = best.value
        else:
            pruning = 0
            table = TranspositionTable()
            alpha_beta_search(state, alpha, beta, table=table)
            best = table.lookup(state)
            best_move = best.best_move
            minimax_value = best.value

        print(state.to_2d_string())
        print("It is {}'s turn".format(state.player_to_move))
        print("Minimax value for this state: {} and The best move is: {}".format(minimax_value, best_move))
        if player == 1:
            player_move = int(input("Human Enter move: "))
            state = state.make_move(player_move)
        else:
            print("Computer choose move: {}".format(best_move))
            state = state.make_move(best_move)

        player = 3 - player
    return state
