from utils.board import Board
from utils.minimax import MinimaxInfo


class TranspositionTable:
    def __init__(self):
        self.table = {}

    def store(self, key: Board, value: MinimaxInfo):
        self.table[hash(key)] = value

    def lookup(self, key: Board):
        return self.table.get(hash(key))
