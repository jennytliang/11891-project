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


def encode_atbash(s: str):
    """
    returns encoded string by swapping every character with its opposite in the alphabet.
    """
    return "".join(
        [chr((ord("z") - ord(ch) + ord("a")) % 26) for ch in s.lower() if ch.isalpha()]
    )


def decode_atbash(s: str):
    """
    takes as input string encoded with encode_atbash function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""

    return "".join(
        [chr((ord("z") - ord(ch) + ord("a")) % 26) for ch in s.lower() if ch.isalpha()]
    )
