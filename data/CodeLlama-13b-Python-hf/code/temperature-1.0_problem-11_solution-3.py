from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join([str(int(char_a) ^ int(char_b)) for char_a, char_b in zip(a, b)])


def string_xor_bytes(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor_bytes('010', '110')
    '100'
    """
    return ''.join([str(int(char_a) ^ int(char_b)) for char_a, char_b in zip(a, b)])


def string_xor_int(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor_int('010', '110')
    '100'
    """
    return ''.join([str(int(char_a) ^ int(char_b)) for char_a, char_b in zip(a, b)])


def string_xor_bitwise(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor_bitwise('010', '110')
    '100'
    """
    return ''.join([str(int(char_a) ^ int(char_b)) for char_a, char_b in zip(a, b)])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
