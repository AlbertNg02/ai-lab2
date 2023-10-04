from utils.gamestate import GameState
from utils.table import TranspositionTable
from utils.minimax import MinimaxInfo
from utils.board import Board
from utils.player import Player
from utils import gamestate
from utils.stateUtils import is_terminal, utility_val, actions, result, is_cutoff, evalC
import math


def alpha_beta_heuristic_search(state: Board, alpha: int, beta: int, depth: int,
                                table: TranspositionTable, max_depth: int) -> MinimaxInfo:
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
                return MinimaxInfo(v, best_move)

        info = MinimaxInfo(v, best_move)
        table.store(state, info)
        return info


def game(state: Board, alpha: int, beta: int, table: TranspositionTable) -> Board:
    max_depth = int(input("Number of moves to look ahead: "))
    player = int(input("Who plays first? 1=human, 2=computer: "))

    while state.get_game_state().value == gamestate.GameState.IN_PROGRESS.value:
        info = alpha_beta_heuristic_search(state, alpha, beta, depth=0, table=table, max_depth=max_depth)
        best_move = table.lookup(state).best_move
        print(state.to_2d_string())
        if player == 1:
            # Human turn
            print("It is human turn")
            print("The best move is: {}".format(best_move))
            player_move = int(int(input("Enter move: ")))
            state = state.make_move(player_move)
        else:
            # Computer turn
            print("It is computer turn")
            state = state.make_move(best_move)

        player = 3 - player
        table = TranspositionTable()
    return state
