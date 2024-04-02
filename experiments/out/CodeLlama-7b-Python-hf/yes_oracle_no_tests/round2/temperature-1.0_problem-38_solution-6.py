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
    groups = re.findall(".{3}", s)
    if not groups:
        return " "
    # cycle elements in each group by shifting by one. Unless group has fewer
    # elements than 3
    groups = [
        (group[1:] + group[0] if len(group) == 3 else group)
        for group in groups[: len(groups) - 1]
    ]
    # merge groups
    return "".join(groups[0:])


# tester for encode and decode
# def test_encode_decode(string):
#     """
#    :param s: string to be encoded or decoded
# :return: None. prints result of encoding or decoding
#    """
#     encoded_s = encode_cyclic(string)
#     print("Encoded:", encoded_s)
#     decoded_s = decode_cyclic(encoded_s)
#     print("Decoded:", decoded_s)
#     if string == decoded_s:
#         print("SUCCESS")
#     else:
#         print("FAILED")
#
# test = "aaabbbccc"
# test = "aaabbbc"
test = "bacbac"
tester(test)