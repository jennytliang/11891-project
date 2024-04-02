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


def encode_substitution(s: str):
    """
    returns encoded string by using substitution cipher.
    """
    return "".join([chr(ord(ch) ^ ord("a")) for ch in s])


def decode_substitution(s: str):
    """
    takes as input string encoded with encode_substitution function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""

    return "".join([chr(ord(ch) ^ ord("a")) for ch in s])


def encode_vigenere(s: str, k: str):
    """
    returns encoded string by using vigenere cipher.
    """
    return "".join([chr(((ord(ch) + ord(k[i % len(k)])) % 26) + ord("a")) for i, ch in enumerate(s)])


def decode_vigenere(s: str, k: str):
    """
    takes as input string encoded with encode_vigenere function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""
    return "".join([chr(((ord(ch) - ord(k[i % len(k)])) % 26) + ord("a")) for i, ch in enumerate(s)])


def encode_bifid(s: str):
    """
    returns encoded string by using bifid cipher.
    """
    return "".join([chr(((ord(ch) - ord("a") + 1) * 2) % 26 + ord("a")) for ch in s])


def decode_bifid(s: str):
    """
    takes as input string encoded with encode_bifid function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""
    return "".join([chr((((ord(ch) - ord("a")) // 2)