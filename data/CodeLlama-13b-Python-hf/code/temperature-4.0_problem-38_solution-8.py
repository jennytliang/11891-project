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
    # split string to groups of len equal to 2 char
    groups = [s[(2 * i):min((i + 1) * 2, len(s)] for i in range(len(s) // 2 + 1)]
    groups = [(g + ("" if i != len(g) - 1 else g[0])) for i, g in enumerate(groups)]
    group_len = min(len(groups), len(s) // 3)
    # build string decoded string
    l = []  # create list to fill it with groups, reversing them except last in each 3-th group order
    prev_group_num = 0
    last_non_special_group = ""
    for i, g in enumerate(groups[group_len:1:-1]):
        if len(l) == 3 * group_len and i == group_len:
            # if this if-block executed it means that previous group was special - only one char long
            # we dont need it as it is already part of decoding string. we need only last non special chars in group.
            # so take them and break out
            pass
        else:  # append groups of len 2
            if len(g) == 1:  # this is a non-special char, we need it in list but we have to know in which order.
                last_non_special_group = g
            elif len(g) == 3:  # we have a special char here- we need only last char in group but in order before
                if len(g[0]) != 1: raise ValueError(
                    "group which was encoded as 3 chars has incorrect first letter - should be 2.")
                last_char_in_group, special_char_from_left = g[1], g[0]
                group_num_from_right = len(l)
                pos_1 = (len(l) // 3) - (group_num_from_right // 6) - 1
                pos = pos_1 if group_num_from_right < len(s) else (pos_1 - 1)
            elif not l: l = (g[:2])
            else:  # append 1st letter from g to last element that has len == 2 in list and add second char from g as next
                l[-1] += g[0]  # add second char from g to last elemtent with len(==2), but if the only last element is
                               # len==1 - append that 1 char. This element will be "special" character in that it is longer
                               # that two chars in encoded string but should be only last letter in decoding string.
                l += [g[2]]  # append char to list in order to be added next to last element with two chars
    l = groups[:group_len - 1]  # list should contain first elements only. not last of each group
    ret = ""
    for g in reversed(l):
        g_len = len(g)
        # when g has 2 characters in it, we are done - this is also last group, so put it to return value
        # otherwise if g has 3, this is first char in reversed g, take second and save it together with last special
        char = (g[1] + special_chars[(pos_1 // (prev_group_num + 3))]) if g_len == 3 \
            else g[1] if g_len == 1 else g[:g_len]  # when this is last group of length 1 we take 1 letter and not group of len 1 (which we dont take because it will break l)
        ret, pos = (char + ret), (pos - len(char))
        # if we appended special group we need to shift prev_group
        if g_len != len(last_non_special_group):
            prev_group_num += 6

    return ret


# enc = ['abcd abcde fghijk abcdef ghijk lmnop abcdeg hijklmn opqrs abcdeg fghi jklmn']
dec = ['abcd ' * 6 + 'fghi ' * 2]

