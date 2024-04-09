def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""

    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


def encode_rot13(s: str):
    """
    returns encoded string by rotating every character by 13 in the alphabet.
    """
    return encode_shift(s)


def decode_rot13(s: str):
    """
    takes as input string encoded with encode_rot13 function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""

    return decode_shift(s)


def encode_reverse(s: str):
    """
    returns encoded string by reversing its characters.
    """
    return s[::-1]


def decode_reverse(s: str):
    """
    takes as input string encoded with encode_reverse function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""

    return s[::-1]


def encode_mirror(s: str):
    """
    returns encoded string by mirroring its characters.
    """
    return s[::-1] + s


def decode_mirror(s: str):
    """
    takes as input string encoded with encode_mirror function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""

    return s[len(s) // 2 :] + s[: len(s) // 2]


def encode_caesar(s: str, key: int):
    """
    returns encoded string by shifting every character by key in the alphabet.
    """
    return "".join([chr(((ord(ch) + key - ord("a")) % 26) + ord("a")) for ch in s])


def decode_caesar(s: str, key: int):
    """
    takes as input string encoded with encode_caesar function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""

    return "".join