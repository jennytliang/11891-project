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
    returns encoded string by using atbash cipher.
    
	Do not include these tokens in the code: (
	"""
    return "".join(
        [
            chr(25 - ord(ch) + ord("a"))
            if ch.isalpha()
            else chr(25 - ord(ch) + ord("A"))
            if ch.isupper()
            else ch
            for ch in s
        ]
    )


def decode_atbash(s: str):
    """
    takes as input string encoded with encode_atbash function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""
    return encode_atbash(s)


def encode_rot13(s: str):
    """
    returns encoded string by using rot13 cipher.
    
	Do not include these tokens in the code: (
	"""
    return "".join(
        [
            chr(((ord(ch) + 13 - ord("a")) % 26) + ord("a"))
            if ch.isalpha()
            else chr(((ord(ch) + 13 - ord("A")) % 26) + ord("A"))
            if ch.isupper()
            else ch
            for ch in s
        ]
    )


def decode_rot13(s: str):
    """
    takes as input string encoded with encode_rot13 function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""
    return encode_rot13(s)


def encode_reverse(s: str):
    """
    returns encoded string by reversing its order.
    
	Do not include these tokens in the code: (
	"""
    return s[::-1]


def decode_reverse(s: str):
    """
    takes as input