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
    returns encoded string by rotating every character by 13 in the alphabet.
    """
    return "".join([chr(((ord(ch) - 13 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_rot13(s: str):
    """
    takes as input string encoded with encode_rot13 function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""

    return "".join([chr(((ord(ch) + 13 - ord("a")) % 26) + ord("a")) for ch in s])


def encode_atbash(s: str):
    """
    returns encoded string by atbash cipher.
    """
    return "".join([chr((25 - ord(ch) + ord("a"))) for ch in s])


def decode_atbash(s: str):
    """
    takes as input string encoded with encode_atbash function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""

    return "".join([chr((25 - ord(ch) - ord("a"))) for ch in s])


def encode_railfence(s: str, key: int):
    """
    returns encoded string by railfence cipher.
    """
    if key == 1:
        return s
    result = ""
    k = 2 * (key - 1)
    for i in range(k):
        j = i
        while j < len(s):
            if j % k == i:
                result += s[j]
                j += 1
    return result


def decode_railfence(s: str, key: int):
    """
    takes as input string encoded with encode_railfence function. Returns decoded string.
    