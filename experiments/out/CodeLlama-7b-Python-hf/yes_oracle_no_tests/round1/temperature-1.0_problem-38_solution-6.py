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
    # reverse elements in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[0:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def encode_caesar(s: str):
    """
    returns encoded string by shifting each character by 3 places.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # shift each group by 3 places. Unless group has fewer elements than 3.
    groups = [(group[3:] + group[0:3]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_caesar(s: str):
    """
    takes as input string encoded with encode_caesar function. Returns decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # shift each group by 3 places. Unless group has fewer elements than 3.
    groups = [(group[0:3] + group[3:]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def encode_atbash(s: str):
    """
    returns encoded string by substituting each character by its atbash equivalent.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 