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


def decode_shift_2(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""
    return "".join([chr(((ord(ch) - ord("a")) % 26) + ord("a")) for ch in s])


def encode_vignere(s: str, k: str):
    """
    returns encoded string by vigenere cipher with given key.
    """
    return "".join([chr(((ord(ch) + ord(k[i % len(k)])) % 26) + ord("a")) for i, ch in enumerate(s)])


def decode_vignere(s: str, k: str):
    """
    takes as input string encoded with encode_vignere function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""
    return "".join([chr(((ord(ch) - ord(k[i % len(k)])) % 26) + ord("a")) for i, ch in enumerate(s)])


def encode_rot13(s: str):
    """
    returns encoded string by rot13 cipher.
    """
    return "".join([chr(((ord(ch) + 13 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_rot13(s: str):
    """
    takes as input string encoded with encode_rot13 function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""
    return "".join([chr(((ord(ch) - 13 - ord("a")) % 26) + ord("a")) for ch in s])


def encode_rot18(s: str):
    """
    returns encoded string by rot18 cipher.
