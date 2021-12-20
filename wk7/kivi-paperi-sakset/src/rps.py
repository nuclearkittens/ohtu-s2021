from console_io import CONSOLE_IO as default_io
from menu import Menu

class RPS:
    def __init__(self):
        self._io = default_io
        self._menu = Menu(self._io)
        self.running = True

    def run(self):
        while self.running:
            cmd = self._menu.get_command()
            if cmd:
                cmd.play()
            else:
                self.running = False
