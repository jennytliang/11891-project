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
    groups = [
        (group[1:] + group[0]) if len(group) == 3 else group for group in groups
    ]
    # join groups to string.
    return "".join(groups)


def encode_atbash(s: str):
    """
    returns encoded string by atbash cipher.
    """
    # create dict.
    atbash = {
        "a": "z",
        "b": "y",
        "c": "x",
        "d": "w",
        "e": "v",
        "f": "u",
        "g": "t",
        "h": "s",
        "i": "r",
        "j": "q",
        "k": "p",
        "l": "o",
        "m": "n",
        "n": "m",
        "o": "l",
        "p": "k",
        "q": "j",
        "r": "i",
        "s": "h",
        "t": "g",
        "u": "f",
        "v": "e",
        "w": "d",
        "x": "c",
        "y": "b",
        "z": "a",
    }
    # replace each char in string with its value in atbash dict.
    return "".join([atbash[c] if c in atbash else c for c in s])


def decode_atbash(s: str):
    """
    takes as input string encoded with encode_atbash function. Returns decoded string.
    """
    # create dict.
    atbash = {
        "a": "z",
        "b": "y",
        "c": "x",
        "d": "w",
       