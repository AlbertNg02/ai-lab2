from utils.gamestate import GameState
from utils.board import Board

def is_terminal(state: Board):
    return state.get_game_state() in (GameState.MAX_WIN, GameState.MIN_WIN, GameState.TIE)

def utility_val(state: Board):
    score_string = state.get_game_state()

    if score_string == "MAX_WIN":
        score = GameState.MAX_WIN.value
    elif score_string == "MIN_WIN":
        score = GameState.MIN_WIN.value
    elif score_string == "IN_PROGRESS":
        score = GameState.IN_PROGRESS.value
    elif score_string == "TIE":
        score = GameState.TIE.value
    else:
        score = 0

    return score

def actions(state: Board):
    legal_actions =[]
    for col in range(state.get_cols()):
        # print(col)
        if state.is_column_full(col):
            legal_actions.append(col)
    return legal_actions

def result(state: Board, action: int):
    return state.make_move(action)