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
    # uncycle elements in each group. Unless group has fewer elements than 3.
    groups = [
        (groups[i][-1] + groups[i][0: len(groups[i]) - 1])
        if len(groups[i]) == 3
        else groups[i]
        for i in range(len(groups))
    ]
    # return decoded string by joining all the groups.
    return "".join(groups)


def encode_snailfish(s: str):
    # encoding is the same as encoding any other string
    return encode_cyclic(s)


def decode_snailfish(s: str):
    # decoding is the same as decoding any string, then reversing it
    return decode_cyclic(s[::-1])


def test():
    import random

    s = ""
    for _ in range(1000):
        s += random.choice("abcdefghijklmnopqrstuvwxyz1234567890")
    assert decode_cyclic(s) == s


if __name__ == "__main__":
    test()
