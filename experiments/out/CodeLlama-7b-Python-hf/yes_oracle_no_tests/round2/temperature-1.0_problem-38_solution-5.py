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
    # split string to list of length 3
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3
    groups = [
        [groups[i][0], groups[i + 1][1], groups[i + 1][2]]
        if len(groups[i]) == 3
        else groups[i]
        for i in range((len(groups) + 1) // 2)
    ]
    # concat to string
    return "".join("".join(x) for x in groups)


def encode_repeat(s: str):
    """
    returns encoded string with repeat symbols.
    
    Do not include these tokens in the code: . Split string to groups. Each of length  . Join array groups
    """
    # split string in groups. Each group is length <= 4
    groups = [
        s[(i * (len(s) // i + 1)) : (i + 1) * (len(s) // i + 1)]
        for i in range(1, (len(s) + len(s) % i + 1) // i)
    ]
    # if string has additional character
    if len(s) % len(groups[-1]) == 1:
        groups[-1] += groups[-1]
    return "".join(
        [f"{(groups[i][-1], groups[i + 1][0])[len(groups[i]) == 4]}" for i in range(len(groups))]
    )


def decode_repeat(s: str):
    """
    takes as input string encoded with encode_repeat function. Returns decoded string.
	Do not include these tokens in the code: . Split string by repeating symbols. In the example below groups are (AB, BA), (a, ba), (aa, aa)
    """
    symbol = [s[i : i + 2] for i in range(0, len(s), 2