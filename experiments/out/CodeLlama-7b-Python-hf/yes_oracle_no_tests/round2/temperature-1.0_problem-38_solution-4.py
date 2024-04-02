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
    groups = [(group[-1:] + group[0:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Testing


def test_encode_cyclic():
    assert encode_cyclic("") == ""
    assert encode_cyclic("AAA") == "AAA"
    assert encode_cyclic("AAAAB") == "ABAAA"
    assert encode_cyclic("AAAABBBCCM") == "ABAABBCCM"
    assert encode_cyclic("AAAABBBCCMDDEEFF") == "ABAABBCCMADDFF"


def test_decode_cyclic():
    assert decode_cyclic("") == ""
    assert decode_cyclic("AAA") == "AAA"
    assert decode_cyclic("ABAAA") == "AAAAB"
    assert decode_cyclic("ABAABBCCM") == "AAAABBBCCM"
    assert decode_cyclic("ABAABBCCMADDFF") == "AAAABBBCCMDDEEFF"


# Testing

if __name__ == "__main__":
    test_encode_cyclic()
    test_decode_cyclic()
