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


def encode_rot(s: str):
    """
    returns encoded string by rotating every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5) % 26) + ord("a")) for ch in s])


def decode_rot(s: str):
    """
    takes as input string encoded with encode_rot function. Returns decoded string.
    
	Do not include these tokens in the code: ( ord ( ch ) + 5 - ord
	"""
    return "".join([chr(((ord(ch) - 5) % 26) + ord("a")) for ch in s])


def encode_vigenere(s: str, key: str):
    """
    returns encoded string by vigenere cipher.
    """
    return "".join([chr(((ord(ch) + ord(key[i % len(key)])) % 26) + ord("a")) for i, ch in enumerate(s)])


def decode_vigenere(s: str, key: str):
    """
    takes as input string encoded with encode_vigenere function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - ord(key[i % len(key)])) % 26) + ord("a")) for i, ch in enumerate(s)])
