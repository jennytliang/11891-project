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


def encode_substitution(s: str, letters: str):
    """
    returns encoded string by replacing every character by the character from letters.
    
	Do not include these tokens in the code: (
	"""
    return "".join([letters[ord(ch) - ord("a")] for ch in s])


def decode_substitution(s: str, letters: str):
    """
    takes as input string encoded with encode_substitution function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""
    return "".join([chr(ord(letters[ord(ch) - ord("a")]) - ord("a")) for ch in s])


def encode_affine(s: str, a: int, b: int):
    """
    returns encoded string by multiplying every character by a and adding b.
    
	Do not include these tokens in the code: (
	"""
    return "".join([chr(((ord(ch) - ord("a")) * a + b) % 26 + ord("a")) for ch in s])


def decode_affine(s: str, a: int, b: int):
    """
    takes as input string encoded with encode_affine function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""
    return "".join([chr((((ord(ch) - ord("a")) - b) * 26 // a + ord("a")) % 26 + ord("a")) for ch in s])


def encode_vigenere(s: str, k: str):
    """
    returns encoded string by shifting every character by the corresponding character in k.
    
	Do not include these tokens in the code: (
	"""
    return "".join([chr(((ord(ch) + ord(k[(ord(ch) - ord("a")) % len(k)])) - ord("a")) % 2