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
    returns encoded string by performing atbash cipher on it.
    """
    return "".join(
        [
            chr(25 - ord(ch) + ord("A"))
            if ord(ch) >= ord("A") and ord(ch) <= ord("Z")
            else chr(25 - ord(ch) + ord("a"))
            if ord(ch) >= ord("a") and ord(ch) <= ord("z")
            else ch
            for ch in s
        ]
    )


def decode_atbash(s: str):
    """
    takes as input string encoded with encode_atbash function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""
    return "".join(
        [
            chr(ord(ch) - 26 + ord("A"))
            if ord(ch) >= ord("A") and ord(ch) <= ord("Z")
            else chr(ord(ch) - 26 + ord("a"))
            if ord(ch) >= ord("a") and ord(ch) <= ord("z")
            else ch
            for ch in s
        ]
    )


def encode_rot13(s: str):
    """
    returns encoded string by performing rot13 cipher on it.
    """
    return encode_shift(s)


def decode_rot13(s: str):
    """
    takes as input string encoded with encode_rot13 function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""
    return decode_shift(s)


def encode_vigenere(s: str, key: str):
    """
    returns encoded string by performing vigenere cipher on it.
    """
    key_len = len(key)
    key_iter = iter(key)
    return "".join(
       