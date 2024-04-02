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
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# tests

# test_cases = [
#     ("", ""),
#     ("a", "a"),
#     ("ab", "ba"),
#     ("abc", "bca"),
#     ("abcd", "bcad"),
#     ("abcde", "bcdea"),
#     ("abcdef", "bcdef"),
#     ("abcdefg", "bcdefga"),
#     ("abcdefgh", "bcdefgha"),
#     ("abcdefghi", "bcdefghia"),
#     ("abcdefghij", "bcdefghij"),
#     ("abcdefghijk", "bcdefghijka"),
#     ("abcdefghijkl", "bcdefghijkl"),
#     ("abcdefghijklm", "bcdefghijklma"),
#     ("abcdefghijklmn", "bcdefghijklmna"),
#     ("abcdefghijklmno", "bcdefghijklmno"),
# ]
#
# for s, expected in test_cases:
#     actual = encode_cyclic(s)
#     assert actual == expected, f"{s} -> {actual}"
#
#     actual = decode_cyclic(actual)
#     assert actual == s, f"{s} -> {actual}"
