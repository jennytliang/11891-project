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


def encode_reverse(s: str):
    """
    encoded string by reversing the string.
    """
    return s[::-1]


def decode_reverse(s: str):
    """
    takes as input string encoded by encode_reverse. Returns original string.
    
    Do not include these tokens in the code: (
    """

    return s[::-1]


def encode_rot13(s: str):
    """
    encoded string by rotating all alphabetic characters forward by 13 places.
    """
    return encode_shift(s)


def decode_rot13(s: str):
    """
    takes as input string encoded by encode_rot13. Returns original string.
    
    Do not include these tokens in the code: (
    """

    return decode_shift(s)


def encode_mirror(s: str):
    """
    encoded string by mirroring the alphabetic characters.
    """
    return "".join(
        [
            ("|".join(list(reversed(row))))
            for row in ["".join(list(reversed(ch))) for ch in s.split("") if ch.isalpha()]
        ]
    )


def decode_mirror(s: str):
    """
    takes as input string encoded by encode_mirror. Returns original string.
    
    Do not include these tokens in the code: (
    """
    return encode_mirror(s)
