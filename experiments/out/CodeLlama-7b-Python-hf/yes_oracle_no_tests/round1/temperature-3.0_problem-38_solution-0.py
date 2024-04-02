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
    # swap first and last elements in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[1:len(group) - 1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def encode_with_key(s: str, key: str):
    """
    returns encoded string by cycling groups of three characters and using key.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [
        (group[key[i % len(key)]] + group[0 if i % len(key) == 0 else 1] + group[2 if i % len(key) == 0 else 1])
        if len(group) == 3 else group
        for i, group in enumerate(groups)
    ]
    return "".join(groups)


def decode_with_key(s: str, key: str):
    """
    takes as input string encoded with encode_with_key function. Returns decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # swap first and last elements in each group. Unless group has fewer elements than 3.
    groups = [
        (group[2 if key[i % len(key)] == 0 else 1] + group[key[i % len(key)]] + group[0 if key[i % len(key)] == 0 else