from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join(map(lambda x: '1' if x[0] != x[1] else '0', zip(a, b)))


def string_xor_bytes(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor_bytes('010', '110')
    '100'
    """
    return ''.join(map(lambda x: '1' if x[0] != x[1] else '0', zip(a, b)))


def string_xor_list(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor_list('010', '110')
    '100'
    """
    return ''.join(map(lambda x: '1' if x[0] != x[1] else '0', zip(a, b)))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
