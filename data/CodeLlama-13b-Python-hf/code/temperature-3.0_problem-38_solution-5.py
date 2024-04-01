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
    """
    # split string by group of 3 elements.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # if last group is > 1 we need to prepend it to the beginning of string
    if len(groups[-1]) != 3:
        groups = [groups[-1] + groups[0]] + groups[1:-1]

    # cycle back each group. Unless the group has fewer than three elements.
    groups = [group[1:] + group[0] if len(group) == 3 else group for group in groups]
    return "".join(groups)



if __name__ == "__main__":
    text = "test" * 5
    encoded = encode_cyclic(text)
    assert decode_cyclic(encoded) == text

