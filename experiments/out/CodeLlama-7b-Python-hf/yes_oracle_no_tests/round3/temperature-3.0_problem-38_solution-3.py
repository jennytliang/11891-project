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
    groups = [(group[-1] + group[0] + group[1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def encode_atbash(s: str):
    """
    returns encoded string by using atbash cipher.
    """
    # create a dictionary of pairs of characters.
    # 1st character has the same value as the last character.
    # 2nd character has the same value as the second last character.
    # 3rd character has the same value as the first character.
    #
    # for example:
    # 'abc' becomes 'zyx'
    # '123' becomes '987'

    # create a dictionary of pairs of characters.
    # 1st character has the same value as the last character.
    # 2nd character has the same value as the second last character.
    # 3rd character has the same value as the first character.
    #
    # for example:
    # 'abc' becomes 'zyx'
    # '123' becomes '987'
    pairs = {
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