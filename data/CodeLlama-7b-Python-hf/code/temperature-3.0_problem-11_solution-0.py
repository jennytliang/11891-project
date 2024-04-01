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


def string_to_int(s: str) -> int:
    """ Input is string consisting of only digits.
    Convert it to an integer and return that integer
    """
    int_sum = 0
    for i, s_i in zip(range(len(s)), s):
        int_sum += int(s_i) * 2 ** i
    return int_sum


def int_to_string(i: int) -> str:
    """ Input is integer
    Convert it to a string consisting of only digits.
    Return result as a string
    """
    int_list = []
    while i > 0:
        int_list.append(str(i % 10))
        i //= 10

    return ''.join(reversed(int_list))
