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
    #  split string to groups. Each of length 3. groups = [s[ # for i in
    # range(( len(s) + 2)//3 )] for group in groups  # if len(group) == 3:#
    # group[0]+group[1:]+group[0]#  return "".join(groups)

    #  split string to groups. Each of length 3. groups = [s[
    # for i in  # range(( len(s) + 2)//3 )] for group in  # groups  # if 3 in group:
    #  group[0]+group[1:]+group[0]   # return "".join(groups)

    #    split string to groups. Each of length 3.
    return "".join(
        [s[3 * i + 1 : min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    )


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert (
        encode_cyclic("Abced IF __") == "Abce R__ FI"
    ), "First from the last"
    assert encode_cyclic("More than enough for him") == "More axytg tufu mnhe cyi", "More than"
    assert encode_cyclic("One two Three Four Five Six") == "One xo Two Twxf Ir Wo Rhg Yi", "Rotated once"
    assert encode_cyclic("One two three four five six\nseven") == "One xo Two Twxf Ir Wo Rhg Yivoe", "Contains newline"
    assert decode_cyclic("One xo Two Twxf Ir Wo Rhg Yi") == "One two Three Four Five Six", "Rotated back"
    assert decode_cyclic("One xo Two Twxf Ir Wo Rhg Yivoe") == "One two three four five six\nseven", "Decoding with newline"
