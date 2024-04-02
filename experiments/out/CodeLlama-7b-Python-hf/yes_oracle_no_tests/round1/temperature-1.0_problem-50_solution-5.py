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
    returns encoded string with rot13.
    """
    return encode_shift(s)


def decode_rot13(s: str):
    """
    takes as input string encoded with encode_rot13 function. Returns decoded string.
    """
    return decode_shift(s)


def encode_subst(s: str, d: dict):
    """
    returns encoded string by substituting every character by the character in the dictionary.
    """
    return "".join([d.get(ch, ch) for ch in s])


def decode_subst(s: str, d: dict):
    """
    returns decoded string by substituting every character by the character in the dictionary.
    """
    return "".join([d.get(ch, ch) for ch in s])


def encode_subst_inverse(s: str, d: dict):
    """
    returns encoded string by substituting every character by the character in the dictionary.
    """
    return "".join([d.get(ch, ch) for ch in s])


def decode_subst_inverse(s: str, d: dict):
    """
    returns decoded string by substituting every character by the character in the dictionary.
    """
    return "".join([d.get(ch, ch) for ch in s])


def encode_vigenere(s: str, k: str):
    """
    returns encoded string by vigenere algorithm.
    """
    return "".join([chr(((ord(ch) + ord(k[i % len(k)])) % 26) + ord("a")) for i, ch in enumerate(s)])


def decode_vigenere(s: str, k: str):
    """
    returns decoded string by vigenere algorithm.
    """
    return "".join([chr(((ord(ch) - ord(