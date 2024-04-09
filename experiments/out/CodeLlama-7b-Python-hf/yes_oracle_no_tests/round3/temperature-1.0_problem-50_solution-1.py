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


def encode_vigenere(s: str, k: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_vigenere(s: str, k: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""

    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


def encode_rot13(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join(
        [
            chr(ord(ch) - 13 if ord(ch) >= ord("n") else ord(ch) + 13)
            for ch in s.lower()
        ]
    )


def decode_rot13(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""

    return "".join(
        [
            chr(ord(ch) + 13 if ord(ch) <= ord("n") else ord(ch) - 13)
            for ch in s.lower()
        ]
    )


def encode_atbash(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join(
        [
            chr(25 - ord(ch) if ord(ch) <= ord("z") else 25 - ord(ch) + ord("A"))
            for ch in s.upper()
       