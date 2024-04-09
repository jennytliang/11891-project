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
    groups = [(group[-1] + group[0] + group[1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert encode_cyclic("Cyc") == "Cyc", "First"
    assert encode_cyclic("Codefights") == "Cofefghitar", "Second"
    assert encode_cyclic("ABA") == "ABA", "Third"
    assert encode_cyclic("ABABA") == "ABABA", "Fourth"
    assert encode_cyclic("") == "", "Empty"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
