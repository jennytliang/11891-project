def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


def encode_rot13(s: str):
    """
    returns encoded string by rotating every character by 13 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 13 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_rot13(s: str):
    """
    takes as input string encoded with encode_rot13 function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 13 - ord("a")) % 26) + ord("a")) for ch in s])


def encode_caesar(s: str, k: int):
    """
    returns encoded string by shifting every character by k in the alphabet.
    """
    return "".join([chr(((ord(ch) + k - ord("a")) % 26) + ord("a")) for ch in s])


def decode_caesar(s: str, k: int):
    """
    takes as input string encoded with encode_caesar function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - k - ord("a")) % 26) + ord("a")) for ch in s])


def encode_vigenere(s: str, k: str):
    """
    returns encoded string by shifting every character by k in the alphabet.
    """
    return "".join([chr(((ord(ch) + ord(k[i % len(k)]) - ord("a")) % 26) + ord("a")) for i, ch in enumerate(s)])


def decode_vigenere(s: str, k: str):
    """
    takes as input string encoded with encode_vigenere function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - ord(k[i % len(k)]) - ord("a")) % 26) + ord("a")) for i, ch in enumerate(s)])
