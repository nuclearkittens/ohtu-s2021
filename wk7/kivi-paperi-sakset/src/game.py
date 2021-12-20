from config import (
    ROCK, PAPER, SCISSORS, END_GAME,
    MOVE_P1, MOVE_P2_AI, MOVE_P2_HUMAN
)
from points import Points
from rps_ai import SimpleAI, SmarterAI

class RPSGame:
    def __init__(self, io, ai=None):
        self._ai = ai
        self._io = io
        self._pts = Points()

    def play(self):
        playing = True
        while playing:
            move_p1 = self._io.read(MOVE_P1)
            move_p2 = self._move_p2(move_p1)
            if self._is_valid(move_p1) and self._is_valid(move_p2):
                self._pts.log_points(move_p1, move_p2)
                self._io.write(self._pts)
            else:
                playing = False
        self._end_game()

    def _end_game(self):
        self._io.write(self._pts)
        self._io.write(END_GAME)
        self._reset()

    def _is_valid(self, move):
        return move in [ROCK, PAPER, SCISSORS]

    def _move_p2(self, move_p1):
        return ROCK

    def _reset(self):
        self._pts.reset()
        if self._ai:
            self._ai.reset()

class RPSPvP(RPSGame):
    def __init__(self, io):
        super().__init__(io)

    def _move_p2(self, move_p1):
        return self._io.read(MOVE_P2_HUMAN)

class RPSAI(RPSGame):
    def __init__(self, io, ai='simple'):
        super().__init__(io)
        self._ai = SimpleAI() if ai == 'simple' else SmarterAI(10)

    def _move_p2(self, move_p1):
        move = self._ai.get_move()
        self._io.write(MOVE_P2_AI + move)
        self._ai.set_move(move_p1)
        return move
