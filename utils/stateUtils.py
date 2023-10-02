from utils.gamestate import GameState
from utils.board import Board

def is_terminal(state: Board):
    return state.get_game_state() in (GameState.MAX_WIN, GameState.MIN_WIN, GameState.TIE)

def utility_val(state: Board):
    util_score = int

    if state.get_game_state().value == GameState.MAX_WIN.value:
        util_score = int(10000 * state.get_rows() * state.get_cols() / state.moves_made_so_far)
    elif state.get_game_state().value == GameState.MIN_WIN.value:
        util_score = -int(10000 * state.get_rows() * state.get_cols() / state.moves_made_so_far)
    elif state.get_game_state().value == GameState.TIE.value:
        util_score = 0
    else:
        print("Error in utility_val")

    return util_score


def actions(state: Board):
    """
    :param state: Accepts a board state
    :return: return legal actions from that state
    """
    legal_actions =[]
    for col in range(state.get_cols()):
        # print(col)
        if not state.is_column_full(col):
            legal_actions.append(col)
    return legal_actions

def result(state: Board, action: int):
    """
    :param state:
    :param action:
    :return: a copy of the board modified after an action
    """
    return state.make_move(action)

def is_cutoff(state: Board, depth: int) -> bool:

    pass

def evalC(state: Board):
    pass

def getScore(state: Board):
    heuristic_consec = state.consec_to_win - 1
    heuristic_max = 0
    heuristic_min = 0
    for r in range(0, state.num_rows):
        for c in range(0, state.num_cols):
            if state.board[r][c] == 0:
                continue

            if ((c <= state.num_cols - heuristic_consec and state.all_match_in_a_row(r, c))
                    or (r <= state.num_rows - heuristic_consec and state.all_match_in_a_col(r, c))
                    or (
                            r <= state.num_rows - heuristic_consec and c <= state.num_cols - heuristic_consec and state.all_match_in_ne_diag(
                        r, c))
                    or (
                            r <= state.num_rows - heuristic_consec and c - heuristic_consec >= -1 and state.all_match_in_nw_diag(
                        r, c))):

                if state.board[r][c] == 1:
                    heuristic_max += 5
                elif state.board[r][c] == -1:
                    heuristic_min -= 5

    
    pass
