from . import core

if __name__ == "__main__":
    filename = input("File to run: ")
    with open(filename) as f:
        code = f.read()
        core.run(code)