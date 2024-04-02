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
    groups = [s[min((3 * i + 1), len(s)) : min((3 * i + 4), len(s))] for i in range((len(s) + 2) // 3)]
    groups = [(group[-1] + group[0:2]) if len(group) == 3 else group for group in groups]
    # returns encoded string
    return "".join(groups)


if __name__ == "__main__":
    import sys

    argv = sys.argv
    argc = len(argv)
    print(argv, argc)

    string = encode_cyclic(argv[1])
    print(string)

    print(decode_cyclic(string))
