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


def encode_rotate(s: str):
    """
    returns encoded string by rotating every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_rotate(s: str):
    """
    takes as input string encoded with encode_rotate function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


def encode_reverse(s: str):
    """
    returns encoded string by reversing the order of the characters in the string.
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
    returns encoded string by mirroring the string.
    """
    return "".join(reversed(s))


def decode_mirror(s: str):
    """
    takes as input string encoded with encode_mirror function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""
    return "".join(reversed(s))


def encode_vigenere(s: str, key: str):
    """
    returns encoded string by using the Vigenere cipher.
    """
    key_cycle = (key + s)[: len(s)]
    return "".join([chr(((ord(ch) + ord(key_cycle[i])) % 26) + ord("a")) for i, ch in enumerate(s)])