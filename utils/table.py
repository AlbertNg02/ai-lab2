from utils.board import Board
from utils.minimax import MinimaxInfo
class TranspositionTable:
    def __init__(self):
        self.table = {}

    def store(self, key: Board, value: MinimaxInfo):
        self.table[key] = value

    def lookup(self, key):
        return self.table.get(key, None)