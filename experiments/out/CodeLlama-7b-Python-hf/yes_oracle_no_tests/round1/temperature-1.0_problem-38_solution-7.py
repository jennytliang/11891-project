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
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def encode_caesar(s: str):
    """
    returns encoded string by cycling elements of group of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [
        (group[1:] + group[0]) if len(group) == 3 else group for group in groups
    ]
    # split each group to groups of 3.
    groups = [groups[i : i + 3] for i in range(0, len(groups), 3)]
    # join groups to string.
    return "".join(["".join(group) for group in groups])


def decode_caesar(s: str):
    """
    takes as input string encoded with encode_caesar function. Returns decoded string.
    """
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    groups = [
        (group[1:] + group[0]) if len(group) == 3 else group for group in groups
    ]
    groups = [groups[i : i + 3] for i in range(0, len(groups), 3)]
    return "".join(["".join(group) for group in groups])
