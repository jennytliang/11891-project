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
    returns encoded string by replacing the characters of the alphabet with the characters of the alphabet shifted by 5.
    """
    return "".join([chr((ord(ch) + 5 - ord("a")) % 26) for ch in s])


def decode_substitution(s: str):
    """
    takes as input string encoded with encode_substitution function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""

    return "".join([chr((ord(ch) - 5 - ord("a")) % 26) for ch in s])


def encode_vigenere(s: str, k: str):
    """
    takes as input string to encode and keyword. Returns encoded string.
    """
    encoded_string = ""
    i = 0
    for ch in s:
        if ch == " ":
            encoded_string += ch
        else:
            encoded_string += chr(
                (ord(ch) + ord(k[i % len(k)]) - 2 * ord("a")) % 26 + ord("a")
            )
            i += 1
    return encoded_string


def decode_vigenere(s: str, k: str):
    """
    takes as input string encoded with encode_vigenere function and keyword used for encoding. Returns decoded string.
    """
    decoded_string = ""
    i = 0
    for ch in s:
        if ch == " ":
            decoded_string += ch
        else:
            decoded_string += chr(
                (ord(ch) - ord(k[i % len(k)]) - ord("a")) % 26 + ord("a")
            )
            i += 1
    return decoded_string


def encode_columnar_transposition(s: str, k: str):
    """
    takes as input