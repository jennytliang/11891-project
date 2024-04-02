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
    groups = [(group[-1] + group[0:2]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def encode_base(s: str, base: int):
    """
    takes as input string and base to encode it in.
    """
    if base < 2:
        raise ValueError("Base must be greater or equal than 2")
    if base == 2:
        return "".join(format(ord(x), "08b") for x in s)
    if base == 10:
        return s
    if base > 36:
        raise ValueError("Base must be less or equal than 36")
    return "".join(format(ord(x), "0" + str(base) + "o") for x in s)


def decode_base(s: str, base: int):
    """
    takes as input string and base to decode it from.
    """
    if base < 2:
        raise ValueError("Base must be greater or equal than 2")
    if base == 2:
        return "".join(chr(int(x, 2)) for x in s)
    if base == 10:
        return s
    if base > 36:
        raise ValueError("Base must be less or equal than 36")
    return "".join(chr(int(x, base)) for x in s)


def encode_morse(s: str):
    """
    takes as input string to encode in morse code.
    """
    # replace all letters with their corresponding morse code
    code = "".join([morse[x] for x in s.lower() if x in morse])
    # separate morse code into groups of 5
    groups = [code[(5 * i):min((5 * i + 5), len(code))] for i in range((len(code