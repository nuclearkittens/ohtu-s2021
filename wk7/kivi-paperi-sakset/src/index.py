from console_io import CONSOLE_IO as default_io
from rps import RPS

def main():
    rps = RPS(default_io)
    rps.run()

if __name__ == "__main__":
    main()
