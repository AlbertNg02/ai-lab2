from utils.gamestate import GameState
from utils.table import TranspositionTable
from utils.minimax import MinimaxInfo
from utils.board import Board
from utils.player import Player
from utils import gamestate
from utils.stateUtils import is_terminal, utility_val, actions, result, is_cutoff, evalC, debug_log, winner_log
import math


pruning = 0
def alpha_beta_heuristic_search(state: Board, alpha: int, beta: int, depth: int,
                                table: TranspositionTable, max_depth: int) -> MinimaxInfo:
    global pruning
    hashed_state = hash(state)
    if hashed_state in table.table.keys():
        # print(table.table.keys())
        return table.lookup(state)
    elif is_cutoff(state, depth=depth, max_depth=max_depth):
        heuristic = evalC(state)
        info = MinimaxInfo(heuristic, None)
        table.store(state, info)
        return info
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
            child_info = alpha_beta_heuristic_search(child_state, alpha, beta, depth + 1, table, max_depth=max_depth)
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
            child_info = alpha_beta_heuristic_search(child_state, alpha, beta, depth + 1, table, max_depth=max_depth)
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
    max_depth = int(input("Number of moves to look ahead: "))
    player = int(input("Who plays first? 1=human, 2=computer: "))

    if debug:
        debug_log(table)

    while state.get_game_state().value == gamestate.GameState.IN_PROGRESS.value:
        info = alpha_beta_heuristic_search(state, alpha, beta, depth=0, table=table, max_depth=max_depth)

        best = table.lookup(state)
        best_move = best.best_move
        minimax_value = best.value

        print(state.to_2d_string())
        winner_log(info)
        print("The tree was pruned {} times".format(pruning))
        print("Transposition table has {} states".format(len(table.table.keys())))
        print("It is {}'s turn".format(state.player_to_move))
        print("Minimax value for this state: {} and The best move is: {}".format(minimax_value, best_move))
        if player == 1:
            player_move = int(input("Human Enter move: "))
            state = state.make_move(player_move)
        else:
            print("Computer choose move: {}".format(best_move))
            state = state.make_move(best_move)

        pruning = 0
        player = 3 - player
        table = TranspositionTable()
    return state
