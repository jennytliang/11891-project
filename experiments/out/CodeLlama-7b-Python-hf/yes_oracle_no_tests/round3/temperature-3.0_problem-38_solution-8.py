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
    groups = [(group[0] + group[1:]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def encode_xor(s: str):
    """
    takes as input string and returns encoded string by applying XOR cypher on each byte.
    """
    # convert string to bytes
    b = s.encode()
    # XOR each byte with 0x33
    return bytes([b[i] ^ 0x33 for i in range(len(b))]).decode()


def decode_xor(s: str):
    """
    takes as input string encoded with encode_xor function and returns decoded string.
    """
    # convert string to bytes
    b = s.encode()
    # XOR each byte with 0x33
    return bytes([b[i] ^ 0x33 for i in range(len(b))]).decode()


# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------


def encode_cyclic_xor(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    # XOR each byte with 0x33
    return bytes([b[i] ^ 0x33 for i