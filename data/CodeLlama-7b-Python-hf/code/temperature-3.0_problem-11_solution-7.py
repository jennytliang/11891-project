from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    xor_list = []
    # If a bit is 1 and b is 1 or a bit is 0 and b is 0:
    # xor of that bit is 0. so add 0.
    for a_i, b_i in zip(a, b):
        if a_i == b_i:
            xor_list.append('0')
        else:
            xor_list.append('1')
    return ''.join(xor_list)
