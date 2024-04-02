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


def encode_subst(s: str):
    """
    takes as input string and returns encoded string with substitution cipher.
    """
    return "".join([chr((ord(ch) + 13 - ord("a")) % 26) for ch in s])


def decode_subst(s: str):
    """
    takes as input string encoded with encode_subst function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) + 13 - ord("a")) % 26) for ch in s])


def encode_vigenere(s: str, key: str):
    """
    takes as input string and key and returns encoded string with vigenere cipher.
    """
    s = s.lower()
    key = key.lower()
    key *= int(len(s) / len(key)) + 1
    return "".join([chr(((ord(ch) + ord(key[i]) - 2 * ord("a")) % 26) + ord("a")) for i, ch in enumerate(s)])


def decode_vigenere(s: str, key: str):
    """
    takes as input string encoded with encode_vigenere function. Returns decoded string.
    """
    s = s.lower()
    key = key.lower()
    key *= int(len(s) / len(key)) + 1
    return "".join([chr(((ord(ch) - ord(key[i]) - 2 * ord("a")) % 26) + ord("a")) for i, ch in enumerate(s)])


def encode_bifid(s: str):
    """
    takes as input string and returns encoded string with bifid cipher.
    """
    s = s.lower()
    return "".join(["".join(s[i::5]) for i in range(5)])


def decode_bifid(s