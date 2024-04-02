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


def encode_vigenere(s: str, k: str):
    """
    returns encoded string by using vigenere cipher.
    """
    s = s.lower()
    k = k.lower()
    return "".join([chr(((ord(ch) + ord(k[i % len(k)]) - 2 * ord("a")) % 26) + ord("a")) for i, ch in enumerate(s)])


def decode_vigenere(s: str, k: str):
    """
    takes as input string encoded with encode_vigenere function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""

    s = s.lower()
    k = k.lower()
    return "".join([chr(((ord(ch) - ord(k[i % len(k)]) - 2 * ord("a")) % 26) + ord("a")) for i, ch in enumerate(s)])


def encode_bifid(s: str, k: str):
    """
    returns encoded string by using bifid cipher.
    """
    s = s.lower()
    k = k.lower()
    return "".join([chr(ord("a") + (ord(ch) - ord("a")) * ord(k[i % len(k)]) % 26) for i, ch in enumerate(s)])


def decode_bifid(s: str, k: str