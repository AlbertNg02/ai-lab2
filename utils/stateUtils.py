from utils.gamestate import GameState
from utils.board import Board

def is_terminal(state: Board):
    return state.get_game_state() in (GameState.MAX_WIN, GameState.MIN_WIN, GameState.TIE)

def utility_val(state: Board):
    score = state.get_game_state()
    return score