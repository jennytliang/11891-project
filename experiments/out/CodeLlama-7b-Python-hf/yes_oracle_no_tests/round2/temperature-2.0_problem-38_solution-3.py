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
    # remove first element from each group. Unless group has fewer elements than 3.
    groups = [(group[1:]) if len(group) == 3 else group for group in groups]
    # join groups.
    return "".join(groups)


def encode_atbash(s: str):
    """
    returns encoded string by Atbash cipher.
    """
    # create a dictionary with each character and its encoding.
    dict = {"a": "z", "b": "y", "c": "x", "d": "w", "e": "v", "f": "u", "g": "t", "h": "s", "i": "r", "j": "q", "k": "p", "l": "o", "m": "n", "n": "m", "o": "l", "p": "k", "q": "j", "r": "i", "s": "h", "t": "g", "u": "f", "v": "e", "w": "d", "x": "c", "y": "b", "z": "a", "A": "Z", "B": "Y", "C": "X", "D": "W", "E": "V", "F": "U", "G": "T", "H": "S", "I": "R", "J": "Q", "K": "P", "L": "O", "M": "N", "N": "M", "O": "L", "P": "K", "Q": "J", "R": "I", "S": "H", "T": "G", "U": "F", "V": "E", "W": "D", "X": "C", "Y": "B", "Z": "A"}
    # create an empty string to store encoded string.
    encoded_string = ""
    # loop through string.
   