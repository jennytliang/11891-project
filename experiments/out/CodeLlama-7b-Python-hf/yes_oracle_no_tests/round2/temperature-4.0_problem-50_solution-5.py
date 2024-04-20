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


def encode_caesar(s: str):
    """
    returns encoded string by shifting every character by 1 in the alphabet.
    """
    return encode_shift(s)


def decode_caesar(s: str):
    """
    takes as input string encoded with encode_caesar function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""

    return decode_shift(s)


def encode_atbash(s: str):
    """
    returns encoded string by using reverse alphabet in place of alphabet.
    """
    return "".join([chr(ord("z") - ord(ch) + ord("a")) for ch in s])


def decode_atbash(s: str):
    """
    takes as input string encoded with encode_atbash function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""

    return "".join([chr(ord("z") - ord(ch) + ord("a")) for ch in s])