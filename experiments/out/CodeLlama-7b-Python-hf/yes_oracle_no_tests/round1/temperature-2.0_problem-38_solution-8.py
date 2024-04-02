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
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [
        (group[1:] + group[0]) if len(group) == 3 else group for group in groups
    ]
    # join groups into one string.
    return "".join(groups)


def encode_bases(s: str, bases: list):
    """
    takes as input string and list of bases. Returns encoded string.
    """
    # encode each character in string by its position in bases list.
    return "".join([str(bases.index(char)) for char in s])


def decode_bases(s: str, bases: list):
    """
    takes as input string and list of bases. Returns decoded string.
    """
    # decode each character in string by its position in bases list.
    return "".join([bases[int(char)] for char in s])
