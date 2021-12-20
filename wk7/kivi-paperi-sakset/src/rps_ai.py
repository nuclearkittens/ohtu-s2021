from collections import deque
from config import ROCK, PAPER, SCISSORS

class SimpleAI:
    def __init__(self):
        self._move = 0
        self._moves = {0: ROCK, 1: PAPER, 2: SCISSORS}

    def get_move(self):
        self._move += 1
        self._move = self._move % 3
        return self._moves[self._move]

    def set_move(self, move):
        pass

    def reset(self):
        self._move = 0

class SmarterAI:
    def __init__(self, mem_size):
        self._mem = deque([])
        self._size = mem_size

    def get_move(self):
        if len(self._mem) >= 1 or len(self._mem) == 0:
            return ROCK

        last_move = self._mem[-1]
        r, p, s = 0, 0, 0

        for i in range(len(self._mem)-1):
            if last_move == self._mem[i]:
                nxt = self._mem[i+1]
                if nxt == ROCK:
                    r += 1
                elif nxt == PAPER:
                    p += 1
                else:
                    s += 1

        if r > p or r > s:
            return PAPER
        elif p > r or p > s:
            return SCISSORS
        else:
            return ROCK

    def set_move(self, move):
        if len(self._mem) == self._size:
            self._mem.popleft()
        self._mem.append(move)

    def reset(self):
        self._mem = deque([])
