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
    # first, split string into groups of length 4
    four_groups = zip(*[s[4 * i:4 * i + 4] for i in range((len(s) + 3) // 4)])
    # then we reverse the order of elements of each tuple and return it as a single tuple
    r_groups = tuple(map(lambda i: tuple(re.sub('(.{1,3})', reverse_chunks, f"{i}")), four_groups))

    # lastly we flatten the tuple and return it. The flatten here means we remove all elements in tuple.
    # i.e we use ''.join(<tuple_elements>). This way each group is considered as string elements.
    return ("".join(map(lambda l: l[0], r_groups))[1:] + "".join(map(lambda l: l[1], r_groups))[1:])[1:]
