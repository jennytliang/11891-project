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
    # split reversely, so the groups of three.
    groups = [s[len(s) - 3 * i - 3:] if s and s[(len(s) - 3 * i - 3) + 1:] else s[len(s) -
                                                                                  3 * i:] for i in  list(range(round(len(s) / 3)))]
    # reconstruct the reversed groups.
    groups = [groups[0][-1:] + groups[0][:-1] if not groups[0] else groups[0]] + [groups[i][-1:] +
                                                                                  groups[i][:-1] for i in range(1, len(groups))]
    return "".join(groups)
