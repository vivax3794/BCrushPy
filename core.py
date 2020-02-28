"""
The core interpreter
"""
from typing import Dict


class InfiniteArray:
    """
    If an to big index is given, extend the array
    """

    def __init__(self, padding_value: any):
        self.values = []
        self.padding_value = padding_value

    def extend(self, index: int):
        needed = index - len(self.values) + 1
        self.values.extend([self.padding_value] * needed)

    def __getitem__(self, index: int) -> any:
        if index >= len(self.values):
            self.extend(index)
            return self.values[index]
        else:
            return self.values[index]

    def __setitem__(self, index, value):
        if index >= len(self.values):
            self.extend(index)
            self.values[index] = value
        else:
            self.values[index] = value

    def __str__(self):
        return str(self.values)

    def __repr__(self):
        return f"InfiniteArray: {self.values}"


def run(code: str) -> None:
    """
    Run BrainLove code
    :param code: The code to run
    """
    jumps = find_jump(code)
    memory = InfiniteArray(0)
    pointer = 0
    buffer_in = []
    buffer_out = []

    code_pos = 0
    while code_pos < len(code):
        print("memory:", memory)
        letter = code[code_pos]

        if letter == "+":
            memory[pointer] += 1
            if memory[pointer] == 256:
                memory[pointer] = 0

        elif letter == "-":
            memory[pointer] -= 1
            if memory[pointer] == -1:
                memory[pointer] = 255

        elif letter == ">":
            pointer += 1

        elif letter == "<":
            pointer -= 1
            if pointer == -1:
                raise ValueError("Pointer went to -1")

        elif letter == "[":
            if memory[pointer] == 0:
                jump_to = jumps[code_pos]
                code_pos = jump_to

        elif letter == "]":
            if memory[pointer] != 0:
                jump_to = jumps[code_pos]
                code_pos = jump_to

        code_pos += 1


def find_jump(code: str) -> Dict[int, int]:
    """
    Find the jumps so we don't have to do it during runtime
    :param code:
    :return: A Dict of the {code_pos_of_jump: jump_to}
    """
    jumps = {}
    code_pos = 0

    while code_pos < len(code):
        letter = code[code_pos]
        if letter == "[":
            needed = 1
            for searching_code_pos, searching_letter in enumerate(code[code_pos + 1:]):
                if searching_letter == "[":
                    needed += 1
                if searching_letter == "]":
                    needed -= 1

                if needed == 0:
                    break
            else:
                raise SyntaxError("Miss matched [ and ]")

            jump_to_pos = code_pos + searching_code_pos + 1
            jumps[code_pos] = jump_to_pos
            jumps[jump_to_pos] = code_pos

        code_pos += 1

    return jumps


if __name__ == "__main__":
    code = ""
    run(code)
