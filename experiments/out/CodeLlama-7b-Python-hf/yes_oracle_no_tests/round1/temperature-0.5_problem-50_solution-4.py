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

    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((o - 5 - ord("a")) % 26) + ord("a")) for o in map(ord, s)])


def encode_rot13(s: str):
    """
    returns encoded string by rotating every character by 13 in the alphabet.
    """
    return encode_shift(s)


def decode_rot13(s: str):
    """
    takes as input string encoded with encode_rot13 function. Returns decoded string.
    """
    return decode_shift(s)


def encode_substitution(s: str, key: str):
    """
    returns encoded string by performing substitution cipher.
    """
    return "".join([key[ord(ch) - ord("a")] for ch in s])


def decode_substitution(s: str, key: str):
    """
    takes as input string encoded with encode_substitution function. Returns decoded string.
    """
    return "".join([chr(key.index(ch) + ord("a")) for ch in s])


def encode_vigenere(s: str, key: str):
    """
    returns encoded string by performing vigenere cipher.
    """
    return "".join([chr(((ord(ch) + ord(key[i % len(key)])) % 26) + ord("a")) for i, ch in enumerate(s)])


def decode_vigenere(s: str, key: str):
    """
    takes as input string encoded with encode_vigenere function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - ord(key[i % len(key)]) + 26) % 26) + ord("a")) for i, ch in enumerate(s)])


def encode_hill(s: str, key: str):
    """
    returns encoded string by performing hill cipher.
    """
    s_key = key.upper()
    s_key = s_key + s_key[0 : 3 * (len(s_key) // 3) -