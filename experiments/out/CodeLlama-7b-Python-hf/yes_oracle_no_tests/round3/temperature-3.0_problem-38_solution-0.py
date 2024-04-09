def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    
	Do not include these tokens in the code: # split string to groups . Each
	"""
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    # return string without last element in each group.
    return "".join([group[0] for group in groups])


def encode_atbash(s: str):
    """
    returns encoded string using atbash cipher.
    """
    # create dictionary with letters and their cipher codes
    chars = "abcdefghijklmnopqrstuvwxyz"
    cipher = chars[::-1]
    code = dict(zip(chars, cipher))
    # return encoded string.
    return "".join([code[c] for c in s])


def decode_atbash(s: str):
    """
    takes as input string encoded with encode_atbash function. Returns decoded string.
    """
    # create dictionary with letters and their cipher codes
    chars = "abcdefghijklmnopqrstuvwxyz"
    cipher = chars[::-1]
    code = dict(zip(chars, cipher))
    # return decoded string.
    return "".join([code[c] for c in s])


def encode_caesar(s: str, k: int):
    """
    returns encoded string by caesar cipher.
    """
    # create dictionary with letters and their cipher codes
    chars = "abcdefghijklmnopqrstuvwxyz"
    cipher = chars[k:] + chars[:k]
    code = dict(zip(chars, cipher))
    # return encoded string.
    return "".join([code[c] for c in s])


def decode_caesar(s: str, k: int):
    """
    takes as input string encoded with