class MinimaxInfo:



    def __init__(self, value: int, best_move: int):
        """
        :param value: the minimax value for that game state
        :param best_move: best move (column in which to drop the token) from that game state
        """
        self.value = value
        self.best_move = best_move

    def __str__(self):
        print("Info: value = {}; best_moves = {}".format(self.value, self.best_move))
