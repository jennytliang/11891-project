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
    
	Do not include these tokens in the code:  # split string to groups . Each of length
	"""

    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def encode_atbash(s: str):
    """
    takes as input string. Returns encoded string by Atbash cipher.
    """
    # create dictionary to map letters to numbers.
    # letters: 0, 1, 2, ..., 9, A, B, ..., Z
    # numbers: Z, Y, X, ..., 0, 9, 8, ..., A
    # map = {letter: number for letter in string.ascii_uppercase}
    # map = {number: letter for number in string.ascii_uppercase}
    # map = {letter: number for letter in string.ascii_lowercase}
    # map = {number: letter for number in string.ascii_lowercase}
    # map = {letter: number for letter in string.ascii_letters}
    # map = {number: letter for number in string.ascii_letters}

    # create dictionary to map letters to numbers.
    # letters: 0, 1, 2, ..., 9, A, B, ..., Z
    # numbers: Z, Y, X, ..., 0, 9, 8, ..., A
    # map = {letter: number for letter in string.ascii_uppercase}
    # map = {number: letter for number in string.ascii_uppercase}
    # map = {letter: number for letter in string.ascii_lowercase}
    # map = {number: letter for number in string.ascii_lowercase}
    # map = {letter: number for letter in string.ascii_letters}
    # map = {number: letter for