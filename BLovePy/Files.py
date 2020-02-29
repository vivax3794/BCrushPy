def read(*arguments):
    path = "".join(chr(code) for code in arguments)
    with open(path, "r") as f:
        content = f.read()
        return [ord(l) for l in content]


def write(*arguments):
    arguments = "".join(chr(code) for code in arguments)
    path, *content = arguments.split("||")
    content = "||".join(content)
    with open(path, "w+") as f:
        f.write(content)

    return []


INPUT = {
    1: read
}

OUTPUT = {
    1: write
}