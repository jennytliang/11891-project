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
    returns encoded string by rotating every character by 13 in the alphabet.
    """
    return "".join(
        [chr(((ord(ch) + 13 - ord("a")) % 26) + ord("a")) for ch in s]
    )


def decode_rot13(s: str):
    """
    takes as input string encoded with encode_rot13 function. Returns decoded string.
    
	Do not include these tokens in the code: ( ord ( ch ) + 13 - ord
	"""

    return "".join(
        [chr(((ord(ch) - 13 - ord("a")) % 26) + ord("a")) for ch in s]
    )


def encode_rot(s: str, n: int):
    """
    returns encoded string by rotating every character by n in the alphabet.
    """
    return "".join(
        [chr(((ord(ch) + n - ord("a")) % 26) + ord("a")) for ch in s]
    )


def decode_rot(s: str, n: int):
    """
    takes as input string encoded with encode_rot function. Returns decoded string.
    
	Do not include these tokens in the code: ( ord ( ch ) + n - ord
	"""
    return "".join(
        [chr(((ord(ch) - n - ord("a")) % 26) + ord("a")) for ch in s]
    )


def encode_substitution(s: str, d: dict):
    """
    returns encoded string by replacing every character by the character in the dictionary.
    """
    return "".join(
        [chr(ord(ch) - ord("a")).join(d[ch]) for ch in s]
    )


def decode_substitution(s: str, d: dict):
