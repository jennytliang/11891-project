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
    return "".join([chr(((ord(ch) + 13 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_rot13(s: str):
    """
    takes as input string encoded with encode_rot13 function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""

    return "".join([chr(((ord(ch) - 13 - ord("a")) % 26) + ord("a")) for ch in s])


def encode_atbash(s: str):
    """
    returns encoded string by using Atbash cipher.
    """
    return "".join([chr(25 - ord(ch)) for ch in s])


def decode_atbash(s: str):
    """
    takes as input string encoded with encode_atbash function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""

    return "".join([chr(25 - ord(ch)) for ch in s])


def encode_reverse(s: str):
    """
    returns encoded string by reversing the string.
    """
    return s[::-1]


def decode_reverse(s: str):
    """
    takes as input string encoded with encode_reverse function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""

    return s[::-1]


def encode_base64(s: str):
    """
    returns encoded string by using Base64 encoding.
    """
    return "".join([chr(ord(ch) // 64 + 65) + chr((ord(ch) % 64) // 26 + 65