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
    groups = [(group[-1] + group[0:2]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def encode_repeat(s: str):
    """
    returns encoded string by repeating each character.
    """
    return "".join([c * (i + 1) for i, c in enumerate(s)])


def decode_repeat(s: str):
    """
    takes as input string encoded with encode_repeat function. Returns decoded string.
    
	Do not include these tokens in the code: # split string to groups . Each
	"""
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[0:2]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def encode_vigenere(s: str, k: str):
    """
    returns encoded string by using Vigenere cipher.
    """
    # convert to uppercase
    s = s.upper()
    k = k.upper()
    return "".join([chr(((ord(c) - 65) + (ord(k[i % len(k)]) - 65)) % 26 + 65) for i, c in enumerate(s)])


def decode_vigenere(s: str, k: str):
    """
    takes as input string encoded with encode_vigenere function. Returns decoded string.
    
	Do not include these