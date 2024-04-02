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
    groups = [(group[1::-1] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def encode_repeat(s: str):
    """
    returns encoded string by repeating groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # repeat elements in each group. Unless group has fewer elements than 3.
    groups = [group * 3 for group in groups]
    return "".join(groups)


def decode_repeat(s: str):
    """
    takes as input string encoded with encode_repeat function. Returns decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # repeat elements in each group. Unless group has fewer elements than 3.
    groups = [group * 3 for group in groups]
    return "".join(groups)


if __name__ == '__main__':
    print("Cyclic encoding and decoding")
    s = "abcdefghijk"
    print("Original string:", s)
    print("Encoded string:", encode_cyclic(s))
    print("Decoded string:", decode_cyclic(encode_cyclic(s)))
    print("Original string:", s)
    print("Encoded string:", encode_repeat(s))
    print("Decoded string:", decode_repeat(encode_repeat(s)))
    print