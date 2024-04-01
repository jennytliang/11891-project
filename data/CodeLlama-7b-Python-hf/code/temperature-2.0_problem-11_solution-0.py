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
    >>> string_and('010', '110')
    '100'
    """
    return ''.join(str(int(a_i) & int(b_i)) for a_i, b_i in zip(a, b))


def string_or(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary OR on these inputs and return result also as a string.
    >>> string_or('010', '110')
    '110'
    """
    return ''.join(str(int(a_i) | int(b_i)) for a_i, b_i in zip(a, b))


def string_not(a: str) -> str:
    """ Input is a string a consisting only of 1s and 0s.
    Perform binary NOT on this input and return result also as a string.
    >>> string_not('010')
    '101'
    """
    return ''.join(str(1 - int(a_i)) for a_i in a)


def string_nand(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary NAND on these inputs and return result also as a string.
    >>> string_nand('010', '110')
    '101'
    """
    return string_not(string_and(a, b))


def string_nor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary NOR on these inputs and return result also as a string.
    >>> string_nor('010', '110')
    '001'
    """
    return string_not(string_or(a, b))
