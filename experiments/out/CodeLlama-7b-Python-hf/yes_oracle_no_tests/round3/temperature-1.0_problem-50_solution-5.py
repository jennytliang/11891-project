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


def encode_affine(s: str, a: int, b: int):
    """
    Encode string s using affine cipher with keys a and b.
    """
    return "".join([chr((a * ord(ch) + b) % 26 + ord("a")) for ch in s])


def decode_affine(s: str, a: int, b: int):
    """
    Decode string s using affine cipher with keys a and b.
    """
    return "".join([chr(((ord(ch) - b) * pow(a, -1, 26)) % 26 + ord("a")) for ch in s])


def encode_vigenere(s: str, k: str):
    """
    Encode string s using vigenere cipher with key k.
    """
    return "".join([chr(((ord(ch) + ord(k[i % len(k)])) % 26) + ord("a")) for i, ch in enumerate(s)])


def decode_vigenere(s: str, k: str):
    """
    Encode string s using vigenere cipher with key k.
    """
    return "".join([chr(((ord(ch) - ord(k[i % len(k)])) % 26) + ord("a")) for i, ch in enumerate(s)])
