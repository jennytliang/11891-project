from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join(str(int(a_i) ^ int(b_i)) for a_i, b_i in zip(a, b))


def string_and(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary AND on these inputs and return result also as a string.
    >>> string_and('110', '110')
    '110'
    """
    return ''.join(str(int(a_i) & int(b_i)) for a_i, b_i in zip(a, b))
