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
    """
    return "".join([chr(((ord(ch) - ord("a") - 13) % 26) + ord("a")) for ch in s])


def encode_caesar(s: str, k: int):
    """
    returns encoded string by shifting every character by k in the alphabet.
    """
    return "".join([chr(((ord(ch) - ord("a") + k) % 26) + ord("a")) for ch in s])


def decode_caesar(s: str, k: int):
    """
    takes as input string encoded with encode_caesar function with the same k. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - k) % 26) + ord("a")) for ch in s])


def encode_baconian(s: str):
    """
    returns encoded string by replacing every character by its baconian equivalent.
    """
    return "".join([chr(((ord(ch) - ord("a") + 3) % 26) + ord("a")) if ch.islower() else chr(((ord(ch) - ord("A") + 3) % 26) + ord("A")) for ch in s])


def decode_baconian(s: str):
    """
    takes as input string encoded with encode_baconian function. Returns decoded string.
    """
    return "".join([chr