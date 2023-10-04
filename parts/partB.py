from utils.gamestate import GameState
from utils.table import TranspositionTable
from utils.minimax import MinimaxInfo
from utils.board import Board
from utils.player import Player
from utils.stateUtils import is_terminal, utility_val, actions, result
import math

pruning = 0

def alpha_beta_search(state: Board, alpha:int, beta:int, table: TranspositionTable) -> MinimaxInfo:
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
                beta = min(beta,v)
            if v <= alpha:
                pruning += 1
                return MinimaxInfo(v, best_move)

        info = MinimaxInfo(v, best_move)
        table.store(state, info)
        return info


