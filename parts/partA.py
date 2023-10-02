from utils.gamestate import GameState
from utils.table import TranspositionTable
from utils.minimax import MinimaxInfo
from utils.board import Board
from utils.stateUtils import is_terminal

def minimaxSearch(state: Board, table:TranspositionTable ) -> MinimaxInfo:
    if state in table:
        return table[state]
    elif is_terminal(state):
        util =







    return None
