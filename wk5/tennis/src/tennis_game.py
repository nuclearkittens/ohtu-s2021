class TennisGame:
    def __init__(self, player1, player2):
        self._p1 = player1
        self._p2 = player2
        self._players = {player1: 0, player2: 0}
        self._scores = {0: 'Love', 1: 'Fifteen', 2: 'Thirty', 3: 'Forty'}

    def won_point(self, player):
        self._players[player] += 1

    def _equal_points(self):
        return True if self._players[self._p1] == self._players[self._p2] else False

    def _get_score(self, score):
        if score not in self._scores:
            return None
        return self._scores[score]

    def _get_diff(self):
        return self._players[self._p1] - self._players[self._p2]

    def _points_within_limits(self):
        for score in self._players.values():
            if score not in self._scores:
                return False
        return True

    def _get_winning_player(self):
        return max(self._players, key=self._players.get)

    def print_score(self):
        if self._equal_points():
            score = self._get_score(self._players[self._p1])
            if score:
                return score + '-All'
            return 'Deuce'
        elif self._points_within_limits():
            return self._get_score(self._players[self._p1]) + '-' + self._get_score(self._players[self._p2])
        else:
            diff = self._get_diff()
            player = self._get_winning_player()
            if abs(diff) == 1:
                return f'Advantage {player}'
            return f'Win for {player}'
