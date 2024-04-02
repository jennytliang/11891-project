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

    return "".join([chr((-(ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


def is_isogram(s: str):
    """
    checks given string is isogram. Returns True if it is and False otherwise.
    """
    if len(s) == len(set(s.lower())):
        return True
    return False


def encode_rot13(s: str):
    """
    returns encoded string using rot13
    """
    l = list(s)
    for i in range(len(l)):
        if ord(l[i]) >= 97 and ord(l[i]) <= 122:
            if ord(l[i]) + 13 <= 122:
                l[i] = chr(ord(l[i]) + 13)
            else:
                l[i] = chr(ord(l[i]) - 13)
        if ord(l[i]) >= 65 and ord(l[i]) <= 90:
            if ord(l[i]) + 13 <= 90:
                l[i] = chr(ord(l[i]) + 13)
            else:
                l[i] = chr(ord(l[i]) - 13)
    return "".join(l)


def decode_rot13(s: str):
    """
    takes as input string encoded using encode_rot13 function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""
    s = s.replace(" ", "")[1:]
    return "".join(
        [
            chr(ord("a") + (ord(ch) - ord("a") + 13) % 26) if ch != " " else ch
            for ch in s
        ]
    )


def encode_vigenere(s: str, k: str):
    """
    returns encoded string using vigenère algorithm.
    k is short key to encode the string s
    """
    import