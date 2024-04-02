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
    groups = [(group[1::-1] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def encode_arithmetic(s: str):
    """
    returns encoded string by adding three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # add elements in each group. Unless group has fewer elements than 3.
    groups = [(str(int(group[0]) + int(group[1]) + int(group[2]))) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_arithmetic(s: str):
    """
    takes as input string encoded with encode_arithmetic function. Returns decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # reverse elements in each group. Unless group has fewer elements than 3.
    groups = [(str(int(group[0]) - int(group[1]) - int(group[2]))) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def encode_base_n(s: str, n: int):
    """
    returns encoded string by using base-n encoding.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3),