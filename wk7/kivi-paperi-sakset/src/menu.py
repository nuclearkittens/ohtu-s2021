from config import MENU, END
from game import RPSPvP, RPSAI

class Menu:
    def __init__(self, io):
        self._io = io
        self._cmds = {
            'a': RPSPvP(self._io),
            'b': RPSAI(self._io),
            'c': RPSAI(self._io, 'smarter')
        }

    def get_command(self):
        command = self._io.read(MENU)
        if command in self._cmds:
            self._io.write(END)
            return self._cmds[command]
        return None
