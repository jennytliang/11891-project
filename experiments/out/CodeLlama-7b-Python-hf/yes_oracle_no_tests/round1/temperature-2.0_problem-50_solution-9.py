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
    returns encoded string by rotating each character by 13 in the alphabet.
    """
    return encode_shift(s)


def decode_rot13(s: str):
    """
    takes as input string encoded with encode_rot13 function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""
    return decode_shift(s)


def encode_caesar(s: str, shift: int = 3):
    """
    returns encoded string by shifting every character by shift in the alphabet.
    """
    return encode_shift(s)


def decode_caesar(s: str, shift: int = 3):
    """
    takes as input string encoded with encode_caesar function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""
    return decode_shift(s)


def encode_base64(s: str):
    """
    returns encoded string by converting every character to base64.
    """
    return s.encode("utf-8").hex()


def decode_base64(s: str):
    """
    takes as input string encoded with encode_base64 function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""
    return bytes.fromhex(s).decode("utf-8")


def encode_morse(s: str):
    """
    returns encoded string by converting every character to morse code.
    """
    morse_code = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",