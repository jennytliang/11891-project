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
    return "".join([chr(((ord(ch) - ord("a") + 13) % 26) + ord("a")) for ch in s])


def decode_rot13(s: str):
    """
    takes as input string encoded with encode_rot13 function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""

    return "".join([chr(((ord(ch) - ord("a") + 13) % 26) + ord("a")) for ch in s])


def encode_atbash(s: str):
    """
    returns encoded string by using atbash cipher.
    """
    return "".join([chr(25 - ord(ch) + ord("a")) for ch in s])


def decode_atbash(s: str):
    """
    takes as input string encoded with encode_atbash function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""

    return "".join([chr(25 - ord(ch) + ord("a")) for ch in s])


def encode_vigenere(s: str, k: str):
    """
    takes as input string to be encoded and key. Returns encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + ord(k[i % len(k)])) % 26) + ord("a")) for i, ch in enumerate(s)])


def decode_vigenere(s: str, k: str):
    """
    takes as input string encoded with encode_vigenere function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - ord(k[i % len(k)])