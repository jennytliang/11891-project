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
    for i in range(len(groups)):
        if len(groups[i]) == 3:
            groups[i] = groups[i][-1] + groups[i][: - 1]
    return "".join(groups)


# Examples

assert encode_cyclic("C_CyCl_e_cody_Cycle") == "CyCyClCeecody"
assert decode_cyclic("CyCyClCeecody") == "C_CyCl_e_cody_Cycle"
