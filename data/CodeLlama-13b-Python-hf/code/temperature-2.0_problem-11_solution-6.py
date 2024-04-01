from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join([str(int(x) ^ int(y)) for x, y in zip(a, b)])


def string_xor_sol(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor_sol('010', '110')
    '100'
    """
    return str(int(a, 2) ^ int(b, 2))


def string_xor_sol_2(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor_sol_2('010', '110')
    '100'
    """
    return bin(int(a, 2) ^ int(b, 2))[2:]


if __name__ == "__main__":
    import doctest
    doctest.testmod()


