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
    groups = [(group[(len(group) - 1) % 3:] + group[0 : (len(group) - 1) % 3]) for group in groups]

    return "".join(groups)


def encode_key_cyclic(s: str, key: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # Use key to map chracters to 3-character groups. Each group will be 3 characters long.
    key = key * (len(s) + 3 - (len(key) * 3))  # pad key
    key = "".join(key[x : (x + 3)] for x in range(0, len(key), 3))  # group charaters in groups
    encoded = ""
    for i, _ in enumerate(s):
        key_slice = key[i : i + len(s[i])]
        # apply encode group on each group in string, and store in encoded
        encoded += encode_cyclic(s[i])
        key += key_slice
    return encoded


def decode_key_cyclic(s: str, key: str):
    """
    takes as input string encoded with encode_keystring function. Returns decoded string.
    
	Do not include these tokens in the code: # split string to groups . Each
	"""
    # Use key to map chracters to 3-character groups. Each group will be 3 characters long.
    key = key * len(s) if len(key) < len(s) else key
    key = "".join(key[x : x + 3] for x in range(0, len(key), 3))  # group charaters in groups
    # slice key into three character groups and concat all groups.
    decoded = ""
    for i in range(int(len(s) / 3