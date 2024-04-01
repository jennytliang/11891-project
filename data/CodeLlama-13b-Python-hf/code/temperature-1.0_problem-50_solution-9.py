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
    returns encoded string by shifting every character by 13 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 13 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_rot13(s: str):
    """
    takes as input string encoded with encode_rot13 function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 13 - ord("a")) % 26) + ord("a")) for ch in s])


def encode_atbash(s: str):
    """
    returns encoded string by shifting every character by 23 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 23 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_atbash(s: str):
    """
    takes as input string encoded with encode_atbash function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 23 - ord("a")) % 26) + ord("a")) for ch in s])


def encode_base64(s: str):
    """
    returns encoded string in base64.
    """
    pass


def decode_base64(s: str):
    """
    takes as input string encoded with encode_base64 function. Returns decoded string.
    """
    pass