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


def encode_bubble(s: str):
    """
    takes as input string and returns encoded string by bubbling groups of four characters.
    
	Do not include these tokens in the code: # split string to groups . Each
	"""
    groups = [s[(4 * i):min((4 * i + 4), len(s))] for i in range((len(s) + 3) // 4)]
    groups = [(group[2:] + group[0] + group[1]) if len(group) == 4 else group for group in groups]
    return "".join(groups)


def decode_bubble(s: str):
    """
    takes as input string encoded with encode_bubble function. Returns decoded string.
    
	Do not include these tokens in the code: # split string to groups . Each
	"""
    groups = [s[(4 * i):min((4 * i + 4), len(s))] for i in range((len(s) + 3) // 4)]
    groups = [(group[2:] + group[0] + group[1]) if len(group) == 4 else group for group in groups]
    return "".join(groups)


def encode_bubble_and_cyclic(s: str):
    """
    takes as input string and returns encoded string by bubbling groups of five characters.
    
	Do not include these tokens in the code: # split string to groups . Each
	"""
    groups = [s[(5 * i):min((5 * i + 5), len(s))] for i in range((len(s) + 4) // 5)]
    groups = [(group[2:] + group[0] + group[1]) if len(group) == 5 else group for group