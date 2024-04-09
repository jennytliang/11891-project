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


def encode_substitution(s: str, key: str):
    """
    returns encoded string by substituting every character by the corresponding one in the key.
    """
    return "".join([key[ord(ch) - ord("a")] for ch in s])


def decode_substitution(s: str, key: str):
    """
    takes as input string encoded with encode_substitution function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""
    return "".join([chr(ord(key[ord(ch) - ord("a")]) - ord("a")) for ch in s])


def encode_vigenere(s: str, key: str):
    """
    returns encoded string by applying vigenere cipher.
    """
    return "".join(
        [
            chr(
                (ord(ch) + ord(key[(ord(ch) + ord(key[ord(s[i]) - ord("a")]) - ord("a")) % len(key)]) - ord("a"))
                % 26
            )
            for i, ch in enumerate(s)
        ]
    )


def decode_vigenere(s: str, key: str):
    """
    takes as input string encoded with encode_vigenere function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""
    return "".join(
        [
            chr(
                (ord(ch) - ord(key[(ord(ch) - ord(key[ord(s[i]) - ord("a")]) - ord("a")) % len(key)]) - ord("a"))
                % 26
            )
            for i, ch in enumerate(s)
        ]
    )


def encode_autokey(s: str, key: str):
    """
    returns encoded string by applying autokey cipher.
    """
    key = key +