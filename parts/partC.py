from utils.gamestate import GameState
from utils.table import TranspositionTable
from utils.minimax import MinimaxInfo
from utils.board import Board
from utils.player import Player
from utils.stateUtils import is_terminal, utility_val, actions, result, is_cutoff, evalC
import math


def alphaBetaSearch(state: Board, alpha: int, beta: int, depth: int, table: TranspositionTable) -> MinimaxInfo:
    hashed_state = hash(state)
    if hashed_state in table.table.keys():
        # print(table.table.keys())
        return table.lookup(state)
    # TODO: Create is_cutoff function
    elif is_cutoff(state, depth):
        heuristic = utility_val(state)
        info = MinimaxInfo(heuristic, None)
        table.store(state, info)
        return info
    elif is_terminal(state):
        util = evalC(state)
        info = MinimaxInfo(util, None)
        table.store(state, info)
        return info
    elif state.player_to_move == Player.MAX:
        v = -math.inf
        best_move = None
        for action in actions(state):
            child_state = result(state, action)
            child_info = alphaBetaSearch(child_state, alpha, beta, depth + 1, table)
            v2 = child_info.value
            if v2 > v:
                v = v2
                best_move = action
                alpha = max(alpha, v)
            if v >= beta:
                return MinimaxInfo(v, best_move)
        info = MinimaxInfo(v, best_move)
        table.store(state, info)
        return info
    else:
        v = math.inf
        best_move = None
        for action in actions(state):
            child_state = result(state, action)
            child_info = alphaBetaSearch(child_state, alpha, beta, depth + 1, table)
            v2 = child_info.value
            if v2 < v:
                v = v2
                best_move = action
                beta = min(beta, v)
            if v <= alpha:
                return MinimaxInfo(v, best_move)

        info = MinimaxInfo(v, best_move)
        table.store(state, info)
        return info
