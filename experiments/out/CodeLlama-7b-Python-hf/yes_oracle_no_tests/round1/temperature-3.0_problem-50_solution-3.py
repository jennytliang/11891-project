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


def encode_substitution(s: str, key: str):
    """
    returns encoded string by replacing every character by the character in the key at the same index.
    """
    return "".join([key[ord(ch) - ord("a")] for ch in s])


def decode_substitution(s: str, key: str):
    """
    takes as input string encoded with encode_substitution function. Returns decoded string.
    """
    return encode_substitution(s, "abcdefghijklmnopqrstuvwxyz"[::-1])


def encode_vigenere(s: str, key: str):
    """
    returns encoded string by shifting every character by the character at the same index of the key.
    """
    return "".join([chr(((ord(ch) + ord(key[i % len(key)])) % 26) + ord("a")) for i, ch in enumerate(s)])


def decode_vigenere(s: str, key: str):
    """
    takes as input string encoded with encode_vigenere function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - ord(key[i % len(key)])) % 26) + ord("a")) for i, ch in enumerate(s)])
