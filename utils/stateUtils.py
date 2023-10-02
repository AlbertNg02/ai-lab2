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