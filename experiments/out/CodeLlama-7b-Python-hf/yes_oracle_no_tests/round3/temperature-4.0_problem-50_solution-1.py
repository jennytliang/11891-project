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


def encode_substitution(s: str, key: str):
    """
    takes as input string and key. Returns encoded string using key.
    """
    return "".join([key[ord(ch) - ord("a")] for ch in s])


def decode_substitution(s: str, key: str):
    """
    takes as input string and key. Returns decoded string using key.
    """
    return "".join([chr(key.index(ch)) for ch in s])


def encode_vigenere(s: str, key: str):
    """
    takes as input string and key. Returns encoded string using key.
    """
    return "".join([s[(ord(ch) - ord("a") + key.index(k)) % 26] for ch, k in zip(s, key)])


def decode_vigenere(s: str, key: str):
    """
    takes as input string and key. Returns decoded string using key.
    """
    return "".join([s[(ord(ch) - ord(k) - ord("a")) % 26] for ch, k in zip(s, key)])


def encode_transposition(s: str, key: int):
    """
    takes as input string and key. Returns encoded string using key.
    """
    return "".join(s[key * i : key * (i + 1)] for i in range(len(s) // key)) + s[len(s) // key * key :]


def decode_transposition(s: str, key: int):
    """
    takes as input string and key. Returns decoded string using key.
    """
    return encode_transposition(s, key)


def encode_arithmetic(s: str):
    """
    takes as input string. Returns encoded string.
    """
    return "".join([str(ord(ch) - ord("a") + 1) for ch