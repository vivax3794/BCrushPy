import requests


def get(*ascii_codes):
    url = "".join(chr(code) for code in ascii_codes)
    res = requests.get(url)
    result = [ord(letter) for letter in res.text]
    return result


INPUT = {
    1: get
}
