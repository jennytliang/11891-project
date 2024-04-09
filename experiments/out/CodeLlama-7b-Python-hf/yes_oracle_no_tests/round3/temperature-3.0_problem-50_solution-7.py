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


def encode_subst(s: str):
    """
    returns encoded string by substituting every character by 5 characters in the alphabet.
    """
    return "".join(
        [
            chr(((ord(ch) - ord("a") + 5) % 26) + ord("a"))
            if not ch.isupper()
            else chr(((ord(ch) - ord("A") + 5) % 26) + ord("A"))
            for ch in s
        ]
    )


def decode_subst(s: str):
    """
    takes as input string encoded with encode_subst function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""
    return "".join(
        [
            chr(((ord(ch) - ord("a") - 5) % 26) + ord("a"))
            if not ch.isupper()
            else chr(((ord(ch) - ord("A") - 5) % 26) + ord("A"))
            for ch in s
        ]
    )


def encode_subst_and_shift(s: str):
    """
    returns encoded string by substituting every character by 5 characters in the alphabet and then shifting every character by 1 in the alphabet.
    """
    return encode_shift(encode_subst(s))


def decode_subst_and_shift(s: str):
    """
    takes as input string encoded with encode_subst_and_shift function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""
    return decode_subst(decode_shift(s))


def encode_vigenere(s: str, k: str):
    """
    returns encoded string by using vigenere cipher.
    """
    return "".join(
        [
            chr(((ord(ch) + ord(k[i % len(k)]))