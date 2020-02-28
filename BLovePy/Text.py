def get():
    ascii_codes = [ord(letter) for letter in input("? ")]
    if any(code > 255 for code in ascii_codes):
        raise ValueError("Invalid input from user")

    return ascii_codes


def write(*ascii_codes):
    text = "".join(chr(code) for code in ascii_codes)
    print(text)
    return []


INPUT = {
    1: get
}
OUTPUT = {
    1: write
}

