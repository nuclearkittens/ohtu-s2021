class ConsoleIO:
    def write(self, prompt):
        print(prompt)

    def read(self, prompt):
        return input(prompt)

CONSOLE_IO = ConsoleIO()
