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
    return "".join([chr(((ord(ch) - 13 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_rot13(s: str):
    """
    takes as input string encoded with encode_rot13 function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""
    return "".join([chr(((ord(ch) + 13 - ord("a")) % 26) + ord("a")) for ch in s])


def encode_atbash(s: str):
    """
    returns encoded string by swapping every character by its opposite in the alphabet.
    """
    return "".join(
        [
            chr((25 - ord(ch) + ord("a")) % 26 + ord("a"))
            for ch in s
            if ch.isalpha()
        ]
    )


def decode_atbash(s: str):
    """
    takes as input string encoded with encode_atbash function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""
    return "".join(
        [
            chr((25 - ord(ch) - ord("a")) % 26 + ord("a"))
            for ch in s
            if ch.isalpha()
        ]
    )


def encode_railfence(s: str, n: int):
    """
    returns encoded string by using railfence cipher.
    """
    r = range(n)
    return "".join(
        [s[r[-i % (n - 1) - 1]] if (i // (n - 1) % 2 == 0) else s[r[i % (n - 1)]