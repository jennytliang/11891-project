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
    returns encoded string by substituting every character by its neighbor in the alphabet.
    """
    return "".join([chr(((ord(ch) + 1 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_substitution(s: str):
    """
    takes as input string encoded with encode_substitution function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""
    return "".join([chr(((ord(ch) - 1 - ord("a")) % 26) + ord("a")) for ch in s])


def encode_mix(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet and then substituting every character by its neighbor in the alphabet.
    """
    return encode_substitution(encode_shift(s))


def decode_mix(s: str):
    """
    takes as input string encoded with encode_mix function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""
    return decode_substitution(decode_shift(s))


def encode_monoalphabetic(s: str):
    """
    returns encoded string by substituting every character by its neighbor in the alphabet.
    """
    return encode_substitution(s)


def decode_monoalphabetic(s: str):
    """
    takes as input string encoded with encode_monoalphabetic function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""
    return decode_substitution(s)
