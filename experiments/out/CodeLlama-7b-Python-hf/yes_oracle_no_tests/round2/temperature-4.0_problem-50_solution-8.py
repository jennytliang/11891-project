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
    returns encoded string using atbash cipher.
    """
    return "".join([chr(ord("z") - ord(ch) + ord("a")) for ch in s])


def decode_atbash(s: str):
    """
    takes as input string encoded with encode_atbash function. Returns decoded string.
    """
    return "".join([chr(ord("z") - ord(ch) + ord("a")) for ch in s])


def encode_rot13(s: str):
    """
    returns encoded string using rot13 cipher.
    """
    return "".join([chr(ord("n") - ord(ch) + ord("a")) if ord(ch) >= ord("a") and ord(ch) <= ord("m") else chr(
        ord("a") + ord(ch) - ord("a") - 13) if ord(ch) >= ord("n") and ord(ch) <= ord("z") else ch for ch in s])


def decode_rot13(s: str):
    """
    takes as input string encoded with encode_rot13 function. Returns decoded string.
    """
    return "".join([chr(ord("n") - ord(ch) + ord("a")) if ord(ch) >= ord("a") and ord(ch) <= ord("m") else chr(
        ord("a") + ord(ch) - ord("a") - 13) if ord(ch) >= ord("n") and ord(ch) <= ord("z") else ch for ch in s])


def encode_xor(s: str, key: str):
    """
    returns encoded string using xor cipher with key.
    """
    return "".join([chr(ord(ch) ^ ord(key[i % len(key)])) for i, ch in enumerate(s)])


def decode_xor(s: str, key: