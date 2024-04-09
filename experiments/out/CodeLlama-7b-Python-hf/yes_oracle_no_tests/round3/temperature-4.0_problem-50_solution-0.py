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


def encode_substitution(s: str):
    """
    returns encoded string with substituted characters.
    """
    return "".join(
        [
            chr((ord(ch) + (ord(ch) % 97) - 96) % 26 + ord("a"))
            if ch.isalpha()
            else ch
            for ch in s
        ]
    )


def decode_substitution(s: str):
    """
    takes as input string encoded with encode_substitution function. Returns decoded string.
    """
    return "".join(
        [
            chr((ord(ch) - (ord(ch) % 97) + 96) % 26 + ord("a"))
            if ch.isalpha()
            else ch
            for ch in s
        ]
    )


def encode_vignere(s: str, k: str):
    """
    returns encoded string with vignere cipher.
    """
    return "".join(
        [
            chr(((ord(ch) + (ord(k[i % len(k)]) - ord("a"))) % 26) + ord("a"))
            for i, ch in enumerate(s)
        ]
    )


def decode_vignere(s: str, k: str):
    """
    takes as input string encoded with encode_vignere function. Returns decoded string.
    """
    return "".join(
        [
            chr(((ord(ch) - (ord(k[i % len(k)]) - ord("a"))) % 26) + ord("a"))
            for i, ch in enumerate(s)
        ]
    )


def encode_xor(s: str, k: str):
    """
    returns encoded string with xor cipher.
    """
    return "".join(
        [chr(ord(ch) ^ ord(k[i % len