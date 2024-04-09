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
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def encode_columnar(s: str):
    """
    takes as input string. Returns encoded string.
    """
    # split string to groups. Each group has one character.
    groups = [s[(3 * i):min((3 * i + 1), len(s))] for i in range((len(s) + 2) // 3)]
    # add spaces between each group.
    groups = [group + " " for group in groups]
    return "".join(groups)


def decode_columnar(s: str):
    """
    takes as input string encoded with encode_columnar function. Returns decoded string.
    """
    # split string to groups. Each group has one character.
    groups = s.split(" ")
    # remove spaces between each group.
    groups = [group[:-1] for group in groups]
    return "".join(groups)


def encode_morse(s: str):
    """
    takes as input string. Returns encoded string.
    """
    # split string to groups. Each group has one character.
    groups = [s[(3 * i):min((3 * i + 1), len(s))] for i in range((len(s) + 2) // 3)]
    # convert each group to morse code.
    groups = [morse_code[group] for group in groups]
    return " ".join(groups)


def decode_morse(s: str):
    """
    takes as input string encoded with encode_morse function. Returns decoded string.
    """
    # split string to groups. Each group has one character.
    groups =