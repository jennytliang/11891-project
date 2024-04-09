def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
	Do not include these tokens in the code: ( ord ( ch ) + 5 - ord
	"""

    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


def encode_rot13(s: str):
    """
    returns encoded string with rot13 encoding.
    """
    return encode_shift(s)


def decode_rot13(s: str):
    """
    takes as input string encoded with encode_rot13 function. Returns decoded string.
    """
    return decode_shift(s)


def encode_xor(s: str, key: str):
    """
    returns encoded string by xor-ing every character with the key.
    """
    return "".join([chr(ord(ch) ^ ord(key)) for ch in s])


def decode_xor(s: str, key: str):
    """
    takes as input string encoded with encode_xor function. Returns decoded string.
    """
    return encode_xor(s, key)


def encode_base64(s: str):
    """
    returns encoded string with base64 encoding.
    """
    import base64

    return base64.b64encode(s.encode("ascii")).decode("ascii")


def decode_base64(s: str):
    """
    takes as input string encoded with encode_base64 function. Returns decoded string.
    """
    import base64

    return base64.b64decode(s.encode("ascii")).decode("ascii")


def encode_caesar(s: str, key: int):
    """
    returns encoded string by caesar cipher with the key.
    """
    return encode_shift(s)


def decode_caesar(s: str, key: int):
    """
    takes as input string encoded with encode_caesar function. Returns decoded string.
    """
    return decode_shift(s)


def encode_morse(s: str):
    """
    returns encoded string with morse code.
    """
    MOR