from config import ROCK, PAPER, SCISSORS

class Points:
    def __init__(self):
        self.p1_pts = 0
        self.p2_pts = 0
        self.draws = 0

    def log_points(self, move_p1, move_p2):
        if self._draw(move_p1, move_p2):
            self.draws += 1
        elif self._p1_wins(move_p1, move_p2):
            self.p1_pts += 1
        else:
            self.p2_pts += 1

    def reset(self):
        self.p1_pts = 0
        self.p2_pts = 0
        self.draws = 0

    def _draw(self, move_p1, move_p2):
        if move_p1 == move_p2:
            return True
        return False

    def _p1_wins(self, move_p1, move_p2):
        if (
            (move_p1 == ROCK and move_p2 == SCISSORS) or
            (move_p1 == SCISSORS and move_p2 == PAPER) or
            (move_p1 == PAPER and move_p2 == ROCK)
        ):
            return True
        return False

    def __str__(self):
        return f"Pelitilanne: {self.p1_pts} - {self.p2_pts}\nTasapelit: {self.draws}"
