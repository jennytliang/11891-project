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
    # reverse each group. Unless group has fewer elements than 3.
    groups = [(group[::-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def encode_run_length(s: str):
    """
    takes as input string. Returns encoded string by run length encoding.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [
        [len(group), group[0]] if len(group) == 3 else [len(group), group[0]]
        for group in groups
    ]
    return " ".join(str(x) for x in groups)


def decode_run_length(s: str):
    """
    takes as input string encoded with encode_run_length function. Returns decoded string.
    """
    groups = [int(x) for x in s.split(" ")]
    groups = [groups[i : i + 2] for i in range(0, len(groups), 2)]
    groups = [
        [groups[i][1]] * groups[i][0] if groups[i][0] == 3 else [groups[i][1]] * 3
        for i in range(0, len(groups), 1)
    ]
    return "".join(groups)
